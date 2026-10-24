#!/usr/bin/env python3
"""Observer les cinq témoins démarrés et l’isolation de leurs écritures."""
import json
from pathlib import Path
import subprocess
import sys
import uuid
import process
import worktrees


def check(cwd):
    root, _ = worktrees.context(cwd)
    infos = [process.settings(root / 'worktree' / layer)
             for layer in ('backoffice', 'api', 'web', 'devops', 'design')]
    mounts, networks = [], []
    marker = '.process-check-proof-' + uuid.uuid4().hex
    for info in infos:
        process.verify(info)
        cid = process.compose(info, 'ps', '-q', 'witness', capture=True).stdout.strip()
        if not cid:
            raise ValueError('Conteneur témoin absent')
        inspect = json.loads(subprocess.check_output(['docker', 'inspect', cid], text=True))[0]
        proof = next(m for m in inspect['Mounts'] if m['Destination'] == '/proof')
        if proof['Source'] != str(Path(info['worktree']) / '.local/process-check') or proof['RW']:
            raise ValueError('Montage de preuve incorrect')
        mounts.append(next(m['Name'] for m in inspect['Mounts'] if m['Destination'] == '/data'))
        networks.append(tuple(sorted(inspect['NetworkSettings']['Networks'])))
        process.compose(info, 'exec', '-T', 'witness', 'test', '!', '-e', '/data/' + marker)
    if len(set(mounts)) != 5 or len(set(networks)) != 5:
        raise ValueError('Réseaux ou volumes partagés entre couches')
    for index, info in enumerate(infos):
        # Arguments positionnels : aucun nom de couche interpolé dans le code shell.
        process.compose(info, 'exec', '-T', 'witness', 'sh', '-c',
                        'printf "%s" "$1" > "$2"', 'proof', info['layer'], '/data/' + marker)
        for other in infos[index+1:]:
            process.compose(other, 'exec', '-T', 'witness', 'test', '!', '-e', '/data/' + marker)
    for info in infos:
        actual = process.compose(info, 'exec', '-T', 'witness', 'cat', '/data/' + marker,
                                 capture=True).stdout
        if actual != info['layer']:
            raise ValueError('Écriture visible depuis une autre couche')
    print(json.dumps({'result': 'cinq endpoints, montages, réseaux et volumes isolés',
                      'volumes': mounts, 'networks': networks, 'marker': marker}, indent=2))


if __name__ == '__main__':
    try:
        check(Path.cwd())
    except (ValueError, OSError, KeyError, StopIteration, subprocess.CalledProcessError) as exc:
        sys.exit(f'Erreur : {exc}')
