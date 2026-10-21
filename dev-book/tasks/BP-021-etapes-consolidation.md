# BP-021 — Intégrer les étapes validées de consolidation

- Statut : réalisée le 2026-10-21.
- Date : 2026-10-21.
- Mission historique : maintenance du cadre, sur la branche historique de maintenance, worktree principal (chemin absolu obtenu par `git rev-parse --show-toplevel`).
- Périmètre : étapes et détails de consolidation dans la vue HTML, test navigateur et cette carte. Préserver les autres changements.
- Demande : intégrer Interview, Analyse globale, Arbitrage, Implémentation, Vérification et Livraison, avec les textes validés dans le chat.
- Critères : six étapes numérotées, quatre IA et deux humaines ; analyse de toute la base de code ; arbitrage de la règle distinct de la vérification de son application ; entrée et sorties conservées ; pas de défilement vertical.
- Preuve : test Chromium ouvrant les six panneaux, contrôle des rôles et numéros, captures relues.

## Livré et vérifié

Les six étapes et leurs textes validés sont intégrés aux panneaux : Interview, Analyse globale, Arbitrage, Implémentation, Vérification, Livraison. Les numéros indiquent le sens de lecture ; Arbitrage (03) et Vérification (05) sont humains, les quatre autres étapes sont IA. Le retour de correction relie Vérification à Implémentation. Entrée, sorties et liens existants conservés.

- `node tests/browser/vue-aiod.cjs web/targets/app` : réussi. Numéros, intitulés, acteurs et six panneaux vérifiés ; analyse de toute la base de code, arbitrage de la règle, vérification des contrôles réalisés et exécution sans IA couverts.
- Capture à 1366 × 768 relue ; géométrie, liens, interaction au clic et absence de défilement vertical toujours validés sur ordinateur/mobile.
- `git diff --check` : réussi. Aucun commit ni modification des autres processus.

## Mise en commit — 2026-10-21

`node tests/browser/vue-aiod.cjs web/targets/app` réussi dans Chromium, avec `PLAYWRIGHT_BROWSERS_PATH=/tmp/aiod-playwright` et les bibliothèques de `/tmp/aiod-browser-libs/root/usr/lib/x86_64-linux-gnu`. `git diff --check` réussi. Les cartes BP-013 à BP-021 sont livrées ensemble avec la version finale de la vue et de son test : leurs états intermédiaires non commités ne sont pas reconstruits. Écart à la convention un commit par tâche pour cette reprise du travail accumulé.
