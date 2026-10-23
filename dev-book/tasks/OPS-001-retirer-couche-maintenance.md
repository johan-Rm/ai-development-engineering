# OPS-001 — Rattacher la maintenance du cadre à devops

> Note historique ajoutée lors d’OPS-010 : les mentions de fusion préparée, de fichiers non commités ou d’anciens chemins décrivent l’état lors de cette tâche. Elles ne décrivent pas l’état Git actuel ni un travail restant. Les cartes sont désormais réunies dans `dev-book/tasks/`.

- Statut : réalisée ; réunion des historiques préparée sans commit.
- Date : 2026-10-21.
- Demande : conserver uniquement les cinq couches validées et retirer la couche de maintenance supplémentaire.
- Mission : devops, branche `layers/devops`, worktree `/home/johan/www/lab/ai-orchestrated-development/worktree/devops`.
- Périmètre autorisé : configuration des couches, gouvernance, documentation de routage et références des cartes historiques.
- Dépendances : état courant du cadre `841378d` et initialisation devops `79dd507`.
- Critères : cinq couches configurées ; maintenance du cadre attribuée à devops ; aucune référence à une sixième couche dans les fichiers courants ; historique conservé sans réattribution fictive des anciennes missions.
- Preuve attendue : tests de l’outillage, recherche des références retirées et contrôle du diff.

## Préservation Git

Les deux historiques ont été réunis dans l’index du worktree devops par une fusion locale
préparée sans commit. La branche historique reste conservée tant que cette réunion n’est pas
commitée ; aucune suppression forcée, publication ou réécriture des commits historiques.

## Livré et vérifié

- Configuration limitée aux cinq couches ; identifiants et branches de ces couches conservés.
- Consignes, documentation et outillage communs attribués à devops, préfixe OPS.
- Gouvernance, tableau des responsabilités et exemple de création de worktree actualisés.
- Références aux anciennes missions reformulées sans réécrire leur rattachement historique.
- `python3 -B codebase-quality-control/scripts/check.py` : 15 tests réussis.
- Contrôle de la configuration réelle : cinq couches, branches cohérentes et identifiants 1 à 5.
- Recherche dans les fichiers suivis : aucune référence restante au nom de l’ancienne branche.
- `git diff --check` : réussi pour les modifications de cette tâche. Le diff de fusion déjà
  préparé contient un espace de fin de ligne préexistant dans la charte graphique, conservée intacte.
- La branche Git historique existe encore, localement et comme référence distante connue :
  ses commits sont préservés. Aucune suppression distante ni aucun commit demandés ou exécutés.
