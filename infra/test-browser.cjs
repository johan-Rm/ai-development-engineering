// Optional real-browser recipe, also runnable in the isolated Playwright image.
const { chromium, expect } = require(process.env.AIDE_PLAYWRIGHT_MODULE || '../app/backoffice/node_modules/@playwright/test')
const fs = require('node:fs/promises')
const path = require('node:path')
const assert = require('node:assert/strict')

async function main() {
  const [layer, port] = process.argv.slice(2)
  if (!/^[a-z]+$/.test(layer || '') || !/^\d+$/.test(port || '')) throw new Error('Usage: node infra/test-browser.cjs <layer> <port> [--reload]')
  const base = name => `http://${name}.wt-${layer}.localhost:${port}`
  const browser = await chromium.launch({ headless: true })
  const context = await browser.newContext()
  const page = await context.newPage()
  const reader = await context.newPage()
  const errors = []
  page.on('pageerror', error => errors.push(error.message))
  reader.on('pageerror', error => errors.push(error.message))
  const title = `DEM-005 ${layer} ${Date.now()}`
  let id
  try {
    const collection = await context.request.get(`${base('api')}/api/articles`)
    assert.equal(collection.status(), 200)
    console.log(JSON.stringify({ layer, initialTotal: (await collection.json()).totalItems }))
    assert.equal((await page.goto(base('backoffice'), { timeout: 120000 })).status(), 200)
    await expect(page.getByRole('button', { name: 'Créer l’article' })).toBeEnabled({ timeout: 120000 })
    await page.getByLabel('Titre').fill(title)
    await page.getByLabel('Contenu').fill('Preuve Docker autonome DEM-005.')
    const created = page.waitForResponse(r => r.url().endsWith('/api/articles') && r.request().method() === 'POST')
    await page.getByRole('button', { name: 'Créer l’article' }).click()
    const response = await created
    assert.equal(response.status(), 201)
    id = (await response.json()).id
    await expect(page.getByRole('heading', { name: title, exact: true })).toBeVisible()
    assert.equal((await reader.goto(base('web'), { timeout: 120000 })).status(), 200)
    await expect(reader.getByRole('heading', { name: title, exact: true })).toBeVisible({ timeout: 120000 })
    await page.getByRole('button', { name: `Modifier ${title}`, exact: true }).click()
    await page.getByLabel('Titre').fill(`${title} modifié`)
    await page.getByLabel('Publier cet article').check()
    await page.getByRole('button', { name: 'Enregistrer', exact: true }).click()
    await expect(page.getByRole('heading', { name: `${title} modifié`, exact: true })).toBeVisible()
    await reader.getByRole('button', { name: 'Actualiser' }).click()
    await expect(reader.getByRole('heading', { name: `${title} modifié`, exact: true })).toBeVisible()
    await page.screenshot({ path: path.join(process.env.AIDE_BROWSER_ARTIFACT_DIR || '/tmp', `DEM-005-${layer}-backoffice.png`), fullPage: true })
    await reader.screenshot({ path: path.join(process.env.AIDE_BROWSER_ARTIFACT_DIR || '/tmp', `DEM-005-${layer}-web.png`), fullPage: true })
    if (process.argv.includes('--reload')) {
      // Temporarily edit only this worktree, and restore the exact bytes even on failure.
      for (const [relative, target] of [['app/web/targets/app/app/app.vue', reader], ['app/backoffice/app/app.vue', page]]) {
        const file = process.env.AIDE_RELOAD_SOURCE_DIR
          ? path.join(process.env.AIDE_RELOAD_SOURCE_DIR, relative.includes('backoffice') ? 'backoffice.vue' : 'web.vue')
          : path.join(process.cwd(), relative)
        const original = await fs.readFile(file)
        const marker = `Reload DEM005 ${layer} ${Date.now()}`
        const modified = original.toString().replace('<h1>', `<h1><span>${marker}</span>`)
        assert.notEqual(modified, original.toString())
        try {
          await fs.writeFile(file, modified)
          await expect(target.getByText(marker, { exact: true })).toBeVisible({ timeout: 120000 })
        } finally {
          await fs.writeFile(file, original)
        }
        await expect(target.getByText(marker, { exact: true })).toHaveCount(0, { timeout: 120000 })
        assert.deepEqual(await fs.readFile(file), original)
      }
      const file = process.env.AIDE_RELOAD_SOURCE_DIR
        ? path.join(process.env.AIDE_RELOAD_SOURCE_DIR, 'router.php')
        : path.join(process.cwd(), 'app/api/app/public/router.php')
      const original = await fs.readFile(file)
      try {
        const code = original.toString().replace('<?php', "<?php\nif ($_SERVER['REQUEST_URI'] === '/__aide_reload') { echo 'reload-dem005'; return; }")
        await fs.writeFile(file, code)
        await expect.poll(async () => {
          const response = await context.request.get(`${base('api')}/__aide_reload`)
          return response.text()
        }, { timeout: 15000 }).toBe('reload-dem005')
      } finally {
        await fs.writeFile(file, original)
      }
      assert.equal((await context.request.get(`${base('api')}/__aide_reload`)).status(), 404)
      assert.deepEqual(await fs.readFile(file), original)
      console.log(`${layer}: rechargement automatique web/backoffice et PHP observé ; sources restaurées`)
    }
    page.once('dialog', dialog => dialog.accept())
    await page.getByRole('button', { name: `Supprimer ${title} modifié`, exact: true }).click()
    await expect(page.getByRole('status').filter({ hasText: 'Article supprimé.' })).toBeVisible()
    assert.equal((await context.request.get(`${base('api')}/api/articles/${id}`)).status(), 404)
    id = undefined
    assert.deepEqual(errors, [])
    console.log(`${layer}: Caddy, CRUD navigateur et lecture web réussis`)
  } finally {
    if (id) await context.request.delete(`${base('api')}/api/articles/${id}`)
    await browser.close()
  }
}
main().catch(error => { console.error(error); process.exitCode = 1 })
