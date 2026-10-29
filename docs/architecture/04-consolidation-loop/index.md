# Boucle de consolidation

> Corriger les écarts à l’échelle du projet et enrichir les conventions techniques et leurs contrôles.

La boucle part d’un constat et examine toute la base concernée. L’humain arbitre les évolutions du cadre et valide leur application.

| Étape | Acteur principal |
| --- | --- |
| [01 — Interview](01-interview.md) | IA, avec décisions humaines requises |
| [02 — Analyse globale](02-analyse-globale.md) | IA, avec décisions humaines requises |
| [03 — Arbitrage](03-arbitrage.md) | Humain |
| [04 — Implémentation](04-implementation.md) | IA, avec décisions humaines requises |
| [05 — Vérification](05-verification.md) | Humain |
| [06 — Livraison](06-livraison.md) | IA, avec décisions humaines requises |

Une correction revient à l’implémentation puis à la vérification humaine. Chaque tâche validée produit un commit ; la livraison présente les contrôles exécutés et leurs limites.

Les six skills indiqués dans les pages des étapes sont propres à cette boucle.
Elle peut être parcourue sans invoquer un skill de l’autre boucle. Les outils Git transversaux
ne déclenchent aucune autre étape ; les verdicts restent humains.
