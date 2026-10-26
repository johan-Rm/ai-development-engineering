---
name: implementer-consolidation
description: "Implémenter un arbitrage de consolidation avec ses cartes par couche, corrections globales et contrôles déterministes."
---

# Consolidation · 04 Implémentation

## Entrée

Arbitrage humain approuvé, analyse des occurrences et périmètre autorisé ; aucune étape de développement requise.

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

Traduire l’arbitrage en cartes par couche dans l’emplacement du projet si elles ne sont pas déjà prêtes :
objectifs, chemins, exclusions, tests, documentation, critères, preuves, missions et dépendances par commits.
Vérifier les identifiants dans toutes les références et les cartes des worktrees, puis confirmer le découpage
avec l’humain si l’arbitrage ne le détermine pas. Préparer les branches autorisées sans rebase implicite.
Réaliser une carte à la fois dans son worktree disponible. Documenter la convention approuvée au plus près
du code, corriger les occurrences retenues et implémenter le contrôle autorisé. Tester cas conformes,
écarts et exceptions ; son exécution doit rester indépendante du jugement d’une IA.
Exécuter les contrôles concernés et produire les preuves avant la vérification humaine. Ne pas étendre
les exceptions ou réduire les seuils au-delà de l’arbitrage. Consigner les occurrences non traitées.
Si plusieurs cartes sont nécessaires, présenter chacune à la vérification humaine puis attendre le commit
explicitement demandé avant la suivante ; ne pas enchaîner les autres étapes automatiquement.

## Sortie et preuve

Cartes affectées, corrections, convention documentée, tests du contrôle et commande reproductible avec résultats réels.

## Arrêt

Arbitrage insuffisant, couche occupée, dépendance non commitée ou contrôle qui ne prouve pas la règle : exposer le problème sans élargir la décision.
