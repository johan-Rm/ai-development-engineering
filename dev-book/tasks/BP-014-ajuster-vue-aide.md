# BP-014 — Ajuster la vue AIDE

- Statut : réalisée le 2026-10-20.
- Date : 2026-10-20.
- Mission historique : maintenance du cadre, sur la branche historique de maintenance, worktree principal.
- Périmètre : vue HTML interactive, schéma SVG de référence pour sa mention de version, index, tests navigateur et cette carte. Préserver les autres travaux.
- Demande : panneau superposé sans déplacement, fermeture fiable, signature discrète en bas à droite, nom « AIDE — AI Development Workflow Engineering », suppression de la mention « Pointillés : boucle de retour · Proposition v10 ».
- Preuves : test navigateur de stabilité géométrique et fermeture persistante souris/clavier/tactile ; captures relues.

## Preuves

- Suppression de la réduction de largeur à l’ouverture du panneau : position et dimensions de la zone de travail identiques avant/après, vérifiées par Chromium.
- Fermeture : annulation du survol différé, suspension jusqu’au mouvement volontaire du pointeur, retour du focus sans réouverture. Le survol différé permet également de cliquer les éléments placés sous le futur panneau.
- Signature AIDE en Rationale, avec les deux phrases demandées, en petit en bas à droite. Ancien grand titre retiré de la vue HTML. Nom mis à jour dans le titre du document, les descriptions accessibles et le panneau.
- Mention de version supprimée du schéma SVG de référence ; elle n’était pas présente dans la vue HTML.
- `node codebase-quality-control/tests/browser/vue-aiod.cjs web/targets/app` : réussi. Stabilité géométrique, fermeture persistante par bouton, Échap, clavier et tactile ; captures ordinateur/mobile relues.
- `git diff --check` : réussi. Aucun commit ni changement applicatif.

## Correction du nom

L’utilisateur corrige le développement de AIDE : « AI Development Engineering ». Signature, titre accessible et test navigateur actualisés ; le nom antérieur reste seulement dans le rappel historique de la demande.

## Espace des boucles et légende

Mention de pilotage humain supprimée. Légende Humain/IA réduite et déplacée en bas à gauche du cadre. Les deux boucles et leurs actions s’étirent dans l’espace libéré ; présentation mobile empilée conservée.

Vérification de cet ajustement : test Chromium réussi (légende en bas à gauche et absence de mention de pilotage incluses), capture ordinateur relue ; interactions et largeur mobile toujours validées. `git diff --check` réussi.

## Mise en commit — 2026-10-21

`node codebase-quality-control/tests/browser/vue-aiod.cjs web/targets/app` réussi dans Chromium, avec `PLAYWRIGHT_BROWSERS_PATH=/tmp/aiod-playwright` et les bibliothèques de `/tmp/aiod-browser-libs/root/usr/lib/x86_64-linux-gnu`. `git diff --check` réussi. Les cartes BP-013 à BP-021 sont livrées ensemble avec la version finale de la vue et de son test : leurs états intermédiaires non commités ne sont pas reconstruits. Écart à la convention un commit par tâche pour cette reprise du travail accumulé.
