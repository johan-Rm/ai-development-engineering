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

Les worktrees se trouvent sous `worktree/<couche>`. La configuration de routage est dans `config/layers.json` ; l’adapter avec cette table lors de l’adoption.

## Suivre les couches dans le workspace

Le fichier `aide.code-workspace`, à la racine du dépôt principal, fournit une vue
commune du dépôt et des worktrees dans VS Code. Le [guide d’installation](../../SETUP.md#préparer-le-workspace-de-développement)
explique sa préparation. Ses chemins relatifs permettent de conserver cette
configuration dans le projet sans imposer un chemin personnel.

Pendant la boucle de développement :

1. Au découpage, indiquer le worktree relativement à la racine du dépôt principal
   (par exemple `worktree/devops`) et la branche de chaque mission.
2. À l’implémentation, ouvrir les fichiers dans le dossier de la couche affectée.
   Résoudre localement le chemin absolu depuis le dépôt principal, sans le conserver
   dans la carte. Dans le terminal, vérifier `pwd` et `git status --short --branch` avant toute écriture.
   Le dossier « ◆ principal » sert de repère pour l’intégration ; les changements de
   tâche sont réalisés dans les worktrees des couches.
3. À la vérification, consulter les changements Git du dépôt de la couche concernée
   et exécuter ses commandes de preuve depuis ce même worktree.
4. À la reconstitution et à la livraison, suivre les commits identifiés et la branche
   de réunion autorisée selon les étapes de la boucle.

Le workspace facilite la navigation et la lecture des changements de plusieurs
couches. Il ne crée pas les worktrees, n’affecte pas les missions et ne synchronise
pas les branches. Les recherches excluent `worktree/` sous le dossier principal
pour éviter les résultats en double. L’isolation des services et la coordination
des missions restent à vérifier séparément.

## Coordonner les dépendances

Un fichier partagé se rattache à sa couche consommatrice et nécessite une coordination si une autre mission le touche. Plusieurs sites peuvent partager la couche web tant que les tâches restent séquentielles ; les écrivains simultanés demandent des périmètres distincts.

La reconstitution réunit les commits validés sur une branche explicitement choisie. Elle ne copie jamais le travail non commité d’un autre worktree.

La [documentation d’infrastructure](../../infra/README.md) décrit les témoins Docker et leurs ressources. Leur isolation ne prouve pas celle des applications de démonstration.

## Consulter les applications d’une couche

La stack applicative autonome décrite dans le [runbook](../../dev-book/runbooks/stacks-applicatives.md)
se lance depuis chaque worktree équipé avec `python3 infra/apps.py up --interface web`,
`backoffice` ou `both`. Chaque couche utilise son API et sa base SQLite, ses domaines
`web.wt-<couche>.localhost`, `backoffice.wt-<couche>.localhost` et `api.wt-<couche>.localhost`.
Les ports locaux par défaut vont de 19301 à 19305 selon les identifiants des couches.
`down` conserve les volumes. Ce fonctionnement complète la recette BusyBox ; sa preuve
exige l’observation des applications et de leurs ressources réelles.
