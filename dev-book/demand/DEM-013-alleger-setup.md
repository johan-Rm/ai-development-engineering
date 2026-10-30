# DEM-013 — Alléger SETUP

- Type : développement
- Session intervenante (typage DEM-022) : `01a18b94-1588-7021-869d-d11d9ff6ba72`.
- Date : 2026-10-28.
- État : reconstituée sur `demands/DEM-013` ; à livrer.
- Session de création : `01a182d3-1898-7e92-8fdc-c16b502fecbf`.
- Couche concernée : devops.

## Besoin et utilisateurs

Permettre aux développeurs de préparer leur environnement pour ce dépôt avec un parcours
court dans [SETUP](../../SETUP.md), sans relire les informations déjà documentées.

## Décisions et critères d’acceptation

Cadrage révisé et structure approuvée dans le chat après refus de la première
proposition : SETUP explique comment travailler dans ce dépôt.

1. Prérequis : outils et préparation des skills AIDE.
2. Créer les worktrees.
3. Ouvrir le workspace.
4. Démarrer les applications avec Docker.
5. Réaliser une demande : lien vers le workflow et ses vérifications.

Titre : « Préparer son environnement de développement AIDE ». Appliquer la
[règle de concision et de référence unique](../../AGENTS.md#réponses-et-documents).
Vérifier l’existant et privilégier les liens ; maintenir les liens entrants.
Ajouter le nom complet d’AIDE et une courte description du blueprint sous le H1.
Présenter les prérequis en paragraphes sans puces ni retrait.

## Périmètre et exclusions

SETUP et ajustements des références entrantes. Retirer les instructions de
lancement sur l’hôte et d’adoption dans un autre projet. Aucun changement de code,
de skills ni de comportement des outils.

## Vérification attendue

Comparer avant/après pour vérifier la conservation des informations utiles et
l’absence de répétitions évitables ; vérifier les cibles et ancres des liens.
Exécuter les contrôles documentaires applicables selon les
[points de contrôle](../../docs/architecture/01-codebase-integrity/points-de-controle.md#exécuter-dans-ce-dépôt).
Résultat final explicitement validé par l’humain (« validé »).

## Questions ouvertes

Aucune au cadrage.

## Tâches issues du découpage

| Carte | Couche / branche | Dépendances | État |
| --- | --- | --- | --- |
| [OPS-066](../tasks/OPS-066-alleger-setup.md) | devops / `layers/devops` | Aucune | Validée et commitée |

Une seule carte couvre la demande. Le principal (`.`) porte `demands/DEM-013` ;
retour prévu sur develop après fusion distante. Les couches restent sur layers/*.

## Reconstitution

Base develop locale : `92c64ba4893cbda4818e349c54bb997e296730fc`.
Principal libre, arbre et index propres avant création de branche ; aucun fetch.
Cherry-picks avec provenance, sans conflit :

| Source validée | Commit obtenu |
| --- | --- |
| `1d2c5bb9031e5237260d3ae4a2fb42d5a6b7f3ee` | `fca26dc1f1014411bcd4e3097cae729d51e39904` |
| `48438eca18e95e2418c1610aa1e27332dfb50d95` | `3ab62a92f54f7c1d078f1308abc9d72842612ca3` |

Verdict humain : « validé », sur OPS-066 et ses preuves. Demande matérialisée
après cherry-picks ; brouillon local conservé. Traces documentaires de cette
reconstitution non commitées, prévues pour la livraison.

Contrôles de reconstitution : `git diff --check` réussi ; 14 liens et ancres
locaux valides ; contenu livré par les cherry-picks identique à layers/devops
pour SETUP et ses références. Tests de l’outillage : 23 réussis. Qualité
complète restant à exécuter avant PR.

## Préparation de livraison

Le 2026-10-29, les cinq worktrees de couche sont propres et sans nouvelle mission
identifiée dans cette session. Les quatre couches hors devops pointent sur la
base develop ; devops ne porte que les deux commits validés d’OPS-066.
Historique devops rattaché par merge ciblé `2ce8280` après vérification de l’égalité
des arbres avec les cherry-picks ; aucun changement de contenu. Cette ascendance
permet les avances rapides finales. Fusion GitHub par merge commit autorisée.

Qualité complète locale réussie le 2026-10-29 : `python3 codebase-integrity/scripts/quality.py`, journal `/tmp/dem013-quality.log`. Contenu applicatif identique après rattachement ; seules les traces documentaires de livraison sont ajoutées ensuite.

PR : https://github.com/johan-Rm/ai-development-engineering/pull/13
Source `demands/DEM-013`, cible `develop` ; merge commit après réussite des checks distants. Suivi réel après fusion dans le brouillon conservé sous tmp/.
