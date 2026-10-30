# Convention de commits — Conventional Commits et scope

> Comprendre ce que le type, le scope et le titre disent du changement.

Le message permet de comprendre une contribution indépendamment de sa branche
et de la PR qui la transporte. Le type indique la nature du changement ; le scope
identifie ici la carte, plutôt qu'un dossier ou une application.

Par exemple, `ci(OPS-075): vérifier les messages de chaque commit de la PR`
annonce un changement d'intégration continue et permet de retrouver sa carte.
`docs(OPS-075): consigner le SHA du commit validé` désigne une trace documentaire
complémentaire pour cette même carte. Ces deux commits ont des rôles différents,
ce qui justifie des titres différents.

Le choix du type suit le changement principal. Ajouter un contrôle exécutable
n'est pas simplement documenter son existence ; corriger un comportement ne se
confond pas avec réorganiser son code.

La liste des types, la syntaxe exacte et les exceptions sont définies dans les
[conventions techniques de cette thématique](README.md#conventions-techniques).
