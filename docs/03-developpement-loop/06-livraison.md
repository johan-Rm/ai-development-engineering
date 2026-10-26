# Livraison

> Livrer en autonomie une demande validée, des contrôles à la fusion et au suivi.

## Entrée

Changement reconstitué et tâches validées.

## Déroulement

L’IA exécute les contrôles sur l’ensemble à livrer, corrige les échecs et vérifie que les tests et la documentation accompagnent le comportement final. Elle prépare une PR décrivant le besoin traité, les preuves et les limites.

## Sortie

Une PR correspondant à la demande initiale. Sa validation exige la réussite des tests du Codebase Integrity et des autres contrôles bloquants. Un résultat inconnu n’est pas une réussite.

## Procédure associée

`livrer-demande`.

L’invocation de `livrer-demande` autorise la livraison complète : contrôles, commits
documentaires nécessaires, vérification distante, push, création ou mise à jour de la PR vers
`develop`, fusion et suivi après fusion. Aucune confirmation intermédiaire n’est nécessaire.
Une instruction explicitement limitée à une PR conserve cette limite. Les validations humaines
acquises, les contrôles bloquants et les protections GitHub restent nécessaires ; ne pas les contourner.
Seules les branches confirmées libres sont réalignées sans perte de données.
Un écart de périmètre ou une contribution non validée reste à résoudre ; l’autonomie de livraison
n’autorise pas à intégrer du travail étranger. Toute modification de cette procédure et du skill
met à jour AGENTS.md et les guides concernés ensemble.
