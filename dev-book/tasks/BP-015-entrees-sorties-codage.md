# BP-015 — Séparer les demandes et PR du cycle de codage

- Statut : réalisée le 2026-10-20.
- Date : 2026-10-20.
- Mission historique : maintenance du cadre, sur la branche historique de maintenance, worktree principal.
- Périmètre : vue HTML, test navigateur et cette carte ; préserver les autres changements.
- Demande : demandes en entrée et PR en sortie, hors de la boucle, dans un en-tête et un pied de bloc.
- Décision : chaque demande alimente une ou plusieurs tâches ; le cycle commence par une tâche et conserve la livraison d’un commit. Les PR rassemblent les commits à l’extérieur du cycle.
- Preuve : DOM, panneau de détails et rendu ordinateur/mobile dans Chromium.

## Vérifications

Test Chromium réussi : demandes et PR absentes du cycle, présentes dans l’en-tête et le pied de bloc ; douze actions des deux boucles conservées. Interactions souris/clavier/tactile et superposition du panneau validées. Capture ordinateur relue ; largeur mobile vérifiée. `git diff --check` réussi.

## Correction demandée

L’utilisateur demande de limiter le changement aux ajouts demandés : en-tête Demande(s) et footer PR collés au bloc, sans flèches d’espacement ni sous-titres ajoutés. Le renommage proposé de Besoin en Tâche est annulé. Hauteur compactée pour conserver le schéma sans défilement sur ordinateur.

Le panneau s’ouvre uniquement par activation du bouton (clic, toucher, Entrée ou Espace), jamais au survol ni au simple focus. Les indications et le test navigateur sont actualisés.

Vérification finale : test Chromium réussi après simplification ; survol sans ouverture, activation au clic/Entrée/toucher, fermeture persistante. Capture à 1366 × 768 relue : en-tête et footer collés, ensemble visible sans défilement.

## Égalité des bandes du cadre

Bandes haute et basse de même hauteur : 56px sur ordinateur, 96px sur mobile pour conserver la lisibilité des textes. Signature limitée au titre « AIDE AI Development Engineering » et à la phrase sur le codage et la consolidation.

Égalité géométrique des bandes haute/basse vérifiée dans Chromium à 1918 × 924, 1366 × 768 et 390 × 844. Une seule phrase sous le titre, captures relues ; interactions toujours validées.

## Suppression du défilement vertical

Indication « Cliquez pour explorer. » supprimée ; marges et espacements réduits. Zone de contenu sans défilement vertical ; sur les petits écrans, les deux boucles restent côte à côte et se parcourent horizontalement, avec des actions plus compactes sur les fenêtres peu hautes. Le panneau de détails garde son défilement indépendant si nécessaire.

Vérification finale Chromium réussie : absence de texte d’aide, hauteur du contenu ne dépassant pas la zone et overflow vertical interdit à 1366 × 768 et 390 × 844 ; captures relues. Les tests de panneau restent réussis.

## Picto de séparation

Symbole composé officiel repris depuis les masques SVG et les proportions du document de charte, sans redessiner ses tracés. Variante en réserve, hauteur 12px, entre AIDE et son intitulé long. Décoratif pour les lecteurs d’écran ; aucune modification de hauteur du cadre.

## Libellés centrés et pluriels

En-tête « Demandes » et footer « PRs » centrés. Footer en terre cuite IA avec texte blanc cassé ; détails associés actualisés.

## Mise en commit — 2026-10-21

`node tests/browser/vue-aiod.cjs web/targets/app` réussi dans Chromium, avec `PLAYWRIGHT_BROWSERS_PATH=/tmp/aiod-playwright` et les bibliothèques de `/tmp/aiod-browser-libs/root/usr/lib/x86_64-linux-gnu`. `git diff --check` réussi. Les cartes BP-013 à BP-021 sont livrées ensemble avec la version finale de la vue et de son test : leurs états intermédiaires non commités ne sont pas reconstruits. Écart à la convention un commit par tâche pour cette reprise du travail accumulé.
