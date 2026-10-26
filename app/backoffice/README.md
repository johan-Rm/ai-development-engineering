# Dashboard — Nuxt

Mini administration Nuxt 4 / Vue 3 / TypeScript, avec rendu serveur.
Couche `backoffice`. Node >= 22.12 et npm requis.

Depuis la racine du dépôt ou du worktree concerné, entrer dans `app/backoffice/` :

```sh
cd backoffice
npm ci
npm run dev
```

Ouvrir http://127.0.0.1:3001. Démarrer séparément l'API sur 127.0.0.1:8000
(voir `api/README.md` dans le worktree API).
La liste dispose d'une pagination, d'états chargement, vide et erreur.
Le formulaire crée et modifie les articles ; la suppression demande confirmation.
Les saisies restent présentes en cas d'échec. Aucune donnée n'est injectée au lancement.
Le témoin `codebase-integrity/scripts/process.py` reste indépendant de l'application.

## Configuration et contrat

Copier `.env.example` vers `.env` seulement si nécessaire et sans remplacer un fichier existant.
`NUXT_API_BASE` désigne la racine de l'API (défaut `http://127.0.0.1:8000/api`) et reste côté serveur.
Les routes Nuxt `/api/articles` (GET, POST) et `/api/articles/{id}` (GET, PATCH, DELETE)
relaient uniquement ces opérations vers l'API, avec les types MIME JSON-LD et merge-patch attendus.
Le contrat attend une collection `member`, `totalItems` et des articles `id`, `title`, `content`, `published`.
Les compteurs « publiés » et « brouillons » portent sur la page courante, le total sur toute la collection.
Le contrat API est versionné dans `app/api/app/openapi.json`.

Ce boilerplate de développement local ne fournit pas d'authentification ni de contrôle de permissions.

## Vérifier et construire

```sh
npm run typecheck
npm run build
npm run preview
# API démarrée ; installer Chromium à la première exécution :
npx playwright install chromium
npm run test:e2e
```

Le test démarre Nuxt si nécessaire et crée un article temporaire via le formulaire,
le modifie, le publie et le supprime. Il vérifie aussi la conservation des saisies après
une panne simulée et l'absence de débordement mobile. Utiliser une API de développement locale.
Les versions sont verrouillées dans `package-lock.json` ; `npm ci` reproduit l'installation.

Pour lancer le build directement : `NITRO_HOST=127.0.0.1 NITRO_PORT=3001 node .output/server/index.mjs`.
Dans ce cas, fournir `NUXT_API_BASE` dans l'environnement du processus si nécessaire.

## Dépendances

Nuxt est fixé à 4.6.2. L'audit npm de cette session signale des alertes transitives,
notamment `braces` et `node-forge`. La correction automatique rétrograde Nuxt et ajoute
alors des alertes critiques ; elle n'est pas retenue. Réévaluer avec `npm audit` avant
un usage autre que ce socle local. DevTools est désactivé et les serveurs de développement
écoutent seulement sur 127.0.0.1.

Documentation officielle : [Nuxt](https://nuxt.com/docs/4.x/getting-started/introduction).
