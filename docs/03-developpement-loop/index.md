# Boucle de développement

> Transformer les demandes humaines en contributions vérifiées et livrables.

La boucle applique le cadre existant. **Elle ne modifie aucun élément de `codebase-integrity/`.** Un besoin de changement du cadre devient une demande de consolidation.

| Étape | Acteur principal |
| --- | --- |
| [01 — Interview](01-interview.md) | IA, avec décisions humaines requises |
| [02 — Découpage](02-decoupage.md) | IA, avec décisions humaines requises |
| [03 — Implémentation](03-implementation.md) | IA, avec décisions humaines requises |
| [04 — Vérification](04-verification.md) | Humain |
| [05 — Reconstitution](05-reconstitution.md) | IA, avec décisions humaines requises |
| [06 — Livraison](06-livraison.md) | IA, avec décisions humaines requises |

Une correction revient à l’implémentation puis à la vérification humaine. Chaque tâche reste non commitée à l’implémentation ; après validation humaine, la vérification crée son commit avec ses preuves et son verdict ; la livraison présente les contrôles exécutés et leurs limites.

Le [workspace de développement](../02-cadre/couches/index.md#suivre-les-couches-dans-le-workspace)
regroupe le dépôt principal et les worktrees des couches pour naviguer entre les
missions et consulter leurs changements. Sa [préparation](../../SETUP.md#3-ouvrir-le-workspace)
fait partie de l’installation ; chaque intervention reste attachée au worktree et
à la branche prévus par sa mission.

Les six skills indiqués dans les pages des étapes sont propres à cette boucle.
Elle peut être parcourue sans invoquer un skill de l’autre boucle. Les outils Git transversaux
ne déclenchent aucune autre étape ; les verdicts restent humains.
