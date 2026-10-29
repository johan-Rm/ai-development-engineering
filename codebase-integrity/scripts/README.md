# Outillage

`apps.py` installe, lance et vérifie les applications. `quality.py` regroupe les contrôles ;
`check.py` exécute seulement les tests de l’outillage.
`worktrees.py` gère les arbres Git ; `process.py` et `check_docker.py` vérifient la recette Docker.
Les scripts consomment les configurations depuis le worktree appelant :
`worktrees.py` lit `infra/config/layers.json` (couches, branches, rôles et identifiants),
sans dépendre de Docker ; `process.py` lit aussi `infra/process-check.json`
(image et base des ports de la recette). Les deux fichiers conservent respectivement
les enveloppes JSON `layers` et `process`. Un fichier absent ou invalide provoque
une erreur, sans création implicite ni repli vers l’ancien fichier de configuration.

Les scripts utilisent leur dépôt comme référence et ne parcourent pas les worktrees imbriqués.
Les commandes publiques et leurs préconditions sont documentées dans `SETUP.md` et `docs/architecture/01-codebase-integrity/points-de-controle.md`.
