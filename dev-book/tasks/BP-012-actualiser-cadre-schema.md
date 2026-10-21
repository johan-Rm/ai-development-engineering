# BP-012 — Actualiser les quatre éléments du cadre

- Statut : réalisée le 2026-10-20.
- Date : 2026-10-20.
- Mission historique : maintenance du cadre, sur la branche historique de maintenance, worktree principal.
- Périmètre : `docs/aiod/cadre-aiod.html` et cette carte. Préserver BP-011 non commité.
- Demande : représenter les quatre éléments et leurs sous-éléments validés dans le chat : Couches, Consolidation, IA Engineering, Documentation.
- Choix : un élément sur chaque côté du cadre olive, avec des libellés courts. Les deux boucles seront retravaillées séparément.
- Preuve : rendu Chromium sur ordinateur et mobile ; texte contenu dans le cadre, polices et couleurs conservées.
- Tests automatisés sans objet : modification d’une illustration SVG statique ; vérification visuelle et géométrique ponctuelle.

## Critères

- [x] Quatre thèmes avec leurs éléments sous-jacents.
- [x] Plein écran, coins arrondis et charte conservés.
- [x] Boucles inchangées et textes lisibles.

## Preuves

- SVG analysé : quatre groupes thématiques, coins arrondis conservés, actions des boucles inchangées.
- Chromium : plein écran à 1918 × 924 et 1366 × 768, tous les textes dans le cadre, Rationale et Inter chargées, aucune erreur JavaScript.
- Capture ordinateur relue : textes des quatre côtés lisibles, fonds des rôles et texte blanc cassé conservés.
- Mobile 390 × 844 : page sans débordement, schéma défilant horizontalement.
- PDF : une page paysage ; aucun bouton ajouté.
- `git diff --check` : réussi.

Le contenu intérieur a été légèrement resserré horizontalement pour réserver la place des textes latéraux. Les étapes et relations des deux boucles sont conservées. BP-011 reste non commité et n’a pas été modifié.

## Mise en commit — 2026-10-21

`git diff --check` réussi. Les preuves visuelles datées ci-dessus sont conservées. La suppression de la mention de version, demandée pendant BP-014, accompagne ici le même fichier statique.
