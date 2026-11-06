import { test, expect } from '@playwright/test'

test('crée, modifie et supprime un article via le dashboard', async ({ page, request }) => {
  const title = `Dashboard E2E ${Date.now()}`
  let id: number | undefined
  try {
    await page.goto('/')
    const create = page.getByRole('button', { name: 'Créer l’article' })
    await expect(create).toBeEnabled()
    await page.getByLabel('Titre').fill(title)
    await page.getByLabel('Contenu').fill('Contenu du dashboard.')
    const responsePromise = page.waitForResponse(response => response.url().endsWith('/api/articles') && response.request().method() === 'POST')
    await create.click()
    const response = await responsePromise
    expect(response.status()).toBe(201)
    id = (await response.json()).id
    await expect(page.getByRole('status').filter({ hasText: 'Article créé.' })).toBeVisible()
    await page.screenshot({ path: 'test-results/dashboard-desktop.png', fullPage: true })
    await page.getByRole('button', { name: `Modifier ${title}`, exact: true }).click()
    await expect(page.getByLabel('Contenu')).toHaveValue('Contenu du dashboard.')
    await page.getByLabel('Titre').fill(`${title} modifié`)
    await page.getByLabel('Publier cet article').check()
    await page.getByRole('button', { name: 'Enregistrer', exact: true }).click()
    await expect(page.getByRole('heading', { name: `${title} modifié`, exact: true })).toBeVisible()
    await expect(page.getByRole('status').filter({ hasText: 'Article modifié.' })).toBeVisible()
    await expect(page.getByRole('listitem').filter({ hasText: `${title} modifié` })).toContainText('Publié')
    await page.getByRole('button', { name: `Modifier ${title} modifié`, exact: true }).click()
    await page.route('**/api/articles/*', route => route.request().method() === 'PATCH'
      ? route.fulfill({ status: 503, json: {} }) : route.continue())
    await page.getByRole('button', { name: 'Enregistrer', exact: true }).click()
    await expect(page.getByRole('alert')).toContainText('L’enregistrement a échoué')
    await expect(page.getByLabel('Titre')).toHaveValue(`${title} modifié`)
    await page.unroute('**/api/articles/*')
    await page.getByRole('button', { name: 'Annuler', exact: true }).click()
    await page.setViewportSize({ width: 390, height: 844 })
    expect(await page.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth)).toBe(true)
    await page.screenshot({ path: 'test-results/dashboard-mobile.png', fullPage: true })
    page.once('dialog', dialog => dialog.accept())
    await page.getByRole('button', { name: `Supprimer ${title} modifié`, exact: true }).click()
    await expect(page.getByRole('status').filter({ hasText: 'Article supprimé.' })).toBeVisible()
    await expect(page.getByRole('heading', { name: `${title} modifié`, exact: true })).toHaveCount(0)
  } finally {
    if (id) await request.delete(`/api/articles/${id}`)
  }
})
