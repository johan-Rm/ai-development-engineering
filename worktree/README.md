# Dossiers de travail Git

Ce dossier est réservé aux worktrees réels, créés sur affectation d’une tâche.

```sh
python3 scripts/worktrees.py list
python3 scripts/worktrees.py add --layer blueprint --branch layers/blueprint --base develop
```

Si `layers/blueprint` est déjà sortie à la racine, la commande retourne cette racine.
La création ne lance rien, ne copie pas de secrets et conserve les fichiers existants.
Un dossier non enregistré ou une branche inattendue déclenche une erreur.
Lire [la procédure complète](../docs/aiod/parallel-work.md).
