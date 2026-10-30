# Administrer les articles dans le backoffice

> Le backoffice permet de créer, modifier, publier et supprimer les articles de l’API.

## Utiliser l’administration

Suivre la [procédure commune de lancement et de vérification](interfaces.md).
La liste gère la pagination, le chargement, l’absence de résultats et les erreurs.
Les compteurs « publiés » et « brouillons » portent sur la page courante ; le total
porte sur toute la collection.

Le formulaire conserve les saisies en cas d’échec. La suppression demande une
confirmation. Le serveur relaie la lecture et la création via `/api/articles`,
puis la lecture, la modification et la suppression via `/api/articles/{id}`,
avec les formats définis par le [contrat API](api.md#consulter-le-contrat).

## Vérifier le parcours

Le test navigateur crée un article via le formulaire, le modifie, le publie et le
supprime. Il vérifie aussi la conservation des saisies après une panne simulée.
Les commandes et préconditions sont dans la
[procédure commune](interfaces.md#vérifier-et-construire).
