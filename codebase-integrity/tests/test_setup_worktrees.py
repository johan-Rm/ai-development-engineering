"""Recette de setup dans des dépôts et HOME jetables ; aucun réseau ni IDE réel."""
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]
ALIAS = 'vscode-worktree-ai-powered-development-engineering'


class SetupWorktrees(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='setup-worktrees-')
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "projet avec espaces et ' apostrophe $variable"
        self.home = Path(self.temp.name) / 'home isolé'
        self.root.mkdir()
        self.home.mkdir()
        self.env = dict(os.environ, HOME=str(self.home), GIT_CONFIG_NOSYSTEM='1',
                        GIT_CONFIG_GLOBAL='/dev/null')
        self.run_command('git', 'init', '-b', 'develop')
        self.run_command('git', 'config', 'user.name', 'Setup Test')
        self.run_command('git', 'config', 'user.email', 'test@example.invalid')
        for name in ['Makefile', 'infra/config/layers.json',
                     'codebase-integrity/scripts/worktrees.py',
                     'codebase-integrity/scripts/setup_worktrees.py']:
            target = self.root / name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / name, target)
        (self.root / '.gitignore').write_text('/worktree/\n/.env\n')
        self.run_command('git', 'add', '.')
        self.run_command('git', 'commit', '-m', 'fixture')
        self.sha = self.run_command('git', 'rev-parse', 'HEAD').stdout.strip()
        self.layers = json.loads((self.root / 'infra/config/layers.json').read_text())['layers']

    def run_command(self, *args, success=True, cwd=None, **kwargs):
        result = subprocess.run(args, cwd=cwd or self.root, env=self.env,
                                text=True, capture_output=True, **kwargs)
        if success:
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        else:
            self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
        return result

    def prepare(self, **kwargs):
        return self.run_command('make', 'setup-worktrees', **kwargs)

    def test_creation_rerun_and_alias_execution_preserve_local_work(self):
        aliases = self.home / '.bash_aliases'
        aliases.write_text("alias personnel='echo conserver'\n")
        self.prepare()
        workspace = self.root / 'aide.code-workspace'
        paths = {item['path'] for item in json.loads(workspace.read_text())['folders']}
        self.assertEqual(paths, {'.'} | {f'worktree/{layer}' for layer in self.layers})
        for layer, config in self.layers.items():
            target = self.root / 'worktree' / layer
            self.assertEqual(self.run_command('git', 'branch', '--show-current', cwd=target).stdout.strip(), config['branch'])
            self.assertEqual(self.run_command('git', 'rev-parse', 'HEAD', cwd=target).stdout.strip(), self.sha)
        local = self.root / 'worktree/api/.env'
        local.write_text('LOCAL=conserver')
        dirty = self.root / 'worktree/api/Makefile'
        dirty.write_text('travail en cours')
        before = aliases.read_bytes(), workspace.read_bytes()
        self.prepare()
        self.assertEqual(before, (aliases.read_bytes(), workspace.read_bytes()))
        self.assertEqual(local.read_text(), 'LOCAL=conserver')
        self.assertEqual(dirty.read_text(), 'travail en cours')
        binary = self.home / 'bin'
        binary.mkdir()
        code = binary / 'code'
        code.write_text('#!/bin/bash\nprintf "%s\\n" "$#" "$1"\n')
        code.chmod(0o755)
        self.env['PATH'] = str(binary) + os.pathsep + self.env['PATH']
        result = self.run_command('bash', '-O', 'expand_aliases', '-c',
                                  'source "$HOME/.bash_aliases"\n' + ALIAS)
        self.assertEqual(result.stdout.splitlines(), ['1', str(workspace)])

    def test_existing_workspace_customizations_are_preserved(self):
        target = self.root / 'aide.code-workspace'
        shutil.copyfile(ROOT / target.name, target)
        document = json.loads(target.read_text())
        document['settings']['editor.fontSize'] = 19
        target.write_text(json.dumps(document))
        before = target.read_bytes()
        self.prepare()
        self.assertEqual(target.read_bytes(), before)

    def test_incompatible_workspace_or_alias_refused_before_creation(self):
        target = self.root / 'aide.code-workspace'
        target.write_text('{"folders": []}')
        self.prepare(success=False)
        self.assertFalse((self.root / 'worktree').exists())
        target.unlink()
        aliases = self.home / '.bash_aliases'
        for content in [f"alias {ALIAS}='code /autre/projet'\n", "alias casse='\n"]:
            aliases.write_text(content)
            self.prepare(success=False)
            self.assertEqual(aliases.read_text(), content)
            self.assertFalse((self.root / 'worktree').exists())
            self.assertFalse(target.exists())

    def test_occupied_last_destination_prevents_partial_creation(self):
        occupied = self.root / 'worktree/design'
        occupied.mkdir(parents=True)
        (occupied / '.env').write_text('conserver')
        self.prepare(success=False)
        self.assertEqual(list((self.root / 'worktree').iterdir()), [occupied])
        self.assertEqual((occupied / '.env').read_text(), 'conserver')
        self.assertFalse((self.home / '.bash_aliases').exists())

    def test_relocated_branch_refused_without_modification(self):
        self.run_command('git', 'worktree', 'add', '-b', 'layers/design', 'ailleurs', 'develop')
        self.prepare(success=False)
        self.assertFalse((self.root / 'worktree').exists())
        self.assertTrue((self.root / 'ailleurs/.git').is_file())

    def test_symlink_alias_file_is_preserved(self):
        external = self.home / 'personnel'
        external.write_text('conserver\n')
        (self.home / '.bash_aliases').symlink_to(external)
        self.prepare(success=False)
        self.assertEqual(external.read_text(), 'conserver\n')
        self.assertFalse((self.root / 'worktree').exists())

    def test_invocation_from_layer_uses_main_workspace(self):
        self.prepare()
        before = (self.home / '.bash_aliases').read_bytes()
        self.prepare(cwd=self.root / 'worktree/devops')
        self.assertEqual((self.home / '.bash_aliases').read_bytes(), before)
        self.assertFalse((self.root / 'worktree/devops/worktree').exists())
