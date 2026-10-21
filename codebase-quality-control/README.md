# Codebase Quality Control

Ce dossier regroupe les outils et les tests auparavant placés à la racine.

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
