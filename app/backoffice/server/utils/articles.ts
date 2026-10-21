import type { H3Event } from 'h3'

export function forwardArticles(event: H3Event, id?: string) {
  const method = getMethod(event)
  const allowed = id ? ['GET', 'PATCH', 'DELETE'] : ['GET', 'POST']
  if (!allowed.includes(method)) {
    setHeader(event, 'Allow', allowed.join(', '))
    throw createError({ statusCode: 405, statusMessage: 'Méthode non autorisée' })
  }
  const page = getQuery(event).page ?? '1'
  if (typeof page !== 'string' || !/^[1-9]\d*$/.test(page)) {
    throw createError({ statusCode: 400, statusMessage: 'Page invalide' })
  }
  const base = useRuntimeConfig(event).apiBase.replace(/\/$/, '')
  const target = id ? `${base}/articles/${id}` : `${base}/articles?page=${page}`
  return proxyRequest(event, target, {
    headers: {
      accept: 'application/ld+json',
      ...(method === 'POST' ? { 'content-type': 'application/ld+json' } : {}),
      ...(method === 'PATCH' ? { 'content-type': 'application/merge-patch+json' } : {}),
    },
    fetchOptions: { signal: AbortSignal.timeout(8000) },
  })
}
