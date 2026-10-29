# Découpage

> Répartir la demande en tâches réalisables, rattachées à leurs couches et à leurs dépendances.

## Entrée

Demande cadrée.

## Déroulement

L’IA définit pour chaque tâche l’objectif, les chemins autorisés, les exclusions, les preuves attendues et la documentation touchée. Elle distingue les dépendances et les tâches indépendantes. Une couche peut recevoir plusieurs tâches successives.

L’IA ajoute dans le fichier de demande les liens vers les cartes créées dans
`dev-book/tasks/`. Chaque carte référence en retour la demande d’origine. Elle conserve
l’identité du fichier de cadrage, selon les [règles du dev-book](../../../dev-book/README.md).
Le découpage prévoit la branche de demande et un worktree existant pour la reconstitution.
Prévoir `demands/<identifiant>`, branche dédiée distincte des branches de couche, de
l’intégration et de la production, même pour une seule couche. La reconstitution la crée. Ce découpage ne lance pas l’implémentation.

## Sortie

Des cartes ordonnées par couche, rattachées à la demande initiale. Chaque tâche produira son commit à l’étape 04, après validation humaine.
Une dépendance amont non commitée bloque son consommateur jusqu’à cette validation
et à son commit ; prévoir cette alternance entre implémentation et vérification.

## Procédure associée

`decouper-demande`.

Prévoir `demands/<identifiant>` depuis develop, dans un worktree existant libre et
propre, puis des cherry-picks des commits validés. Noter la branche de couche à
retrouver après livraison. Aucune copie de réunion supplémentaire à prévoir.

Chaque carte applique les [règles de session](../../../AGENTS.md#demandes-et-cartes).
