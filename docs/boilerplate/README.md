# Historique et exemples du boilerplate

`tasks/` conserve les cartes de construction antérieures à l’adoption : BP-001 à BP-010,
API-001, WEB-001 et BO-001. Ce sont des archives, jamais des tâches à reprendre automatiquement.
Les chemins personnels historiques sont remplacés par des placeholders ; les originaux restent dans Git.
Les anciennes preuves datées ne valent pas exécution actuelle des contrôles.

## Exemples remplaçables

- L’entité Article, sa migration et les parcours associés dans les trois applications sont une démonstration CRUD.
- Les tests HTTP, le contrat OpenAPI et les parcours Playwright correspondent à cette démonstration : les adapter ensemble lorsqu’elle est remplacée.
- `design/Brand Guidelines - Graines Digitales (standalone).html`, le schéma `docs/aiod/cadre-aiod.html`, sa synthèse graphique et `docs/aiod/sources/` sont les références du boilerplate. Les remplacer ou retirer si le nouveau projet ne les utilise pas, puis adapter les liens et la consigne graphique dans `AGENTS.md`.
- `infra/compose.process.yaml` et le runbook associé sont une recette du processus, indépendante de l’application.

La procédure d’adoption indique comment démarrer avec un journal de projet propre.
