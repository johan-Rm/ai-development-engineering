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
`develop`, puis vers `master`, fusions et nettoyage des branches temporaires livrées. Aucune confirmation intermédiaire n’est nécessaire.
Une instruction explicitement limitée à une PR conserve cette limite. Les validations humaines
acquises, les contrôles bloquants et les protections GitHub restent nécessaires ; ne pas les contourner.
Seules les branches confirmées libres sont réalignées sans perte de données.
Un écart de périmètre ou une contribution non validée reste à résoudre ; l’autonomie de livraison
n’autorise pas à intégrer du travail étranger. Toute modification de cette procédure et du skill
met à jour AGENTS.md et les guides concernés ensemble.

## Livraison finale et nettoyage

La livraison complète suit deux PR : branche dédiée → `develop`, puis `develop` → `master`.
`master` est la branche par défaut et de production. Vérifier le diff complet de la promotion :
toute autre contribution doit être validée et incluse dans le périmètre autorisé ; sinon arrêter
avant promotion. Attendre les contrôles et protections de chaque PR et vérifier chaque SHA de fusion.
Une fusion ne constitue pas une preuve de déploiement applicatif.

Après fusion finale vérifiée, supprimer les branches temporaires livrées locales et distantes,
libres et sans travail inédit ni autre PR ouverte, sans suppression forcée. Conserver les branches
`master`, `develop`, les couches locales `layers/*` et les branches occupées. Les couches ne sont
pas publiées sur le distant. Conserver les worktrees et leurs `.env` ; détacher uniquement celui
de la livraison s’il est propre et libre avant suppression de sa branche. Rapporter les suppressions
réelles et les exceptions. Une demande explicitement limitée conserve sa limite.
