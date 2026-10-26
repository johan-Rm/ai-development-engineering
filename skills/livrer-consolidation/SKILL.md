---
name: livrer-consolidation
description: "Réunir et contrôler les commits validés d’une consolidation, puis préparer ses PRs et les commandes de contrôle durables."
---

# Consolidation · 06 Livraison

## Entrée

Arbitrage, tâches validées, SHA des contributions et destinations de livraison autorisées.

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

Vérifier que toutes les occurrences et cartes retenues par l’arbitrage sont traitées. Réunir les commits
nécessaires dans les branches de livraison autorisées en respectant les dépendances, sans copier le travail
non commité. Cette réunion appartient à la consolidation et ne requiert aucun skill de développement.
Faire arbitrer les conflits qui changent la règle ou le résultat validé. Exécuter les contrôles de livraison
sur chaque ensemble et attendre les résultats requis avant toute PR. Vérifier que chaque nouveau contrôle
dispose d’une commande stable, de préconditions, de cas vérifiés et d’un résultat attendu documentés.
Préparer les PRs avec le constat, l’arbitrage, les corrections, exceptions, preuves et zones non couvertes.
Utiliser `creer-pr` comme outil transversal si disponible et si l’ouverture est demandée ; réutiliser les
résultats actuels couvrant le même HEAD pour éviter les exécutions identiques. Sans autorisation distante,
fournir les contenus prêts à relire. Ne pas merger ni lancer automatiquement le suivi après fusion.

## Sortie et preuve

Contributions contrôlées, commandes durables et dossiers de PR ; URLs seulement pour les PRs autorisées et réellement ouvertes.

## Arrêt

Carte non validée, occurrence oubliée, contrôle requis inconnu ou échoué : ne pas ouvrir de PR et exposer le travail restant.
