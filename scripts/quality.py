#!/usr/bin/env python3
"""Point d’entrée qualité : outillage puis contrôles des trois applications."""
from pathlib import Path
import subprocess
import sys

root = Path(__file__).resolve().parents[1]
subprocess.run([sys.executable, str(root / 'scripts/check.py')], check=True)
subprocess.run([sys.executable, str(root / 'scripts/apps.py'), 'check', 'all', *sys.argv[1:]], check=True)
