export default defineEventHandler((event) => {
  const id = getRouterParam(event, 'id')
  if (!id || !/^[1-9]\d*$/.test(id)) {
    throw createError({ statusCode: 400, statusMessage: 'Identifiant invalide' })
  }
  return forwardArticles(event, id)
})
