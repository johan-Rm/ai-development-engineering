---
name: analyser-convention
description: "Analyser toute la base concernée par une proposition de convention et préparer les options d’arbitrage."
---

# Consolidation · 02 Analyse globale

## Entrée

Proposition de convention et périmètre à analyser ; aucun livrable de développement requis.

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

Examiner toutes les zones concernées par la règle, en respectant les exclusions du projet et sans parcourir
les copies de worktrees comme des occurrences supplémentaires. Relever fichiers, occurrences conformes,
écarts, exceptions et limites. Distinguer ce qui a été lu de ce qui reste non vérifié.
Rechercher les contrôles existants, leur portée et leurs angles morts. Proposer les corrections et un
contrôle déterministe avec cas conformes, écarts détectables et exceptions ; distinguer règle documentée
et règle déjà contrôlée. Comparer les options et leurs coûts, niveaux bloquants et impacts par couche.
Documenter l’analyse dans le dossier de la demande sans modifier code, contrôles ou conventions.
Un état Git ou un échantillon ne prouve pas une analyse globale ; expliciter toute zone inaccessible.

## Sortie et preuve

État des lieux référencé, couverture examinée, options de règle et de contrôle, périmètres de correction proposés.

## Arrêt

Zone essentielle inaccessible ou périmètre inconnu : signaler la couverture incomplète avant arbitrage.
