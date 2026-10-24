# IA Engineering

> L’IA Engineering donne aux agents le contexte, les instructions et les procédures nécessaires pour intervenir dans le périmètre autorisé.

## Répartir les instructions

| Support | Rôle |
| --- | --- |
| [AGENTS.md](../../AGENTS.md) | Instructions propres au projet, limites d’autorisation et repères documentaires. |
| [.codex/config.toml](../../.codex/config.toml) | Configuration Codex propre au projet. Le socle actuel ne fixe ni modèle ni permissions. |
| Skills disponibles dans la session | Procédures réutilisables pour les étapes des boucles. |
| Carte de tâche | Objectif, périmètre, dépendances, affectation et preuves attendues. |

AGENTS.md indique les skills à privilégier sans recopier leurs procédures. Une mention n’installe pas un skill et ne déclenche pas une étape automatiquement.

## Donner une mission précise

Une mission indique le worktree absolu, la branche, les chemins autorisés et le résultat à prouver. Les dépendances sont identifiées par commit. Le travail reste dans ce périmètre ; une ambiguïté ou un besoin supplémentaire est signalé.

Les instructions explicites de l’utilisateur priment. Dans ce dépôt, la délégation n’est autorisée que sur demande explicite. La validation d’un plan ne remplace pas les verdicts humains prévus par les boucles.

## Utiliser les skills

`creer-tache` cadre ; `demarrer-tache` implémente ; `commit-tache` clôture et committe ; `creer-pr` prépare la PR ; `apres-pr-mergee` intervient après fusion. `evoquer-un-sujet` sert à discuter avant d’ouvrir une tâche et `etat-des-lanes` à lire l’état des branches.

Les skills personnels restent hors du dépôt. Si un skill manque, suivre la carte et les instructions disponibles ; signaler la procédure manquante sans inventer son contenu.
