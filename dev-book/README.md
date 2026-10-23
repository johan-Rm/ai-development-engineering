# Dev-book

Le journal opérationnel du projet qui adopte AIOD. La méthode est dans `docs/`. Les guides Markdown y sont placés directement ;
les ressources HTML, PDF et images sont dans `resources/`.

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

Toutes les cartes, de construction ou de maintenance, ouvertes ou clôturées, sont conservées
dans `tasks/`, sans sous-dossier d’archives. Leur statut indique le travail restant.
Les cartes clôturées sont des traces historiques, jamais des tâches à reprendre automatiquement.
Les preuves datées et les mentions d’état Git décrivent le moment de leur rédaction ; elles ne
constituent pas une vérification de l’état actuel. Les chemins personnels historiques sont
remplacés par des placeholders ; les originaux restent consultables dans Git.

La maintenance du cadre appartient à devops (cartes `OPS`). Les cartes `BP` conservent
leurs identifiants et leur contexte historiques ; elles ne définissent aucune couche supplémentaire.
