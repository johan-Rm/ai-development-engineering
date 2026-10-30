# Dossiers de travail Git

Ce dossier est réservé aux worktrees des couches, créés sur affectation d’une tâche.

```sh
python3 codebase-integrity/scripts/worktrees.py list
python3 codebase-integrity/scripts/worktrees.py add --layer devops --branch layers/devops --base develop
```

Si `layers/devops` est déjà sortie dans un worktree, la commande retourne son chemin.
La création ne lance rien, ne copie pas de secrets et conserve les fichiers existants.
Un dossier non enregistré ou une branche inattendue déclenche une erreur.
Lire [le guide des couches](../docs/architecture/02-cadre/couches/organisation.md).

La reconstitution utilise une branche de demande dans un worktree existant libre
et propre. Aucun dossier de réunion supplémentaire ni nom `DEM-*` dans ce dossier.
Voir [la reconstitution](../docs/architecture/03-developpement-loop/05-reconstitution.md).
