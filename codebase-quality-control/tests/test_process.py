"""Identité et préservation locale sans nécessiter Docker."""
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'codebase-quality-control/scripts'))
import process
import test_worktrees


class Process(unittest.TestCase):
    def setUp(self):
        self.fixture = test_worktrees.Worktrees()
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.root = self.fixture.root
        p = self.root / 'codebase-quality-control/scripts/aiod.json'
        self.config = json.loads(p.read_text())
        self.config['process'] = {'port_base': 18100, 'image': 'busybox:1.37.0'}
        self.config['layers']['api']['id'] = 2
        self.config['layers']['web']['id'] = 3
        p.write_text(json.dumps(self.config))
        self.fixture.git('add', 'codebase-quality-control/scripts/aiod.json')
        self.fixture.git('commit', '-m', 'configuration témoin')
        self.fixture.sha = self.fixture.git('rev-parse', 'HEAD')

    def test_distinct_ports_projects_paths_and_preserved_files(self):
        api, _ = self.fixture.add()
        web, _ = self.fixture.add('web')
        a, b = process.settings(api), process.settings(web)
        self.assertNotEqual(a['port'], b['port'])
        self.assertNotEqual(a['project'], b['project'])
        self.assertNotEqual(a['worktree'], b['worktree'])
        process.prepare(a)
        witness = api / '.aiod/runtime/index.html'
        before = witness.stat().st_mtime_ns
        process.prepare(a)
        self.assertEqual(before, witness.stat().st_mtime_ns)
        witness.write_text('travail tiers')
        with self.assertRaises(ValueError): process.prepare(a)
        self.assertEqual(witness.read_text(), 'travail tiers')

    def test_wrong_branch_and_symlink_refused(self):
        with self.assertRaises(ValueError): process.settings(self.root)
        api, _ = self.fixture.add()
        (api / '.aiod').symlink_to(self.root, target_is_directory=True)
        with self.assertRaises(ValueError): process.settings(api)

    def test_duplicate_ids_refused(self):
        api, _ = self.fixture.add()
        p = api / 'codebase-quality-control/scripts/aiod.json'
        c = json.loads(p.read_text())
        c['layers']['web']['id'] = 2
        p.write_text(json.dumps(c))
        with self.assertRaises(ValueError): process.settings(api)


if __name__ == '__main__': unittest.main()
