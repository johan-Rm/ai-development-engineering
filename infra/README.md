# Infrastructure de recette AIDE

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

Les identifiants stables sont dans `codebase-integrity/scripts/aiod.json` ; leur ordre dans le fichier ne change
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
- Aucun framework ni application : cet environnement sert uniquement à la recette AIDE.
- Vérifier la disponibilité de la couche avant une mission, même si Git affiche un arbre propre.

## Maintenance du cadre

La couche devops porte aussi les consignes, la documentation et l’outillage communs du cadre.
Ces travaux utilisent la branche `layers/devops` et le préfixe de tâche `OPS`, sans couche supplémentaire.

Les artefacts générés sont dans `.local/process-check/identity.json`, exclus de Git, de la
recherche et du contexte Docker. L’ancien dossier `.aiod/` n’est plus utilisé ; ses données
ne sont pas supprimées automatiquement. Relancer les témoins pour adopter le nouvel endpoint.
