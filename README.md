# AI-Orchestrated Development

Un blueprint pour organiser le travail avec des assistants IA : définir les responsabilités,
isoler les dossiers de travail, cadrer les tâches et vérifier ce qui est livré.

## Commencer

1. Lire [les principes](docs/aiod/principes.md).
2. Suivre [le guide d’adoption](docs/aiod/adoption.md) pour un projet nouveau ou existant.
3. Essayer [une première tâche](docs/aiod/premiere-tache.md) dans un dépôt temporaire.

Python 3 et Git suffisent pour l’outillage Git. Docker et Compose permettent de tester
l’isolation du processus avec des conteneurs témoins, sans stack applicative.

```sh
python3 scripts/worktrees.py list
python3 scripts/check.py
```

Le blueprint propose cinq couches : **backoffice**, **api**, **web** (plusieurs webapps/sites)
**devops** (domaines et infrastructure) et **design** (maquettes et direction artistique). Elles restent indépendantes de la stack.
La couche `blueprint` sert uniquement à entretenir ce dépôt.

## Se repérer

| Chemin | Usage |
| --- | --- |
| `docs/aiod/` | Principes, adoption et gouvernance AIOD |
| `dev-book/` | Besoins, cartes, preuves et procédures du projet |
| `AGENTS.md`, `CLAUDE.md` | Entrées des assistants vers une référence commune |
| `scripts/` | Outillage local Git et vérifications |
| `tests/` | Tests dans des dépôts jetables, sans accès au remote |
| `design/` | Maquettes et recherches non livrées |
| `worktree/` | Dossiers Git créés uniquement pour une tâche affectée |

Les [documents originaux](docs/aiod/sources/README.md) expliquent la démarche.
Les adaptations opérationnelles sont indiquées dans les principes.

Ce dépôt n’installe aucun skill personnel et ne lance aucun agent automatiquement.

La [recette AIOD](dev-book/runbooks/recette-aiod.md) décrit les cinq environnements témoins
et la vérification de leurs écritures isolées.
