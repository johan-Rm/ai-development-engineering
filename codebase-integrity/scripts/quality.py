#!/usr/bin/env python3
"""Point d’entrée qualité : outillage puis contrôles des trois applications."""
from pathlib import Path
import subprocess
import sys

root = Path(__file__).resolve().parents[2]
subprocess.run([sys.executable, str(root / 'codebase-integrity/scripts/check_demands.py')], check=True)
subprocess.run([sys.executable, str(root / 'codebase-integrity/scripts/check.py')], check=True)
subprocess.run([sys.executable, str(root / 'codebase-integrity/scripts/apps.py'), 'check', 'all', *sys.argv[1:]], check=True)
