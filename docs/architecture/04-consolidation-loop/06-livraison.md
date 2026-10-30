# Livraison

> Livrer les corrections et les contrôles qui renforceront les développements suivants.

## Entrée

Tâches validées et branche produite par la reconstitution de l’étape 05.

## Déroulement

L’IA exécute les contrôles de livraison, finalise les références documentaires et prépare les PRs. Chaque nouveau contrôle dispose d’une commande stable, de préconditions et d’un résultat attendu.

## Sortie

Des PRs de consolidation et des conventions techniques protégées par des vérifications reproductibles. Les contrôles bloquants doivent réussir avant la PR.

## Procédure associée

`livrer-consolidation`.

L’invocation autorise la livraison complète, selon les
[autorisations du projet](../../../AGENTS.md#workflow-et-autorisations).
Appliquer les [règles communes d’intégration et de suivi](../03-developpement-loop/06-livraison.md#intégration-et-suivi-communs-aux-deux-boucles) :
Rebase and merge, vérification distante, traçabilité des nouveaux SHA et protection
des couches occupées. L’étape 06 ne remplace pas la reconstitution de l’étape 05.
