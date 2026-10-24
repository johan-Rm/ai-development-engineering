# Installer et adapter AIDE

> Préparer les outils du dépôt, puis adapter les couches et les contrôles aux besoins du projet.

## Prérequis

Git et Python 3.12 ou supérieur pour l’outillage. Pour les applications fournies : PHP 8.4 ou supérieur avec PDO SQLite, SQLite3, mbstring et XML, Composer 2, Node.js 22.12 ou supérieur et npm. Un accès aux registres est nécessaire à l’installation.

Docker et Compose servent uniquement à la recette d’isolation ; les applications tournent sur l’hôte.

## Lancer les applications de démonstration

Depuis la racine du clone ou du worktree :

```sh
python3 codebase-quality-control/scripts/apps.py install all
```

Les fichiers `.env` existants sont conservés. Dans trois terminaux, depuis cette même racine :

```sh
python3 codebase-quality-control/scripts/apps.py serve api
python3 codebase-quality-control/scripts/apps.py serve web
python3 codebase-quality-control/scripts/apps.py serve backoffice
```

| Application | Adresse |
| --- | --- |
| API | http://127.0.0.1:8000/api/docs |
| Web | http://127.0.0.1:3000 |
| Backoffice | http://127.0.0.1:3001 |

L’API applique ses migrations et utilise `app/api/app/var/app.db`. Aucun article n’est créé automatiquement. Arrêter chaque processus avec Ctrl+C.

Chaque worktree dispose de ses propres dépendances. Installer uniquement l’application nécessaire avec `install api`, `install web` ou `install backoffice`. Les scripts acceptent aussi `--root chemin/du/worktree`.

Les ports applicatifs ne sont pas attribués automatiquement par couche. Avant de lancer plusieurs instances, adapter les ports et `NUXT_API_BASE` selon les README des applications.

## Exécuter les contrôles

```sh
python3 codebase-quality-control/scripts/check.py
python3 codebase-quality-control/scripts/quality.py
```

La première commande vérifie l’outillage sans dépendances applicatives ; un test nécessite un port HTTP local temporaire. La seconde vérifie aussi les trois applications et demande leurs dépendances installées.

Pour les parcours navigateur, démarrer l’API de développement, puis :

```sh
(cd app/web/targets/app && npx playwright install --with-deps chromium)
python3 codebase-quality-control/scripts/apps.py check web --browser
python3 codebase-quality-control/scripts/apps.py check backoffice --browser
```

Ces tests créent puis suppriment des articles. Utiliser une API de développement. Les [points de contrôle](docs/01-codebase-quality-control/points-de-controle.md) décrivent les commandes et leur portée ; la [recette Docker](dev-book/runbooks/recette-aiod.md) vérifie séparément les témoins d’isolation.

## Adapter au projet

1. Lire [AGENTS.md](AGENTS.md) et les README existants ; préserver les consignes, fichiers et environnements du projet d’accueil.
2. Définir les [couches](docs/02-cadre/couches.md), leurs responsabilités, branches et chemins. Adapter ensemble cette table et `codebase-quality-control/scripts/aiod.json`.
3. Compléter les instructions et examiner `.codex/config.toml`. Les skills personnels restent externes ; leur mention ne les installe pas.
4. Définir les conventions techniques dans les README locaux, puis implémenter les contrôles par la consolidation autorisée.
5. Adapter les commandes de qualité et la CI. Vérifier les protections GitHub si les tests doivent bloquer la fusion ; aucun déploiement n’est fourni.
6. Conserver ou remplacer explicitement les exemples Article, Symfony/API Platform, Nuxt et la marque Graines Digitales. Mettre à jour ensemble les contrats, tests et références concernés.
7. Choisir le sort des cartes historiques dans la copie adoptée ; ne pas les reprendre comme des missions actives. Affecter une première tâche et produire ses preuves.

Le dépôt doit posséder un premier commit avant la création des worktrees. Les scripts ne copient pas les `.env`, ne démarrent pas les services lors de la création Git et ne synchronisent pas le remote.

`docs_save/` est la sauvegarde temporaire de l’ancienne documentation pendant sa relecture. Elle n’est pas une seconde source de règles actives.
