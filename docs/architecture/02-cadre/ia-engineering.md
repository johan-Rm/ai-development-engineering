# IA Engineering

> L’IA Engineering donne aux agents le contexte, les instructions et les procédures nécessaires pour intervenir dans le périmètre autorisé.

## Répartir les instructions

| Support | Rôle |
| --- | --- |
| [AGENTS.md](../../../AGENTS.md) | Instructions propres au projet, limites d’autorisation et repères documentaires. |
| [.codex/config.toml](../../../.codex/config.toml) | Configuration Codex propre au projet. Le socle actuel ne fixe ni modèle ni permissions. |
| Skills disponibles dans la session | Procédures réutilisables pour les étapes des boucles. |
| Carte de tâche | Objectif, périmètre, dépendances, affectation et preuves attendues. |

Les étapes des deux boucles indiquent leur skill associé ; une mention n’installe
pas un skill et ne déclenche aucune étape automatiquement.

## Donner une mission précise

Une mission indique le worktree relatif à la racine du dépôt principal, la branche,
les chemins autorisés, les dépendances par commits et le résultat à prouver.
Résoudre le chemin absolu localement sans l’inscrire dans les cartes versionnées.
Respecter les [consignes d’intervention](../../../AGENTS.md#avant-dintervenir) et la
[règle de rédaction](../../../AGENTS.md#réponses-et-documents). Une ambiguïté ou un besoin
supplémentaire est signalé ; valider un plan ne remplace pas les verdicts des boucles.

## Utiliser les skills

Les skills du cadre sont conservés dans le répertoire personnel de skills de l’outil, hors du dépôt :
six skills pour le développement et six autres pour la consolidation. Chaque boucle possède
ses propres entrées, procédures et sorties, sans dépendance aux skills de l’autre.

Les skills d’arbitrage et de vérification préparent les éléments et consignent le verdict humain.
Les [autorisations du projet](../../../AGENTS.md#workflow-et-autorisations) encadrent
les opérations Git ; les skills ne déclenchent pas automatiquement l’étape suivante.

Avant livraison, les skills nécessaires doivent être disponibles et vérifiés dans
la session. Aux autres étapes, signaler un skill manquant et suivre la carte et
les instructions disponibles, sans inventer sa procédure.

Les outils hors des boucles sont `etat-des-lanes` et `configurer-worktrees-aide`.

Les anciens `creer-tache` et `demarrer-tache` sont remplacés par les skills propres aux étapes.
`configurer-worktrees-aiod` devient `configurer-worktrees-aide`. `etat-des-lanes` reste hors des boucles. Les anciennes procédures distinctes de discussion,
commit, PR et après-fusion sont retirées ; les opérations Git nécessaires sont intégrées
dans les skills propres à chaque boucle.
