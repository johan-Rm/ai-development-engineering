# design

## Couche design — initialisation AIOD

- Branche : `layers/design` ; préfixe des futures tâches : `UX`.
- Dossier Git : le chemin absolu enregistré par `git worktree list`.
- La [carte BP-008](../dev-book/tasks/BP-008-initialiser-worktree-design.md)
  consigne l’initialisation, la base et les preuves.
- Le [routage commun](../docs/couches.md) définit les responsabilités de cette couche.
- Depuis ce worktree, `python3 codebase-quality-control/scripts/process.py up` démarre le conteneur témoin ;
  `verify` observe sa page et `down` arrête son environnement en conservant les volumes.
- Aucun framework ni application : cet environnement sert uniquement à la recette AIOD.
- Vérifier la disponibilité de la couche avant une mission, même si Git affiche un arbre propre.

Les maquettes et prototypes peuvent être relus au navigateur. Les composants livrés appartiennent au consommateur web ou backoffice.
