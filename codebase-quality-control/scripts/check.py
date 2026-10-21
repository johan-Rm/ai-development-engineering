#!/usr/bin/env python3
"""Contrôle local ciblé, sans parcourir les copies sous worktree/."""
from pathlib import Path
import subprocess
import sys

root = Path(__file__).resolve().parents[2]
result = subprocess.run([sys.executable, '-B', '-m', 'unittest', 'discover',
                         '-s', str(root / 'codebase-quality-control/tests'), '-p', 'test_*.py'], cwd=root)
sys.exit(result.returncode)
