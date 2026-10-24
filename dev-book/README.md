# Dev-book

Le journal opérationnel du projet qui adopte AIDE. La méthode est dans [docs/index.md](../docs/index.md), organisée par thèmes ;
les ressources HTML, PDF et images sont dans `resources/`.

| Dossier | Contenu |
| --- | --- |
| `demand/` | Besoins, contexte et décisions de cadrage |
| `tasks/` | Une carte par tâche, ses critères et sa preuve |
| `runbooks/` | Procédures reproductibles avec préconditions et vérifications |
| `resources/` | Ressources techniques utilisées pour réaliser ou vérifier |

## Rubriques d’une demande

Contexte, problème observé, résultat attendu, contraintes, questions ouvertes et décisions humaines.

## Rubriques d’une carte

Identifiant et titre ; état (à cadrer, prête, en cours, bloquée, clôturée) ; date ; demande d’origine ;
couche ; périmètre et exclusions ; critères d’acceptation ; dépendances par commit ; affectation
(session, branche, chemin absolu) ; réalisation ; preuves et commandes ; documentation mise à jour.

Une carte clôturée voyage dans le commit de sa tâche. Les identifiants sont attribués après
vérification des branches concernées. Une carte découverte ne constitue pas une autorisation de travail.

## Rubriques d’une procédure

Objectif, préconditions, étapes, vérifications, arrêt en cas d’erreur et retour arrière si applicable.
Les dossiers sans contenu sont créés lors de leur premier usage ; Git ne conserve pas les dossiers vides.

Toutes les cartes, de construction ou de maintenance, ouvertes ou clôturées, sont conservées
dans `tasks/`, sans sous-dossier d’archives. Leur statut indique le travail restant.
Les cartes clôturées sont des traces historiques, jamais des tâches à reprendre automatiquement.
Les preuves datées et les mentions d’état Git décrivent le moment de leur rédaction ; elles ne
constituent pas une vérification de l’état actuel. Les chemins personnels historiques sont
remplacés par des placeholders ; les originaux restent consultables dans Git.

La maintenance du cadre appartient à devops (cartes `OPS`). Les anciennes cartes BP utilisent désormais des identifiants OPS. Leurs affectations et
preuves restent historiques ; les commits antérieurs conservent leurs anciens identifiants.

## Correspondance des cartes migrées — OPS-012

Les références des cartes ont été actualisées ; les SHA, statuts et missions historiques restent inchangés.

| Ancien identifiant | Carte actuelle |
| --- | --- |
| BP-001 | [OPS-013](tasks/OPS-013-blueprint-adoptable.md) |
| BP-002 | [OPS-014](tasks/OPS-014-initialiser-master.md) |
| BP-003 | [OPS-015](tasks/OPS-015-initialiser-develop.md) |
| BP-004 | [OPS-016](tasks/OPS-016-initialiser-worktree-backoffice.md) |
| BP-005 | [OPS-017](tasks/OPS-017-initialiser-worktree-api.md) |
| BP-006 | [OPS-018](tasks/OPS-018-initialiser-worktree-web.md) |
| BP-007 | [OPS-019](tasks/OPS-019-initialiser-worktree-devops.md) |
| BP-008 | [OPS-020](tasks/OPS-020-initialiser-worktree-design.md) |
| BP-009 | [OPS-021](tasks/OPS-021-dockeriser-les-environnements.md) |
| BP-010 | [OPS-022](tasks/OPS-022-schematiser-le-cadre-aiod.md) |
| BP-011 | [OPS-023](tasks/OPS-023-preparer-adoption.md) |
| BP-012 | [OPS-024](tasks/OPS-024-actualiser-cadre-schema.md) |
| BP-013 | [OPS-025](tasks/OPS-025-vue-ensemble-html.md) |
| BP-014 | [OPS-026](tasks/OPS-026-ajuster-vue-aide.md) |
| BP-015 | [OPS-027](tasks/OPS-027-entrees-sorties-codage.md) |
| BP-016 | [OPS-028](tasks/OPS-028-corriger-cycle-codage.md) |
| BP-017 | [OPS-029](tasks/OPS-029-relier-consolidation.md) |
| BP-018 | [OPS-030](tasks/OPS-030-clarifier-controles-partages.md) |
| BP-019 | [OPS-031](tasks/OPS-031-textes-process-developpement.md) |
| BP-020 | [OPS-032](tasks/OPS-032-definir-themes-cadre.md) |
| BP-021 | [OPS-033](tasks/OPS-033-etapes-consolidation.md) |
