# Règles de PR

> Présenter et vérifier une demande complète avant son intégration.

La PR présente une demande reconstituée vers develop. Son titre exprime le résultat
global, par exemple `Clarifier les conventions des commits (DEM-024)` ; il ne
reprend pas le titre de la première carte. Le corps explique le problème résolu,
le comportement obtenu, les vérifications et leurs limites.

Avant ouverture, les cartes attendues ont leurs verdicts et leurs commits, et
les contrôles qualité portent sur l'ensemble à livrer. Le vérificateur des messages
examine toute la plage : un commit invalide au milieu de la série bloque la PR.
Les références sont confrontées aux documents présents dans l'arbre reconstitué.
Le contrôle de contribution applique les [règles selon la boucle](README.md#vérification),
avec les associations déclarées dans la demande. Sa réussite ne dispense pas
de la revue de leur adéquation. Un statut obligatoire et une protection du workflow
doivent être vérifiés sur GitHub avant d’annoncer une fusion techniquement bloquée.

La relecture humaine porte aussi sur ce que les contrôles ne peuvent pas établir :
la précision du titre, la pertinence du type et l'adéquation du résultat au besoin.
Une correction fonctionnelle nécessite une nouvelle validation. La réussite
technique ne vaut pas verdict humain, et un contrôle inconnu ne vaut pas réussite.

La préparation de la PR, son intégration et le suivi sont distincts. Une instruction
limitée à la PR n'autorise pas sa fusion. Les conditions et commandes d'exécution
sont conservées dans les procédures de livraison et de Codebase Integrity.

## Exécuter les contrôles

Depuis la racine de la copie contenant les commits candidats :

```sh
python3 codebase-integrity/scripts/contribution.py --repo . --base develop --head HEAD
python3 codebase-integrity/scripts/quality.py --commit-base develop --commit-head HEAD
```

Remplacer `develop` par le SHA d’intégration vérifié. Git, Python et un historique
complet sont nécessaires au contrôle de contribution ; les applications ont leurs
propres prérequis. Les fichiers non commités ne sont pas examinés par ce contrôle.
Sans base explicite, `quality.py` exécute les contrôles locaux mais ne prouve pas
la conformité de la contribution.

Le lanceur lit les objets Git et charge le vérificateur depuis la base. La CI
sépare cette vérification de l’exécution applicative ; les tests de la version
candidate restent exécutés séparément. La revue humaine apprécie le type déclaré,
la pertinence des conventions, le renforcement réel des tests et la qualification
des fichiers d’accompagnement. Le format de déclaration est défini dans les
[conventions du dev-book](../../dev-book/README.md#types-de-demandes).

Pour le premier amorçage, fournir le commit explicitement approuvé via
`--bootstrap-policy-sha <SHA>`. En CI, renseigner après validation humaine la variable
de dépôt utilisée par le [workflow de qualité](../../.github/workflows/quality.yml). Le lanceur
limite ce mode à sa demande et à sa base initiales configurées ; il compare le
contenu complet du candidat à celui du commit approuvé. Rebase and merge peut
réécrire les SHA sans changer ce contenu. Toute édition après approbation,
même documentaire, nécessite une nouvelle approbation.

Après intégration vérifiée, supprimer la variable d’amorçage. Le lanceur utilise
alors exclusivement le vérificateur présent dans la base. L’identité de contenu
ne garantit pas à elle seule la protection du workflow : statut obligatoire et
protections distantes restent à vérifier avant d’annoncer le blocage d’une fusion.
