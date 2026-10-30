# Consulter les articles dans la webapp

> La webapp affiche les articles de l’API et permet de parcourir leurs pages.

## Utiliser la liste

Suivre la [procédure commune de lancement et de vérification](interfaces.md).
La liste gère le chargement, la pagination et l’absence de résultats. Si l’API
est indisponible, elle affiche une erreur et un bouton « Réessayer ».

Le serveur relaie uniquement la lecture de la collection par `GET /api/articles` ;
les modifications ne sont pas exposées par cette interface. Les brouillons sont
visibles, conformément aux [limites du socle API](api.md#consulter-le-contrat).
Le dossier `app/web/shared/` est réservé à un futur socle commun à plusieurs cibles.

## Vérifier le parcours

Le test navigateur crée temporairement un article via l’API pour vérifier sa
lecture réelle, puis le supprime. Il simule aussi les listes vides et les erreurs.
`TEST_API_URL` permet de choisir l’API locale de développement utilisée par ce test.
Les commandes et préconditions sont dans la
[procédure commune](interfaces.md#vérifier-et-construire).
