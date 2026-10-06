#!/usr/bin/env python3
"""Contrôle local ciblé, sans parcourir les copies sous worktree/."""
from pathlib import Path
import subprocess
import sys

root = Path(__file__).resolve().parent.parent
result = subprocess.run([sys.executable, '-B', '-m', 'unittest', 'discover',
                         '-s', str(root / 'tests'), '-p', 'test_*.py'], cwd=root)
sys.exit(result.returncode)
