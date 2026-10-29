#!/usr/bin/env python3
"""Préparer les worktrees configurés, le workspace et son alias Bash sans réseau."""
import json
import os
from pathlib import Path
import re
import shlex
import subprocess
import sys

import worktrees

ALIAS = 'vscode-worktree-ai-powered-development-engineering'
WORKSPACE = 'aide.code-workspace'


def regular_file(path):
    if path.is_symlink() or (path.exists() and not path.is_file()):
        raise ValueError(f'Fichier ordinaire requis : {path}')


def setup(cwd, home):
    root, records = worktrees.context(cwd)
    tree = Path(worktrees.git(cwd, 'rev-parse', '--show-toplevel'))
    layers = json.loads((tree / 'infra/config/layers.json').read_text())['layers']
    if not isinstance(layers, dict) or not layers:
        raise ValueError('Configuration des couches vide ou invalide')
    worktrees.git(root, 'rev-parse', '--verify', 'develop^{commit}')
    # Vérifier toutes les destinations avant la première création.
    parent = root / 'worktree'
    if parent.is_symlink() or (parent.exists() and not parent.is_dir()):
        raise ValueError('worktree doit être un dossier sans lien symbolique')
    for layer, config in layers.items():
        if not re.fullmatch('[a-z][a-z0-9-]*', layer):
            raise ValueError('Nom de couche invalide')
        branch = config['branch']
        worktrees.git(root, 'check-ref-format', '--branch', branch)
        destination = parent / layer
        matching = [item for item in records if
                    item['worktree'] == str(destination) or
                    item.get('branch') == 'refs/heads/' + branch]
        if destination.is_symlink():
            raise ValueError(f'Destination symbolique : {destination}')
        if matching:
            if (len(matching) != 1 or matching[0]['worktree'] != str(destination)
                    or matching[0].get('branch') != 'refs/heads/' + branch):
                raise ValueError(f'Worktree incompatible pour {layer}')
            if worktrees.git(destination, 'branch', '--show-current') != branch:
                raise ValueError(f'Branche incompatible pour {layer}')
        elif destination.exists():
            raise ValueError(f'Destination existante non enregistrée : {destination}')

    workspace = root / WORKSPACE
    regular_file(workspace)
    folders = [{'name': '◆ principal', 'path': '.'}]
    folders += [{'name': layer, 'path': f'worktree/{layer}'} for layer in layers]
    if workspace.exists():
        document = json.loads(workspace.read_text())
        present = {item['path'] for item in document['folders']}
        if not all(item['path'] in present for item in folders):
            raise ValueError('Workspace incompatible ; configuration conservée')
    else:
        document = {'folders': folders, 'settings': {
            'files.exclude': {'worktree': True},
            'search.exclude': {'worktree': True},
            'git.openRepositoryInParentFolders': 'never',
            'git.branchProtection': ['develop', 'master', 'main'],
            'git.branchProtectionPrompt': 'alwaysPrompt'}}

    aliases = home / '.bash_aliases'
    regular_file(aliases)
    previous = aliases.read_text() if aliases.exists() else ''
    command = shlex.join(['code', str(workspace)])
    definition = f'alias {ALIAS}={shlex.quote(command)}'
    mentions = [line for line in previous.splitlines()
                if ALIAS in line and not line.lstrip().startswith('#')]
    for line in mentions:
        tokens = shlex.split(line)
        if (len(tokens) != 2 or tokens[0] != 'alias'
                or not tokens[1].startswith(ALIAS + '=')
                or shlex.split(tokens[1].split('=', 1)[1]) != ['code', str(workspace)]):
            raise ValueError('Alias existant incompatible ; fichier conservé')
    separator = '\n' if previous and not previous.endswith('\n') else ''
    content = previous if mentions else previous + separator + definition + '\n'
    syntax = subprocess.run(['bash', '-n'], input=content, text=True, capture_output=True)
    if syntax.returncode:
        raise ValueError('Syntaxe de .bash_aliases invalide ; fichier conservé')

    for layer, config in layers.items():
        path, created = worktrees.add(cwd, layer, config['branch'], 'develop')
        print(('Créé' if created else 'Réutilisé') + ' : ' + str(path))
    if not workspace.exists():
        with workspace.open('x') as stream:
            stream.write(json.dumps(document, ensure_ascii=False, indent=2) + '\n')
    if content != previous:
        home.mkdir(parents=True, exist_ok=True)
        if aliases.exists():
            with aliases.open('a') as stream:
                stream.write(content[len(previous):])
        else:
            with aliases.open('x') as stream:
                stream.write(content)
    print(f'Workspace : {workspace}')
    print('Activer dans le terminal courant : source ~/.bash_aliases')


if __name__ == '__main__':
    try:
        setup(Path.cwd(), Path(os.environ['HOME']))
    except (ValueError, OSError, KeyError, TypeError) as exc:
        sys.exit(f'Erreur : {exc}')
