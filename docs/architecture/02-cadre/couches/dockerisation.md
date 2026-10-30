# Utiliser la dockerisation des couches

> Démarrer et vérifier une stack isolée pour chaque couche.

## Préparer l’environnement local

Consulter le code d’une couche dans une stack Docker autonome. Sous Linux/WSL,
prévoir GNU Make 4+, Bash, Git, Docker Engine local avec Compose v2+, Perl avec son
module standard JSON::PP, les outils usuels coreutils et `ss` (iproute2).
Les registres Docker, Composer et npm doivent être accessibles au premier démarrage.
Python, PHP, Composer et Node ne sont pas nécessaires sur l’hôte pour le pilotage.

Vérifier la disponibilité de la couche, sa branche `layers/<couche>` et l’état Git.
Réparer les liens si le dépôt a été déplacé selon le
[guide de réparation](../../../../dev-book/runbooks/reparer-liens-worktrees.md). Exécuter les
commandes depuis la racine du worktree équipé des commits de stack.

## Démarrer une couche

Depuis la racine du dépôt principal équipé de ce Makefile :

```sh
make docker-up-api
make docker-up-web
make docker-up-backoffice
make docker-up-design
make docker-up-devops
make docker-status-api
make docker-stop-api
```

Chaque nom démarre uniquement la stack de cette couche, avec API et les deux
interfaces. `docker-stop-<couche>` conserve ses données ; `docker-status-<couche>` affiche son état.
`INTERFACE=web` ou `INTERFACE=backoffice` reste disponible pour limiter les interfaces.
Ces raccourcis fonctionnent aussi depuis un worktree équipé du Makefile.

```sh
make help
make info
make config INTERFACE=both
make prepare
make up INTERFACE=web
```

Le Makefile appelle directement Docker Compose ; aucun lanceur Python n’intervient.
`infra/stack-env.sh` prépare seulement le contexte Git, l’identité et les paramètres.
`prepare` construit l’image PHP et télécharge les images communes. `up` effectue
le build nécessaire ; les dépendances verrouillées sont installées au premier
démarrage et quand leur lock change. Les migrations SQLite sont appliquées.
La base Docker est indépendante de celle utilisée sur l’hôte et démarre vide.

```sh
make up INTERFACE=backoffice
make up INTERFACE=both
make status
make down
```

Sans `INTERFACE`, la couche backoffice choisit son interface, les autres le web.
Un second `up` conserve une interface déjà lancée : pour passer à un mode plus léger,
faire `make down` puis `make up` avec le choix voulu. La base et les dépendances restent.
Le premier lancement peut prendre plusieurs minutes ; `up` attend les services.

## Adresses et isolation

| Worktree | Port par défaut | Exemple web |
| --- | --- | --- |
| backoffice | 19301 | http://web.wt-backoffice.localhost:19301 |
| api | 19302 | http://web.wt-api.localhost:19302 |
| web | 19303 | http://web.wt-web.localhost:19303 |
| devops | 19304 | http://web.wt-devops.localhost:19304 |
| design | 19305 | http://web.wt-design.localhost:19305 |

Remplacer `web` par `backoffice` pour l’administration ou par `api` avec `/api/docs`
pour la documentation API. Seules les interfaces démarrées répondent ; une interface
éteinte peut répondre 502 sans gêner les autres. Caddy gère aussi les WebSockets.
Les domaines `*.localhost` visent la boucle locale ; un outil sans cette résolution
peut utiliser une résolution explicite vers `127.0.0.1`. Aucun DNS public n’est modifié.
Seul Caddy publie un port, lié à `127.0.0.1`.

Les projets conservent l’identité dépôt/couche et les volumes de la première version.
Un déplacement du clone change cette identité : observer les anciennes ressources
avant de déplacer un dépôt utilisé par Docker.

En cas de port occupé, `make up` refuse sans arrêter le service tiers. Pour un autre
clone ou une collision locale : `make up AIDE_APP_PORT_BASE=20300 INTERFACE=web`.
La base peut aussi venir de l’environnement ; garder la même valeur pour toutes
les commandes de cette stack. Les noms de projets distincts ne suffisent pas à
éviter les collisions entre clones. Les connexions récemment fermées ne sont pas
assimilées à une écoute active ; un Caddy du même projet peut déjà tenir son port.

Les sources sont montées en lecture seule. Les volumes privés contiennent SQLite/var,
vendor/Composer et, pour chaque interface, node_modules, .nuxt et .output.
Les répertoires de montage ignorés manquants sont créés sous l’utilisateur hôte,
sans remplacer les répertoires existants ; les liens symboliques sont refusés.
L’initialisation attribue les volumes à l’UID/GID appelant et les applications
ne tournent pas en root. Aucun `.env` n’est écrit ou copié. Symfony lit `.env.example`
via `APP_RUNTIME_OPTIONS.dotenv_path`, avec les valeurs locales Docker explicites.
Compose ignore les `.env` et les variables `COMPOSE_*` héritées.

## Vérifier et arrêter

```sh
make test
make test-browser RELOAD=1
make test-runtime EXPECT_EMPTY=1
make down
```

`test` vérifie les identités, les 15 configurations, les paramètres et les collisions
sans démarrer les applications ; il fonctionne avec un exécutable Python factice
qui échoue s’il est appelé. `test-browser` exige les deux interfaces et utilise une
image Chromium construite depuis `infra/Dockerfile.browser`, sans paquet système hôte.
Il crée/modifie/supprime son article. `RELOAD=1` modifie temporairement trois fichiers
ciblés pour vérifier leur rechargement et restaure exactement les sources, y compris
en cas d’échec. Réserver la couche pendant cette recette. Sans cette option, aucun
code n’est modifié. Les montages de test restent limités ; aucun `.env` n’est exposé.
Les captures sont dans `/tmp/DEM-005-make-browser-artifacts/`.

`test-runtime` nécessite Node 22+ sur l’hôte pour les assertions de recette, pas pour
le pilotage quotidien. Il appelle Make pour l’arrêt/relance, observe les ressources,
vérifie la persistance et supprime son seul article temporaire. `EXPECT_EMPTY=1`
exige une collection initialement vide ; omettre cette option pour une base existante.
Les observations sont dans `/tmp/DEM-005-make-runtime-<couche>.json`.

`down` retire les conteneurs et le réseau du projet sans supprimer les volumes.
Les données et dépendances restent disponibles à la relance. Ne pas utiliser un
nettoyage global de Docker ou une suppression de volumes pour résoudre une panne.
La [recette des cinq stacks](../../../../dev-book/runbooks/recette-stacks-applicatives.md) détaille la vérification.

## Diagnostiquer une erreur

Conserver le diagnostic et inspecter uniquement le projet annoncé par `make info`.
Vérifier le moteur, les registres et les droits sans changer les locks ni les contrôles.
Arrêter cette seule stack avec `make down` ; les sources et `.env` restent préservés.
Les modifications temporaires de test doivent être restaurées exactement, sans reset.
La création Git d’un worktree ne démarre aucun service.
