// Explicit live-stack recipe; Make performs all lifecycle actions directly through Compose.
const { execFileSync } = require('node:child_process')
const fs = require('node:fs')
const path = require('node:path')
const crypto = require('node:crypto')
const http = require('node:http')
const assert = require('node:assert/strict')
const run = (file, args) => execFileSync(file, args, { encoding: 'utf8' }).trim()
const make = args => execFileSync('make', ['--no-print-directory', ...args], { stdio: 'inherit' })
const info = Object.fromEntries(run('make', ['--no-print-directory', 'info']).split('\n').map(line => {
  const equals = line.indexOf('=')
  return [line.slice(0, equals), line.slice(equals + 1)]
}))
const digest = file => crypto.createHash('sha256').update(fs.readFileSync(file)).digest('hex')
function request(method, endpoint, data) {
  return new Promise((resolve, reject) => {
    const body = data === undefined ? undefined : JSON.stringify(data)
    const req = http.request({ agent: false, hostname: '127.0.0.1', port: Number(info.port), path: endpoint, method,
      headers: { Host: `api.${info.domain}:${info.port}`, Accept: 'application/ld+json',
        ...(body ? { 'Content-Type': 'application/ld+json', 'Content-Length': Buffer.byteLength(body) } : {}) } }, response => {
      let raw = ''
      response.setEncoding('utf8')
      response.on('data', chunk => { raw += chunk })
      response.on('end', () => {
        try { resolve({ status: response.statusCode, data: raw ? JSON.parse(raw) : null }) } catch (error) { reject(error) }
      })
    })
    req.setTimeout(60000, () => req.destroy(new Error('HTTP timeout')))
    req.on('error', reject)
    req.end(body)
  })
}
async function main() {
  const files = ['.env', 'app/api/app/.env', 'app/backoffice/.env', 'app/web/targets/app/.env'].map(p => path.join(info.root, p))
  const before = files.map(file => fs.existsSync(file) ? digest(file) : null)
  const diff = run('git', ['diff', '--', 'app'])
  const initial = await request('GET', '/api/articles')
  assert.equal(initial.status, 200)
  if (process.env.EXPECT_EMPTY === '1') assert.equal(initial.data.totalItems, 0)
  const ids = run('docker', ['ps', '-q', '--filter', `label=com.docker.compose.project=${info.project}`]).split(/\s+/).filter(Boolean)
  assert.ok(ids.length)
  const containers = JSON.parse(run('docker', ['inspect', ...ids]))
  for (const container of containers) {
    const service = container.Config.Labels['com.docker.compose.service']
    if (['api', 'web', 'backoffice'].includes(service)) {
      assert.equal(container.Config.User, `${process.getuid()}:${process.getgid()}`)
      const source = container.Mounts.find(m => m.Destination === '/app')
      assert.equal(source.RW, false)
      assert.ok(source.Source.startsWith(`${info.root}/app/`))
      const generated = service === 'api' ? ['/app/vendor', '/app/var'] : ['/app/node_modules', '/app/.nuxt', '/app/.output']
      assert.equal(run('docker', ['exec', container.Id, 'find', ...generated, '-type', 'f', '-uid', '0', '-print', '-quit']), '')
    }
    for (const mount of container.Mounts) if (mount.Type === 'volume') assert.ok(mount.Name.startsWith(`${info.project}_`))
  }
  const title = `Persistance Make DEM005 ${info.layer} ${Date.now()}`
  const article = await request('POST', '/api/articles', { title, content: 'Temporary Make proof', published: true })
  assert.equal(article.status, 201)
  try {
    make(['down'])
    make(['up', 'INTERFACE=both'])
    const persisted = await request('GET', `/api/articles/${article.data.id}`)
    assert.equal(persisted.status, 200)
    assert.equal(persisted.data.title, title)
  } finally {
    try { assert.equal((await request('DELETE', `/api/articles/${article.data.id}`)).status, 204) }
    catch (error) { console.error(`Nettoyage différé de l’article ${article.data.id}:`, error.message); throw error }
  }
  assert.equal((await request('GET', '/api/articles')).data.totalItems, initial.data.totalItems)
  assert.equal(run('git', ['diff', '--', 'app']), diff)
  for (const [i, file] of files.entries()) assert.equal(fs.existsSync(file) ? digest(file) : null, before[i])
  const result = { layer: info.layer, port: Number(info.port), initialTotal: initial.data.totalItems,
    persistence: true, envPreserved: true, applicationDiffPreserved: true, rootOwnedGeneratedFiles: false,
    containers: containers.map(c => ({ service: c.Config.Labels['com.docker.compose.service'], user: c.Config.User,
      mounts: c.Mounts.map(m => ({ Type: m.Type, Source: m.Source, Destination: m.Destination, RW: m.RW })),
      networks: Object.keys(c.NetworkSettings.Networks) })) }
  fs.writeFileSync(`/tmp/DEM-005-make-runtime-${info.layer}.json`, JSON.stringify(result, null, 2))
  console.log(JSON.stringify({ ...result, containers: undefined }))
}
main().catch(error => { console.error(error); process.exitCode = 1 })
