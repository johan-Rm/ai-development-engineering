# Dossiers de travail Git

Ce dossier est réservé aux worktrees des couches, créés sur affectation d’une tâche.

```sh
python3 codebase-integrity/scripts/worktrees.py list
python3 codebase-integrity/scripts/worktrees.py add --layer devops --branch layers/devops --base develop
```

Si `layers/devops` est déjà sortie dans un worktree, la commande retourne son chemin.
La création ne lance rien, ne copie pas de secrets et conserve les fichiers existants.
Un dossier non enregistré ou une branche inattendue déclenche une erreur.
Lire [le guide des couches](../docs/02-cadre/couches/index.md).

Les réunions utilisent un temporaire extérieur au dépôt, avec un nom comme
`<projet>-reunion-008`. Aucun dossier de réunion ni nom `DEM-*` dans ce dossier.
Voir [la reconstitution](../docs/03-developpement-loop/05-reconstitution.md).
