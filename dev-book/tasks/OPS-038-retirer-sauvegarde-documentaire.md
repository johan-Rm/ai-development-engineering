# OPS-038 — Retirer la sauvegarde documentaire temporaire

- **Créée le** : 2026-10-24.
- **Session** : non disponible (Codex).
- **Statut** : ✅ fait le 2026-10-24.
- **Type** : docs.
- **Tests** : sans objet — suppression de documentation temporaire ; diff et absence de références actives vérifiés.
- **Mission** : devops, `layers/devops`, `worktree/devops`.
- **Demande** : supprimer docs_save/ de toutes les couches après réécriture de la documentation.
- **Périmètre** : neuf fichiers de docs_save/ et mention temporaire dans SETUP.md.
- **Hors périmètre** : nouvelle documentation et historique Git ; les mentions des cartes restent historiques.

## Livré et vérifié

Les neuf fichiers suivis ont été supprimés après vérification de l’absence de contenu supplémentaire. La mention active dans SETUP.md a été retirée. Les anciennes versions restent disponibles dans Git. `git diff --check` réussi. Nettoyage destiné à être intégré à develop puis propagé par avance rapide aux cinq couches après vérification de leurs états Git.
