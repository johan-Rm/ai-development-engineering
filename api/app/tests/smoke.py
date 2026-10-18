"""Contrat HTTP réel, avec base et serveur jetables ; aucune donnée locale modifiée."""
import json
import os
from pathlib import Path
import socket
import sqlite3
import subprocess
import tempfile
import time
import unittest
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]


class ArticleContract(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory(prefix='aiod-api-')
        cls.env = dict(os.environ, APP_ENV='dev', APP_DEBUG='0',
                       DATABASE_URL=f'sqlite:///{cls.tmp.name}/test.db')
        subprocess.run(['php', 'bin/console', 'doctrine:migrations:migrate', '-n'],
                       cwd=ROOT, env=cls.env, check=True, stdout=subprocess.DEVNULL)
        with socket.socket() as sock:
            sock.bind(('127.0.0.1', 0))
            port = sock.getsockname()[1]
        cls.base = f'http://127.0.0.1:{port}'
        cls.log = open(f'{cls.tmp.name}/server.log', 'w+')
        cls.server = subprocess.Popen(['php', '-d', 'variables_order=EGPCS', '-S', f'127.0.0.1:{port}', '-t', 'public',
                                       'public/router.php'], cwd=ROOT, env=cls.env,
                                      stdout=cls.log, stderr=cls.log)
        cls.addClassCleanup(cls.cleanup)
        for _ in range(100):
            try:
                if cls.request('GET', '/api/articles')[0] == 200:
                    return
            except (URLError, ConnectionError):
                pass
            time.sleep(0.1)
        cls.log.seek(0)
        raise RuntimeError(cls.log.read())

    @classmethod
    def cleanup(cls):
        cls.server.terminate()
        cls.server.wait(timeout=5)
        cls.log.close()
        cls.tmp.cleanup()

    @classmethod
    def request(cls, method, path, data=None, accept='application/ld+json'):
        headers = {'Accept': accept}
        if data is not None:
            headers['Content-Type'] = ('application/merge-patch+json' if method == 'PATCH'
                                       else 'application/ld+json')
        req = Request(cls.base + path, method=method, headers=headers,
                      data=None if data is None else json.dumps(data).encode())
        try:
            response = urlopen(req, timeout=10)
        except HTTPError as error:
            response = error
        with response:
            body = response.read()
            return response.status, json.loads(body) if body else None

    def test_crud_validation_pagination_and_docs(self):
        status, collection = self.request('GET', '/api/articles')
        self.assertEqual(status, 200)
        self.assertEqual(collection['totalItems'], 0)
        self.assertEqual(collection['member'], [])
        for title in ['', '   ', 'a' * 161]:
            self.assertEqual(self.request('POST', '/api/articles', {'title': title})[0], 422)
        status, article = self.request('POST', '/api/articles', {'title': 'Premier article'})
        self.assertEqual(status, 201)
        with sqlite3.connect(f'{self.tmp.name}/test.db') as db:
            self.assertEqual(db.execute('SELECT COUNT(*) FROM article').fetchone()[0], 1)
        self.assertEqual(article['content'], '')
        self.assertFalse(article['published'])
        path = article['@id']
        self.assertEqual(self.request('GET', path)[1]['title'], 'Premier article')
        status, updated = self.request('PATCH', path, {'title': 'Article modifié',
                                                      'content': 'Contenu', 'published': True})
        self.assertEqual(status, 200)
        self.assertTrue(updated['published'])
        self.assertEqual(self.request('PATCH', path, {'title': ' '})[0], 422)
        self.assertEqual(self.request('GET', path)[1]['title'], 'Article modifié')
        for i in range(20):
            self.assertEqual(self.request('POST', '/api/articles', {'title': f'Article {i}'})[0], 201)
        first = self.request('GET', '/api/articles')[1]
        second = self.request('GET', '/api/articles?page=2')[1]
        self.assertEqual(first['totalItems'], 21)
        self.assertEqual(len(first['member']), 20)
        self.assertEqual(len(second['member']), 1)
        self.assertEqual(self.request('DELETE', path)[0], 204)
        self.assertEqual(self.request('GET', path)[0], 404)
        status, docs = self.request('GET', '/api/docs.jsonopenapi',
                                    accept='application/vnd.openapi+json')
        self.assertEqual(status, 200)
        self.assertIn('/api/articles', docs['paths'])
        self.assertIn('post', docs['paths']['/api/articles'])


if __name__ == '__main__':
    unittest.main(verbosity=2)
