# Préparer son environnement de développement

**AI-powered Development Engineering**

Ce dépôt est un blueprint pour développer des applications avec l’aide d’agents IA, dans un cadre structuré et vérifiable.

## 1. Prérequis

Outils de développement : Git, Python 3.12+ pour créer les worktrees et VS Code pour ouvrir le workspace.

Environnement Docker : installer les [outils requis sous Linux/WSL](docs/02-cadre/couches/dockerisation.md#préparer-lenvironnement-local).

Skills du cadre : les installer dans le répertoire personnel de skills de l’outil utilisé, puis vérifier qu’ils sont disponibles dans la session. Les [guides des étapes](docs/03-developpement-loop/index.md) indiquent leurs noms ; le [guide IA Engineering](docs/02-cadre/ia-engineering.md#utiliser-les-skills) précise leur organisation. Ils ne sont pas fournis dans ce dépôt.

## 2. Créer les worktrees

Chaque couche possède un dossier de travail et une branche dédiés. Depuis le dépôt
principal, consulter `git worktree list`, puis créer uniquement les worktrees
manquants avec la [commande du guide des couches](docs/02-cadre/couches/index.md#couches-de-ce-dépôt).
Le dépôt doit avoir un premier commit et une branche locale `develop`.

## 3. Ouvrir le workspace

Depuis le dépôt principal :

```sh
code aide.code-workspace
```

Le workspace regroupe le dépôt principal et les worktrees dans VS Code.
Une couche dont le worktree n’existe pas reste indisponible.
Voir [comment utiliser le workspace](docs/02-cadre/couches/index.md#suivre-les-couches-dans-le-workspace).

## 4. Démarrer les applications avec Docker

Choisir la couche à consulter, puis suivre le [guide de démarrage Docker](docs/02-cadre/couches/dockerisation.md#démarrer-une-couche).
Il décrit les commandes, le choix des interfaces, les adresses et l’arrêt des applications.
Les dépendances applicatives et la base sont gérées dans les conteneurs.

## 5. Réaliser une demande

Commencer par l’[interview de la demande](docs/03-developpement-loop/01-interview.md),
puis suivre la [boucle de développement](docs/03-developpement-loop/index.md).
Chaque étape indique le skill à utiliser, les vérifications attendues et les décisions humaines nécessaires.
