"""Identité et préservation locale sans nécessiter Docker."""
import json
import os
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import threading
from unittest.mock import patch
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'codebase-integrity/scripts'))
import process
import test_worktrees


class Process(unittest.TestCase):
    def setUp(self):
        self.fixture = test_worktrees.Worktrees()
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.root = self.fixture.root
        p = self.root / 'infra/config/layers.json'
        self.config = json.loads(p.read_text())
        (self.root / 'infra').mkdir(exist_ok=True)
        (self.root / 'infra/process-check.json').write_text(json.dumps({
            'process': {'port_base': 18100, 'image': 'busybox:1.37.0'}}))
        self.config['layers']['api']['id'] = 2
        self.config['layers']['web']['id'] = 3
        p.write_text(json.dumps(self.config))
        self.fixture.git('add', 'infra/config/layers.json', 'infra/process-check.json')
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
        witness = api / '.local/process-check/identity.json'
        before = witness.stat().st_mtime_ns
        process.prepare(a)
        self.assertEqual(before, witness.stat().st_mtime_ns)
        witness.write_text('travail tiers')
        with self.assertRaises(ValueError): process.prepare(a)
        self.assertEqual(witness.read_text(), 'travail tiers')

    def test_compose_parameters_override_inherited_values_without_mutation(self):
        api, _ = self.fixture.add()
        info = process.settings(api)
        inherited = {
            'PROCESS_CHECK_IMAGE': 'wrong-image',
            'PROCESS_CHECK_PORT': '1',
            'PROCESS_CHECK_PROOF_DIR': '/wrong-path',
            'UNCHANGED_PARAMETER': 'preserved',
        }
        with patch.dict(os.environ, inherited, clear=True):
            before = dict(os.environ)
            with patch.object(process.subprocess, 'run') as run:
                result = process.compose(info, 'config', capture=True)
            self.assertIs(result, run.return_value)
            self.assertEqual(dict(os.environ), before)
        run.assert_called_once()
        args, kwargs = run.call_args
        self.assertEqual(args[0], [
            'docker', 'compose', '--env-file', os.devnull,
            '-f', str(api / 'infra/compose.process.yaml'),
            '-p', info['project'], 'config',
        ])
        self.assertEqual(kwargs, dict(
            cwd=info['worktree'], text=True, check=True, capture_output=True,
            env={
                'PROCESS_CHECK_IMAGE': info['image'],
                'PROCESS_CHECK_PORT': str(info['port']),
                'PROCESS_CHECK_PROOF_DIR': str(api / '.local/process-check'),
                'UNCHANGED_PARAMETER': 'preserved',
            },
        ))

    def test_wrong_branch_and_symlink_refused(self):
        with self.assertRaises(ValueError): process.settings(self.root)
        api, _ = self.fixture.add()
        (api / '.local').symlink_to(self.root, target_is_directory=True)
        with self.assertRaises(ValueError): process.settings(api)

    def test_identity_served_as_json_and_wrong_identity_refused(self):
        api, _ = self.fixture.add()
        info = process.settings(api)
        process.prepare(info)
        directory = api / '.local/process-check'
        handler = partial(SimpleHTTPRequestHandler, directory=str(directory))
        with ThreadingHTTPServer(('127.0.0.1', 0), handler) as server:
            thread = threading.Thread(target=server.serve_forever, daemon=True)
            thread.start()
            self.addCleanup(thread.join)
            self.addCleanup(server.shutdown)
            info['port'] = server.server_port
            (directory / 'identity.json').write_text(json.dumps(info))
            process.verify(info)
            with patch.dict(info, layer='wrong-layer'):
                with self.assertRaises(ValueError):
                    process.verify(info)

    def test_secondary_reads_both_configurations_from_its_worktree(self):
        api, _ = self.fixture.add()
        (self.root / 'infra/config/layers.json').unlink()
        (self.root / 'infra/process-check.json').unlink()
        path = api / 'infra/process-check.json'
        recipe = json.loads(path.read_text())
        recipe['process'].update(port_base=19100, image='local-witness:custom')
        path.write_text(json.dumps(recipe))
        info = process.settings(api)
        self.assertEqual(info['port'], 19102)
        self.assertEqual(info['image'], 'local-witness:custom')
        self.assertEqual(info['layer'], 'api')

    def test_missing_or_invalid_configurations_do_not_fall_back_or_write_artifacts(self):
        api, _ = self.fixture.add()
        legacy = api / 'codebase-integrity/scripts/aiod.json'
        legacy.parent.mkdir(parents=True)
        legacy.write_text(json.dumps(dict(self.config, process={
            'port_base': 18100, 'image': 'busybox:1.37.0'})))
        for relative in ('infra/config/layers.json', 'infra/process-check.json'):
            path = api / relative
            original = path.read_text()
            for content in (None, '{invalid', '{}'):
                with self.subTest(path=relative, content=content):
                    if content is None:
                        path.unlink()
                    else:
                        path.write_text(content)
                    with self.assertRaises((OSError, ValueError, KeyError)):
                        process.settings(api)
                    self.assertFalse((api / '.local').exists())
                    path.write_text(original)

    def test_duplicate_ids_refused(self):
        api, _ = self.fixture.add()
        p = api / 'infra/config/layers.json'
        c = json.loads(p.read_text())
        c['layers']['web']['id'] = 2
        p.write_text(json.dumps(c))
        with self.assertRaises(ValueError): process.settings(api)


if __name__ == '__main__': unittest.main()
