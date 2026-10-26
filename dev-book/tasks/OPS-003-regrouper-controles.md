# OPS-003 — Regrouper scripts et tests

> Note historique ajoutée lors d’OPS-010 : les mentions de fusion préparée, de fichiers non commités ou d’anciens chemins décrivent l’état lors de cette tâche. Elles ne décrivent pas l’état Git actuel ni un travail restant. Les cartes sont désormais réunies dans `dev-book/tasks/`.

- Statut : réalisée.
- Date : 2026-10-21.
- Mission : devops, branche `layers/devops`, worktree `/home/johan/www/lab/ai-orchestrated-development/worktree/devops`.
- Demande : rassembler les dossiers racine `scripts/` et `tests/` sous `codebase-quality-control/`.
- Périmètre : déplacement des deux dossiers, résolution des chemins, commandes CI et références documentaires.
- Dépendances : OPS-001 et OPS-002 préparées dans le même worktree.
- Critères : un dossier commun ; commandes utilisables après déplacement ; CI et documentation cohérentes ; tests applicatifs conservés dans leurs applications.
- Preuves attendues : suite Python depuis un autre dossier, commandes publiques, test navigateur et vérification du diff.

## Livré et vérifié

- Scripts et tests regroupés sous `codebase-quality-control/`, README commun ajouté.
- Chemins des commandes, de la configuration et de la CI actualisés.
- Imports, découverte des tests et racines des commandes corrigés après déplacement.
- Le créateur de worktrees lit la configuration du worktree appelant, même lorsque
  la racine principale utilise encore une ancienne organisation ; régression testée.
- Suite Python exécutée depuis `/tmp` : 16 tests réussis.
- Aide des commandes apps et worktrees : réussie.
- Test Chromium après déplacement : réussi.
- `git diff --check` : réussi.
