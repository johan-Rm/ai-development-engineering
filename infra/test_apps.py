"""Behavior tests for the local stack launcher; no Integrity checker is changed."""
import importlib.util
import json
import os
from pathlib import Path
import socket
import subprocess
import tempfile
import unittest
from unittest.mock import patch

SPEC = importlib.util.spec_from_file_location('stack_apps', Path(__file__).with_name('apps.py'))
apps = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(apps)
ROOT = Path(__file__).resolve().parent.parent


class LauncherTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory(prefix='aide-stack-test-')
        cls.main = Path(cls.temp.name) / 'main'
        cls.main.mkdir()
        def git(*args):
            subprocess.run(['git', '-C', str(cls.main), *args], check=True, capture_output=True)
        git('init', '-b', 'develop')
        (cls.main / 'config').mkdir()
        (cls.main / 'config/layers.json').write_text((ROOT / 'config/layers.json').read_text())
        git('add', 'config/layers.json')
        git('-c', 'user.name=Stack test', '-c', 'user.email=test@example.invalid', 'commit', '-m', 'fixture')
        cls.wt = Path(cls.temp.name) / 'api'
        git('worktree', 'add', '-b', 'layers/api', str(cls.wt))

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    def test_registered_layer_identity(self):
        info = apps.identity(self.wt)
        self.assertEqual(info['layer'], 'api')
        self.assertEqual(info['domain'], 'wt-api.localhost')
        self.assertEqual(info['port'], 19302)
        self.assertEqual(apps.identity(self.wt, 20000)['port'], 20002)

    def test_main_repository_and_invalid_port_refused(self):
        with self.assertRaises(apps.StackError):
            apps.identity(self.main)
        with self.assertRaises(apps.StackError):
            apps.identity(self.wt, 65535)

    def test_wrong_branch_and_detached_head_refused(self):
        real_git = apps.git
        for branch in ['develop', 'master', '', 'feature/foreign']:
            with self.subTest(branch=branch):
                def fake_git(root, *args):
                    return branch if args == ('branch', '--show-current') else real_git(root, *args)
                with patch.object(apps, 'git', side_effect=fake_git), self.assertRaises(apps.StackError):
                    apps.identity(self.wt)

    def test_compose_environment_does_not_read_or_override_env_files(self):
        envfile = self.wt / '.env'
        envfile.write_text('SENTINEL=preserved\n')
        info = apps.identity(self.wt)
        with patch.dict(os.environ, {'COMPOSE_FILE': '/foreign', 'COMPOSE_PROFILES': '*', 'AIDE_APP_ROOT': '/foreign'}):
            env = apps.environment(info)
            self.assertNotIn('COMPOSE_FILE', env)
            self.assertNotIn('COMPOSE_PROFILES', env)
            self.assertEqual(env['AIDE_APP_ROOT'], str(self.wt))
        command = apps.compose_command(info)
        self.assertEqual(command[command.index('--env-file') + 1], '/dev/null')
        self.assertEqual(envfile.read_text(), 'SENTINEL=preserved\n')

    def test_collision_reports_error_without_stopping_any_service(self):
        with socket.socket() as listener:
            listener.bind(('127.0.0.1', 0))
            info = apps.identity(self.wt)
            info['port'] = listener.getsockname()[1]
            with patch.object(apps, 'compose', return_value=subprocess.CompletedProcess([], 0, stdout='')) as mocked:
                with self.assertRaisesRegex(apps.StackError, 'occupé'):
                    apps.check_port(info)
                self.assertEqual(mocked.call_count, 1)
                self.assertEqual(mocked.call_args.args[1], ['ps', '-q', 'caddy'])

    def test_recently_closed_connection_does_not_block_restart(self):
        with socket.socket() as listener:
            listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            listener.bind(('127.0.0.1', 0))
            listener.listen()
            port = listener.getsockname()[1]
            with socket.create_connection(('127.0.0.1', port)) as client:
                connection, _ = listener.accept()
                connection.close()
        info = apps.identity(self.wt)
        info['port'] = port
        with patch.object(apps, 'compose', return_value=subprocess.CompletedProcess([], 0, stdout='')):
            apps.check_port(info)

    def test_mountpoints_belong_to_caller_and_do_not_touch_source_or_env(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            for source in ['app/api/app', 'app/web/targets/app', 'app/backoffice']:
                (root / source).mkdir(parents=True)
            envfile = root / 'app/api/app/.env'
            apps.prepare_mountpoints({'root': str(root)}, 'web')
            self.assertFalse(envfile.exists())
            envfile.write_text('preserve')
            apps.prepare_mountpoints({'root': str(root)}, 'web')
            self.assertEqual(envfile.read_text(), 'preserve')
            self.assertEqual((root / 'app/web/targets/app/node_modules').stat().st_uid, os.getuid())
            self.assertFalse((root / 'app/backoffice/node_modules').exists())
            link = root / 'app/backoffice/node_modules'
            link.symlink_to(root / 'app/web/targets/app/node_modules')
            with self.assertRaises(apps.StackError):
                apps.prepare_mountpoints({'root': str(root)}, 'backoffice')

    def test_browser_recipe_exposes_only_script_artifacts_and_optional_three_files(self):
        import sys
        with patch.dict(sys.modules, {'apps': apps}):
            spec = importlib.util.spec_from_file_location('browser_recipe', ROOT / 'infra/browser.py')
            browser = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(browser)
        for reload, expected in [(False, 2), (True, 5)]:
            command = browser.command_for(ROOT, {'layer': 'api', 'port': 19302, 'image_key': 'test'}, Path('/tmp/artifacts'), reload)
            mounts = [command[i + 1] for i, arg in enumerate(command) if arg == '--mount']
            self.assertEqual(len(mounts), expected)
            self.assertFalse(any(f'source={ROOT},' in mount for mount in mounts))
            self.assertFalse(any('.env' in mount for mount in mounts))
            self.assertTrue(mounts[0].endswith(',readonly'))
            self.assertIn('aide-app-browser:test', command)

    def test_fifteen_compose_configurations(self):
        layers = json.loads((ROOT / 'config/layers.json').read_text())['layers']
        projects, ports = set(), set()
        for layer, data in layers.items():
            info = apps.identity(self.wt)
            info.update(root=str(ROOT), layer=layer, project=f'test-app-{layer}',
                        domain=f'wt-{layer}.localhost', port=19300 + data['id'])
            projects.add(info['project'])
            ports.add(info['port'])
            for interface in ['web', 'backoffice', 'both']:
                with self.subTest(layer=layer, interface=interface):
                    result = apps.compose(info, ['config', '--format', 'json'], interface, capture=True)
                    config = json.loads(result.stdout)
                    services = config['services']
                    expected = {'init', 'api', 'caddy'} | ({'web', 'backoffice'} if interface == 'both' else {interface})
                    self.assertEqual(set(services), expected)
                    binding = services['caddy']['ports'][0]
                    self.assertEqual(binding['host_ip'], '127.0.0.1')
                    self.assertEqual(str(binding['published']), str(info['port']))
                    self.assertEqual(services['api']['environment']['DATABASE_URL'], 'sqlite:////app/var/app.db')
                    self.assertTrue(services['api']['volumes'][0]['read_only'])
                    self.assertEqual(json.loads(services['api']['environment']['APP_RUNTIME_OPTIONS'])['dotenv_path'], '.env.example')
                    self.assertNotIn('/app/.env', [m['target'] for m in services['api']['volumes']])
        self.assertEqual(len(projects), 5)
        self.assertEqual(len(ports), 5)


if __name__ == '__main__':
    unittest.main()
