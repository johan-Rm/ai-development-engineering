# AIDE — AI Development Engineering

Cadre de développement agnostique organisé par couches et worktrees, avec des preuves vérifiables.
Les applications de démonstration sont regroupées dans `app/` : API Platform / Symfony, webapp et dashboard Nuxt.

## Démarrer

Prérequis et détails : [installation et lancement](docs/demarrage.md).
Depuis la racine du dépôt :

```sh
python3 codebase-quality-control/scripts/apps.py install all
```

Dans trois terminaux : `python3 codebase-quality-control/scripts/apps.py serve api`, `python3 codebase-quality-control/scripts/apps.py serve web`
et `python3 codebase-quality-control/scripts/apps.py serve backoffice`.

API : http://127.0.0.1:8000/api/docs · Web : http://127.0.0.1:3000 · Dashboard : http://127.0.0.1:3001.

```sh
python3 codebase-quality-control/scripts/quality.py
```

[Adopter le boilerplate](docs/adoption.md) · [Contrôles et CI](docs/qualite.md).
Les applications tournent sur l’hôte ; Docker fournit séparément des conteneurs témoins pour la recette AIOD.

## Se repérer

| Thème | Chemins et responsabilités |
| --- | --- |
| Couches | `app/api/`, `app/web/`, `app/backoffice/`, `design/`, `infra/`, `worktree/` ; routage dans `codebase-quality-control/scripts/aiod.json` |
| Codebase Quality Control | `codebase-quality-control/`, tests applicatifs et CI : rendre les exigences vérifiables |
| IA Engineering | `AGENTS.md`, `CLAUDE.md`, `ia-engineering/`, `.claude/` : consignes des agents |
| Documentation | `docs/`, `dev-book/`, `**/README.md` : produit, responsabilités, tâches et preuves |

Chaque README définit les responsabilités de son dossier. Aucun skill personnel n’est requis.
Les cartes de construction et de maintenance sont conservées dans [le dev-book](dev-book/README.md).
Toutes les cartes restent dans `dev-book/tasks/`, distinguées par leur statut.

[Principes AIOD](docs/principes.md) · [Couches](docs/couches.md) · [Consignes](ia-engineering/README.md)
· [Recette Git isolée](docs/premiere-tache.md).
