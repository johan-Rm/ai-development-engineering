---
name: interviewer-constat
description: "Clarifier un constat de consolidation et documenter une proposition de convention technique à examiner."
---

# Consolidation · 01 Interview

## Entrée

Constat humain direct, revue ou observation disponible ; aucune demande de développement préalable nécessaire.

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

Lire les règles existantes et préciser avec l’humain le problème observé, ses conséquences et le domaine
concerné. Distinguer correction ponctuelle et convention à examiner globalement. Formuler la règle envisagée,
son périmètre, ses critères de conformité et ses exceptions supposées sans les présenter comme approuvés.
Clarifier les contraintes et le résultat attendu ; ne poser que les questions encore ouvertes.
Après confirmation de la restitution, documenter la proposition dans l’emplacement des demandes du projet,
avec le constat, les exemples disponibles et les questions pour l’analyse. Ne pas modifier le code,
les conventions en vigueur ni leurs contrôles ; ne pas préparer de cartes d’implémentation avant arbitrage.

## Sortie et preuve

Proposition documentée, exemples du constat et critères de conformité à analyser ; aucune règle adoptée implicitement.

## Arrêt

Constat invérifiable ou intention ambiguë : préciser les informations manquantes sans inventer de règle.
