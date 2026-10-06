# Gouvernance commune

## Avant d’écrire

Lire la demande, sa carte, [les couches](couches.md), [le workflow Git](git-workflow.md)
et [l’isolation](parallel-work.md). Vérifier les missions actives auprès du coordinateur.
Exécuter `python3 scripts/worktrees.py list` et `git status --short`.

Établir le chemin absolu du worktree et vérifier sa branche avec
`git -C /chemin/absolu branch --show-current`. Une mission indique : tâche, couche, branche,
chemin absolu, chemins autorisés, dépendances par SHA et preuve attendue.
Les commandes et écritures visent ce dossier explicitement.

## Conventions de workflow

- Référence publique : `master`. `main` est conservée comme référence historique.
- Intégration actuelle : branche de travail, en attendant la création de `develop` (BP-003).
  Aucun déploiement applicatif n’est configuré.
- Travail du blueprint : `layers/blueprint`. Aucun changement de tâche directement sur `main`.
- Cartes : `dev-book/tasks/BP-NNN-slug.md`. Vérifier les identifiants sur les branches concernées
  avant attribution ; aucun compteur concurrent automatique n’est fourni.
- Création : `python3 scripts/worktrees.py add --layer blueprint --branch layers/blueprint --base main`.
  La base est explicite, locale et résolue à un commit ; la commande ne fait pas de fetch.
- Une tâche à la fois, un commit par tâche avec tests pertinents, documentation et carte clôturée.
- Contrôle avant PR : `python3 scripts/check.py`. La relecture vérifie le comportement et le diff.
- Merge proposé : merge commit pour conserver les commits par tâche. Respecter la politique GitHub
  réellement configurée, vérifier le merge distant, puis réaligner les branches au repos.
- Commit, push, PR et merge uniquement lorsqu’ils sont demandés ; aucune action distante automatique.

## Réaliser et livrer

Écrire seulement dans le périmètre demandé. Les fichiers communs nécessaires sont coordonnés
avec leur consommateur. Ne pas reprendre une carte non commitée découverte dans un worktree.
Les dépendances reposent sur des commits identifiés, jamais sur la copie de changements non commités.

Préserver le travail existant et les `.env`. Ne pas stasher, forcer un push, supprimer un worktree
ou utiliser `reset --hard` pour résoudre une situation. Signaler les blocages et les besoins hors périmètre.

La fin de mission indique ce qui est livré, la preuve observée, les fichiers encore ouverts et
les points croisés hors périmètre. Ne pas lancer un agent ni entamer une autre tâche sans demande.
