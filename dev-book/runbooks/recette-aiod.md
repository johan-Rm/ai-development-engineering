# Recette du processus AIOD

## Préconditions

Python 3, Git, Docker avec accès au moteur et Docker Compose. Les branches et les cinq worktrees
ont été initialisés depuis un commit develop identifié. Aucun framework ou service produit.

## Observer un environnement

Depuis `worktree/api/`, par exemple :

```sh
python3 -B codebase-quality-control/scripts/process.py info
python3 -B codebase-quality-control/scripts/process.py config
python3 -B codebase-quality-control/scripts/process.py up
python3 -B codebase-quality-control/scripts/process.py verify
python3 -B codebase-quality-control/scripts/process.py status
```

Même procédure depuis chacun des quatre autres worktrees.
La création Git ne démarre aucun conteneur. `up` conserve les artefacts compatibles existants
et refuse de remplacer une identité JSON incompatible. Les `.env` sont ignorés par cette recette.

| Couche | Branche | Endpoint local |
| --- | --- | --- |
| backoffice | layers/backoffice | http://127.0.0.1:18101/identity.json |
| api | layers/api | http://127.0.0.1:18102/identity.json |
| web | layers/web | http://127.0.0.1:18103/identity.json |
| devops | layers/devops | http://127.0.0.1:18104/identity.json |
| design | layers/design | http://127.0.0.1:18105/identity.json |

Le fichier généré est `.local/process-check/identity.json` dans chaque worktree.
L’ancien `.aiod/` est conservé s’il existe mais n’est plus utilisé ; relancer les témoins
après mise à jour des scripts et de Compose.

Les ports correspondent à la base 18100. Chaque conteneur a son réseau et son volume.
Les fichiers JSON reflètent l’identité du worktree et l’environnement, pas une application.

## Prouver l’isolation

Une fois les cinq témoins démarrés, depuis la racine :

```sh
python3 -B codebase-quality-control/scripts/check_docker.py
python3 -B codebase-quality-control/scripts/worktrees.py list
```

Le contrôle vérifie les réponses HTTP, les chemins montés en lecture seule, les réseaux et
les volumes effectifs. Il écrit un marqueur unique par couche dans `/data/`, vérifie que
les couches suivantes ne le voient pas, puis relit les cinq valeurs différentes.
Ces petits marqueurs de preuve sont conservés dans les volumes.

Relancer `up` depuis deux worktrees et vérifier que leurs identités et données persistent.
Un état Git propre ne suffit pas à autoriser une nouvelle mission : vérifier l’affectation.

## Arrêter

Depuis chaque worktree lancé :

```sh
python3 -B codebase-quality-control/scripts/process.py down
```

Les conteneurs et réseaux de cette couche sont arrêtés, les volumes conservés.
En cas d’échec, lire la sortie et `status`, préserver le travail et arrêter la recette ;
ne pas forcer une branche ni supprimer des volumes pour contourner le problème.

## Cycle humain à tester ensemble

Nommer une tâche, affecter une couche, vérifier branche et chemin absolu, produire une preuve,
valider le résultat puis livrer un commit avec carte et documentation. Les initialisations
prouvent le socle de ce cycle ; elles ne constituent pas une validation de tous les futurs workflows
transversaux, PR ou opérations distantes.
