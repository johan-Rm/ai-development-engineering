# api

## Couche api — initialisation AIOD

- Branche : `layers/api` ; préfixe des futures tâches : `API`.
- Dossier Git : le chemin absolu enregistré par `git worktree list`.
- La [carte BP-005](../dev-book/tasks/BP-005-initialiser-worktree-api.md)
  consigne l’initialisation, la base et les preuves.
- Le [routage commun](../docs/aiod/couches.md) définit les responsabilités de cette couche.
- Depuis ce worktree, `python3 scripts/process.py up` démarre le conteneur témoin ;
  `verify` observe sa page et `down` arrête son environnement en conservant les volumes.
- Aucun framework ni application : cet environnement sert uniquement à la recette AIOD.
- Vérifier la disponibilité de la couche avant une mission, même si Git affiche un arbre propre.
