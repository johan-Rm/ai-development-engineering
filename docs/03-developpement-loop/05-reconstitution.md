# Reconstitution

> Réunir les commits validés pour obtenir le changement complet demandé.

## Entrée

Toutes les tâches attendues sont validées et possèdent leur commit.

## Déroulement

L’IA vérifie la complétude, les dépendances et la branche de réunion définie au découpage, sans redemander un choix déjà autorisé. Elle rassemble les commits, traite les conflits et vérifie les échanges entre les contributions. Une preview peut aider à observer l’ensemble.

Créer la branche dédiée `demands/<identifiant>` si elle n’existe pas, même pour une seule couche.
Si les SHA validés et la trace documentaire des verdicts sont déjà
présents sur cette branche, vérifier leur ascendance et constater la réunion sans rejouer les commits.

## Sortie

Une branche réunissant la demande initiale, prête pour les vérifications de livraison.

## Procédure associée

`reconstituer-demande`.
