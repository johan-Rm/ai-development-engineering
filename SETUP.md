# Installer et adapter AIDE

> Préparer les outils du dépôt, puis adapter les couches et les contrôles aux besoins du projet.

## Prérequis

Git et Python 3.12 ou supérieur pour l’outillage. Pour les applications fournies : PHP 8.4 ou supérieur avec PDO SQLite, SQLite3, mbstring et XML, Composer 2, Node.js 22.12 ou supérieur et npm. Un accès aux registres est nécessaire à l’installation.

Docker et Compose permettent aussi de lancer les applications dans chaque worktree de couche,
sans installer les runtimes sur l’hôte. Le pilotage direct utilise GNU Make, Bash, Git,
Perl/JSON::PP et les outils Linux/WSL décrits dans le runbook, sans Python.
Le lancement sur l’hôte reste disponible ci-dessous.

## Préparer le workspace de développement

Pour travailler avec VS Code, ouvrir le fichier versionné `aide.code-workspace`
depuis le dépôt principal, après avoir créé les worktrees des couches nécessaires.
Depuis la racine du dépôt principal, créer chaque worktree manquant avec la commande
suivante, en remplaçant `api` par `backoffice`, `web`, `design` ou `devops` selon le besoin :

```sh
python3 codebase-integrity/scripts/worktrees.py add --layer api --branch layers/api --base develop
code aide.code-workspace
```

Le dépôt doit déjà posséder un premier commit et une branche locale `develop`.
Vérifier les worktrees existants avec `git worktree list` avant toute création.

Le workspace regroupe le dossier principal et les cinq couches dans une fenêtre.
Ses chemins sont relatifs au fichier : `.` pour le dépôt principal et
`worktree/<couche>` pour chaque couche. Conserver le fichier à la racine du dépôt
principal ; adapter la liste `folders` si les couches ou leur disposition changent.
Une entrée dont le worktree n’existe pas encore restera indisponible.

La configuration masque `worktree/` dans la vue du dossier principal et les recherches,
tout en exposant chaque couche comme dossier distinct. Elle active la détection des
dépôts Git et une confirmation VS Code avant un commit sur `develop`, `master` ou
`main`. Ces réglages accompagnent les consignes de travail ; les protections distantes
restent à configurer séparément.

Un alias personnel peut faciliter l’ouverture, en adaptant le chemin absolu du clone :

```sh
alias aide-code-workspace='code /chemin/absolu/du/projet/aide.code-workspace'
```

Ajouter cette ligne à `~/.bash_aliases`, puis recharger ce fichier avec
`source ~/.bash_aliases`. Le fichier d’alias reste personnel et extérieur au dépôt.
Le [guide des couches](docs/02-cadre/couches/index.md#suivre-les-couches-dans-le-workspace)
décrit l’utilisation du workspace pendant la boucle de développement.

## Lancer les applications avec Docker

Pour démarrer une couche depuis la racine équipée du Makefile, utiliser
`make docker-up-api`, `make docker-up-web`, `make docker-up-backoffice`,
`make docker-up-design` ou `make docker-up-devops`. Chaque commande lance
son API et ses deux interfaces. `make docker-status-api` consulte la couche API ;
`make docker-stop-api` l’arrête en conservant les données. Ces commandes concernent
uniquement les environnements locaux de développement.

Depuis un worktree de couche équipé de la stack :

```sh
make up INTERFACE=web
make status
make down
```

Choisir `INTERFACE=backoffice` ou `INTERFACE=both` pour les autres interfaces. Chaque stack possède son API,
sa base SQLite persistante et ses domaines locaux derrière Caddy. Le [guide des environnements locaux](docs/02-cadre/couches/dockerisation.md)
donne les cinq ports, les adresses, les prérequis et les procédures de préparation et diagnostic.
Les témoins BusyBox restent une recette distincte. Les worktrees ne démarrent aucun service
lors de leur création et doivent recevoir les commits nécessaires avant utilisation.

## Lancer les applications de démonstration sur l’hôte

Depuis la racine du clone ou du worktree :

```sh
python3 codebase-integrity/scripts/apps.py install all
```

Les fichiers `.env` existants sont conservés. Dans trois terminaux, depuis cette même racine :

```sh
python3 codebase-integrity/scripts/apps.py serve api
python3 codebase-integrity/scripts/apps.py serve web
python3 codebase-integrity/scripts/apps.py serve backoffice
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
python3 codebase-integrity/scripts/check.py
python3 codebase-integrity/scripts/quality.py
```

La première commande vérifie l’outillage sans dépendances applicatives ; un test nécessite un port HTTP local temporaire. La seconde vérifie aussi les trois applications et demande leurs dépendances installées.

Pour les parcours navigateur, démarrer l’API de développement, puis :

```sh
(cd app/web/targets/app && npx playwright install --with-deps chromium)
python3 codebase-integrity/scripts/apps.py check web --browser
python3 codebase-integrity/scripts/apps.py check backoffice --browser
```

Ces tests créent puis suppriment des articles. Utiliser une API de développement. Les [points de contrôle](docs/01-codebase-integrity/points-de-controle.md) décrivent les commandes et leur portée ; la [documentation d’infrastructure](infra/README.md) décrit les témoins Docker utilisés pour vérifier l’isolation.

## Adapter au projet

1. Lire [AGENTS.md](AGENTS.md) et les README existants ; préserver les consignes, fichiers et environnements du projet d’accueil.
2. Définir les [couches](docs/02-cadre/couches/index.md), leurs responsabilités, branches et chemins. Adapter ensemble cette table et `infra/config/layers.json`. La recette Docker possède sa configuration distincte dans `infra/process-check.json` (`process.image` et `process.port_base`).
3. Compléter les instructions et examiner `.codex/config.toml`. Les skills restent personnels, hors du dépôt ; vérifier leur disponibilité avant livraison.
4. Définir les conventions techniques dans les README locaux, puis implémenter les contrôles par la consolidation autorisée.
5. Adapter les commandes de qualité et la CI. Vérifier les protections GitHub si les tests doivent bloquer la fusion ; aucun déploiement n’est fourni.
6. Conserver ou remplacer explicitement les exemples Article, Symfony/API Platform, Nuxt et la marque Graines Digitales. Mettre à jour ensemble les contrats, tests et références concernés.
7. Choisir le sort des cartes historiques dans la copie adoptée ; ne pas les reprendre comme des missions actives. Affecter une première tâche et produire ses preuves.

Le dépôt doit posséder un premier commit avant la création des worktrees. Les scripts ne copient pas les `.env`, ne démarrent pas les services lors de la création Git et ne synchronisent pas le remote.

## Skills AIDE

Les douze skills des étapes et les deux outils hors des boucles sont personnels, hors du dépôt.
Leurs noms sont indiqués dans [AGENTS.md](AGENTS.md). Les installer dans le répertoire de skills
configuré pour l’outil et valider leur structure et leurs ressources avant livraison.
Vérifier ensuite qu’ils sont effectivement exposés par la session.

Pour consulter la vue depuis un serveur local, depuis la racine du worktree :

```sh
python3 -m http.server 8080 --bind 127.0.0.1
```

Ouvrir `/dev-book/resources/vue-d-ensemble-ai-development-engineering.html`. Si le port est
occupé, choisir un autre port. Dans le mode historique où seul `dev-book/resources/` est servi,
les détails indiquent les noms des skills et leur emplacement personnel sans créer de lien
hors racine du serveur.
