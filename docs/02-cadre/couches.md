# Couches

> Une couche délimite des responsabilités, des chemins autorisés et un environnement de travail pour isoler les contributions.

## Organiser le travail

Chaque couche possède une branche et un worktree. **Un seul agent y écrit à la fois** ; un arbre Git propre ne prouve pas que la couche est libre. Les missions actives doivent être coordonnées avant toute affectation.

Les contributions échangent des contrats et des commits identifiés. Un worktree isole les fichiers, mais les ports, bases, volumes et fichiers générés doivent aussi être isolés.

## Couches de ce dépôt

| Couche | Chemins | Branche | Préfixe | Preuve |
| --- | --- | --- | --- | --- |
| API | `app/api/` | `layers/api` | API | Requête et réponse, tests du contrat |
| Web | `app/web/` | `layers/web` | WEB | Build et rendu des cibles |
| Backoffice | `app/backoffice/` | `layers/backoffice` | BO | Parcours d’administration |
| Design | `design/` | `layers/design` | UX | Relecture visuelle des parcours |
| Devops | `infra/`, instructions, documentation et outillage du cadre | `layers/devops` | OPS | Configuration ou contrôle adapté au changement |

Les worktrees se trouvent sous `worktree/<couche>`. La configuration de routage est dans `codebase-quality-control/scripts/aiod.json` ; l’adapter avec cette table lors de l’adoption.

## Coordonner les dépendances

Un fichier partagé se rattache à sa couche consommatrice et nécessite une coordination si une autre mission le touche. Plusieurs sites peuvent partager la couche web tant que les tâches restent séquentielles ; les écrivains simultanés demandent des périmètres distincts.

La reconstitution réunit les commits validés sur une branche explicitement choisie. Elle ne copie jamais le travail non commité d’un autre worktree.

La [recette Docker](../../dev-book/runbooks/recette-aiod.md) vérifie séparément les identités et ressources des témoins. Elle ne prouve pas l’isolation des applications de démonstration.
