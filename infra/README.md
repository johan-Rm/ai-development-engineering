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

`compose.apps.yaml`, `Dockerfile.api`, `Caddyfile.apps`, les deux scripts de démarrage
et `apps.py` servent les applications existantes depuis chaque worktree de couche.
Le [runbook](../dev-book/runbooks/stacks-applicatives.md) décrit préparation, commandes,
adresses, ressources, arrêt et diagnostic. Aucun déploiement applicatif n’est configuré.

Depuis un worktree : `python3 infra/apps.py up --interface web`, `backoffice` ou `both`.
`info`, `config`, `prepare`, `status` et `down` complètent le lanceur. Le port vaut
19300 + l’identifiant de couche de `config/layers.json`, surchargeable par
`AIDE_APP_PORT_BASE` dans l’environnement appelant. Les ports sont vérifiés avant `up`.

### Rôle et responsabilités

La stack sert à vérifier le code de la branche locale sans dépendre du service d’une
couche voisine. L’API garde SQLite ; Caddy expose les trois domaines locaux de la couche.
Les applications conservent leurs responsabilités et contrats existants.
Le serveur PHP de développement désactive explicitement OPcache pour refléter les modifications.

### Conventions techniques

Les sources restent en lecture seule ; les volumes de données, dépendances et sorties
sont privés au projet dépôt/couche. Les services applicatifs utilisent l’UID/GID hôte.
Le lanceur ne lit ni n’écrit les `.env` Compose et n’efface jamais les volumes à l’arrêt.
Les ports sont liés exclusivement à `127.0.0.1`. La recette BusyBox demeure indépendante.
Les dépendances applicatives utilisent leurs locks existants. Les images suivent les tags
PHP 8.4 CLI Bookworm, Composer 2, Node 22 Bookworm slim, Caddy 2.10 Alpine et BusyBox 1.37.0 ;
ces tags ne sont pas des digests immuables. Les tests de cette stack sont dans
`infra/test_apps.py`, exécutables avec `python3 infra/test_apps.py` ; ils ne modifient
pas les vérificateurs du Codebase Integrity.

Les recettes réelles `python3 infra/test-runtime.py --expect-empty` et
`python3 infra/browser.py --reload` exigent les deux interfaces lancées. La première
observe les ressources et vérifie la persistance par arrêt/relance, puis supprime son
seul article temporaire. La seconde construit `Dockerfile.browser` depuis Node 22 Bookworm slim, avec
Playwright 1.61.0 et Chromium headless uniquement, sans bibliothèque système sur l’hôte.
Ce lanceur de recette monte seulement le script en lecture seule, les captures et,
avec `--reload`, les trois fichiers ciblés en écriture ; aucun `.env` ni worktree entier
n’est exposé. Il utilise le réseau hôte sous Linux et écrit ses captures dans
`/tmp/DEM-005-browser-artifacts/`. Elle crée/modifie/supprime son seul article temporaire.
L’option `--reload`, réservée à une couche disponible, modifie temporairement les deux
composants racines et le routeur PHP pour observer leur rechargement, puis restaure
exactement les sources dans un bloc de nettoyage, y compris en cas d’échec.
Sans cette option, le test ne modifie pas le code. `node infra/test-browser.cjs <couche>
<port>` permet aussi une exécution sur un hôte déjà équipé de Playwright et de ses
bibliothèques système.
