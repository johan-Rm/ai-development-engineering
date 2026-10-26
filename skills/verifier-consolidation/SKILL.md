---
name: verifier-consolidation
description: "Accompagner la vérification humaine de l’application d’un arbitrage et de ses contrôles de consolidation."
---

# Consolidation · 05 Vérification

## Entrée

Arbitrage, cartes, corrections, documentation, tests et résultats des contrôles disponibles.

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

Confronter les changements à l’arbitrage : occurrences couvertes, exceptions, écarts détectés et cas
conformes acceptés. Présenter la commande reproductible du contrôle, ses préconditions et les preuves
positives et négatives. Distinguer réussite technique et adéquation à la règle.
Demander à l’humain son verdict et consigner validation ou corrections sans inventer de décision.
Les corrections reprennent les cartes de consolidation concernées et reviennent à une nouvelle vérification.
Après validation, utiliser `commit-tache` seulement si le commit est explicitement demandé, avec un commit
par carte. Conserver les SHA pour la livraison de consolidation. Cet outil transversal ne requiert aucun
skill de la boucle de développement. Ne pas clôturer une carte sur une simple suite verte.

## Sortie et preuve

Verdict humain sur la règle appliquée et son garde-fou, corrections éventuelles et SHA des commits réellement autorisés.

## Arrêt

Preuves insuffisantes, couverture incomplète ou verdict absent : signaler ce qui reste à vérifier sans valider.
