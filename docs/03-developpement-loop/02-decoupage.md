# Découpage

> Répartir la demande en tâches réalisables, rattachées à leurs couches et à leurs dépendances.

## Entrée

Demande cadrée.

## Déroulement

L’IA définit pour chaque tâche l’objectif, les chemins autorisés, les exclusions, les preuves attendues et la documentation touchée. Elle distingue les dépendances et les tâches indépendantes. Une couche peut recevoir plusieurs tâches successives.

L’IA ajoute dans le fichier de demande les liens vers les cartes créées dans
`dev-book/tasks/`. Chaque carte référence en retour la demande d’origine. Elle conserve
l’identité du fichier de cadrage, selon les [règles du dev-book](../../dev-book/README.md).
Le découpage est autonome et définit dans la demande la branche et le worktree de réunion.
Prévoir `demands/<identifiant>`, branche dédiée distincte des branches de couche, de
l’intégration et de la production, même pour une seule couche. La reconstitution la crée. Ce découpage ne lance pas l’implémentation.

## Sortie

Des cartes ordonnées par couche, rattachées à la demande initiale. Chaque tâche produira son commit.

## Procédure associée

`decouper-demande`.

Le worktree de réunion est prévu dans un temporaire extérieur au dépôt et à ses
couches : `<temp>/aide-reunions/<projet>-reunion-<numero>`. Aucun nom `DEM-*` hors
`dev-book/demand/` et aucune copie de réunion sous `worktree/`. La résolution du
chemin, les collisions et la conservation du temporaire suivent
[les instructions du projet](../../AGENTS.md#rangement-des-demandes-et-réunions).
