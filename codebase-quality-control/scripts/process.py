#!/usr/bin/env python3
"""Conteneurs témoins pour la recette AIOD, sans application ni secrets."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import urllib.request
import worktrees


def settings(cwd):
    cwd = Path(cwd).resolve()
    root, records = worktrees.context(cwd)
    tree = Path(worktrees.git(cwd, 'rev-parse', '--show-toplevel')).resolve()
    if not any(Path(item['worktree']).resolve() == tree for item in records):
        raise ValueError('Arbre Git non enregistré')
    branch = worktrees.git(tree, 'branch', '--show-current')
    config = json.loads((tree / 'codebase-quality-control/scripts/aiod.json').read_text())
    layers = config['layers']
    ids = [item['id'] for item in layers.values() if 'id' in item]
    if any(type(item) is not int or item < 1 for item in ids) or len(ids) != len(set(ids)):
        raise ValueError('Identifiants de couche invalides ou dupliqués')
    matches = [(name, item) for name, item in layers.items() if item['branch'] == branch and 'id' in item]
    if len(matches) != 1:
        raise ValueError('Exécuter depuis le worktree d’une des cinq couches')
    layer, item = matches[0]
    port_base = config['process']['port_base']
    if type(port_base) is not int or not 1024 <= port_base + item['id'] <= 65535:
        raise ValueError('Base de ports invalide')
    project = 'aiod-' + hashlib.sha256(str(root).encode()).hexdigest()[:8] + '-' + layer
    for candidate in (tree / '.local', tree / '.local/process-check', tree / '.local/process-check/identity.json'):
        if candidate.is_symlink():
            raise ValueError('Lien symbolique inattendu dans les artefacts locaux')
    return dict(root=str(root), worktree=str(tree), branch=branch, layer=layer,
                project=project, port=port_base + item['id'], image=config['process']['image'])


def prepare(info):
    directory = Path(info['worktree']) / '.local/process-check'
    directory.mkdir(parents=True, exist_ok=True)
    path = directory / 'identity.json'
    try:
        with path.open('x') as stream:
            json.dump(info, stream, ensure_ascii=False)
    except FileExistsError:
        if json.loads(path.read_text()) != info:
            raise ValueError('Identité JSON existante incompatible : aucun écrasement')


def compose(info, *args, capture=False):
    env = os.environ.copy()
    env.update(AIOD_IMAGE=info['image'], AIOD_PORT=str(info['port']),
               AIOD_PROOF_DIR=str(Path(info['worktree']) / '.local/process-check'))
    command = ['docker', 'compose', '--env-file', os.devnull,
               '-f', str(Path(info['worktree']) / 'infra/compose.process.yaml'),
               '-p', info['project'], *args]
    return subprocess.run(command, cwd=info['worktree'], env=env, text=True,
                          check=True, capture_output=capture)


def verify(info):
    with urllib.request.urlopen(f"http://127.0.0.1:{info['port']}/identity.json", timeout=5) as response:
        actual = json.load(response)
    if actual != info:
        raise ValueError('Endpoint lié au mauvais environnement')
    print(json.dumps(actual, ensure_ascii=False, indent=2))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=('info', 'config', 'up', 'verify', 'status', 'down'))
    args = parser.parse_args()
    try:
        info = settings(Path.cwd())
        if args.command == 'info': print(json.dumps(info, ensure_ascii=False, indent=2))
        elif args.command == 'config': compose(info, 'config')
        elif args.command == 'up':
            prepare(info)
            compose(info, 'up', '-d', '--wait', '--wait-timeout', '45')
            verify(info)
        elif args.command == 'verify': verify(info)
        elif args.command == 'status': compose(info, 'ps')
        else: compose(info, 'down')  # Conserver les volumes et données.
    except (ValueError, OSError, KeyError, subprocess.CalledProcessError) as exc:
        parser.exit(1, f'Erreur : {exc}\n')


if __name__ == '__main__':
    main()
