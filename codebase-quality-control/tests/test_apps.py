"""Préserver les environnements locaux et propager les échecs des contrôles."""
import importlib.util
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location('apps', Path(__file__).resolve().parents[2] / 'codebase-quality-control/scripts/apps.py')
apps = importlib.util.module_from_spec(spec)
spec.loader.exec_module(apps)


class Apps(unittest.TestCase):
    def test_install_preserves_existing_env_and_uses_selected_root(self):
        with tempfile.TemporaryDirectory(prefix='aiod projet ') as tmp:
            root = Path(tmp)
            directory = root / 'api/app'
            directory.mkdir(parents=True)
            (directory / '.env.example').write_text('DEFAULT=1')
            with patch.object(apps.subprocess, 'run') as execute:
                apps.run('install', 'api', root)
                self.assertEqual((directory / '.env').read_text(), 'DEFAULT=1')
                (directory / '.env').write_text('SECRET=conserver')
                apps.run('install', 'api', root)
                self.assertEqual((directory / '.env').read_text(), 'SECRET=conserver')
                self.assertEqual(execute.call_args.kwargs['cwd'], directory)
                self.assertTrue(execute.call_args.kwargs['check'])

    def test_failed_typecheck_stops_before_build(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'web/targets/app').mkdir(parents=True)
            with patch.object(apps.subprocess, 'run', side_effect=subprocess.CalledProcessError(1, 'npm')) as execute:
                with self.assertRaises(subprocess.CalledProcessError):
                    apps.run('check', 'web', root)
                self.assertEqual(execute.call_count, 1)

    def test_openapi_drift_fails_without_overwriting_contract(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            directory = root / 'api/app'
            directory.mkdir(parents=True)
            contract = directory / 'openapi.json'
            contract.write_text('{"paths": {}}')

            def execute(command, **kwargs):
                if 'api:openapi:export' in command:
                    Path(command[-1].removeprefix('--output=')).write_text('{"paths": {"/new": {}}}')

            with patch.object(apps.subprocess, 'run', side_effect=execute):
                with self.assertRaisesRegex(ValueError, 'OpenAPI obsolète'):
                    apps.run('check', 'api', root)
            self.assertEqual(contract.read_text(), '{"paths": {}}')
