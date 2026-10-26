---
name: apres-pr-mergee
description: "Vérifier une fusion demandée et réaligner seulement les branches de travail libres sans perte de données."
---

# apres-pr-mergee

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

Entrée : PR fusionnée identifiée et demande de suivi après fusion.
Vérifier la fusion avec une preuve autoritative : état de la PR et commit de fusion, puis contenu
sur la cible. Un patch équivalent ou une liste vide de git cherry ne prouve pas à lui seul le merge.
Effectuer les lectures distantes et fetch uniquement selon l’autorisation donnée ; ne pas annoncer
une vérification distante si seule une référence locale a été lue.
Inventorier branches, worktrees, modifications locales, divergences et missions actives.
Mettre l’intégration à jour par avance rapide seulement si son arbre et son affectation le permettent.
Une branche propre peut être occupée : ne réaligner que celles confirmées libres, sans travail inédit.
Utiliser une avance rapide lorsque possible dans le bon worktree ; laisser intactes les divergences
issues de rebase ou squash et proposer leur traitement sans réécrire l’historique.
Sortie et preuve : état du merge, SHA observés, branches avancées et branches laissées intactes avec motif.
Arrêt : fusion non prouvée ou opération destructive nécessaire ; ne pas reset, stash, force-push,
supprimer de branche ou de worktree. Ne pas déclencher une nouvelle tâche.
