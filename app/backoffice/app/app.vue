<script setup lang="ts">
import type { Article, ArticleCollection } from './types/articles'

const hydrated = ref(false)
onMounted(() => { hydrated.value = true })
const page = ref(1)
const { data, status, error, refresh } = await useFetch<ArticleCollection>('/api/articles', {
  query: { page },
})
const articles = computed(() => data.value?.member ?? [])
const total = computed(() => data.value?.totalItems ?? 0)
const pages = computed(() => Math.max(1, Math.ceil(total.value / 20)))
const published = computed(() => articles.value.filter(article => article.published).length)
const form = reactive({ title: '', content: '', published: false })
const editing = ref<number | null>(null)
const busy = ref(false)
const formError = ref('')
const message = ref('')
const titleInput = ref<HTMLInputElement | null>(null)

function clearForm() {
  editing.value = null
  form.title = ''
  form.content = ''
  form.published = false
  formError.value = ''
}

function edit(article: Article) {
  editing.value = article.id
  Object.assign(form, { title: article.title, content: article.content, published: article.published })
  formError.value = ''
  message.value = ''
  titleInput.value?.focus()
}

function newArticle() {
  clearForm()
  titleInput.value?.focus()
}

function explainError(cause: unknown) {
  const details = (cause as { data?: { violations?: { message: string }[] } })?.data
  return details?.violations?.map(item => item.message).join(' ') ||
    'L’enregistrement a échoué. Vérifiez la connexion à l’API et réessayez.'
}

async function save() {
  if (busy.value) return
  formError.value = ''
  message.value = ''
  if (!form.title.trim() || form.title.trim().length > 160) {
    formError.value = 'Le titre doit contenir entre 1 et 160 caractères.'
    return
  }
  busy.value = true
  try {
    const id = editing.value
    await $fetch(`/api/articles${id === null ? '' : `/${id}`}`, {
      method: id === null ? 'POST' : 'PATCH',
      headers: { 'Content-Type': id === null ? 'application/ld+json' : 'application/merge-patch+json' },
      body: { ...form, title: form.title.trim() },
    })
    clearForm()
    message.value = id === null ? 'Article créé.' : 'Article modifié.'
    page.value = 1
    await refresh()
  } catch (cause) {
    formError.value = explainError(cause)
  } finally {
    busy.value = false
  }
}

async function remove(article: Article) {
  if (busy.value || !window.confirm(`Supprimer « ${article.title} » ?`)) return
  busy.value = true
  formError.value = ''
  message.value = ''
  try {
    await $fetch(`/api/articles/${article.id}`, { method: 'DELETE' })
    if (editing.value === article.id) clearForm()
    message.value = 'Article supprimé.'
    if (articles.value.length === 1 && page.value > 1) page.value--
    await refresh()
  } catch {
    formError.value = 'La suppression a échoué. Réessayez.'
  } finally {
    busy.value = false
  }
}
</script>

<template>
  <div class="layout">
    <aside class="sidebar"><a href="/" class="brand">atelier<span> / dashboard</span></a><p class="nav-label">VOTRE ESPACE</p><a href="#articles" class="nav-item" aria-current="page"><span aria-hidden="true">▤</span> Articles</a><div class="sidebar-foot"><span class="dot" /> Environnement local</div></aside>
    <main>
      <header class="topbar"><span>Vue d’ensemble <span aria-hidden="true">/</span> Articles</span><span class="tag">Administration</span></header>
      <section class="heading"><div><p class="eyebrow">VOTRE CONTENU, SIMPLEMENT</p><h1>Les articles.</h1><p>Créez, organisez et donnez vie à vos idées.</p></div><button class="primary" :disabled="!hydrated || busy" @click="newArticle">+ Nouvel article</button></section>
      <div class="stats"><div class="stat"><span>Total des articles</span><strong>{{ total }}</strong></div><div class="stat"><span>Publiés sur cette page</span><strong>{{ published }}</strong></div><div class="stat"><span>Brouillons sur cette page</span><strong>{{ articles.length - published }}</strong></div></div>
      <p v-if="message" class="success" role="status">{{ message }}</p>
      <div class="workspace">
        <section id="articles" class="panel" aria-labelledby="articles-title" :aria-busy="status === 'pending'">
          <div class="panel-heading"><h2 id="articles-title">Tous les articles</h2><button :disabled="!hydrated || busy || status === 'pending'" @click="refresh()">Actualiser</button></div>
          <p v-if="status === 'pending'" class="panel-state" role="status">Chargement…</p>
          <div v-else-if="error" class="panel-state" role="alert"><p>La liste est indisponible.</p><button @click="refresh()">Réessayer</button></div>
          <div v-else-if="!articles.length" class="panel-state empty"><span aria-hidden="true">✳</span><h3>Votre premier article vous attend.</h3><p>Commencez avec le formulaire ci-contre.</p></div>
          <ul v-else class="article-list"><li v-for="article in articles" :key="article.id"><div class="article-info"><h3>{{ article.title }}</h3><span class="badge" :class="{ published: article.published }">{{ article.published ? 'Publié' : 'Brouillon' }}</span></div><div class="actions"><button :disabled="!hydrated || busy" :aria-label="`Modifier ${article.title}`" @click="edit(article)">Modifier</button><button class="danger" :disabled="!hydrated || busy" :aria-label="`Supprimer ${article.title}`" @click="remove(article)">Supprimer</button></div></li></ul>
          <nav v-if="!error && pages > 1" class="pagination" aria-label="Pagination des articles"><button :disabled="page <= 1 || busy || status === 'pending'" @click="page--">Précédent</button><span>{{ page }} / {{ pages }}</span><button :disabled="page >= pages || busy || status === 'pending'" @click="page++">Suivant</button></nav>
        </section>
        <section class="panel editor" aria-labelledby="form-title"><p class="eyebrow">À VOUS D’ÉCRIRE</p><h2 id="form-title">{{ editing === null ? 'Nouvel article' : 'Modifier l’article' }}</h2><form @submit.prevent="save"><fieldset :disabled="!hydrated || busy"><label for="title">Titre <span aria-hidden="true">*</span></label><input id="title" ref="titleInput" v-model="form.title" required maxlength="160" placeholder="Une idée à partager" :aria-invalid="!!formError" :aria-describedby="formError ? 'form-error' : undefined"><label for="content">Contenu</label><textarea id="content" v-model="form.content" rows="6" placeholder="Les premières lignes de votre article…" /><label class="check" for="published"><input id="published" v-model="form.published" type="checkbox"> Publier cet article</label><p v-if="formError" id="form-error" class="error" role="alert">{{ formError }}</p><div class="form-actions"><button class="primary" type="submit">{{ busy ? 'Enregistrement…' : editing === null ? 'Créer l’article' : 'Enregistrer' }}</button><button v-if="editing !== null" type="button" @click="clearForm">Annuler</button></div></fieldset></form></section>
      </div>
      <footer>Un espace pour construire. Une idée après l’autre.</footer>
    </main>
  </div>
</template>
