# AI-Orchestrated Development

Boilerplate API Platform / Symfony et deux applications Nuxt : une webapp et un dashboard.
Le cadre AIOD organise le travail des agents par couches et worktrees, avec des preuves vérifiables.

## Démarrer

Prérequis et détails : [installation et lancement](docs/demarrage.md).
Depuis la racine du dépôt :

```sh
python3 scripts/apps.py install all
```

Dans trois terminaux : `python3 scripts/apps.py serve api`, `python3 scripts/apps.py serve web`
et `python3 scripts/apps.py serve backoffice`.

API : http://127.0.0.1:8000/api/docs · Web : http://127.0.0.1:3000 · Dashboard : http://127.0.0.1:3001.

```sh
python3 scripts/quality.py
```

[Adopter le boilerplate](docs/aiod/adoption.md) · [Contrôles et CI](docs/qualite.md).
Les applications tournent sur l’hôte ; Docker fournit séparément des conteneurs témoins pour la recette AIOD.

## Se repérer

| Thème | Chemins et responsabilités |
| --- | --- |
| Couches | `api/`, `web/`, `backoffice/`, `design/`, `infra/`, `worktree/` ; routage dans `scripts/aiod.json` |
| Consolidation | `scripts/`, `tests/`, tests applicatifs et CI : rendre les exigences vérifiables |
| IA Engineering | `AGENTS.md`, `CLAUDE.md`, `ia-engineering/`, `.claude/` : consignes des agents |
| Documentation | `docs/`, `dev-book/`, `**/README.md` : produit, responsabilités, tâches et preuves |

Chaque README définit les responsabilités de son dossier. Aucun skill personnel n’est requis.
Les tâches de construction du boilerplate sont archivées dans [docs/boilerplate/](docs/boilerplate/README.md).
`dev-book/` accueille le travail du projet adopté.

[Principes AIOD](docs/aiod/principes.md) · [Couches](docs/aiod/couches.md) · [Consignes](ia-engineering/README.md)
· [Recette Git isolée](docs/aiod/premiere-tache.md).
