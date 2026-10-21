# BP-020 — Définir les quatre thèmes du cadre

- Statut : réalisée le 2026-10-20.
- Date : 2026-10-20.
- Mission : blueprint, branche `layers/blueprint`, worktree principal (chemin absolu obtenu par `git rev-parse --show-toplevel`).
- Périmètre : détails des thèmes de la vue HTML, présentation des accroches dans le panneau, test navigateur et cette carte.
- Demande : intégrer les quatre accroches et définitions validées pour Couches, Consolidation, IA Engineering et Documentation ; mettre en avant les bénéfices des couches.
- Critères : accroche visible au premier regard dans le panneau, définition puis éléments sous-jacents ; parallélisme, limitation des conflits, facilité de vérification et périmètres explicités ; schéma et autres détails conservés.
- Preuve : ouverture des quatre thèmes dans Chromium et vérification des accroches, définitions, interactions et géométrie.

## Livré et vérifié

Les quatre thèmes affichent l’accroche validée en Inter 500, une définition puis leurs éléments sous-jacents. Les bénéfices des couches sont détaillés : parallélisme et limitation des conflits, vérification, périmètres, isolation des ressources, contrats et traçabilité.

- `node tests/browser/vue-aiod.cjs web/targets/app` : réussi ; quatre accroches et définitions visibles, graisse vérifiée, absence de définition résiduelle après ouverture d’une étape. Autres interactions et géométrie conservées.
- Capture du panneau Couches relue ; contenu long défilant dans le panneau sans déplacer le schéma.
- `git diff --check` : réussi. Présentation du schéma et autres travaux conservés ; aucun commit.

## Mise en commit — 2026-10-21

`node tests/browser/vue-aiod.cjs web/targets/app` réussi dans Chromium, avec `PLAYWRIGHT_BROWSERS_PATH=/tmp/aiod-playwright` et les bibliothèques de `/tmp/aiod-browser-libs/root/usr/lib/x86_64-linux-gnu`. `git diff --check` réussi. Les cartes BP-013 à BP-021 sont livrées ensemble avec la version finale de la vue et de son test : leurs états intermédiaires non commités ne sont pas reconstruits. Écart à la convention un commit par tâche pour cette reprise du travail accumulé.
