# Infrastructure locale AIDE

`compose.process.yaml` fournit un conteneur témoin BusyBox par couche, sans application.
Il sert un fichier `/identity.json` décrivant sa couche et monte un volume privé pour vérifier les écritures.
Le port est lié exclusivement à `127.0.0.1` ; aucun domaine, proxy ou DNS public n’est nécessaire.

Le script `codebase-integrity/scripts/process.py`, lancé depuis un worktree de couche, impose sa branche,
son identité Compose et le chemin absolu des artefacts. Il ne lit ni ne modifie les `.env`.
Les paramètres de Compose sont explicitement fournis par l’outil dans une copie de
l’environnement appelant, sans modifier celui-ci :

| Paramètre interne | Valeur fournie |
| --- | --- |
| `PROCESS_CHECK_IMAGE` | Image du conteneur témoin définie dans la configuration de recette |
| `PROCESS_CHECK_PORT` | Port local calculé pour la couche |
| `PROCESS_CHECK_PROOF_DIR` | Chemin absolu du dossier `.local/process-check` du worktree |

Ces paramètres obligatoires décrivent la recette ; ils ne sont pas à renseigner dans
un `.env`. Le script et le fichier Compose utilisent les mêmes noms, sans alias des
anciens paramètres. Aucune migration de `.env` n’est nécessaire pour les commandes
pilotées par le script.

La recette possède `infra/process-check.json` : son enveloppe `process` contient
`image` et `port_base`. Les couches, branches, rôles et identifiants stables
appartiennent au cadre, dans [`config/layers.json`](../config/layers.json).
`process.py` lit les deux fichiers depuis le worktree appelant et exige leur présence
et leur validité, sans création implicite ni repli sur l’ancien fichier.

L’ordre des identifiants dans le fichier ne change
pas les ports. Les noms des projets incluent un hash du chemin du dépôt principal et la couche.
Deux clones ont des noms distincts ; leurs ports doivent aussi être configurés avec des bases
différentes s’ils tournent sur le même hôte. Changer `process.port_base` avant le premier démarrage.

L’image BusyBox est un outil de recette, pas un choix de stack applicative.
Les volumes ne sont pas supprimés par la commande d’arrêt.

Références : [projets Compose](https://docs.docker.com/compose/intro/compose-application-model/),
[services et montages](https://docs.docker.com/reference/compose-file/services/).

## Couche devops — initialisation AIDE

- Branche : `layers/devops` ; préfixe des futures tâches : `OPS`.
- Dossier Git : le chemin absolu enregistré par `git worktree list`.
- La [carte OPS-019](../dev-book/tasks/OPS-019-initialiser-worktree-devops.md)
  consigne l’initialisation, la base et les preuves.
- Le [routage commun](../docs/02-cadre/couches.md) définit les responsabilités de cette couche.
- Depuis ce worktree, `python3 codebase-integrity/scripts/process.py up` démarre le conteneur témoin ;
  `verify` observe son identité JSON et `down` arrête son environnement en conservant les volumes.
- Le témoin sert uniquement à la recette AIDE ; la stack applicative ci-dessous est indépendante.
- Vérifier la disponibilité de la couche avant une mission, même si Git affiche un arbre propre.

## Maintenance du cadre

La couche devops porte aussi les consignes, la documentation et l’outillage communs du cadre.
Ces travaux utilisent la branche `layers/devops` et le préfixe de tâche `OPS`, sans couche supplémentaire.

Les artefacts générés sont dans `.local/process-check/identity.json`, exclus de Git, de la
recherche et du contexte Docker. L’ancien dossier `.aiod/` n’est plus utilisé ; ses données
ne sont pas supprimées automatiquement. Relancer les témoins pour adopter le nouvel endpoint.

## Stack applicative par worktree

Le Makefile racine appelle directement Docker Compose, sans Python pour le pilotage.
`compose.apps.yaml`, `Dockerfile.api`, `Caddyfile.apps` et les deux scripts de démarrage
servent les applications depuis chaque worktree. `stack-env.sh` prépare seulement
les paramètres Git, l’identité et les points de montage ; aucune action Docker n’y est déléguée.
Le [runbook](../dev-book/runbooks/stacks-applicatives.md) documente les prérequis,
commandes, adresses, ressources et diagnostics. Aucun déploiement n’est configuré.

Depuis un worktree : `make up INTERFACE=web`, `INTERFACE=backoffice` ou `INTERFACE=both`.
`make help`, `info`, `config`, `prepare`, `status` et `down` complètent le pilotage.
Le port vaut 19300 + l’identifiant de couche, surchargeable par `AIDE_APP_PORT_BASE`.
Les projets et volumes gardent leur identité de la première version Python.

## Rôle et responsabilités

Chaque couche utilise son propre code, son API, sa base SQLite et ses domaines Caddy.
Les applications conservent leurs contrats ; OPcache est désactivé dans le serveur PHP
de développement. Les témoins BusyBox restent une recette indépendante et inchangée.

## Conventions techniques

Les sources restent en lecture seule ; les volumes de données, dépendances et sorties
sont privés au projet dépôt/couche. Les applications utilisent l’UID/GID hôte.
Make conserve les volumes à l’arrêt et ne lit ni n’écrit les `.env` Compose.
Symfony utilise `.env.example` via `APP_RUNTIME_OPTIONS.dotenv_path`, sans créer de `.env`.
Les ports sont liés exclusivement à `127.0.0.1`, avec contrôle des écoutes avant `up`.
Le routage JSON existant est lu avec JSON::PP, module standard de Perl, sans dépendance Python.
Les recettes Make utilisent Bash et les outils Linux/WSL documentés dans le runbook.
Les dépendances applicatives utilisent leurs locks. Les images suivent les tags
PHP 8.4 CLI Bookworm, Composer 2, Node 22 Bookworm slim, Caddy 2.10 Alpine et BusyBox 1.37.0 ;
ces tags ne sont pas des digests immuables.

`make test` exécute `infra/test-make.sh` : fixtures Git, 15 configurations Compose,
préservation des `.env`, contrôles des paramètres, écoutes et points de montage.
`make test-browser RELOAD=1` exécute Chromium via Docker avec les seuls montages ciblés ;
`make test-runtime EXPECT_EMPTY=1` exécute les assertions Node de persistance et appelle
Make pour le cycle de vie. Les quatre anciens scripts Python de cette stack sont supprimés.
Les outils, règles et tests du Codebase Integrity restent inchangés.
