# BP-016 — Corriger les étapes de la boucle IA de codage

- Statut : réalisée le 2026-10-20.
- Date : 2026-10-20.
- Mission historique : maintenance du cadre, sur la branche historique de maintenance, worktree principal.
- Périmètre : vue HTML interactive, test navigateur et cette carte. Préserver les autres changements.
- Demande : appliquer les six étapes validées : Interview, Découpage, Réalisation, Vérification humaine, Reconstitution et Finalisation. Cinq étapes IA, une étape humaine ; retour à la réalisation si corrections.
- Critères : en-tête Demandes et footer PRs conservés hors du cycle, détails actualisés, couleurs correctes, panneau au clic, absence de défilement vertical préservée.
- Preuve : test Chromium, contenu et rôles des étapes, captures ordinateur/mobile relues.

## Vérifications

- Étapes et détails remplacés par les six intitulés validés. Parcours : Interview → Découpage → Réalisation → Vérification → Reconstitution → Finalisation.
- Cinq actions IA en terre cuite ; Vérification en olive. Retour de correction vers Réalisation indiqué par la flèche montante et expliqué dans le panneau.
- Demandes et PRs centrées, hors du cycle, conservées.
- `node codebase-quality-control/tests/browser/vue-aiod.cjs web/targets/app` : réussi. Assertions sur les six actions et leurs rôles, détails de la vérification humaine, comportement au clic et absence de débordement vertical.
- Captures ordinateur/mobile générées ; capture à 1366 × 768 relue. Aucun changement de la boucle de consolidation ni des autres travaux en cours.
- `git diff --check` : réussi.

## Ordre explicite

Numéros 01 à 06 ajoutés aux actions : Interview 01, Découpage 02, Réalisation 03, Vérification 04, Reconstitution 05, Finalisation 06. Parcours supérieur de gauche à droite puis inférieur de droite à gauche ; l’étape humaine précède bien la reconstitution.

## Mise en commit — 2026-10-21

`node codebase-quality-control/tests/browser/vue-aiod.cjs web/targets/app` réussi dans Chromium, avec `PLAYWRIGHT_BROWSERS_PATH=/tmp/aiod-playwright` et les bibliothèques de `/tmp/aiod-browser-libs/root/usr/lib/x86_64-linux-gnu`. `git diff --check` réussi. Les cartes BP-013 à BP-021 sont livrées ensemble avec la version finale de la vue et de son test : leurs états intermédiaires non commités ne sont pas reconstruits. Écart à la convention un commit par tâche pour cette reprise du travail accumulé.
