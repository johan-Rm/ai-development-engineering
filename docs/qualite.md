# Contrôles fournis

Le [Codebase Quality Control](aiod/codebase-quality-control.md) définit l’organisation des
conventions et points de contrôle dans chaque projet. Cette page décrit les commandes réellement fournies.

Depuis la racine du dépôt ou du worktree à vérifier :

| Commande | Portée |
| --- | --- |
| `python3 codebase-quality-control/scripts/check.py` | Tests unitaires de l’outillage Git, de l’isolation et des commandes applicatives |
| `python3 codebase-quality-control/scripts/apps.py check api` | Contrat HTTP CRUD avec SQLite jetable, conteneur Symfony, mapping Doctrine et comparaison OpenAPI |
| `python3 codebase-quality-control/scripts/apps.py check web` | Types puis build Nuxt |
| `python3 codebase-quality-control/scripts/apps.py check backoffice` | Types puis build Nuxt |
| `python3 codebase-quality-control/scripts/quality.py` | Tous les contrôles ci-dessus, arrêt au premier échec |
| `python3 codebase-quality-control/scripts/apps.py check web --browser` | Types, build et parcours Playwright ; API et Chromium requis |
| `python3 codebase-quality-control/scripts/apps.py check backoffice --browser` | Types, build et parcours Playwright ; API et Chromium requis |

Installer les dépendances avant les contrôles applicatifs. `--root` sélectionne explicitement un autre worktree ; par défaut les scripts utilisent leur propre dépôt, sans dépendre du dossier courant. Les builds écrivent les artefacts Nuxt ignorés par Git. La vérification OpenAPI exporte dans un dossier temporaire et ne modifie pas le contrat versionné. Après une évolution voulue du contrat, régénérer celui-ci depuis `app/api/app/` : `php bin/console api:openapi:export --output=openapi.json`.

La CI `.github/workflows/quality.yml` installe les dépendances, exécute les contrôles et les parcours navigateur sur les pull requests et les pushes vers `develop` et `master`. Elle utilise une base et des processus propres au runner. Aucun déploiement n’est configuré.

PHPUnit, Vitest, Deptrac, PHPStan, lint/formatage et types front générés ne sont pas configurés dans ce socle. Leur ajout dépendra des besoins du projet adopté. Les conventions sont d’abord documentées ; seuls les contrôles réellement exécutables sont annoncés comme automatisés.

La recette Docker reste facultative : `python3 codebase-quality-control/scripts/check_docker.py`. Elle demande Docker, Compose et les worktrees de couche ; voir le runbook du processus. Chaque compte rendu précise les commandes exécutées et celles restées non vérifiées.
