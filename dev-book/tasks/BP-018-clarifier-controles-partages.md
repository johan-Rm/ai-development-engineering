# BP-018 — Clarifier les contrôles partagés

- Statut : réalisée le 2026-10-20.
- Date : 2026-10-20.
- Mission : blueprint, branche `layers/blueprint`, worktree principal.
- Périmètre : zone des contrôles de la vue HTML, test navigateur et cette carte. Préserver les autres travaux.
- Demande : clarifier les relations entre développement, consolidation et contrôles ; retirer l’ambiguïté entre PR et livraison.
- Critères : lecture explicite de la production des contrôles par la consolidation et de leur exécution par le développement ; exécution sans IA, en CI/CD ou à la demande ; détails au clic ; pas de défilement vertical.
- Preuve : test Chromium et captures ordinateur/mobile.

## Livré et vérifié

- Retrait des mentions « Produit · changement livré » et « Règles et contrôles enrichissent le cadre » de cette zone.
- Bande commune : Développement (exécute) ← Contrôles déterministes ← Consolidation (enrichit). Le centre précise « Sans IA · CI/CD ou à la demande » et reste cliquable.
- Détails explicitant le rôle de chaque processus, l’indépendance de l’IA à l’exécution et la distinction PR/livraison.
- `node tests/browser/vue-aiod.cjs web/targets/app` : réussi ; contenu de la bande et du panneau, géométrie, interactions et absence de débordement vertical.
- Capture à 1366 × 768 relue ; tests ordinateur/mobile réussis. `git diff --check` réussi.

Ajustement typographique demandé : les deux libellés verticaux « Cycle IA » utilisent Inter 400, 13px.

## Appels aux contrôles dans le développement

Références explicites sur les étapes 03 (contrôles à la demande) et 06 (contrôles obligatoires). La bande partagée référence 03/06 ; la sortie PRs affiche « contrôles OK requis ». Les détails précisent qu’une exécution pendant la réalisation ne supprime pas le passage final et qu’un échec empêche l’ouverture de la PR. La même exigence est rappelée pour les PRs de consolidation.

Vérification de ces appels : test Chromium réussi avec assertions sur 03, 06 et la condition de sortie PR ; capture ordinateur relue, géométrie et interactions ordinateur/mobile toujours validées. `git diff --check` réussi.

## Correction visuelle des liens

Annotations ajoutées dans les cartes et le footer retirées. Liaisons HTML/CSS réelles des étapes 03 et 06 au bloc de contrôles, avec routage dans les espaces libres et interruption au croisement avec la demande de consolidation. Bloc de contrôles en olive et texte blanc cassé, conformément à son rattachement au cadre humain. Les précisions sur contrôles facultatifs en 03 et obligatoires avant PR restent dans le panneau.

Vérification de la correction visuelle : test Chromium réussi, avec coordonnées des liaisons depuis les bords de 03 et 06 jusqu’au bloc vert, couleur olive calculée, absence d’annotations ajoutées, géométrie et interactions ordinateur/mobile. Capture à 1366 × 768 relue. `git diff --check` réussi.

Texte « en cas de correction » retiré à la demande de l’utilisateur ; flèches de retour et disposition conservées.

Indication répétée « Cliquez sur un élément pour afficher ses détails. Échap pour fermer. » supprimée du panneau de détails.

## Mise en commit — 2026-10-21

`node tests/browser/vue-aiod.cjs web/targets/app` réussi dans Chromium, avec `PLAYWRIGHT_BROWSERS_PATH=/tmp/aiod-playwright` et les bibliothèques de `/tmp/aiod-browser-libs/root/usr/lib/x86_64-linux-gnu`. `git diff --check` réussi. Les cartes BP-013 à BP-021 sont livrées ensemble avec la version finale de la vue et de son test : leurs états intermédiaires non commités ne sont pas reconstruits. Écart à la convention un commit par tâche pour cette reprise du travail accumulé.
