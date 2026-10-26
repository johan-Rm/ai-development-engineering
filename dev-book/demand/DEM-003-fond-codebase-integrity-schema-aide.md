# DEM-003 — Passer le bloc Codebase Integrity en terre cuite dans le schéma AIDE

- Date : 2026-10-26.
- État du cadrage : confirmé par l’humain dans le chat.
- Référence de session indisponible ; aucune carte externe fournie.

## Besoin, contexte et utilisateurs

L’humain demande de changer le fond du bloc Codebase Integrity dans la vue interactive
AIDE, destinée aux lecteurs du cadre. Le bloc utilise actuellement un fond olive clair.
Le résultat souhaité est un fond terre cuite `#C07040` et des textes blanc cassé `#FAFAF6`.
La motivation graphique détaillée n’a pas été précisée ; elle n’est pas nécessaire pour
appliquer les couleurs explicitement choisies.

## Résultat attendu et critères observables

1. Dans `dev-book/resources/vue-d-ensemble-ai-development-engineering.html`, le seul bloc
   Codebase Integrity possède un fond opaque `#C07040`.
2. Son titre et son sous-texte utilisent le blanc cassé `#FAFAF6`.
3. Les textes, le rôle « contrôles sans IA », les interactions, la disposition et les
   autres blocs restent inchangés, y compris les éléments IA passés en bleu par DEM-002.
4. L’adaptation est consignée dans `design/charte-graphique.md` ; cette couleur ne
   réattribue pas le bloc à l’IA et ne modifie pas le rôle des contrôles.
5. La preuve attendue comprend un contrôle des couleurs effectives et une relecture
   visuelle du bloc, de ses textes et de ses états interactifs existants.

## Contraintes et exclusions

Conserver la charte officielle Graines Digitales sans modification. La nouvelle couleur
est une adaptation explicitement demandée pour ce bloc du schéma AIDE.
Préserver la typographie, les aplats, le plein écran et les interactions existantes.
Ne pas modifier les applications, l’infrastructure, les sources historiques ou les
couleurs des autres éléments. Aucun changement de contrat, de données, de permissions
ou de parcours applicatif : ces dimensions ne sont pas concernées par cet ajustement visuel.
La modification du skill personnel demandée dans le chat est déjà traitée hors dépôt ;
elle ne fait pas partie de l’implémentation de cette demande.

## Décisions humaines

Le 2026-10-26, l’humain a demandé le fond `#C07040`, puis choisi « Passer le texte en blanc
cassé comme les blocs IA ». Cette réponse fixe la couleur du texte et non le rôle du bloc.
Après restitution dans le chat du périmètre et des preuves attendues, l’humain a répondu
« confirmé ». La confirmation porte sur le besoin, pas sur un résultat implémenté.

## Questions ouvertes

Aucune question de besoin ouverte. La disponibilité opérationnelle de la couche devra
être revérifiée avant toute implémentation ; les cartes consultées ne montrent pas
d’affectation concurrente, sans garantir l’absence de mission externe au dépôt.

## Tâches issues du découpage

| Carte | Couche | Couverture | Dépendances |
| --- | --- | --- | --- |
| [OPS-048](../tasks/OPS-048-fond-codebase-integrity-schema-aide.md) | devops | Critères 1 à 5 | OPS-047 : `8db9d9bd436d835d6119ea55eac461b4d463cb19`, déjà intégré à la branche locale |

Une seule carte : schéma et adaptation graphique associée appartiennent à la même mission.

## Réunion prévue

- Branche dédiée : `demands/DEM-003`.
- Worktree : `/home/johan/www/lab/ai-orchestrated-development/worktree/DEM-003`.
- Création à la reconstitution, à partir des commits validés ; aucune création à cette étape.

## Preuve du découpage

Le 2026-10-26, invocation explicite de `decouper-demande` pour DEM-003.
Historique de toutes les références locales et cartes des worktrees examinés sans fetch :
maximum OPS-047, attribution OPS-048. Branche `layers/devops` conservée au commit
`2c9aeb348af37e9858df4144e00576ee3425bf3b` ; dépendance OPS-047 vérifiée dans son ascendance.
Seul le fichier de cadrage DEM-003 était non suivi avant cette étape. Aucune autre mission
active repérée dans les cartes consultées ; disponibilité à revérifier avant implémentation.
Aucun changement de schéma, commit, rebase ou opération distante réalisé.

## Preuve de cadrage et enregistrement

Cadrage confirmé dans le chat le 2026-10-26. Historique des chemins de demandes de toutes
les références Git locales et fichiers des worktrees examinés sans fetch : maximum DEM-002.
DEM-002 porte sur les éléments IA en bleu ; le présent besoin est distinct.
Enregistrement dans `/home/johan/www/lab/ai-orchestrated-development/worktree/devops`,
branche `layers/devops`, arbre propre avant écriture. Aucun commit, branche, carte ou
changement du schéma créé à cette étape.

## Vérification humaine — 2026-10-26

Demande validée par l’humain : réponse explicite « validé » dans le chat après présentation
d’OPS-048, unique carte couvrant les critères 1 à 5.
Commit d’implémentation accepté : `4930bc99d7678d80f6ddeb2ed6a64b224f5a572a`.
Couleurs et interactions vérifiées dans Chromium ; documentation graphique alignée.
Limites présentées et conservées : contraste 3,563:1, mobile et plein écran non exercés.
Aucune correction demandée. La validation ne vaut pas livraison ; aucune reconstitution,
PR, fusion ou opération distante n’est lancée par cette étape.

## Preuve de reconstitution — 2026-10-26

Branche dédiée `demands/DEM-003`, worktree
`/home/johan/www/lab/ai-orchestrated-development/worktree/DEM-003`.
Base locale explicite `f2fd74382cbcf74132ced8211ffe2cc665107046` (`origin/develop`
observée sans fetch), contenant déjà OPS-047. Le `develop` local divergent est préservé.
Le commit documentaire hors demande `2c9aeb3` de la couche devops est exclu.

Commits autorisés repris sans conflit, dans l’ordre :

| Origine validée | Commit de réunion | Rôle |
| --- | --- | --- |
| `4930bc99d7678d80f6ddeb2ed6a64b224f5a572a` | `bdccc907eb47051e2a06ae99e7a66408d244756e` | Implémentation OPS-048 |
| `b69f00fb856c640894d6656f2f2112597bf3b61e` | `64d099989076afaa8461fba03e037a50541ba3be` | Verdict humain |

Équivalence des deux patchs vérifiée avec `git patch-id --stable`. Les quatre fichiers
de la demande sont strictement identiques au résultat validé dans `b69f00f` avant cette
trace documentaire. Le diff depuis la base contient seulement ces quatre fichiers.
`git diff --check` réussi. `python3 codebase-integrity/scripts/check.py` : 23 tests réussis
après relance hors sandbox pour le serveur localhost temporaire ; premier essai refusé
par les permissions de socket. Aucun contrôle affaibli ni fichier non commité transféré.
Les preuves navigateur du résultat validé restent applicables au HTML identique ;
mobile et plein écran restent non exercés. Aucun contrat applicatif modifié.
La qualité complète avant PR reste à exécuter à la livraison ; aucun push, PR ou merge.
