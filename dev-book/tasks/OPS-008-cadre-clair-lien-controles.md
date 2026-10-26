# OPS-008 — Cadre olive clair et lien vers les contrôles

> Note historique ajoutée lors d’OPS-010 : les mentions de fusion préparée, de fichiers non commités ou d’anciens chemins décrivent l’état lors de cette tâche. Elles ne décrivent pas l’état Git actuel ni un travail restant. Les cartes sont désormais réunies dans `dev-book/tasks/`.

- Statut : clôturée le 2026-10-23.
- Date : 2026-10-23.
- Mission : couche devops, branche `layers/devops`, worktree `worktree/devops` (chemin absolu résolu par Git).
- Périmètre : vue AIDE renommée, synthèse graphique, test navigateur et cette carte ; préserver OPS-007.
- Demande : cadre extérieur olive clair selon la charte ; liaison de Règles et contrôles vers Codebase Quality Control.
- Décision graphique finale : cadre olive pâle `#DDE2CF`, Codebase Quality Control olive clair `#A8B97A` avec texte noir, quatre badges olive principal `#6B7A4A` avec texte blanc cassé. Couleurs des actions inchangées.
- Preuve attendue : couleurs calculées, origine/destination de la liaison et géométrie vérifiées dans Chromium, captures relues.

## Vérifications

- Cadre extérieur en olive clair officiel #A8B97A ; textes du cadre et picto en noir. Actions humaines, demandes et Codebase Quality Control restent en olive #6B7A4A.
- Troisième liaison depuis le bas du footer Règles et contrôles vers le haut de Codebase Quality Control, recalculée au redimensionnement.
- Suite `codebase-quality-control/tests/browser/vue-aiod.cjs` réussie avec le Chromium déjà en cache (révision 1234, lancement explicitement configuré dans un wrapper temporaire) et bibliothèques extraites dans /tmp, sans installation système. Assertions sur couleurs, trois liaisons, origine de la nouvelle liaison, destination des flèches et géométrie ordinateur/mobile.
- Capture à 1366 × 768 relue ; panneau, numéros, rôles, absence de défilement vertical préservés.
- `git diff --check` : réussi. OPS-007 reste non commité ; aucune intégration ou publication distante.

## Correction de nuance

L’utilisateur précise vouloir l’olive pâle (#DDE2CF), et non l’olive clair (#A8B97A). Fond du cadre, référence graphique et assertion de couleur actualisés.

Essai demandé : Codebase Quality Control en olive clair #A8B97A avec texte noir ; cadre extérieur conservé en olive pâle #DDE2CF. Assertion de couleur actualisée.

Les quatre titres du cadre (Couches, Consolidation, IA Engineering, Documentation) utilisent l’olive principal #6B7A4A, à la demande de l’utilisateur.

Essai badges : les quatre titres du cadre ont un fond olive principal #6B7A4A et un texte blanc cassé #FAFAF6. Badges latéraux limités à la hauteur de leur libellé.

## Contrôle avant commit

Version finale validée dans Chromium le 2026-10-23 : cadre olive pâle, CQC olive clair, troisième liaison et interactions/géométrie ordinateur-mobile. Les 17 tests Python de l’outillage passent. `git diff --check` réussi.
