import type { H3Event } from 'h3'

export function forwardArticles(event: H3Event) {
  if (getMethod(event) !== 'GET') {
    setHeader(event, 'Allow', 'GET')
    throw createError({ statusCode: 405, statusMessage: 'Méthode non autorisée' })
  }
  const page = getQuery(event).page ?? '1'
  if (typeof page !== 'string' || !/^[1-9]\d*$/.test(page)) {
    throw createError({ statusCode: 400, statusMessage: 'Page invalide' })
  }
  const base = useRuntimeConfig(event).apiBase.replace(/\/$/, '')
  return proxyRequest(event, `${base}/articles?page=${page}`, {
    headers: { accept: 'application/ld+json' },
    fetchOptions: { signal: AbortSignal.timeout(8000) },
  })
}
