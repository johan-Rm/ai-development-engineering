# BP-013 — Vue d’ensemble AIOD en HTML interactif

- Statut : réalisée le 2026-10-20.
- Date : 2026-10-20.
- Mission historique : maintenance du cadre, sur la branche historique de maintenance, worktree principal.
- Périmètre : nouvelle vue `docs/aiod/vue-d-ensemble-aiod.html`, index documentaire, test navigateur et cette carte. Préserver les corrections BP-011, BP-012 et le schéma SVG existant.
- Demande : convertir la représentation en HTML/CSS, avec détails dans un panneau latéral au survol et au clic.
- Critères : quatre thèmes validés, éléments sous-jacents dans le panneau, boucles conservées, couleurs et polices conservées ; fonctionnement souris, clavier et tactile ; fermeture et absence de débordement mobile.
- Preuve attendue : test navigateur Chromium et captures relues sur ordinateur et mobile.

## Livré et vérifié

- Vue autonome HTML/CSS/JavaScript, sans SVG, canvas, framework ni requête externe. Polices embarquées reprises du schéma de référence, licence conservée.
- Les quatre thèmes restent sur le cadre olive. Leurs éléments sous-jacents sont affichés seulement dans le panneau de détails.
- Douze actions des boucles conservées, avec leur acteur unique ; couleurs olive/terre cuite, texte blanc cassé, aplats sans bordure. Les flèches sont des caractères HTML.
- Survol et focus : exploration. Clic : détails maintenus pendant les autres survols. Fermeture par bouton ou Échap avec retour du focus. Tactile : ouverture et fermeture au toucher.
- `node codebase-quality-control/tests/browser/vue-aiod.cjs web/targets/app` : réussi dans Chromium (bibliothèques et navigateur temporaires fournis par l’environnement de vérification). Absence de SVG, douze actions, contenu du panneau, clic maintenu, clavier, focus et tactile contrôlés.
- Captures relues à 1918 × 924 et 390 × 844, avec et sans panneau. Largeur de page vérifiée aussi à 1366 × 768 ; aucun débordement horizontal. La zone intérieure défile sur les petits écrans.
- `git diff --check` : réussi. Le schéma SVG et les corrections précédentes sont conservés, sans commit supplémentaire.

## Mise en commit — 2026-10-21

`node codebase-quality-control/tests/browser/vue-aiod.cjs web/targets/app` réussi dans Chromium, avec `PLAYWRIGHT_BROWSERS_PATH=/tmp/aiod-playwright` et les bibliothèques de `/tmp/aiod-browser-libs/root/usr/lib/x86_64-linux-gnu`. `git diff --check` réussi. Les cartes BP-013 à BP-021 sont livrées ensemble avec la version finale de la vue et de son test : leurs états intermédiaires non commités ne sont pas reconstruits. Écart à la convention un commit par tâche pour cette reprise du travail accumulé.
