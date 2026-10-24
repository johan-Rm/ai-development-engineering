# Points de contrôle

> Un point de contrôle vérifie l’application d’une convention technique et produit un résultat exploitable sans jugement d’IA.

## Décrire ce qui est vérifié

Chaque point de contrôle identifie la convention technique source, le périmètre examiné, la commande d’exécution et le résultat attendu. Les préconditions doivent être explicites : dépendances, services et données nécessaires.

| Niveau | Effet |
| --- | --- |
| **Bloquant** | L’écart est établi sans ambiguïté et empêche la validation. |
| **Informatif** | Le résultat demande une interprétation humaine. |

Les tests du Codebase Quality Control doivent réussir pour valider une PR de développement. Un test non exécuté ou au résultat inconnu ne satisfait pas cette exigence.

## Vérifier les vérificateurs

Un vérificateur spécifique au projet possède des tests couvrant les cas conformes, les écarts et les exceptions autorisées. Une erreur d’exécution ne doit pas être présentée comme une conformité.

La boucle de développement exécute ces contrôles sans modifier leur dossier. Les adaptations passent par la consolidation, après arbitrage humain.

## Exécuter dans ce dépôt

Depuis la racine du worktree :

| Commande Python | Portée |
| --- | --- |
| `python3 codebase-quality-control/scripts/check.py` | Tests de l’outillage, dont un serveur HTTP local temporaire ; Git et Python requis. |
| `python3 codebase-quality-control/scripts/apps.py check api` | Contrat HTTP, conteneur Symfony, mapping et OpenAPI. |
| `python3 codebase-quality-control/scripts/apps.py check web` | Types et build Nuxt. |
| `python3 codebase-quality-control/scripts/apps.py check backoffice` | Types et build Nuxt. |
| `python3 codebase-quality-control/scripts/quality.py` | Ensemble des contrôles précédents, arrêt au premier échec. |

L’option `--browser` des contrôles web et backoffice ajoute les parcours Playwright ; API de développement et Chromium requis. Installation : [SETUP.md](../../SETUP.md).

La CI est définie dans `.github/workflows/quality.yml`. Le caractère obligatoire de ses résultats pour fusionner une PR dépend des protections GitHub effectivement configurées ; cette documentation ne les active pas.
