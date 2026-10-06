# Couches et responsabilités

Le blueprint décrit cinq couches pour le projet consommateur, indépendamment de sa stack.
Leurs dossiers sont préparés dans les worktrees à l’initialisation ; aucune application n’est installée.

| Couche | Chemins proposés | Branche | Worktree | Préfixe | Preuve attendue |
| --- | --- | --- | --- | --- | --- |
| backoffice | `backoffice/` | `layers/backoffice` | `worktree/backoffice` | BO | Parcours d’administration exécuté |
| api | `api/` | `layers/api` | `worktree/api` | API | Requête et réponse observées, tests du contrat |
| web | `web/` : socle partagé et cibles | `layers/web` | `worktree/web` | WEB | Build et rendu des cibles touchées |
| design | `design/` : maquettes, parcours et direction artistique | `layers/design` | `worktree/design` | UX | Relecture visuelle et validation des parcours |
| devops | `infra/` : domaines, déploiement, architecture serveur | `layers/devops` | `worktree/devops` | OPS | Configuration vérifiée sur l’environnement autorisé |

## Plusieurs webapps et sites

`web/` peut contenir `shared/` et `targets/<nom>/`. Une cible représente un site ou une webapp,
avec sa configuration et sa commande de build. Le nombre de cibles n’impose pas le nombre de
worktrees : une couche web suffit tant que ses tâches sont séquentielles. Si plusieurs cibles
nécessitent des écrivains simultanés, définir des couches avec des chemins distincts.

Le backoffice consomme les contrats de l’API ; les cibles web peuvent les consommer aussi.
Les échanges se font sur des contrats et commits identifiés. Une modification de code partagé
se rattache à son consommateur et doit être coordonnée si une autre tâche le touche.

## Domaines et infrastructure

`devops` fournit les conventions de nommage, la configuration des domaines, les routages,
les services communs et les procédures de déploiement. Chaque couche applicative doit pouvoir
exécuter sa cible avec ses ressources propres. Le worktree devops ne constitue pas la pile
partagée dans laquelle tous les agents écrivent.

Exemples conceptuels de noms : `<projet>-<environnement>-<couche>-<cible>`.
Le DNS public, les certificats et les opérations serveur sont des actions distinctes,
à autoriser pour l’environnement concerné. Aucune de ces actions n’est faite par le créateur Git.

## Design

`design/` accueille les recherches, maquettes et prototypes non livrés. La couche design
peut utiliser un navigateur pour présenter et vérifier ses propositions. La preuve attendue
est une relecture visuelle et une validation humaine des parcours.

Le backoffice et les cibles web implémentent les décisions retenues à partir d’artefacts
et de commits identifiés. Les composants et styles livrés restent dans leur couche consommatrice.
Le worktree design se crée à l’affectation d’une tâche ; aucun serveur n’est imposé.

## Maintenance de ce dépôt

La couche `blueprint`, branche `layers/blueprint`, préfixe BP, possède les consignes,
la documentation et l’outillage de ce dépôt. Elle est une couche de maintenance du blueprint,
distincte des cinq couches proposées pour le projet consommateur. Son worktree peut être la racine si la branche y est sortie.
Preuve : documentation cohérente et `python3 scripts/check.py`.

La configuration `scripts/aiod.json` connaît ces cinq couches et la maintenance du blueprint.
Lors de l’adoption, conserver seulement les couches utiles et adapter cette table avec le JSON.
Chaque couche reçoit un écrivain à la fois ; les consignes ne sont pas des verrous automatiques.

## Preuve du processus

Dans ce blueprint, les preuves applicatives du tableau restent des exemples pour un projet futur.
La recette actuelle vérifie seulement Git, le témoin HTTP et l’isolation des ressources Docker,
y compris pour design et devops. Voir [la recette](../../dev-book/runbooks/recette-aiod.md).
