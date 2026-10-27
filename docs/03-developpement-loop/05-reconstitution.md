# Reconstitution

> Réunir les commits validés pour obtenir le changement complet demandé.

## Entrée

Toutes les tâches attendues sont validées et possèdent leur commit.

## Déroulement

L’IA vérifie la complétude, les dépendances et la branche de réunion définie au découpage, sans redemander un choix déjà autorisé. Elle rassemble les commits, traite les conflits et vérifie les échanges entre les contributions. Une preview peut aider à observer l’ensemble.

Créer la branche dédiée `demands/<identifiant>` si elle n’existe pas, même pour une seule couche.
Si les SHA validés et la trace documentaire des verdicts sont déjà
présents sur cette branche, vérifier leur ascendance et constater la réunion sans rejouer les commits.

## Sortie

Une branche réunissant la demande initiale, prête pour les vérifications de livraison.

## Procédure associée

`reconstituer-demande`.

## Emplacement de réunion

Les noms de fichiers et dossiers `DEM-*` sont réservés aux documents de demande
dans `dev-book/demand/`, dans chaque copie du dépôt. Les rapports utilisent un
nom décrivant leur rôle, sans ce préfixe. Les identifiants dans le texte et les
branches `demands/<identifiant>` sont conservés.

Les worktrees de réunion sont créés dès le départ hors du dépôt et de ses couches,
sous `<temp>/aide-reunions/<projet>-reunion-<numero>` ; par exemple un nom terminé
par `reunion-008`, jamais `DEM-008`. Résoudre `<temp>` selon l’environnement et
l’identité du dépôt localement, sans chemin personnel versionné. Vérifier que la
destination est extérieure, accessible et sans collision. Réutiliser une copie
existante seulement après vérification de son enregistrement Git, de sa branche
et de sa disponibilité ; ne jamais l’écraser. La branche dédiée est créée à la
reconstitution, pas au découpage.

Le temporaire doit rester disponible pendant la mission : ne pas confier une
contribution active à une purge automatique. Conserver les fichiers locaux,
.env et données lors des déplacements et après livraison ; détacher le worktree
livré avant suppression de sa seule branche temporaire. Les couches restent dans
`worktree/<couche>` ; aucune copie de réunion dans ce dossier.

Créer la copie avec `git worktree add -b demands/<identifiant> <destination> <base>`
après vérification de la base locale explicite. Si la branche existe déjà, vérifier
son affectation avant de la reprendre ; ne pas recréer ou déplacer sa référence.
