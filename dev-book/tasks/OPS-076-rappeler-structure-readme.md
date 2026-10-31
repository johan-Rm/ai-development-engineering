# OPS-076 — Rappeler le respect de la structure des README

- Date : 2026-10-30
- Session de création : `01a18c1a-ab5a-7940-b95d-8e44ac3b92fc`
- Demande : DEM-025 ; brouillon `tmp/demande-ranger-ressources-design.md`, relatif au dépôt principal.
- Demande reconstituée : [DEM-025](../demand/DEM-025-ranger-ressources-design.md).
- Couche : devops ; worktree : `worktree/devops` ; branche : `layers/devops` conservée.
- HEAD observé : `e43b8461146522e0e7645e6e1692424acfd9f0ce`.
- État : validée et commitée ; à livrer.

## Objectif et périmètre

Conserver le rappel demandé par l’humain dans `AGENTS.md` : respecter les rubriques
et leur ordre, sans section, sommaire ou inventaire ajouté sans demande explicite ;
vérifier la structure du README dans le diff avant présentation.
Chemins autorisés : `AGENTS.md` et cette carte. Renvoyer aux conventions documentaires
existantes sans les recopier. Aucun changement d’autorisation Git ni de contrôle.

## Dépendances, critères et preuve

Aucune dépendance technique avec UX-002 ou OPS-077. Le diff AGENTS préexistant est
identifié comme issu de cette session et demandé explicitement par l’humain.
Vérifier l’unicité du rappel, la validité de son lien, la cohérence avec les conventions
et `git diff --check`. Consigner les résultats dans cette carte avant présentation.
Ne modifier aucun README, guide, skill ou autre fichier. Aucun commit au découpage.

## Verdict

Aucun verdict sur cette carte ; le changement préexistant reste non commité.

## Preuves — 2026-10-31

Reprise du seul ajout AGENTS identifié de cette session, sur le HEAD observé.
Un seul rappel présent ; `git diff --numstat -- AGENTS.md` : une ligne ajoutée,
aucune suppression. Lien `docs/README.md#conventions-techniques` vérifié : fichier
et rubrique existants. Relecture : structure des README préservée, renvoi aux conventions
sans copie de leur contenu ; aucune autorisation Git modifiée.
`git diff --check` réussi. Périmètre présenté : `AGENTS.md` modifié et cette carte
non suivie ; OPS-077 non suivie conservée sans implémentation. Index vide, aucun commit.

## Verdict humain — 2026-10-31

« validé » après présentation conjointe d’OPS-076 et OPS-077 ; validation des deux
cartes avec la limite navigateur préexistante présentée. Empreinte globale du contenu
soumis revérifiée : `4a6bde5f4e5c0467e06c93042f75c7cedbf4c07f62053674c7e8c700aa764813`.
Aucun changement fonctionnel depuis la présentation ; seules ces traces sont ajoutées.
Le contrôle navigateur reste en échec : cette validation ne vaut pas réussite du contrôle.

Commit local validé : `f14ada8f988c7378a1e37cb61f89e79137cc842c`.
