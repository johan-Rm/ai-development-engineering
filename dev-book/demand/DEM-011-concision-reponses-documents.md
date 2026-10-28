# DEM-011 — Imposer la concision des réponses et documents

- Date : 2026-10-27.
- État : OPS-063 et OPS-064 validées et commitées localement ; reconstituées sur `demands/DEM-011`, à livrer.
- Session de création : `01a17e56-dc43-76f2-83fb-d8006838ac17`.
- Couche concernée : devops.

## Besoin et périmètre

Réduire le bruit dans les réponses de l’IA et les documents qu’elle écrit pour
l’utilisateur : imposer la concision et la précision dans `AGENTS.md`, les autres
consignes pertinentes du dépôt et les skills personnels concernés.

## Décisions confirmées

- Réponses et documents strictement concis, précis, sans répétitions ni détails superflus.
- Si un développement paraît nécessaire, donner d’abord une synthèse concise,
  puis demander l’accord et attendre une validation humaine explicite avant de développer.
- Inclure les skills personnels utilisés dans ce projet.
- Vérifier par relecture la cohérence des consignes et le respect de la règle.

L’humain a confirmé ce cadrage par « oui » dans le chat. Cette confirmation
porte sur le besoin, sans valider une implémentation.

## Critères d’acceptation et preuves

1. Les consignes concernées expriment la règle sans contradiction entre dépôt et skills.
2. Une réponse ou un document courant se limite aux informations utiles, sans répétitions.
3. Lorsqu’un développement est proposé, seule la synthèse est fournie avant l’accord
   explicite ; le silence ne vaut pas accord.
4. La vérification humaine s’appuie sur le diff des consignes et des exemples de
   réponse concise et de demande d’accord avant développement.

## Contraintes et exclusions

Préserver la précision et les informations nécessaires à la compréhension.
Le périmètre vise les consignes de communication et de rédaction ; il n’inclut
aucune modification fonctionnelle des applications. Les skills restent hors du dépôt.
L’interview crée uniquement cette demande, sans carte, implémentation ni opération Git.

## Questions ouvertes

Aucune question de besoin restante. Écriture des skills hors dépôt autorisée et
réalisée ; deux cartes validées par l’humain.

## Tâches issues du découpage

| Carte | Périmètre | Couverture |
| --- | --- | --- |
| [OPS-063](../tasks/OPS-063-concision-consignes-depot.md) | AGENTS.md et guide IA Engineering | Critères 1 à 4 côté dépôt |
| [OPS-064](../tasks/OPS-064-concision-skills-personnels.md) | 18 skills personnels, hors dépôt | Critères 1 à 4 côté skills |

Cartes indépendantes, exécution séquentielle sur `worktree/devops`, branche
`layers/devops`. Seul changement initial : la présente demande non suivie,
identifiée comme appartenant à cette même mission ; index vide.
Maximum OPS observé dans toutes les références Git locales et les cinq worktrees : 062.

À la reconstitution, créer `demands/DEM-011` depuis develop local vérifié dans
un worktree existant libre et propre, selon AGENTS.md, puis appliquer les commits
validés avec `git cherry-pick -x` (OPS-063 puis OPS-064). SHA sources et obtenus
à renseigner après validation ; reconstitution non prête avant ces commits.
Conserver ce document existant, sans brouillon ou copie supplémentaire.
Les skills personnels restent hors du contenu Git livré.

## Validation et commits locaux

Le 2026-10-27, verdict humain global dans le chat : « validé ».

| Carte | Commit source validé | Commit obtenu à la reconstitution |
| --- | --- | --- |
| OPS-063 | `ec1e373471dd3de353badc1a87938f787b318f1b` | `ad9761696ef20283492c88c00f728ca0ec475c10` |
| OPS-064 | `30aa12d2387bc9647af470e639c1419df583f5d9` | `ab5cfe09ac40579cc40b5facb3ba4bba5a208a7d` |

Les skills personnels sont validés dans leur état local ; seul leur suivi est commité.
Aucun push, PR, reconstitution ou livraison réalisé à cette étape.

## Reconstitution

Le 2026-10-27, branche `demands/DEM-011` créée dans le principal (worktree `.`),
depuis develop local `884b0f53a005080bca2c1241122b4f2972e6cedb`, libre et propre.
Retour prévu sur `develop` après livraison ; les couches conservent leurs branches.
Les trois commits ont été appliqués avec `git cherry-pick -x`, sans conflit.
Trace documentaire : `a18dad305e2f2ae0b404c8af13fad535d6233b63` →
`02fb039b0fa86300bf2e4dd78d04dd5a4cbfb5f2`.

`git diff --exit-code layers/devops HEAD` confirme un résultat identique à la
contribution validée. Contrôles qualité précédents conservés pour ce contenu ;
liens locaux et `git diff --check` vérifiés à la reconstitution. Les 18 skills
personnels correspondent toujours à leur état validé, hors du contenu Git.
Seule cette trace de reconstitution reste non commitée pour la livraison.
Aucun fetch, push ou PR réalisé.

## Préparation de livraison

Le 2026-10-28 : contrôle `python3 codebase-integrity/scripts/quality.py` terminé
avec code 0 (journal local `/tmp/dem011-livraison-quality.log`).
Historique source devops rattaché par merge ciblé `5cd9a67`, après vérification
des arbres identiques ; aucun changement du contenu validé.
Dévelop distant vérifié à `884b0f53a005080bca2c1241122b4f2972e6cedb`.
Les cinq couches sont propres ; devops porte uniquement les contributions validées
de DEM-011, les autres sont au repos sur la base. Aucun travail étranger identifié.

PR : [#11](https://github.com/johan-Rm/ai-development-engineering/pull/11),
`demands/DEM-011` → `develop`. Publication sans force réalisée via les identifiants gh ;
création via gh après refus 403 du connecteur. Fusion et alignement à vérifier.
