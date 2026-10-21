import { test, expect } from '@playwright/test'

const api = process.env.TEST_API_URL || 'http://127.0.0.1:8000/api'

test('affiche un article réel, puis les états erreur et vide', async ({ page, request }) => {
  page.on('pageerror', error => console.log('PAGE ERROR', error.message))
  expect((await request.post('/api/articles', { data: {} })).status()).toBe(405)
  expect((await request.get('/api/articles?page=0')).status()).toBe(400)
  const title = `Lecture E2E ${Date.now()}`
  const created = await request.post(`${api}/articles`, {
    headers: { 'Content-Type': 'application/ld+json', Accept: 'application/ld+json' },
    data: { title, content: 'Un contenu visible.', published: true },
  })
  expect(created.status()).toBe(201)
  const article = await created.json()
  try {
    const response = await page.goto('/')
    expect(response?.status()).toBe(200)
    await expect(page.getByRole('heading', { name: title })).toBeVisible()
    await expect(page.getByText('Un contenu visible.')).toBeVisible()
    await page.screenshot({ path: 'test-results/webapp-desktop.png', fullPage: true })
    await page.route('**/api/articles?*', route => route.fulfill({ status: 503, body: '{}' }))
    await expect(page.getByRole('button', { name: 'Actualiser' })).toBeEnabled()
    await page.getByRole('button', { name: 'Actualiser' }).click()
    await expect(page.getByRole('alert')).toContainText('indisponibles')
    await page.unroute('**/api/articles?*')
    await page.route('**/api/articles?*', route => route.fulfill({ json: { member: [], totalItems: 0 } }))
    await page.getByRole('button', { name: 'Réessayer' }).click()
    await expect(page.getByRole('heading', { name: 'Tout commence par un premier article.' })).toBeVisible()
    await page.setViewportSize({ width: 390, height: 844 })
    expect(await page.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth)).toBe(true)
    await page.screenshot({ path: 'test-results/webapp-mobile.png', fullPage: true })
  } finally {
    await request.delete(`${api}/articles/${article.id}`)
  }
})
