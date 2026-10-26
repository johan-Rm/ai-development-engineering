# Implémentation

> Réaliser les cartes d’une demande dans leurs couches et présenter des résultats vérifiables.

## Entrée

Demande découpée en cartes prêtes, couches disponibles et dépendances présentes par commits identifiés. Une carte seule peut limiter le périmètre.

## Déroulement

L’IA suit les dépendances des cartes et, pour chacune, vérifie la branche et le worktree, lit les README applicables, puis réalise le changement. Elle applique les conventions techniques, exécute les contrôles pertinents et prépare les tests et la documentation associés.

## Sortie

Un commit local distinct par carte, avec tests, documentation et preuves, prêt pour vérification
humaine. L’invocation autorise ces commits dans ce projet, après vérification de l’index et du
périmètre ; les changements étrangers restent préservés. Un commit ne vaut pas validation.
Chaque correction produit un nouveau commit de la même carte. Aucun push, PR ou merge implicite.

## Procédure associée

`implementer-demande`.
