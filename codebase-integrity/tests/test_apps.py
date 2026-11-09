"""Préserver les environnements locaux et propager les échecs des contrôles."""
import importlib.util
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location('apps', Path(__file__).resolve().parents[2] / 'codebase-integrity/scripts/apps.py')
apps = importlib.util.module_from_spec(spec)
spec.loader.exec_module(apps)


class Apps(unittest.TestCase):
    def test_backoffice_install_uses_app_directory(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            directory = root / 'apps/backoffice'
            directory.mkdir(parents=True)
            with patch.object(apps.subprocess, 'run') as execute:
                apps.run('install', 'backoffice', root)
                self.assertEqual(execute.call_args.kwargs['cwd'], directory)

    def test_install_preserves_existing_env_and_uses_selected_root(self):
        with tempfile.TemporaryDirectory(prefix='aiod projet ') as tmp:
            root = Path(tmp)
            directory = root / 'apps/api/app'
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
            (root / 'apps/web/targets/app').mkdir(parents=True)
            with patch.object(apps.subprocess, 'run', side_effect=subprocess.CalledProcessError(1, 'npm')) as execute:
                with self.assertRaises(subprocess.CalledProcessError):
                    apps.run('check', 'web', root)
                self.assertEqual(execute.call_count, 1)

    def test_openapi_drift_fails_without_overwriting_contract(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            directory = root / 'apps/api/app'
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


class ApplicationLayouts(unittest.TestCase):
    def test_install_selects_layout_for_every_application_and_root(self):
        for layout in ('app', 'apps'):
            for name, relative in apps.APPS.items():
                with self.subTest(layout=layout, application=name), tempfile.TemporaryDirectory() as tmp:
                    root = Path(tmp) / 'selected root'
                    directory = root / layout / relative
                    directory.mkdir(parents=True)
                    if name == 'api':
                        (directory / '.env.example').write_text('APP_ENV=test')
                    with patch.object(apps.subprocess, 'run') as execute:
                        apps.run('install', name, root)
                    self.assertEqual(execute.call_args.kwargs['cwd'], directory)
                    self.assertTrue(execute.call_args.kwargs['check'])
                    if name == 'api':
                        self.assertEqual((directory / '.env').read_text(), 'APP_ENV=test')
                        (directory / '.env').write_text('SECRET=preserve')
                        with patch.object(apps.subprocess, 'run'):
                            apps.run('install', name, root)
                        self.assertEqual((directory / '.env').read_text(), 'SECRET=preserve')

    def test_new_layout_has_priority_when_both_exist(self):
        for name, relative in apps.APPS.items():
            with self.subTest(application=name), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                for layout in ('app', 'apps'):
                    directory = root / layout / relative
                    directory.mkdir(parents=True)
                    if name == 'api':
                        (directory / '.env.example').write_text(layout)
                with patch.object(apps.subprocess, 'run') as execute:
                    apps.run('install', name, root)
                self.assertEqual(execute.call_args.kwargs['cwd'], root / 'apps' / relative)
                if name == 'api':
                    self.assertFalse((root / 'app' / relative / '.env').exists())

    def test_incomplete_new_layout_never_uses_legacy_application(self):
        for name, relative in apps.APPS.items():
            with self.subTest(application=name), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                (root / 'apps').mkdir()
                (root / 'app' / relative).mkdir(parents=True)
                with patch.object(apps.subprocess, 'run') as execute:
                    with self.assertRaisesRegex(ValueError, 'Application absente'):
                        apps.run('install', name, root)
                execute.assert_not_called()

    def test_absent_layout_never_launches_commands(self):
        with tempfile.TemporaryDirectory() as tmp:
            for name in apps.APPS:
                with self.subTest(application=name), patch.object(apps.subprocess, 'run') as execute:
                    with self.assertRaisesRegex(ValueError, 'Application absente'):
                        apps.run('install', name, Path(tmp))
                    execute.assert_not_called()

    def test_serve_and_check_use_selected_layout(self):
        for layout in ('app', 'apps'):
            for action in ('serve', 'check'):
                with self.subTest(layout=layout, action=action), tempfile.TemporaryDirectory() as tmp:
                    root = Path(tmp)
                    directory = root / layout / apps.APPS['web']
                    directory.mkdir(parents=True)
                    with patch.object(apps.subprocess, 'run') as execute:
                        apps.run(action, 'web', root)
                    self.assertTrue(execute.call_args_list)
                    self.assertTrue(all(call.kwargs['cwd'] == directory for call in execute.call_args_list))

    def test_openapi_drift_message_uses_selected_layout(self):
        for layout in ('app', 'apps'):
            with self.subTest(layout=layout), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                directory = root / layout / apps.APPS['api']
                directory.mkdir(parents=True)
                contract = directory / 'openapi.json'
                contract.write_text('{"paths": {}}')

                def execute(command, **kwargs):
                    if 'api:openapi:export' in command:
                        Path(command[-1].removeprefix('--output=')).write_text('{"paths": {"/new": {}}}')

                with patch.object(apps.subprocess, 'run', side_effect=execute):
                    with self.assertRaises(ValueError) as error:
                        apps.run('check', 'api', root)
                self.assertIn(f'{layout}/api/app/openapi.json', str(error.exception))
                self.assertEqual(contract.read_text(), '{"paths": {}}')
