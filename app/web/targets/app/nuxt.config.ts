export default defineNuxtConfig({
  compatibilityDate: '2026-10-18',
  devtools: { enabled: false },
  runtimeConfig: { apiBase: 'http://127.0.0.1:8000/api' },
  css: ['~/assets/main.css'],
  app: { head: { htmlAttrs: { lang: 'fr' }, title: 'Articles · Webapp' } },
})
