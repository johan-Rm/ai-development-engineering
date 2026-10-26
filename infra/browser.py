#!/usr/bin/env python3
"""Run the live browser recipe in Docker on Linux, without installing system packages."""
import argparse
import os
from pathlib import Path
import subprocess
import apps

def command_for(root, info, artifacts, reload=False):
    command = ['docker', 'run', '--rm', '--network', 'host', '--ipc', 'host',
               '--user', f'{os.getuid()}:{os.getgid()}', '-e', 'HOME=/tmp',
               '-e', 'AIDE_PLAYWRIGHT_MODULE=/opt/aide-browser/node_modules/@playwright/test',
               '-e', 'AIDE_BROWSER_ARTIFACT_DIR=/artifacts',
               '--mount', f'type=bind,source={root / "infra/test-browser.cjs"},target=/recipe/test-browser.cjs,readonly',
               '--mount', f'type=bind,source={artifacts},target=/artifacts',
               '-w', '/tmp']
    for service in ['api', 'web', 'backoffice']:
        command += ['--add-host', f"{service}.wt-{info['layer']}.localhost:127.0.0.1"]
    if reload:
        command += ['-e', 'AIDE_RELOAD_SOURCE_DIR=/sources']
        for relative, name in [('app/web/targets/app/app/app.vue', 'web.vue'),
                               ('app/backoffice/app/app.vue', 'backoffice.vue'),
                               ('app/api/app/public/router.php', 'router.php')]:
            command += ['--mount', f'type=bind,source={root / relative},target=/sources/{name}']
    command += [f"aide-app-browser:{info['image_key']}",
               'node', '/recipe/test-browser.cjs', info['layer'], str(info['port'])]
    if reload:
        command.append('--reload')
    return command


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--reload', action='store_true')
    args = parser.parse_args()
    root = Path(__file__).resolve().parent.parent
    if Path.cwd().resolve() != root:
        raise SystemExit('Exécuter depuis la racine de ce worktree.')
    info = apps.identity(root)
    artifacts = Path('/tmp/DEM-005-browser-artifacts')
    artifacts.mkdir(exist_ok=True)
    subprocess.run(['docker', 'build', '-f', str(root / 'infra/Dockerfile.browser'),
                    '-t', f"aide-app-browser:{info['image_key']}", str(root / 'infra')], check=True)
    subprocess.run(command_for(root, info, artifacts, args.reload), check=True)


if __name__ == '__main__':
    main()
