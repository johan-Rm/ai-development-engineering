# Vérification

> L’humain confronte le résultat aux critères de la demande et de ses cartes et à la trajectoire du projet.

## Entrée

Demande et cartes implémentées, changements, preuves et limites présentés par l’IA.
Une carte seule peut limiter le périmètre de vérification.

## Déroulement

L’humain observe le résultat, examine la cohérence du code et vérifie le respect du périmètre et des conventions techniques. Il valide ou demande une correction, suivie d’une nouvelle vérification.

## Sortie

Des verdicts explicites par carte et un état de couverture de la demande.
La demande reste en attente tant que des cartes sont sans verdict, à corriger ou
sans leur commit attendu. Les changements sont normalement non commités à l’entrée ;
une ancienne contribution déjà commitée reste vérifiable sans réécriture de son histoire.

## Procédure associée

`verifier-demande`.

Le skill présente une restitution lisible et attend un verdict libre dans le chat,
sans formulaire interactif. Il identifie précisément le contenu présenté (HEAD de
base, diff, fichiers non suivis, empreinte ou relevé équivalent). Sans validation
explicite, aucun commit n’est créé ; les corrections retournent à l’implémentation.

Après validation, vérifier que le contenu correspond toujours à celui présenté.
L’invocation autorise un commit local distinct par carte validée, comprenant son
code déjà réalisé, ses tests, documentation, preuves et verdict. Indexer seulement
le périmètre accepté, sans changements étrangers ni cartes non validées. Aucun
nouveau développement à cette étape. Un changement fonctionnel depuis la revue
nécessite une nouvelle validation. Aucun commit sur intégration ou production.

Relever les SHA créés et les associer aux verdicts ; un complément documentaire
peut consigner ces SHA. Une correction validée produit un nouveau commit, sans
amend ni réécriture. Si le résultat était déjà commité, conserver ce SHA et créer
uniquement la trace de verdict nécessaire. Aucun push, PR ou merge implicite.
