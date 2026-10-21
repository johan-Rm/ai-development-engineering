# Web — mini webapp Nuxt

Application Nuxt 4 / Vue 3 / TypeScript avec rendu serveur, dans `targets/app/`.
Couche `web`. Node >= 22.12 et npm requis.

Depuis la racine du dépôt ou du worktree concerné, entrer dans `web/targets/app/` :

```sh
cd web/targets/app
npm ci
npm run dev
```

Ouvrir http://127.0.0.1:3000. Démarrer séparément l'API sur 127.0.0.1:8000
(voir `api/README.md` dans le worktree API). Sans API, l'écran présente une erreur et un bouton Réessayer.
Aucune donnée de démonstration n'est injectée. Liste vide, chargement et pagination sont prévus.
Le témoin `scripts/process.py` reste indépendant de l'application.

## Configuration et contrat

Copier `.env.example` vers `.env` uniquement si nécessaire, sans remplacer un fichier existant.
`NUXT_API_BASE` désigne la racine de l'API (défaut `http://127.0.0.1:8000/api`).
Cette valeur reste côté serveur. Le navigateur interroge GET `/api/articles?page=1`,
un proxy Nuxt limité à la collection des articles. Les mutations ne sont pas exposées par la webapp.
Le contrat JSON-LD attend `member`, `totalItems` et les champs `id`, `title`, `content`, `published`.
La liste inclut les brouillons dans ce boilerplate de développement ; aucune authentification.

Le contrat API est versionné dans `api/app/openapi.json`.
Le dossier `web/shared/` pourra accueillir un socle commun quand une autre cible en aura besoin.

## Vérifier et construire

```sh
npm run typecheck
npm run build
npm run preview
# API démarrée ; installe le navigateur à la première exécution :
npx playwright install chromium
npm run test:e2e
```

Le test navigateur crée un article temporaire puis le supprime, vérifie la lecture réelle,
les états erreur et vide simulés, et l'absence de débordement mobile. Il démarre Nuxt si nécessaire.
`TEST_API_URL` permet de choisir l'API de test. Utiliser une API locale de développement.
`package-lock.json` verrouille les versions, `npm ci` reproduit l'installation.

Pour lancer le build directement : `NITRO_HOST=127.0.0.1 NITRO_PORT=3000 node .output/server/index.mjs`.
Dans ce cas, fournir `NUXT_API_BASE` dans l'environnement du processus si la valeur par défaut ne convient pas.

Documentation officielle : [Nuxt](https://nuxt.com/docs/4.x/getting-started/introduction).

## Dépendances

Nuxt est fixé à 4.6.2. L'audit npm de cette session signale des alertes transitives,
notamment `braces` et `node-forge`. La correction automatique rétrograde Nuxt et ajoute
alors des alertes critiques ; elle n'est pas retenue. Réévaluer avec `npm audit` avant
un usage autre que ce socle local. DevTools est désactivé et les serveurs de développement
écoutent seulement sur 127.0.0.1.
