# web

## Couche web — initialisation AIOD

- Branche : `layers/web` ; préfixe des futures tâches : `WEB`.
- Dossier Git : le chemin absolu enregistré par `git worktree list`.
- La [carte BP-006](../dev-book/tasks/BP-006-initialiser-worktree-web.md)
  consigne l’initialisation, la base et les preuves.
- Le [routage commun](../docs/aiod/couches.md) définit les responsabilités de cette couche.
- Depuis ce worktree, `python3 scripts/process.py up` démarre le conteneur témoin ;
  `verify` observe sa page et `down` arrête son environnement en conservant les volumes.
- Aucun framework ni application : cet environnement sert uniquement à la recette AIOD.
- Vérifier la disponibilité de la couche avant une mission, même si Git affiche un arbre propre.

Les futurs socles `shared/` et cibles `targets/<nom>/` sont à définir avec le projet consommateur. Aucun build produit n’est installé.
