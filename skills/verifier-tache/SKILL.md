---
name: verifier-tache
description: "Accompagner la vérification humaine d’une tâche de développement et consigner son verdict explicite."
---

# Développement · 04 Vérification

## Entrée

Résultat implémenté, critères de carte, diff, tests, documentation et preuves disponibles.

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

Confronter chaque critère à la preuve correspondante et présenter à l’humain le résultat observable,
les chemins utiles, les commandes et limites. Examiner le périmètre et la cohérence avec les conventions.
L’humain valide ou demande des corrections ; sans réponse, aucun verdict n’est acquis.
Consigner fidèlement ce verdict dans la carte. Les corrections retournent à l’implémentation de cette tâche,
sans exécution automatique. Un constat global peut être formulé pour l’humain, sans ouvrir une autre boucle.
Après validation, le commit distinct est réalisé uniquement sur demande via l’outil transversal
`commit-tache`, s’il est disponible, ou la procédure de commit du projet. Conserver son SHA pour la reconstitution.
Ne pas faire dépendre ce verdict de l’ouverture d’une PR.

## Sortie et preuve

Verdict humain explicite par tâche, critères acceptés ou corrections précises ; SHA seulement si un commit a été autorisé et réellement créé.

## Arrêt

Preuve manquante ou verdict absent : rester en attente, sans clôture ni commit implicite.
