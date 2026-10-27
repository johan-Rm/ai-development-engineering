# OPS-006 — Préserver l’initialisation design avant intégration

> Note historique ajoutée lors d’OPS-010 : les mentions de fusion préparée, de fichiers non commités ou d’anciens chemins décrivent l’état lors de cette tâche. Elles ne décrivent pas l’état Git actuel ni un travail restant. Les cartes sont désormais réunies dans `dev-book/tasks/`.

- Statut : réalisée.
- Date : 2026-10-21.
- Mission : devops, branche `layers/devops`, worktree `worktree/devops`.
- Demande : fusionner tout le travail dans `develop` et mettre à jour les cinq couches.
- Périmètre : réunion de l’historique design, README de design et carte historique OPS-020.
- Dépendances : devops `c5067aa` et design `8ce031f`.
- Critères : commit design préservé sans réécriture ; carte clôturée conservée dans les archives ; liens et commandes adaptés à l’organisation actuelle.
- Preuve attendue : suite Python, vérification du diff et des liens, état Git sans conflit.

## Livré et vérifié

- Fusion du commit design préparée sans conflit, avec conservation de son historique.
- Carte OPS-020 clôturée conservée dans les archives et chemins personnels remplacés par `<depot>`.
- README design : lien vers la carte archivée et commande de recette actualisés.
- `python3 -B codebase-quality-control/scripts/check.py` : 17 tests réussis.
- Liens du README design : valides ; diff sans erreurs d’espacement.
- Aucun code applicatif ni point de contrôle modifié. Les contrôles applicatifs et le test
  navigateur avaient déjà réussi sur le code intégré ; cette réunion apporte uniquement de la documentation.
