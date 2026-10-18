<script setup lang="ts">
import type { ArticleCollection } from './types/articles'

const hydrated = ref(false)
onMounted(() => { hydrated.value = true })
const page = ref(1)
const { data, status, error, refresh } = await useFetch<ArticleCollection>('/api/articles', {
  query: { page },
})
const articles = computed(() => data.value?.member ?? [])
const total = computed(() => data.value?.totalItems ?? 0)
const pages = computed(() => Math.max(1, Math.ceil(total.value / 20)))
</script>

<template>
  <div class="shell">
    <header class="topbar"><a class="brand" href="/">atelier<span> / webapp</span></a><span class="tag">Le point de départ</span></header>
    <main id="main">
      <section class="hero">
        <p class="eyebrow">ESPACE LECTURE</p>
        <h1>Les idées prennent<br>leur place ici.</h1>
        <p class="lead">Un espace simple pour parcourir les articles et construire la suite.</p>
      </section>
      <section aria-labelledby="articles-title" :aria-busy="status === 'pending'">
        <div class="section-heading"><h2 id="articles-title">Les articles <span class="count">{{ total }}</span></h2><button :disabled="!hydrated || status === 'pending'" @click="refresh()">Actualiser</button></div>
        <p v-if="status === 'pending'" role="status">Chargement des articles…</p>
        <div v-else-if="error" class="notice" role="alert"><h3>Les articles sont indisponibles.</h3><p>Réessayez dans quelques instants.</p><button @click="refresh()">Réessayer</button></div>
        <div v-else-if="!articles.length" class="empty"><span class="empty-icon" aria-hidden="true">✳</span><h3>Tout commence par un premier article.</h3><p>Les articles créés dans le dashboard apparaîtront ici.</p></div>
        <div v-else class="cards">
          <article v-for="article in articles" :key="article.id" class="card">
            <div class="card-top"><span class="eyebrow">ARTICLE {{ String(article.id).padStart(2, '0') }}</span><span class="badge">{{ article.published ? 'Publié' : 'Brouillon' }}</span></div>
            <h3>{{ article.title }}</h3><p class="content">{{ article.content || 'Cet article attend ses premières lignes.' }}</p>
          </article>
        </div>
        <nav v-if="!error && pages > 1" class="pagination" aria-label="Pagination des articles"><button :disabled="page <= 1 || status === 'pending'" @click="page--">Précédent</button><span>Page {{ page }} sur {{ pages }}</span><button :disabled="page >= pages || status === 'pending'" @click="page++">Suivant</button></nav>
      </section>
    </main>
    <footer>Un début simple. De la place pour la suite.</footer>
  </div>
</template>
