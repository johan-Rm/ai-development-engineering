# DEM-017 — Regrouper la documentation du cadre sous architecture

- Type : développement
- Session intervenante (typage DEM-022) : `01a18b94-1588-7021-869d-d11d9ff6ba72`.
- Date : 2026-10-29
- Session de création : `01a18804-42eb-7d20-8dbc-7430446e4350`
- État : cadrage confirmé par l’humain (« ok »), le 2026-10-29.

## Besoin

Distinguer la documentation du cadre des futures autres documentations dans `docs/`, pour les lecteurs et contributeurs du dépôt.

## Résultat et critères d’acceptation

- Les quatre dossiers `01-codebase-integrity/`, `02-cadre/`, `03-developpement-loop/` et `04-consolidation-loop/` sont déplacés de `docs/` vers `docs/architecture/`, en conservant leur organisation interne.
- Le sommaire actuel de `docs/index.md` est transféré dans `docs/architecture/index.md`. L’entrée générale `docs/index.md` renvoie à cet index sans le dupliquer.
- Les références actives du dépôt et les liens relatifs des documents déplacés sont adaptés ; la navigation mène aux destinations attendues.
- Le contenu est conservé, hors adaptations nécessaires au déplacement.

## Contraintes et exclusions

Les demandes et preuves historiques restent inchangées. Aucune nouvelle documentation thématique ni réécriture de fond n’est demandée. Respecter les conventions existantes ; ce déplacement ne modifie pas les autorisations du workflow.

## Vérifications attendues

Contrôler les chemins déplacés, les références actives et la navigation documentaire ; exécuter les contrôles proportionnés depuis la couche devops, dont `python3 codebase-integrity/scripts/quality.py` avant PR. Consigner les limites dues aux références historiques conservées.

## Questions ouvertes

Aucune question de besoin restante.

## Tâches issues du découpage

| Carte | Couche / branche | Couverture | Dépendance |
| --- | --- | --- | --- |
| [OPS-069](../tasks/OPS-069-regrouper-docs-architecture.md) | devops / `layers/devops` | Tous les critères ; déplacement et références dans une contribution cohérente | Aucune |

Découpage du 2026-10-29, même session que la création. Carte prête ; branche de
couche existante conservée, base locale `ec6efd5`, sans fetch ni commit.

## Reconstitution prévue

Après validation humaine d’OPS-069 et création de son commit à l’étape 04,
créer `demands/DEM-017` depuis develop local vérifié dans le dépôt principal
(worktree relatif `.`), libre et propre. Y réunir le commit validé et matérialiser
`dev-book/demand/DEM-017-regrouper-docs-architecture.md` depuis ce brouillon.
Conserver la couche sur `layers/devops` ; retour du principal sur develop après
fusion distante vérifiée. Aucune branche de demande créée au découpage.

## Suivi de l’implémentation — 2026-10-29

OPS-069 implémentée, non commitée, à vérifier ; tous les critères couverts, aucune
carte bloquée. Résultats et limites des contrôles dans la carte liée ci-dessus.
Le principal reste sur develop sans changement suivi ; aucune reconstitution engagée.

## Suivi de la vérification — 2026-10-29

OPS-069 : écart sur deux références actives, détaillé dans la carte. Correction puis
nouvelle présentation nécessaires ; aucun verdict humain ni commit créé.

## Verdict humain — 2026-10-29

OPS-069 validée et commitée avec la réserve des deux liens actifs non corrigés,
après réponse « validé » réitérée à la clarification. Commit : `c305cf2dffe8c562a04e112468dcdc87b701d859`.
Demande à reconstituer puis livrer ; aucun push ni PR effectué.

## Reconstitution — 2026-10-29

Branche `demands/DEM-017` créée dans le principal depuis develop local
`ec6efd554d16459536233c43f824617df4db2dea`, initialement libre et propre.
Cherry-picks avec provenance, sans conflit :

| Source validée | Commit obtenu |
| --- | --- |
| `c305cf2dffe8c562a04e112468dcdc87b701d859` | `6e30b6386189b378977e727a1135e2fe012427f2` |
| `b3ed1cf13ceffb0af90e3f23066fcfce885823b0` | `4596b783b114f1099bbf44070349b3aaf9b3f14b` |

Arbre reconstitué identique à `layers/devops` avant matérialisation documentaire
(`git diff layers/devops HEAD --exit-code`). Réserve des deux liens conservée ;
aucun correctif ajouté. Les worktrees de couche restent sur leurs branches.
Retour prévu du principal sur develop après fusion distante vérifiée.
Document définitif et traces de reconstitution non commités à cette étape.

Contrôles de reconstitution : `git diff --check` réussi ;
`python3 codebase-integrity/scripts/check.py` : 23 tests réussis avec serveur HTTP
local autorisé. Inspection statique : 98 liens locaux et ancres conformes dans les
documents et entrées vérifiés, hors les deux liens de la réserve connue.
`quality.py` reste requis avant PR. Seul ce document définitif est non suivi ; index vide.

## Livraison — 2026-10-29

`python3 codebase-integrity/scripts/quality.py` : réussite (23 tests de l’outillage,
contrat API, conteneur Symfony, mapping, OpenAPI, types et builds web/backoffice).
Contrôle exécuté sur `4596b78` ; le rattachement `de7360df508ad4e6961e1c465cb13ddcdc0cb4c6`
de `layers/devops` ne change aucun contenu (`git diff HEAD^ HEAD --exit-code`).
Les changements suivants sont uniquement les traces documentaires de livraison.

Les cinq couches sont propres, sans mission concurrente identifiée ; leurs commits
sont ancêtres de la branche de livraison. Distant vérifié, develop sur `ec6efd5`.
PR et commit de fusion requis par la procédure ; protection distante sans contournement.
La réserve acceptée dans OPS-069 reste applicable.

PR : [#16](https://github.com/johan-Rm/ai-development-engineering/pull/16),
`demands/DEM-017` → `develop`. Contrôles GitHub à attendre avant fusion.
