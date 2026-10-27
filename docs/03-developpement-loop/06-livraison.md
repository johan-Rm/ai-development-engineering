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
La livraison complète inclut l’alignement de toutes les couches configurées sur le
même SHA que develop après fusion vérifiée. Avant la PR, inventorier les branches,
leurs missions et les modifications locales. Une divergence composée uniquement de
copies des contributions validées peut être résolue par des merges ciblés dans la
branche de livraison : vérifier les commits et l’équivalence du résultat, et conserver
le contenu validé. Cela rend les couches ancêtres du résultat livré et permet leur
avance rapide finale, sans reset ni réécriture.

Après fusion distante vérifiée, avancer develop et chaque couche libre et propre
par avance rapide, puis contrôler leur égalité de SHA et l’état de leurs worktrees.
Préserver les .env, les données et les commits. Les branches de couche restent locales.
Une couche occupée, sale ou avec du travail inédit reste intacte ; ce blocage signifie
que le suivi de livraison n’est pas terminé, même si la PR est déjà fusionnée.
Un écart de périmètre ou une contribution non validée reste à résoudre ; l’autonomie de livraison
n’autorise pas à intégrer du travail étranger. Toute modification de cette procédure et du skill
met à jour AGENTS.md et les guides concernés ensemble.

Le worktree de réunion reste à son emplacement temporaire extérieur au projet,
sous un nom sans préfixe `DEM-*`. Après fusion vérifiée, conserver son contenu,
le détacher sur le commit livré puis supprimer uniquement la branche temporaire
libre. Ne pas recréer de copie de réunion dans `worktree/`. Le rangement suit
[les instructions du projet](../../AGENTS.md#rangement-des-demandes-et-réunions).
