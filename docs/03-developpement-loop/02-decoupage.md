# Découpage

> Répartir la demande en tâches réalisables, rattachées à leurs couches et à leurs dépendances.

## Entrée

Demande cadrée.

## Déroulement

L’IA définit pour chaque tâche l’objectif, les chemins autorisés, les exclusions, les preuves attendues et la documentation touchée. Elle distingue les dépendances et les tâches indépendantes. Une couche peut recevoir plusieurs tâches successives.

L’IA ajoute dans le fichier de demande les liens vers les cartes créées dans
`dev-book/tasks/`. Chaque carte référence en retour la demande d’origine. Elle conserve
l’identité du fichier de cadrage, selon les [règles du dev-book](../../dev-book/README.md#rubriques-dune-demande).
Ce découpage ne lance pas l’implémentation.

## Sortie

Des cartes ordonnées par couche, rattachées à la demande initiale. Chaque tâche produira son commit.

## Procédure associée

`decouper-demande`.
