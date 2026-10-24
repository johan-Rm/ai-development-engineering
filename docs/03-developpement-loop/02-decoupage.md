# Découpage

> Répartir la demande en tâches réalisables, rattachées à leurs couches et à leurs dépendances.

## Entrée

Demande cadrée.

## Déroulement

L’IA définit pour chaque tâche l’objectif, les chemins autorisés, les exclusions, les preuves attendues et la documentation touchée. Elle distingue les dépendances et les tâches indépendantes. Une couche peut recevoir plusieurs tâches successives.

## Sortie

Des cartes ordonnées par couche, rattachées à la demande initiale. Chaque tâche produira son commit.

## Procédure associée

`creer-tache` écrit les cartes et prépare la branche ; le routage suit [les couches](../02-cadre/couches.md).
