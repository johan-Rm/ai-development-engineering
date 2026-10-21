# Dossiers de travail Git

Ce dossier est réservé aux worktrees réels, créés sur affectation d’une tâche.

```sh
python3 scripts/worktrees.py list
python3 scripts/worktrees.py add --layer devops --branch layers/devops --base develop
```

Si `layers/devops` est déjà sortie dans un worktree, la commande retourne son chemin.
La création ne lance rien, ne copie pas de secrets et conserve les fichiers existants.
Un dossier non enregistré ou une branche inattendue déclenche une erreur.
Lire [la procédure complète](../ia-engineering/parallel-work.md).
