---
name: decouper-demande
description: "Décomposer une demande cadrée de développement en cartes par couche, dépendances et missions prêtes."
---

# Développement · 02 Découpage

## Entrée

Demande cadrée et décisions humaines identifiées.

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

Répartir les responsabilités selon le routage du projet, sans inventer de couche. Pour chaque carte,
fixer objectif, exclusions, chemins autorisés, critères, tests proportionnés, documentation, preuve,
worktree absolu et branche. Identifier les dépendances par commits existants ; une tâche amont sans commit
reste explicitement à résoudre avant son consommateur. Vérifier la complétude par rapport à la demande.
Attribuer les identifiants depuis l’historique de toutes les références locales et les fichiers des
worktrees concernés, sans fetch implicite. Utiliser un identifiant de session fiable ou signaler son absence.
Faire confirmer le découpage avant d’écrire les cartes. Préparer les branches dans les worktrees affectés,
après vérification des missions actives ; conserver une branche existante sans rebase implicite.
Une base locale explicite suffit si le projet le prévoit ; ne pas annoncer de synchronisation distante.
Ne pas implémenter les cartes.

## Sortie et preuve

Cartes et matrice demande/tâches, ordre et dépendances, état réel des branches préparées. Preuve : chemins des cartes et états Git observés.

## Arrêt

Couche occupée, identifiant ambigu ou dépendance sans commit : signaler les missions non prêtes sans copier le travail non commité.
