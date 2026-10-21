# BP-017 — Relier la vérification à la consolidation

- Statut : réalisée le 2026-10-20.
- Date : 2026-10-20.
- Mission historique : maintenance du cadre, sur la branche historique de maintenance, worktree principal.
- Périmètre : vue HTML, test navigateur et cette carte ; préserver les autres changements.
- Demande : liaison depuis la vérification humaine vers les demandes de consolidation ; en-tête Demandes et footer à deux sorties (PRs de consolidation, règles et contrôles).
- Critères : liaison cliquable avec détails ; deux critères de vérification documentés ; consolidation pouvant produire du code, une règle ou les deux ; pas de défilement vertical ni déplacement du contenu par le panneau.
- Preuve : tests Chromium et captures ordinateur/mobile.

## Livré

- En-tête Demandes humain et footer à deux sorties IA, collés au bloc : PRs de consolidation ; Règles et contrôles.
- Liaison HTML/CSS calculée depuis la vérification humaine vers l’en-tête de consolidation. Libellé cliquable « Demande de consolidation » ; tracé adapté au redimensionnement sans SVG.
- Détails de vérification : résultat attendu, cohérence avec la trajectoire, correction de la tâche ou demande de consolidation.
- Détails de sortie : corrections/refactorisations et/ou règles validées, avec contrôles déterministes lorsque c’est possible. Les contrôles enrichis alimentent les prochaines vérifications.

## Preuves

- `node codebase-quality-control/tests/browser/vue-aiod.cjs app/web/targets/app` : réussi ; entrée et deux sorties hors du cycle, détails de liaison et contrôles, origine géométrique de la liaison sur Vérification, interactions et absence de débordement vertical.
- Captures ordinateur/mobile générées ; vue à 1366 × 768 et détail du tracé relus. Tracé : source à droite de Vérification, cible sur l’en-tête Demandes de consolidation.
- `git diff --check` : réussi. Les étapes internes de consolidation sont conservées pour leur examen ultérieur ; aucun commit demandé.

## Finalité déterministe et périmètre global

Titre du processus rendu cliquable. Les détails précisent l’examen et la correction de toute la base de code, l’aide possible de l’IA à l’analyse et à l’écriture, et la sortie durable attendue : tests/vérificateurs reproductibles exécutés sans IA en CI/CD ou à la demande. Détails des demandes, analyse, automatisation, PRs, règles et contrôles harmonisés. Aucun nouveau texte visible hors du panneau.

Vérification de ces précisions : test Chromium réussi, notamment ouverture du titre et présence du périmètre global, de la contribution possible de l’IA et de l’exécution sans IA en CI/CD ou à la demande ; contrôles géométriques et interactions conservés. `git diff --check` réussi.

## Position des titres

Titres des deux processus déplacés au-dessus de leurs en-têtes Demandes. Titre de consolidation toujours cliquable ; espacement compact et coins arrondis conservés sur les en-têtes.

Titres renommés à la demande de l’utilisateur : « Process de développement » et « Process de consolidation ».

## Cycles internes

Mention « Cycle IA » ajoutée dans chacun des deux blocs, avec symbole de répétition et flèche de retour à gauche des actions reliant la fin au début de l’itération. Les titres des processus et leurs entrées/sorties restent distincts ; le retour de correction vers Réalisation est conservé.

Vérification des cycles internes : test Chromium réussi, deux mentions et deux retours présents, interactions et absence de défilement vertical conservées ; capture ordinateur relue.

## Libellé vertical du cycle

Suppression des lignes de titre internes « Cycle IA ». Libellés replacés verticalement sur les flèches de retour à gauche des actions, pour récupérer la hauteur occupée. Les titres de processus restent inchangés.

## Mise en commit — 2026-10-21

`node codebase-quality-control/tests/browser/vue-aiod.cjs app/web/targets/app` réussi dans Chromium, avec `PLAYWRIGHT_BROWSERS_PATH=/tmp/aiod-playwright` et les bibliothèques de `/tmp/aiod-browser-libs/root/usr/lib/x86_64-linux-gnu`. `git diff --check` réussi. Les cartes BP-013 à BP-021 sont livrées ensemble avec la version finale de la vue et de son test : leurs états intermédiaires non commités ne sont pas reconstruits. Écart à la convention un commit par tâche pour cette reprise du travail accumulé.
