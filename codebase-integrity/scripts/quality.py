#!/usr/bin/env python3
"""Point d’entrée qualité : outillage puis contrôles des trois applications."""
from pathlib import Path
import argparse
import subprocess
import sys

root = Path(__file__).resolve().parents[2]
parser = argparse.ArgumentParser()
parser.add_argument('--commit-base')
parser.add_argument('--commit-head', default='HEAD')
args, application_args = parser.parse_known_args()
if args.commit_base:
    subprocess.run([sys.executable, str(root / 'codebase-integrity/scripts/check_commits.py'),
                    '--base', args.commit_base, '--head', args.commit_head], check=True)
else:
    print('Messages de commits non vérifiés : fournir --commit-base avant PR.', flush=True)
subprocess.run([sys.executable, str(root / 'codebase-integrity/scripts/check_demands.py')], check=True)
subprocess.run([sys.executable, str(root / 'codebase-integrity/scripts/check_docs.py')], check=True)
subprocess.run([sys.executable, str(root / 'codebase-integrity/scripts/check.py')], check=True)
subprocess.run([sys.executable, str(root / 'codebase-integrity/scripts/apps.py'), 'check', 'all', *application_args], check=True)
