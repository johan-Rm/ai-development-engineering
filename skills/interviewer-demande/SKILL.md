---
name: interviewer-demande
description: "Clarifier une demande de développement avec l’humain et documenter le besoin avant son découpage."
---

# Développement · 01 Interview

## Entrée

Demande humaine, contexte et documentation produit disponibles.

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

Lire les décisions existantes avant de questionner. Reformuler le manque observable, les utilisateurs,
le résultat attendu et les contraintes. Poser seulement les questions qui changent le résultat ;
proposer des choix concrets et conserver les exclusions décidées. Couvrir les cas limites, preuves,
tests attendus et documentation ; signaler les dimensions sans objet.
Restituer les décisions à l’humain. Après accord, documenter la demande dans l’emplacement du projet
avec contexte, critères observables, contraintes et questions restantes. Ne créer ni cartes ni branches.
Une décision de besoin ne vaut pas validation d’un résultat implémenté.

## Sortie et preuve

Demande cadrée et référencée, décisions humaines et critères observables. Preuve : restitution confirmée et chemin du document.

## Arrêt

Besoin contradictoire ou décision nécessaire absente : garder les questions ouvertes et ne pas présenter la demande comme prête.
