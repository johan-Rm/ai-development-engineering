# Codebase Quality Control

Le **Codebase Quality Control est la brique déterministe du cadre AIDE**. Il rassemble
les outils et les tests qui vérifient l’application des conventions techniques du projet,
sans jugement d’IA à l’exécution.

## Responsabilités

- Vérifier les conventions techniques définies exclusivement par les humains : QA,
  développeurs, tech leads, CTO, architectes et autres responsables du projet.
- Fournir les points de contrôle exécutables et leurs configurations, avec leurs périmètres,
  exceptions et niveaux bloquants ou informatifs.
- Tester les vérificateurs propres au projet pour qu’ils détectent les écarts et acceptent
  les cas conformes.
- Rendre visible l’absence de contrôle implémenté pour une convention documentée.

## Autorité et modifications

**Le processus de développement applique les conventions et exécute les contrôles.
Il ne peut strictement pas modifier le Codebase Quality Control** : conventions,
vérificateurs, tests de ces vérificateurs, configurations, exceptions, seuils ou niveaux de blocage.
Un échec ou une ambiguïté donne lieu à un constat à transmettre à l’humain ; il n’autorise
ni le contournement ni l’affaiblissement d’un contrôle.

Le Codebase Quality Control est propre à chaque projet et reste vivant. Ses évolutions
passent par le processus de consolidation, sous décision et validation humaines.
L’IA peut assister l’implémentation d’une évolution explicitement approuvée dans ce cadre ;
elle ne définit ni ne modifie les conventions de sa propre initiative.

## Contenu et commandes

- [scripts/](scripts/README.md) : commandes de contrôle et outils communs du cadre.
- [tests/](tests/README.md) : tests de l’outillage et vérification du schéma interactif.

Depuis la racine du dépôt :

```sh
python3 codebase-quality-control/scripts/check.py
```

La commande complète, après installation des dépendances applicatives :

```sh
python3 codebase-quality-control/scripts/quality.py
```

Les [principes et domaines](../docs/aiod/codebase-quality-control.md) décrivent la structure
du Codebase Quality Control. Les [commandes fournies](../docs/qualite.md) précisent leur portée.
Les tests applicatifs restent au plus près de chaque application.
