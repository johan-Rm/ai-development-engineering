# Lancer les applications d’un worktree

## Objectif et préconditions

Consulter le code d’une couche dans une stack Docker autonome. Docker Engine local,
Compose v2 ou supérieur, Git et Python 3 sont nécessaires ; PHP, Composer et Node
sur l’hôte ne sont pas nécessaires pour lancer cette stack. Les registres Docker,
Composer et npm doivent être accessibles au premier démarrage.

Vérifier la disponibilité de la couche, sa branche `layers/<couche>` et l’état Git.
Réparer les liens si le dépôt a été déplacé, selon le runbook dédié. Les commandes
suivantes s’exécutent depuis la racine du worktree concerné, équipé du commit de stack.

## Préparer et démarrer

```sh
python3 infra/apps.py info
python3 infra/apps.py config --interface both
python3 infra/apps.py prepare
python3 infra/apps.py up --interface web
```

`prepare` construit l’image PHP et télécharge les images communes. `up` effectue
également le build nécessaire ; les dépendances verrouillées sont installées au
premier démarrage et quand leur lock change. Les migrations SQLite sont appliquées.
La base Docker est indépendante de la base utilisée par PHP sur l’hôte et démarre vide.

`--interface backoffice` sélectionne l’administration et `--interface both` les deux
interfaces. Sans option, la couche backoffice choisit son interface, les autres le web.
Un second `up` conserve une interface déjà lancée : pour passer à un mode plus léger,
faire `down` puis `up` avec le choix voulu. Cela conserve la base et les dépendances.
Le premier lancement peut prendre plusieurs minutes ; `up` attend la santé des services.

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
éteinte peut répondre 502 sans empêcher les autres de fonctionner.
Le proxy gère aussi les WebSockets du rechargement automatique.

Les domaines `*.localhost` visent la boucle locale ; en cas de résolution absente dans
un outil, utiliser une résolution explicite vers `127.0.0.1`. Aucun DNS public n’est modifié.
Seul Caddy publie un port, lié à `127.0.0.1`. Le nom de projet inclut un hash du chemin
principal et la couche. Un déplacement du clone change cette identité : observer les
anciennes ressources avant de déplacer un dépôt utilisé par Docker.

En cas de port occupé, le lanceur refuse sans arrêter le service tiers. Pour un autre
clone ou une collision locale, définir une autre base dans l’environnement appelant :
`AIDE_APP_PORT_BASE=20300 python3 infra/apps.py up --interface web`. Garder cette même
base pour toutes les commandes ultérieures de cette stack. Vérifier l’absence de collision
avec les autres clones et services ; les noms de projet distincts ne suffisent pas.

Le lanceur crée les répertoires de montage ignorés manquants sous l’utilisateur hôte,
pour éviter leur création par Docker en root ; il ne remplace pas les répertoires existants.
Les sources sont montées en lecture seule dans les conteneurs. Les volumes privés
contiennent SQLite/var, vendor/Composer et, pour chaque interface, node_modules,
.nuxt et .output. L’initialisation attribue ces volumes à l’UID/GID de l’utilisateur
appelant ; les applications ne tournent pas en root. Les `.env` hôte ne sont jamais
écrits ou copiés. L’API utilise explicitement les valeurs locales Docker et monte
`.env.example` comme `.env` dans le conteneur ; les paramètres de base sont donc
indépendants des secrets et connexions de l’hôte. Les options internes Compose sont
fournies par le lanceur, qui ignore les `.env` Compose et les variables `COMPOSE_*` héritées.

## Vérifier et arrêter

```sh
python3 infra/apps.py status
python3 infra/test_apps.py
python3 infra/apps.py down
```

`down` retire les conteneurs et le réseau du projet, sans supprimer les volumes.
Les données et dépendances restent disponibles à la relance.
Pour une recette réelle sur une stack de test avec les deux interfaces lancées :

```sh
python3 infra/test-runtime.py --expect-empty
python3 infra/browser.py --reload
```

La première exige une base vide, vérifie les montages et la persistance par arrêt/relance,
puis supprime son article. Omettre `--expect-empty` pour une base existante.
La seconde construit une image Chromium depuis `infra/Dockerfile.browser`, teste le CRUD
et la lecture dans le navigateur, puis le rechargement automatique. Elle ne monte que
le script de recette et les captures, plus les trois fichiers source concernés avec
`--reload`. Cette option modifie temporairement ces fichiers et les restaure exactement ;
réserver la couche à cette recette pendant l’exécution. Sans `--reload`, aucun code n’est modifié.
Le lanceur navigateur utilise le réseau hôte Linux ; les captures sont sous
`/tmp/DEM-005-browser-artifacts/`. Les dépendances système restent dans l’image.

Ne pas utiliser `down -v`
ou un nettoyage global de Docker pour résoudre un problème.

## Arrêt en cas d’erreur et retour arrière

En cas d’échec de build, installation, migration ou santé, conserver le diagnostic et
inspecter les journaux du seul projet annoncé par `info` avec Docker Compose. Vérifier
l’accès au moteur local, aux registres et les droits, sans changer les locks ni les contrôles.
Arrêter seulement cette stack avec `down` ; les sources et `.env` n’ont pas été modifiés.
Les modifications de code pour vérifier le rechargement doivent être temporaires,
coordonnées et restaurées exactement, sans reset global. Aucun démarrage implicite
n’accompagne la création Git d’un worktree.
