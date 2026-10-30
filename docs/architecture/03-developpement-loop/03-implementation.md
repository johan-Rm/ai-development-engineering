# Implémentation

> Réaliser les cartes d’une demande dans leurs couches et présenter des résultats vérifiables.

## Entrée

Demande découpée en cartes prêtes, couches disponibles et dépendances présentes par commits identifiés. Une carte seule peut limiter le périmètre.

## Déroulement

Une demande entière confie toutes ses cartes prêtes, sauf restriction explicite.
L’IA suit leurs dépendances réelles et, pour chacune, vérifie la branche et le worktree, lit les README applicables, puis réalise le changement. Elle applique les conventions techniques, exécute les contrôles pertinents et prépare les tests et la documentation associés.

Avant une nouvelle mission, vérifier `git status --porcelain=v1 --untracked-files=all`
dans le worktree affecté et l’index : une couche sale ou occupée bloque le démarrage,
sans nettoyage ni commit pour contourner le blocage. Une reprise de la même mission
peut conserver ses changements non commités identifiés, sans travail étranger.
Un arbre propre ne suffit pas à établir la disponibilité de la couche.

Réaliser toutes les cartes indépendantes sans validation intermédiaire artificielle.
Une carte amont peut être réalisée puis présentée à la vérification, mais son
consommateur attend le commit issu de sa validation. Aucun transfert de travail
non commité entre missions.

## Sortie

Des changements non commités par carte, avec tests, documentation et preuves,
prêts pour vérification humaine. Aucun commit de code, cadrage, carte ou correction
à cette étape. Identifier le HEAD de base, les fichiers modifiés ou non suivis et
le diff soumis pour retrouver le contenu présenté. Les commits distincts sont
créés à l’étape 04 après validation explicite. Aucun push, PR ou merge implicite.

## Procédure associée

`implementer-demande`.
