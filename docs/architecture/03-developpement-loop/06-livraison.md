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
documentaires nécessaires, vérification distante et fetch, push, création ou mise à jour de la PR vers
`develop`, fusion et suivi après fusion. Aucune confirmation intermédiaire n’est nécessaire.
Une instruction explicitement limitée à une PR conserve cette limite. Les validations humaines
acquises, les contrôles bloquants et les protections GitHub restent nécessaires ; ne pas les contourner.
### Intégration et suivi communs aux deux boucles

Utiliser **Rebase and merge** pour intégrer les PR vers develop. Chaque commit est
conservé avec un nouvel identifiant ; aucun commit de fusion ni squash n’est créé.
Vérifier la méthode permise par GitHub ; si elle est interdite, signaler le blocage
sans substituer une autre stratégie ni modifier les protections. Les branches de
PR doivent être linéaires : ne pas créer de merges pour rattacher les couches.
Une modification nécessaire du contenu validé demande une nouvelle vérification.

Avant intégration, consigner la PR, son HEAD, les SHA sources et reconstitués,
les contrôles et les verdicts. Après intégration, vérifier l’état intégré de la PR,
le SHA résultant et sa présence dans develop distant ; tracer les correspondances
avec les commits réécrits. Une équivalence de patch seule ne prouve pas l’intégration.
Ne pas réécrire les anciens commits de fusion.

Actualiser develop local par avance rapide, dans le dossier principal disponible.
Pour les couches locales libres et propres : avancer par avance rapide si possible.
Si seuls les SHA réécrits empêchent l’avance rapide, vérifier que chaque contribution
locale est bien incluse dans la PR intégrée, sans commit inédit, puis consigner
l’ancien SHA. Un rebase local sans commit à rejouer peut repositionner cette seule
branche sur le develop vérifié (`git rebase --onto <develop-vérifié> <ancien-tip> <couche>`).
Cette autorisation concerne uniquement les couches locales non partagées et confirmées
libres ; elle n’autorise ni rebase d’une branche occupée ni force-push. Au moindre
doute de provenance ou d’équivalence, préserver la branche et signaler le suivi bloqué.
Ne pas utiliser reset, stash ou suppression de worktree pour atteindre l’alignement.

Vérifier l’égalité des SHA de develop et de toutes les couches avant de clôturer
le suivi. Conserver les worktrees, données et `.env` ; ne jamais publier les layers/*.
Une couche sale, occupée ou portant un commit inédit reste intacte et empêche la clôture.

Revenir sur develop dans le dossier principal après l’intégration vérifiée. Supprimer
la branche temporaire distante livrée seulement sans autre PR ouverte ni travail inédit.
Pour la suppression locale sans forcer, vérifier d’abord l’intégration réelle et la
correspondance de tous ses commits ; sur la branche temporaire libre et propre,
un rebase sans commit à rejouer peut la placer sur le develop vérifié, puis revenir
sur develop et exécuter `git branch -d demands/<identifiant>`. Sinon la conserver et
signaler le suivi incomplet. Ne jamais supprimer develop, master ou une couche.

Consigner le suivi après intégration dans le brouillon local de la même demande,
s’il existe, sans modifier directement les fichiers suivis de develop ni créer
un rapport supplémentaire. La promotion vers master nécessite une demande distincte.
