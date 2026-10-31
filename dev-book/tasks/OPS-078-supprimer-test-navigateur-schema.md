# OPS-078 — Supprimer le test navigateur du schéma

- Demande : [DEM-027](../demand/DEM-027-supprimer-test-navigateur-schema.md).
- Date : 2026-10-31
- Session de création : `01a18c1a-ab5a-7940-b95d-8e44ac3b92fc`
- État : validée ; commit local en cours, à livrer.
- Couche : devops ; worktree : `worktree/devops` ; branche : `layers/devops` conservée.
- Base : `b916a7d87e7f58e8ced927951420607adcb3cc41` ; aucune dépendance amont.

## Objectif et chemins autorisés

Appliquer le retrait confirmé et les critères de DEM-027, dont l’analyse fait référence.
Chemins : `codebase-integrity/tests/browser/vue-aiod.cjs`, son `README.md`,
la présente carte et la demande pour ses seules traces de suivi.
Reprendre les deux suppressions préexistantes de cette session sans les restaurer
ni les recréer. Aucun autre appel actif à modifier identifié par l’analyse.

## Exclusions

Ne modifier ni schéma HTML, tests applicatifs, dépendances Playwright, installation
Chromium, workflow CI, conventions générales ou tests des autres vérificateurs.
Préserver les chemins historiques, résultats et verdicts du dev-book.
Aucun nouveau contrôle permanent, aucune modification de structure des README conservés.

## Contrôles et preuves attendus

- Vérifier l’absence des deux fichiers, puis rechercher leurs noms et chemins
  dans les fichiers Git suivis/non ignorés ; qualifier les seules références historiques.
- Comparer le diff à la base : seules les deux suppressions et les documents
  de suivi DEM-027/OPS-078 sont attendus ; schéma et tests des applications inchangés.
- Exécuter `python3 codebase-integrity/scripts/check_docs.py`,
  `git diff --check` et `python3 codebase-integrity/scripts/quality.py`.
  Consigner commandes, résultats finaux et limites ici, sans présumer leur réussite.
- Le contrôle des commits sera exécuté sur la plage à livrer après création
  des commits validés, conformément aux étapes suivantes.

## Livraison prévue

Validation humaine du résultat et commit local distinct à l’étape 04 ; reconstitution
sur `demands/DEM-027` dans le principal à l’étape 05. Aucun commit ni nouvelle
implémentation à l’analyse. Le constat et les décisions restent dans la demande.

## Réalisation et verdict

Reprise le 2026-10-31 des deux suppressions déjà effectuées dans cette session,
sur la base indiquée. Aucun autre changement fonctionnel ajouté.

- Absence des deux fichiers confirmée ; `git diff --name-only` contient uniquement
  leurs chemins. Diff : deux suppressions, 243 lignes retirées.
- Recherche dans les fichiers Git suivis/non ignorés, hors worktrees, binaires et `.env` :
  aucune référence active ; 23 documents de demandes/cartes contiennent uniquement
  des traces historiques ou de suivi. Aucun lien historique réécrit.
- Schéma HTML, tests applicatifs, CI et dépendances : inchangés, confirmé par le diff.
- `python3 codebase-integrity/scripts/check_docs.py` : réussi ; limite signalée
  `docs/README.md` (référence dynamique), aucune exception ajoutée.
- `git diff --check` : réussi.
- `python3 codebase-integrity/scripts/quality.py` : code de sortie 0, exécuté hors
  bac à sable pour le serveur HTTP temporaire des tests. Types des demandes, liens,
  81 tests d’outillage, contrat API, conteneur, mapping, OpenAPI, types et builds
  web/backoffice réussis. Journal local : `/tmp/dem027-quality.log`.

Les parcours Playwright applicatifs ne font pas partie de cette commande sans option
navigateur ; ils restent conservés et exécutés par la CI lors de la livraison.
Le contrôle des messages de commits attend les commits validés ; aucun commit créé ici.

État présenté : HEAD de base inchangé ; deux suppressions suivies, demande DEM-027
et présente carte non suivies. Index vide. Aucun verdict humain sur ce résultat.

## Verdict humain — 2026-10-31

Verdict explicite « validé » après présentation d’OPS-078. Contenu revérifié
identique à la présentation : empreinte `af018dc321c0640e23a3c9fb7519bbdb54cdb2ec1c5240c0f89c0a0652c24532`.
Le commit comprend les deux suppressions, cette carte avec preuves et verdict,
et la demande de consolidation portant l’analyse et les décisions confirmées.
Aucun changement fonctionnel depuis la présentation.
