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

Les [sources des skills AIDE](../../skills/README.md) sont versionnées dans le dépôt :
six skills pour le développement et six autres pour la consolidation. Chaque boucle possède
ses propres entrées, procédures et sorties, sans dépendance aux skills de l’autre.

Les skills d’arbitrage et de vérification préparent les éléments et consignent le verdict humain.
Les outils transversaux servent à discuter, configurer les worktrees, inventorier les couches,
committer les tâches validées, ouvrir les PRs demandées et suivre les fusions.
Ils ne déclenchent aucune autre étape automatiquement.

L’installation personnelle reste distincte de la présence des sources. Le catalogue décrit
les remplacements des anciens noms et la [préparation de l’installation](../../SETUP.md#skills-aide).
Si un skill n’est pas exposé dans la session, lire la source versionnée et les instructions
disponibles ; signaler la procédure manquante sans inventer son contenu.
