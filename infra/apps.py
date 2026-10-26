#!/usr/bin/env python3
"""Local application stacks, independent of the BusyBox process recipe."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import socket
import subprocess
import sys


class StackError(RuntimeError):
    pass


def git(root, *args):
    return subprocess.check_output(['git', '-C', str(root), *args], text=True).strip()


def identity(root, port_base=None):
    root = root.resolve()
    if Path(git(root, 'rev-parse', '--show-toplevel')).resolve() != root:
        raise StackError('Le lanceur doit appartenir à la racine Git du worktree.')
    common = Path(git(root, 'rev-parse', '--path-format=absolute', '--git-common-dir'))
    if common.parent == root:
        raise StackError('Utiliser un worktree de couche, pas le dépôt principal.')
    branch = git(root, 'branch', '--show-current')
    layers = json.loads((root / 'config/layers.json').read_text())['layers']
    matches = [(name, data) for name, data in layers.items() if data['branch'] == branch]
    if len(matches) != 1:
        raise StackError('Branche de couche attendue ; develop/master et HEAD détachée sont refusés.')
    layer, data = matches[0]
    registered = git(root, 'worktree', 'list', '--porcelain').splitlines()
    if f'worktree {root}' not in registered:
        raise StackError('Worktree non enregistré à cet emplacement ; réparer les liens Git.')
    base = int(port_base if port_base is not None else os.environ.get('AIDE_APP_PORT_BASE', '19300'))
    port = base + int(data['id'])
    if not 1024 <= port <= 65535:
        raise StackError('Port calculé hors de la plage 1024..65535.')
    key = hashlib.sha256(str(common.parent).encode()).hexdigest()[:10]
    return {'root': str(root), 'layer': layer, 'branch': branch,
            'project': f'aide-app-{key}-{layer}', 'port': port,
            'domain': f'wt-{layer}.localhost', 'image_key': key}


def environment(info):
    env = {k: v for k, v in os.environ.items() if not k.startswith(('COMPOSE_', 'AIDE_APP_'))}
    env.update(AIDE_APP_ROOT=info['root'], AIDE_APP_DOMAIN=info['domain'],
               AIDE_APP_PORT=str(info['port']), AIDE_APP_UID=str(os.getuid()),
               AIDE_APP_GID=str(os.getgid()), AIDE_APP_IMAGE_KEY=info['image_key'])
    return env


def compose_command(info, interface='both'):
    cmd = ['docker', 'compose', '--env-file', '/dev/null', '--project-directory', info['root'],
           '-p', info['project'], '-f', str(Path(info['root']) / 'infra/compose.apps.yaml')]
    for profile in (['web', 'backoffice'] if interface == 'both' else [interface]):
        cmd += ['--profile', profile]
    return cmd


def compose(info, args, interface='both', capture=False):
    return subprocess.run(compose_command(info, interface) + args, env=environment(info),
                          text=True, check=True, capture_output=capture)


def check_port(info):
    # Only a running Caddy container owned by this exact project may already hold its port.
    ids = compose(info, ['ps', '-q', 'caddy'], capture=True).stdout.split()
    own_port = False
    if ids:
        inspected = json.loads(subprocess.check_output(['docker', 'inspect', *ids], text=True))
        for container in inspected:
            bindings = container['NetworkSettings'].get('Ports', {}).get('80/tcp') or []
            own_port |= any(b['HostIp'] == '127.0.0.1' and int(b['HostPort']) == info['port']
                            for b in bindings)
    if own_port:
        return
    with socket.socket() as probe:
        probe.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            probe.bind(('127.0.0.1', info['port']))
        except OSError as exc:
            raise StackError(f"Port {info['port']} occupé ; choisir AIDE_APP_PORT_BASE sans arrêter le service tiers.") from exc



def prepare_mountpoints(info, interface):
    # Docker otherwise creates absent nested volume mountpoints as root on the host.
    root = Path(info['root'])
    directories = [root / 'app/api/app' / name for name in ('vendor', 'var')]
    for name in (['web', 'backoffice'] if interface == 'both' else [interface]):
        source = root / ('app/web/targets/app' if name == 'web' else 'app/backoffice')
        if not source.is_dir():
            raise StackError(f'Source applicative absente : {source}')
        directories.extend(source / child for child in ('node_modules', '.nuxt', '.output'))
    for directory in directories:
        if directory.is_symlink():
            raise StackError(f'Point de montage symbolique refusé : {directory}')
        directory.mkdir(exist_ok=True)


def urls(info):
    return {name: f"http://{name}.{info['domain']}:{info['port']}" + ('/api/docs' if name == 'api' else '')
            for name in ('api', 'web', 'backoffice')}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=['info', 'config', 'prepare', 'up', 'status', 'down'])
    parser.add_argument('--interface', choices=['web', 'backoffice', 'both'])
    args = parser.parse_args(argv)
    root = Path(__file__).resolve().parent.parent
    try:
        if Path(git(Path.cwd(), 'rev-parse', '--show-toplevel')).resolve() != root:
            raise StackError('Exécuter le lanceur depuis son propre worktree.')
        info = identity(root)
        interface = args.interface or ('backoffice' if info['layer'] == 'backoffice' else 'web')
        if args.action == 'info':
            print(json.dumps({**info, 'urls': urls(info)}, indent=2))
        elif args.action == 'config':
            compose(info, ['config'], interface)
        elif args.action == 'prepare':
            compose(info, ['build', 'api'])
            compose(info, ['pull', 'init', 'web', 'backoffice', 'caddy'])
        elif args.action == 'up':
            check_port(info)
            prepare_mountpoints(info, interface)
            compose(info, ['up', '-d', '--build', '--wait', '--wait-timeout', '600'], interface)
            print(json.dumps(urls(info), indent=2))
            print('Seules les interfaces démarrées répondent ; les autres peuvent renvoyer 502.')
        elif args.action == 'status':
            compose(info, ['ps', '-a'])
            print(json.dumps(urls(info), indent=2))
        else:
            compose(info, ['down'])  # all profiles; never delete volumes
    except (StackError, ValueError, KeyError, OSError, subprocess.CalledProcessError) as exc:
        print(f'Erreur : {exc}', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
