# Vérification

> L’humain confronte le résultat aux critères de la demande et de ses cartes et à la trajectoire du projet.

## Entrée

Demande et cartes implémentées, changements, preuves et limites présentés par l’IA.
Une carte seule peut limiter le périmètre de vérification.

## Déroulement

L’humain observe le résultat, examine la cohérence du code et vérifie le respect du périmètre et des conventions techniques. Il valide ou demande une correction, suivie d’une nouvelle vérification.

## Sortie

Des verdicts explicites par carte et un état de couverture de la demande.
La demande reste en attente tant que des cartes sont sans verdict ou à corriger. Les commits d’implémentation existent déjà ; un constat global peut alimenter une demande de consolidation.

## Procédure associée

`verifier-demande`.

Le skill présente une restitution lisible dans le chat et attend un verdict libre, sans formulaire
interactif. Il consigne les verdicts et les SHA concernés dans les cartes et la demande ; son
invocation autorise un commit documentaire limité à ces traces. Il ne modifie pas le code et
ne crée pas un commit d’implémentation manquant. Les corrections retournent à l’implémentation.
Aucun push, PR ou merge implicite.
