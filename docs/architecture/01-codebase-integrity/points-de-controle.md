# Points de contrôle

> Un point de contrôle vérifie l’application d’une convention technique et produit un résultat exploitable sans jugement d’IA.

## Décrire ce qui est vérifié

Chaque point de contrôle identifie la convention technique source, le périmètre examiné, la commande d’exécution et le résultat attendu. Les préconditions doivent être explicites : dépendances, services et données nécessaires.

| Niveau | Effet |
| --- | --- |
| **Bloquant** | L’écart est établi sans ambiguïté et empêche la validation. |
| **Informatif** | Le résultat demande une interprétation humaine. |

Les tests du Codebase Integrity doivent réussir pour valider une PR de développement. Un test non exécuté ou au résultat inconnu ne satisfait pas cette exigence.

## Vérifier les vérificateurs

Un vérificateur spécifique au projet possède des tests couvrant les cas conformes, les écarts et les exceptions autorisées. Une erreur d’exécution ne doit pas être présentée comme une conformité.

La boucle de développement exécute ces contrôles sans modifier leur dossier. Les adaptations passent par la consolidation, après arbitrage humain.

## Exécuter dans ce dépôt

Depuis la racine du worktree : `python3 codebase-integrity/scripts/quality.py`.
Les tests de l’outillage se lancent séparément avec
`python3 codebase-integrity/scripts/check.py`.

Les [contrôles documentaires](../../README.md#références-et-vérifications)
sont inclus dans cette commande ; leur vérificateur se lance aussi séparément.
