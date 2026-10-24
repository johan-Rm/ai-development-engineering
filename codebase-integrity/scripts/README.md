# Outillage

`apps.py` installe, lance et vérifie les applications. `quality.py` regroupe les contrôles ;
`check.py` exécute seulement les tests de l’outillage.
`worktrees.py` gère les arbres Git ; `process.py` et `check_docker.py` vérifient la recette Docker.
`aiod.json` déclare les couches et les identifiants de cette recette.

Les scripts utilisent leur dépôt comme référence et ne parcourent pas les worktrees imbriqués.
Les commandes publiques et leurs préconditions sont documentées dans `SETUP.md` et `docs/01-codebase-integrity/points-de-controle.md`.
