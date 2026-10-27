# Configuration du cadre

Configuration commune des couches du projet AIDE.

## Rôle et responsabilités

`layers.json` définit les couches : branches, rôles et identifiants stables.
Le cadre possède cette définition ; les scripts la consomment depuis le worktree
appelant. Adapter ensemble ce fichier et la table des [couches](../docs/02-cadre/couches/index.md).
La recette Docker appartient à [infra/](../infra/README.md), dans `process-check.json`.

## Conventions techniques

Conserver l’enveloppe JSON `layers`. Chaque clé de couche correspond à son nom ;
`branch` indique sa branche, `role` sa responsabilité et `id` son identifiant stable
positif et unique. L’ordre des couches ne détermine pas les ports de la recette.
La création des worktrees ne nécessite pas la configuration Docker.
Les outils ne créent pas implicitement une configuration manquante et ne reviennent
pas à l’ancien fichier `codebase-integrity/scripts/aiod.json`.
