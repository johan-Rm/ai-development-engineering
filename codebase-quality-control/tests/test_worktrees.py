"""Exercer Git dans des dépôts jetables ; aucun remote."""
import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[2] / 'codebase-quality-control/scripts/worktrees.py'
spec = importlib.util.spec_from_file_location('worktrees', SCRIPT)
wt = importlib.util.module_from_spec(spec)
spec.loader.exec_module(wt)


class Worktrees(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='aiod-test-')
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / 'projet avec espaces'
        self.root.mkdir()
        self.git('init', '-b', 'main')
        self.git('config', 'user.name', 'AIOD Test')
        self.git('config', 'user.email', 'test@example.invalid')
        (self.root / 'codebase-quality-control/scripts').mkdir(parents=True)
        (self.root / 'codebase-quality-control/scripts/aiod.json').write_text(json.dumps({'layers': {
            'api': {'branch': 'layers/api'}, 'web': {'branch': 'layers/web'}}}))
        (self.root / '.gitignore').write_text('/worktree/*\n!/worktree/README.md\n')
        (self.root / 'reference').write_text('base connue')
        self.git('add', 'codebase-quality-control/scripts/aiod.json', '.gitignore', 'reference')
        self.git('commit', '-m', 'base')
        self.sha = self.git('rev-parse', 'HEAD')

    def git(self, *args):
        return wt.git(self.root, *args)

    def add(self, layer='api', cwd=None):
        return wt.add(cwd or self.root, layer, 'layers/' + layer, self.sha)

    def test_creation_base_and_rerun_preserve_dirty_files_and_env(self):
        path, created = self.add()
        self.assertTrue(created)
        self.assertEqual(wt.git(path, 'rev-parse', 'HEAD'), self.sha)
        (path / '.env').write_text('LOCAL=conserver')
        (path / 'reference').write_text('travail en cours')
        self.assertEqual(self.add(), (path, False))
        self.assertEqual((path / '.env').read_text(), 'LOCAL=conserver')
        self.assertEqual((path / 'reference').read_text(), 'travail en cours')
        self.assertEqual(self.git('status', '--porcelain'), '')

    def test_branch_already_checked_out_at_main_root(self):
        self.git('switch', '-c', 'layers/api')
        self.assertEqual(self.add(), (self.root, False))

    def test_secondary_call_creates_under_main_root(self):
        api, _ = self.add()
        web, _ = self.add('web', api)
        self.assertEqual(web, self.root / 'worktree/web')
        self.assertFalse((api / 'worktree').exists())

    def test_secondary_uses_its_config_when_main_layout_differs(self):
        api, _ = self.add()
        (self.root / 'codebase-quality-control/scripts/aiod.json').unlink()
        web, _ = self.add('web', api)
        self.assertEqual(web, self.root / 'worktree/web')

    def test_unregistered_occupied_directory_preserved(self):
        occupied = self.root / 'worktree/api'
        occupied.mkdir(parents=True)
        (occupied / '.env').write_text('conserver')
        with self.assertRaises(ValueError): self.add()
        self.assertEqual((occupied / '.env').read_text(), 'conserver')
        self.assertEqual(sorted(p.name for p in occupied.iterdir()), ['.env'])

    def test_destination_wrong_branch(self):
        self.git('worktree', 'add', '-b', 'other', str(self.root / 'worktree/api'), self.sha)
        with self.assertRaisesRegex(ValueError, 'inattendue'): self.add()

    def test_symbolic_link_parent_and_path_escape(self):
        outside = Path(self.temp.name) / 'outside'
        outside.mkdir()
        (self.root / 'worktree').symlink_to(outside, target_is_directory=True)
        with self.assertRaises(ValueError): self.add()
        self.assertEqual(list(outside.iterdir()), [])
        with self.assertRaises(ValueError): wt.add(self.root, '../escape', 'layers/api', self.sha)

    def test_unknown_layer_wrong_branch_and_invalid_base(self):
        for layer, branch, base in [('unknown', 'layers/unknown', self.sha),
                                    ('api', 'other', self.sha),
                                    ('api', 'layers/api', 'missing')]:
            with self.assertRaises(ValueError): wt.add(self.root, layer, branch, base)
        self.assertFalse((self.root / 'worktree').exists())

    def test_existing_unchecked_branch_is_preserved(self):
        self.git('branch', 'layers/api', self.sha)
        path, _ = self.add()
        self.assertEqual(wt.git(path, 'rev-parse', 'HEAD'), self.sha)

    def test_foreign_repository_destination_refused(self):
        path = self.root / 'worktree/api'
        path.mkdir(parents=True)
        wt.git(path, 'init', '-b', 'main')
        with self.assertRaises(ValueError): self.add()
        self.assertTrue((path / '.git').is_dir())


if __name__ == '__main__':
    unittest.main()
