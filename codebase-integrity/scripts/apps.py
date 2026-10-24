#!/usr/bin/env python3
"""Installer, lancer et vérifier les applications depuis le dépôt ou un worktree."""
import argparse
import json
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[2]
APPS = {'api': 'app/api/app', 'web': 'app/web/targets/app', 'backoffice': 'app/backoffice'}


def commands(action, app):
    if app == 'api':
        return {
            'install': [['composer', 'install', '--no-interaction']],
            'serve': [['php', '-d', 'variables_order=EGPCS', '-S', '127.0.0.1:8000', '-t', 'public', 'public/router.php']],
            'check': [[sys.executable, 'tests/smoke.py'], ['php', 'bin/console', 'lint:container'],
                      ['php', 'bin/console', 'doctrine:schema:validate', '--skip-sync']],
        }[action]
    return {'install': [['npm', 'ci']], 'serve': [['npm', 'run', 'dev']],
            'check': [['npm', 'run', 'typecheck'], ['npm', 'run', 'build']]}[action]


def run(action, app, root, browser=False):
    directory = root / APPS[app]
    if not directory.is_dir():
        raise ValueError(f'Application absente : {directory}')
    if app == 'api' and action == 'install':
        # Création exclusive : ne jamais remplacer une configuration locale.
        try:
            with (directory / '.env').open('x') as stream:
                stream.write((directory / '.env.example').read_text())
        except FileExistsError:
            pass
    for command in commands(action, app):
        if app == 'api' and action == 'serve':
            subprocess.run(['php', 'bin/console', 'doctrine:migrations:migrate', '-n'], cwd=directory, check=True)
        print(f'[{app}] {" ".join(command)}', flush=True)
        subprocess.run(command, cwd=directory, check=True)
    if app == 'api' and action == 'check':
        with tempfile.TemporaryDirectory(prefix='aiod-openapi-') as tmp:
            export = Path(tmp) / 'openapi.json'
            subprocess.run(['php', 'bin/console', 'api:openapi:export', f'--output={export}'], cwd=directory, check=True)
            if json.loads(export.read_text()) != json.loads((directory / 'openapi.json').read_text()):
                raise ValueError('Contrat OpenAPI obsolète : régénérer app/api/app/openapi.json')
    if browser and app != 'api':
        subprocess.run(['npm', 'run', 'test:e2e'], cwd=directory, check=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=('install', 'serve', 'check'))
    parser.add_argument('app', choices=(*APPS, 'all'))
    parser.add_argument('--root', type=Path, default=ROOT, help='Racine du dépôt/worktree à utiliser')
    parser.add_argument('--browser', action='store_true', help='Ajouter Playwright (API de développement déjà démarrée)')
    args = parser.parse_args()
    if args.action == 'serve' and args.app == 'all':
        parser.error('Lancer chaque application dans son propre terminal')
    if args.browser and args.action != 'check':
        parser.error('--browser est réservé à check')
    try:
        for app in APPS if args.app == 'all' else [args.app]:
            run(args.action, app, args.root.resolve(), args.browser)
    except (OSError, ValueError, subprocess.CalledProcessError) as exc:
        parser.exit(1, f'Erreur : {exc}\n')


if __name__ == '__main__':
    main()
