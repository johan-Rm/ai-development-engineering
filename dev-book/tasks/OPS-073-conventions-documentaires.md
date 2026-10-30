# OPS-073 — Consolider le cadre documentaire

- Demande : [DEM-021](../demand/DEM-021-conventions-documentaires.md#arbitrage-humain--2026-10-30).
- Session de création : `01a18c38-1b13-7953-9118-aadc8cde8794`.
- Couche : devops ; worktree `worktree/devops` ; branche `layers/devops`.
- Statut : validée humainement le 2026-10-30 ; commit local à créer.
- Dépendance : aucune ; base `3fe38fca51bab7a2ea972e688601240344985f5a`.

## Mission et périmètre

Appliquer la portée des noms ajustée dans la demande, extraire les index, centraliser les conventions, migrer les liens, supprimer les README infra/config et resources après transfert ; créer le contrôle documentaire et ses tests.

Chemins autorisés : `docs/`, `AGENTS.md`, `SETUP.md`, `app/README.md`, `infra/README.md`, `infra/config/README.md`, `dev-book/`, `worktree/README.md`, `codebase-integrity/`.

Exclusions : code applicatif, données, `.env`, sources graphiques et autres worktrees.
Une carte à la fois ; aucun transfert de travail non commité. Les cartes sont préparées
dans devops et ne seront disponibles ailleurs qu’après commit validé.

## Critères et preuves

Appliquer l’arbitrage de la demande sans étendre les exceptions. Informations utiles
conservées à une seule source ; liens migrés ; contrôles conformes, cas d’écart et
exceptions couverts pour le vérificateur. Préserver les preuves historiques.

Vérifications : Contrôle documentaire, tests de l’outillage, typage des demandes, `git diff --check`. Qualité complète avant PR.

## Résultat et verdict

Numérotation des 4 rubriques et 12 étapes conservée après la précision humaine
de portée consignée dans la demande ; seuls les dossiers thématiques directement
sous `docs/` sont soumis à l’interdiction. Aucun renommage requis ici.
Extraction des explications
des 3 index vers `organisation.md` ou `fonctionnement.md`, index d’architecture
réduit à la navigation. Citations ajoutées à dockerisation et reconstitution.
Conventions documentaires centralisées ; ajout dans `app/README.md` annulé à la
demande humaine. Liens et ancres
migrés, sans réécriture des chemins littéraux de preuves. Les deux liens déjà
cassés du README des worktrees sont réparés.

README infra/config, resources et scripts supprimés après transfert aux README parents ;
les sources originales restent intactes. Les trois suppressions applicatives
restent aux cartes suivantes. Les cartes sont créées ici, aucun autre worktree modifié.

`check_docs.py` est intégré à `quality.py`. Pas d’exception historique ajoutée :
les liens navigables ont été réparés. Sources contrôlées : fichiers Git suivis
et non ignorés, hors copies de worktrees et `.env` ; voir les limites dans
[les conventions](../../docs/README.md#références-et-vérifications).

Preuves exécutées le 2026-10-30 depuis le worktree devops :

- `python3 -m unittest discover -s codebase-integrity/tests -p test_docs.py` :
  27 tests réussis (noms, index, citations, liens, ancres, exceptions et erreurs).
- `python3 codebase-integrity/scripts/check.py` : 66 tests réussis après autorisation
  de socket locale ; le premier passage dans le bac à sable échouait uniquement
  sur `test_identity_served_as_json_and_wrong_identity_refused` (PermissionError).
- `python3 codebase-integrity/scripts/check_docs.py` : conforme, aucun avis dynamique.
- `python3 codebase-integrity/scripts/check_demands.py` : conforme.
- `git diff --check` et vérification des espaces des nouveaux fichiers : réussis.

Qualité applicative complète non exécutée : aucun code applicatif modifié ; elle
reste obligatoire avant PR. Lisibilité, pertinence des citations et absence de
répétitions restent à apprécier humainement. Les liens sortants des sources HTML,
les skills hors dépôt et les destinations réseau ne sont pas vérifiés ici.

Verdict humain du 2026-10-30, session intervenante de la demande :
« ok lets go c'est validé ». Validation d’OPS-073 après les corrections de portée,
les simplifications des README, la suppression supplémentaire du README des
scripts et le rétablissement d’`app/README.md`. Les cartes applicatives ne sont
pas implémentées ni validées. Commit local autorisé par ce verdict.

L’empreinte ci-dessous a été vérifiée identique avant consignation du verdict.
Le diff suivi et les nouveaux fichiers correspondent au périmètre de cette carte ;
aucun fichier étranger ni changement applicatif. Les seuls changements suivants
consignent le verdict, l’état de la demande et les références des commits.

Contenu corrigé présenté avant consignation du verdict : base ci-dessus, 34 chemins modifiés/supprimés/non suivis.
Empreinte SHA-256 des chemins triés et contenus (suppressions marquées, hors cette
carte) : `afc7001f5b98ac34261049d7987e0c720e6b378e5015495051c1296e55a4acaa`. Index Git vide.
