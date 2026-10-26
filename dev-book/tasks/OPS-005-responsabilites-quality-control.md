# OPS-005 — Définir les responsabilités du Codebase Quality Control

- Statut : réalisée.
- Date : 2026-10-21.
- Mission : devops, branche `layers/devops`, worktree `worktree/devops`.
- Demande : définir les responsabilités dans le README à la racine du dossier Codebase Quality Control.
- Périmètre : `codebase-quality-control/README.md` et cette carte.
- Dépendance : OPS-004, commit `9c5a987`.
- Critères : brique déterministe ; conventions définies exclusivement par les humains ; aucune modification par le processus de développement ; évolutions par consolidation sous décision et validation humaines.
- Preuve attendue : relecture du contenu, vérification des liens locaux et du diff.

## Livré et vérifié

Le README racine précise la fonction déterministe, l’autorité exclusive des humains sur les
conventions, l’interdiction de modification par le processus de développement et le passage
par la consolidation sous décision et validation humaines. Les commandes existantes sont conservées.

- Liens locaux du README : valides.
- Relecture du contenu et `git diff --check` : réussis.
- Modification documentaire uniquement ; aucune nouvelle suite de tests nécessaire.
