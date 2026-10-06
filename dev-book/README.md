# Dev-book

Le journal opérationnel du projet qui adopte AIOD. La méthode est dans `docs/aiod/`.

| Dossier | Contenu |
| --- | --- |
| `demand/` | Besoins, contexte et décisions de cadrage |
| `tasks/` | Une carte par tâche, ses critères et sa preuve |
| `runbooks/` | Procédures reproductibles avec préconditions et vérifications |
| `resources/` | Ressources techniques utilisées pour réaliser ou vérifier |

## Rubriques d’une demande

Contexte, problème observé, résultat attendu, contraintes, questions ouvertes et décisions humaines.

## Rubriques d’une carte

Identifiant et titre ; état (à cadrer, prête, en cours, bloquée, clôturée) ; date ; demande d’origine ;
couche ; périmètre et exclusions ; critères d’acceptation ; dépendances par commit ; affectation
(session, branche, chemin absolu) ; réalisation ; preuves et commandes ; documentation mise à jour.

Une carte clôturée voyage dans le commit de sa tâche. Les identifiants sont attribués après
vérification des branches concernées. Une carte découverte ne constitue pas une autorisation de travail.

## Rubriques d’une procédure

Objectif, préconditions, étapes, vérifications, arrêt en cas d’erreur et retour arrière si applicable.
Les dossiers sans contenu sont créés lors de leur premier usage ; Git ne conserve pas les dossiers vides.
