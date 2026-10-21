# Installer, lancer, vérifier

Prérequis : Git, Python 3, PHP >= 8.4 avec PDO SQLite, SQLite3, mbstring et XML, Composer 2, Node >= 22.12 et npm. Accès aux registres requis à l’installation. Utiliser les versions verrouillées par Composer et npm.

Depuis la racine du clone ou du worktree contenant les applications :

```sh
python3 codebase-quality-control/scripts/apps.py install all
```

L’installation conserve tout `.env` existant et crée celui de l’API s’il manque. Ensuite, dans trois terminaux à la même racine :

```sh
python3 codebase-quality-control/scripts/apps.py serve api
```

```sh
python3 codebase-quality-control/scripts/apps.py serve web
```

```sh
python3 codebase-quality-control/scripts/apps.py serve backoffice
```

L’API applique ses migrations puis écoute sur http://127.0.0.1:8000/api/docs ; la webapp sur http://127.0.0.1:3000 et le dashboard sur http://127.0.0.1:3001. Chaque processus s’arrête avec Ctrl+C. SQLite persiste dans `api/app/var/app.db`. Aucun article n’est créé automatiquement.

```sh
python3 codebase-quality-control/scripts/quality.py
```

Pour Playwright, API démarrée sur le port 8000 :

```sh
cd web/targets/app
npx playwright install --with-deps chromium
cd ../../..
python3 codebase-quality-control/scripts/apps.py check web --browser
python3 codebase-quality-control/scripts/apps.py check backoffice --browser
```

Les tests navigateur créent puis suppriment des articles dans cette API de développement. Ne pas viser une API de production.

## Travailler dans les worktrees

Chaque worktree contient une copie complète du dépôt, avec ses propres dépendances et sa configuration. Installer uniquement l’application utile avec `python3 codebase-quality-control/scripts/apps.py install api` (ou `web`, `backoffice`), depuis ce worktree. Les commandes prennent aussi `--root chemin/du/worktree`.

Lancer une seule instance de chaque application sur les ports par défaut. Pour plusieurs instances, adapter les commandes Nuxt/PHP et `NUXT_API_BASE` selon les README applicatifs ; les ports des applications ne sont pas attribués automatiquement par l’outillage AIOD.

Les applications se lancent actuellement sur l’hôte. Les conteneurs Docker fournis servent à la recette d’isolation du processus, indépendamment des applications : [infrastructure](../infra/README.md).
