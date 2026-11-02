#!/usr/bin/env python3
"""Charger la règle intégrée, ou le contenu explicitement approuvé pour amorcer DEM-028."""
import argparse
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile

MODULES = ('check_contributions.py', 'check_commits.py', 'check_demands.py', 'check_docs.py')
BOOTSTRAP_BASE = '531f4db38c93f4fab61bc190ec4d26c46062e57b'


def run(repo, base, head, approved_sha=None):
    def git(*args):
        return subprocess.run(['git', '-C', str(repo), *args], check=True, capture_output=True).stdout
    base = git('rev-parse', '--verify', '--end-of-options', base + '^{commit}').decode().strip()
    head = git('rev-parse', '--verify', '--end-of-options', head + '^{commit}').decode().strip()
    policy = base
    bootstrap_args = []
    source = 'codebase-integrity/scripts/check_contributions.py'
    if not git('ls-tree', base, '--', source).strip():
        if not approved_sha:
            raise ValueError('vérificateur de base absent ; amorçage requis : approbation explicite manquante')
        if not re.fullmatch(r'[0-9a-f]{40}', approved_sha):
            raise ValueError('approbation attendue : SHA complet de commit, sans nom de branche')
        if base != BOOTSTRAP_BASE:
            raise ValueError('amorçage limité à la base initiale de DEM-028')
        policy = git('rev-parse', '--verify', '--end-of-options', approved_sha + '^{commit}').decode().strip()
        if git('rev-parse', policy + '^{tree}') != git('rev-parse', head + '^{tree}'):
            raise ValueError('contenu candidat différent du commit explicitement approuvé')
        bootstrap_args = ['--demand', 'DEM-028']
        print(f'Amorçage DEM-028 : contenu approuvé {policy}, sans désactivation des contrôles.', flush=True)
    with tempfile.TemporaryDirectory(prefix='contribution-policy-') as folder:
        for name in MODULES:
            source = 'codebase-integrity/scripts/' + name
            metadata = git('ls-tree', policy, '--', source).decode().split()
            if not metadata or metadata[0] not in ('100644', '100755'):
                raise ValueError(f'vérificateur de base absent ou non régulier : {source} ; amorçage requis')
            (Path(folder) / name).write_bytes(git('cat-file', 'blob', metadata[2]))
        # -I exclut PYTHONPATH et le dossier courant ; seul le dossier extrait est ajouté.
        bootstrap = 'import runpy,sys; sys.path.insert(0,sys.argv[1]); sys.argv=sys.argv[2:]; runpy.run_path(sys.argv[0],run_name="__main__")'
        return subprocess.run([sys.executable, '-I', '-B', '-c', bootstrap, folder,
                               str(Path(folder) / MODULES[0]), '--repo', str(repo),
                               '--base', base, '--head', head, *bootstrap_args], cwd=folder, check=True)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument('--base', required=True)
    parser.add_argument('--head', default='HEAD')
    parser.add_argument('--bootstrap-policy-sha', default=os.environ.get('DEM028_BOOTSTRAP_POLICY_SHA'),
                        help='commit explicitement approuvé, réservé au premier amorçage de DEM-028')
    args = parser.parse_args(argv)
    try:
        run(args.repo.resolve(), args.base, args.head, args.bootstrap_policy_sha)
        return 0
    except (OSError, ValueError, subprocess.CalledProcessError) as exc:
        print(f'Contrôle de contribution impossible : {exc}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
