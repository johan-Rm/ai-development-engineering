#!/usr/bin/env python3
"""Explicit live-stack persistence recipe. Runs down/up and deletes only its own test article."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import time
import sys
import urllib.request

import apps


def request(info, method, endpoint, data=None):
    body = None if data is None else json.dumps(data).encode()
    headers = {'Host': f"api.{info['domain']}:{info['port']}", 'Accept': 'application/ld+json'}
    if body is not None:
        headers['Content-Type'] = 'application/ld+json'
    req = urllib.request.Request(f"http://127.0.0.1:{info['port']}{endpoint}", data=body, headers=headers, method=method)
    with urllib.request.urlopen(req, timeout=60) as response:
        raw = response.read()
        return response.status, json.loads(raw) if raw else None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--expect-empty', action='store_true')
    args = parser.parse_args()
    root = Path.cwd().resolve()
    info = apps.identity(root)
    envfiles = [p for p in [root / '.env', root / 'app/api/app/.env', root / 'app/backoffice/.env', root / 'app/web/targets/app/.env'] if p.is_file()]
    before = {p: hashlib.sha256(p.read_bytes()).hexdigest() for p in envfiles}
    before_diff = apps.git(root, 'diff', '--', 'app')
    _, initial = request(info, 'GET', '/api/articles')
    if args.expect_empty:
        assert initial['totalItems'] == 0, initial
    ids = apps.compose(info, ['ps', '-q'], capture=True).stdout.split()
    containers = json.loads(subprocess.check_output(['docker', 'inspect', *ids], text=True))
    observed = []
    for container in containers:
        service = container['Config']['Labels']['com.docker.compose.service']
        if service in ['api', 'web', 'backoffice']:
            assert container['Config']['User'] == f'{apps.os.getuid()}:{apps.os.getgid()}'
            source = next(m for m in container['Mounts'] if m['Destination'] == '/app')
            assert not source['RW']
            assert source['Source'].startswith(str(root / 'app') + '/')
            generated = ['/app/vendor', '/app/var'] if service == 'api' else ['/app/node_modules', '/app/.nuxt', '/app/.output']
            unexpected = subprocess.check_output(['docker', 'exec', container['Id'], 'find',
                                                 *generated, '-type', 'f', '-uid', '0', '-print', '-quit'], text=True)
            assert not unexpected, f'Fichier généré root dans {service}: {unexpected}'
        for mount in container['Mounts']:
            if mount['Type'] == 'volume':
                assert mount['Name'].startswith(info['project'] + '_')
        observed.append({'service': service, 'user': container['Config']['User'],
                         'mounts': [{k: m[k] for k in ['Type', 'Source', 'Destination', 'RW']} for m in container['Mounts']],
                         'networks': list(container['NetworkSettings']['Networks'])})
    marker = f"Persistance DEM-005 {info['layer']} {time.time_ns()}"
    status, article = request(info, 'POST', '/api/articles', {'title': marker, 'content': 'temporary runtime proof', 'published': True})
    assert status == 201
    try:
        subprocess.run(['python3', 'infra/apps.py', 'down'], check=True)
        subprocess.run(['python3', 'infra/apps.py', 'up', '--interface', 'both'], check=True)
        _, persisted = request(info, 'GET', f"/api/articles/{article['id']}")
        assert persisted['title'] == marker
    finally:
        try:
            request(info, 'DELETE', f"/api/articles/{article['id']}")
        except Exception as exc:
            print(f"Nettoyage différé de l’article de test {article['id']} : {exc}", file=sys.stderr)
    assert request(info, 'GET', '/api/articles')[1]['totalItems'] == initial['totalItems']
    assert apps.git(root, 'diff', '--', 'app') == before_diff
    assert all(hashlib.sha256(p.read_bytes()).hexdigest() == digest for p, digest in before.items())
    result = {'layer': info['layer'], 'port': info['port'], 'initialTotal': initial['totalItems'],
              'persistence': True, 'envPreserved': True, 'applicationDiffPreserved': True, 'rootOwnedGeneratedFiles': False,
              'containers': observed}
    Path(f"/tmp/DEM-005-runtime-{info['layer']}.json").write_text(json.dumps(result, indent=2))
    print(json.dumps({k: v for k, v in result.items() if k != 'containers'}))


if __name__ == '__main__':
    main()
