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

Les réponses et documents suivent la [règle de concision](../../AGENTS.md#réponses-et-documents) :
informations utiles et précises, sans répétitions. Tout développement rédactionnel
jugé nécessaire commence par une synthèse concise et attend l’accord humain explicite.
Les preuves et validations requises restent nécessaires.

Une mission indique le worktree relatif à la racine du dépôt principal, la branche, les chemins autorisés et le résultat à prouver. Le chemin absolu est résolu et vérifié localement à l’exécution, avec la branche et l’état Git ; il n’est pas inscrit dans les cartes versionnées. Les dépendances sont identifiées par commit. Le travail reste dans ce périmètre ; une ambiguïté ou un besoin supplémentaire est signalé.

Les instructions explicites de l’utilisateur priment. Dans ce dépôt, la délégation n’est autorisée que sur demande explicite. La validation d’un plan ne remplace pas les verdicts humains prévus par les boucles.

## Utiliser les skills

Les skills AIDE sont conservés dans le répertoire personnel de skills de l’outil, hors du dépôt :
six skills pour le développement et six autres pour la consolidation. Chaque boucle possède
ses propres entrées, procédures et sorties, sans dépendance aux skills de l’autre.

Les skills d’arbitrage et de vérification préparent les éléments et consignent le verdict humain.
Les deux outils hors des boucles servent à configurer les worktrees et inventorier les couches.
Les skills de vérification réalisent les commits autorisés après verdict humain ; les skills de
livraison réalisent directement push, PR, fusion et suivi après fusion lorsque demandés.
Ils ne déclenchent aucune autre étape automatiquement.

Les skills doivent être installés et vérifiés avant la livraison. Leur mention dans le dépôt
ne prouve pas leur disponibilité ; consulter les skills réellement exposés par la session.
Si un skill manque, signaler la procédure absente et suivre la carte et les instructions disponibles.

Les anciens `creer-tache` et `demarrer-tache` sont remplacés par les skills propres aux étapes.
`configurer-worktrees-aiod` devient `configurer-worktrees-aide`. `etat-des-lanes` reste hors des boucles. Les anciennes procédures distinctes de discussion,
commit, PR et après-fusion sont retirées ; les opérations Git nécessaires sont intégrées
dans les skills propres à chaque boucle.
