---
name: reconstituer-demande
description: "Réunir les commits validés d’une demande de développement sur une branche de réunion autorisée."
---

# Développement · 05 Reconstitution

## Entrée

Liste complète des tâches validées, SHA de leurs commits, dépendances et branche de réunion explicitement autorisée.

## Conventions du projet

Lire les instructions du projet, la demande ou carte fournie et les README applicables.
Résoudre les chemins, couches, branches, commandes de tests et qualité depuis le projet ;
annoncer les valeurs utilisées et les inconnues, sans imposer de valeurs personnelles.
Avant une écriture, confirmer le worktree absolu, la branche autorisée et la disponibilité de la couche.
Préserver les modifications préexistantes et les `.env`. Ne pas utiliser stash, reset --hard,
force-push ou suppression de worktree pour résoudre une situation. Ne pas rebaser une branche occupée.
Commit, push, PR et merge nécessitent l’autorisation prévue par le projet ; une invocation d’étape
ne les autorise pas implicitement. Les autorisations explicites déjà données restent valables.
Ne pas déléguer sans autorisation. Ne pas enchaîner automatiquement une autre étape.

## Procédure

Comparer les cartes à la demande initiale. Vérifier les commits, leur ascendance et l’ordre des dépendances.
Identifier le worktree de réunion et les opérations Git autorisées avant toute intégration ; cette étape
ne permet pas de contourner l’interdiction de changements directs sur intégration ou production.
Réunir seulement les commits autorisés avec la stratégie du projet. Ne copier aucun fichier non commité
entre missions. Résoudre les conflits dans le périmètre approuvé ; faire arbitrer tout changement de comportement.
Vérifier les contrats et parcours de l’ensemble, exécuter les contrôles pertinents et documenter le résultat.
Une preview ne se lance que dans un environnement autorisé dont les écritures et ports sont vérifiés.
Si tout est déjà réuni, vérifier et rapporter ce fait sans rejouer les commits.

## Sortie et preuve

Branche complète, liste des SHA réunis, preuves des échanges et limites, prête pour livraison.

## Arrêt

Contribution absente, branche occupée, opération non autorisée ou conflit sémantique : conserver le travail et préciser le blocage.
