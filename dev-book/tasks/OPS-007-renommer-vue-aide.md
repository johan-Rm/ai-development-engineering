# OPS-007 — Renommer la vue AIDE

- Statut : clôturée le 2026-10-23.
- Date : 2026-10-23.
- Mission : couche devops, branche `layers/devops`, worktree `worktree/devops` (chemin absolu résolu par Git).
- Demande : renommer la vue en `vue-d-ensemble-ai-development-engineering.html` et relancer le serveur.
- Chemins autorisés : les deux noms de vue dans `docs/aiod/`, l’index de ce dossier, le test navigateur et cette carte.
- Preuve attendue : contenu HTML identique après renommage, références actives mises à jour, réponse HTTP 200 au nouveau nom.
- Tests : renommage sans changement de contenu ; comparaison SHA-256, vérification HTTP et `git diff --check`.

## Preuves

Renommage avec SHA-256 identique ; index documentaire et chemins du test navigateur actualisés. Serveur Python relancé sur 127.0.0.1:8090 depuis ce worktree. Nouveau fichier : HTTP 200. `git diff --check` réussi. Les anciennes cartes gardent leurs références historiques ; commit et intégration sur develop demandés le 2026-10-23.
