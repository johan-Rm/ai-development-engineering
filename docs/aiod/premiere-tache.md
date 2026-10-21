# Première tâche à essayer ensemble

Objectif : observer l’isolation Git d’une couche API, puis vérifier qu’une relance conserve
le travail. Cet essai ne lance aucun serveur ; le démarrage des applications est décrit séparément dans [le guide](../demarrage.md).

## Préparer un dépôt jetable

Depuis la racine du blueprint, avec Python 3 et Git :

```sh
AIOD_SOURCE="$PWD"
AIOD_TRIAL="$(mktemp -d /tmp/aiod-recette.XXXXXX)"
mkdir -p "$AIOD_TRIAL/scripts"
cp "$AIOD_SOURCE/codebase-quality-control/scripts/worktrees.py" "$AIOD_SOURCE/codebase-quality-control/scripts/aiod.json" "$AIOD_TRIAL/codebase-quality-control/scripts/"
cd "$AIOD_TRIAL"
git init -b develop
git config user.name 'AIOD Recette'
git config user.email 'recette@example.invalid'
printf '/worktree/
' > .gitignore
git add .gitignore codebase-quality-control/scripts/worktrees.py codebase-quality-control/scripts/aiod.json
git commit -m 'chore: préparer la recette locale'
```

Conserver le chemin affiché par `pwd`. Le dépôt ne possède aucun remote.

## Créer puis réutiliser

```sh
python3 codebase-quality-control/scripts/worktrees.py add --layer api --branch layers/api --base develop
printf 'preuve locale
' > worktree/api/preuve.txt
python3 codebase-quality-control/scripts/worktrees.py add --layer api --branch layers/api --base develop
python3 codebase-quality-control/scripts/worktrees.py list
cat worktree/api/preuve.txt
```

Verdict attendu : première création, puis réutilisation du même chemin absolu ; API modifiée,
principal propre, fichier intact. Une API modifiée reste occupée par cette recette.

## Appeler depuis un arbre secondaire

```sh
cd worktree/api
python3 codebase-quality-control/scripts/worktrees.py add --layer web --branch layers/web --base develop
git worktree list
```

Le dossier web doit être à côté du dossier API, sous le `worktree/` du principal,
jamais à l’intérieur de `worktree/api/`. Aucun `.env` n’est généré.

## Notre verdict ensemble

Vérifier les chemins, les branches et la conservation du fichier. Noter les points de confusion
avant d’appliquer la méthode au produit. Les contrôles automatiques complètent cette recette :
ils exercent aussi les destinations occupées, branches inattendues et liens symboliques.
Les dépôts de test sont nettoyés automatiquement ; ce dépôt manuel reste disponible pour inspection.
