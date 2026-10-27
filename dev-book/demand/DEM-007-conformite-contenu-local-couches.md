# DEM-007 — Vérifier la conformité du contenu local des couches

- Date : 2026-10-27.
- État : périmètre corrigé validé et reconstitué ; non livrée.
- Référence de session : référence de session indisponible.
- Carte externe : aucune fournie.

## Périmètre corrigé — décision humaine du 2026-10-27

L’humain précise : « moi je veux simplement nettoyer et corriger ce qui à été
évoqué, si il y a eu un malentendu il faut le corriger ». Le besoin courant est
le nettoyage ponctuel des résidus identifiés par l’audit OPS-055 validé.
L’extension à une convention, un nouveau contrôle réutilisable et son intégration
à la livraison est abandonnée. Cette décision remplace les exigences et blocages
correspondants dans les sections historiques ci-dessous. Aucun arbitrage technique
supplémentaire n’est requis pour ce nettoyage explicitement demandé.

OPS-056 est sans suite. OPS-057 est ramenée au nettoyage local et à sa preuve.
Aucune modification de Codebase Integrity, des règles de livraison ou des skills.

## Besoin, contexte et utilisateurs

Les contributeurs humains et les agents doivent pouvoir consulter des couches
conformes après livraison. L’humain constate que des dossiers supprimés lors de
travaux antérieurs subsistent dans le dossier principal. Il demande une vérification
globale, sans devoir lui-même identifier chaque anomalie.

Le relevé initial trouve dans le principal `scripts/__pycache__/apps.cpython-312.pyc`
et `tests/__pycache__/test_apps.cpython-312.pyc`. Ces caches maintiennent les dossiers
`scripts/` et `tests/` après suppression des sources. Ces deux dossiers sont absents
des cinq couches au moment du relevé. Un état Git propre et des SHA identiques ne
suffisent donc pas à prouver la conformité du contenu réel.

D’autres contenus locaux hors arborescence suivie sont observés : caches, résultats
de tests, ressources applicatives générées et dossiers d’environnement. Leur seule
absence de Git ne prouve pas qu’ils sont obsolètes. Le relevé exploratoire a exclu
notamment le contenu des dépendances et des caches applicatifs : il ne constitue
pas l’audit exhaustif attendu. Aucun nettoyage n’a été effectué durant l’interview.

## Résultat attendu et périmètre

Auditer le contenu réel du principal et des cinq couches configurées : API, web,
backoffice, design et devops. Examiner aussi les contenus ignorés ou non suivis,
et identifier les restes de suppressions anciennes au-delà des exemples signalés.
Distinguer les résidus certains, les contenus locaux utiles et les cas incertains,
en justifiant leur classement par les sources, usages et règles applicables.

Nettoyer les résidus identifiés avec certitude et fournir une vérification
réutilisable lors des livraisons. Elle nettoie automatiquement les seuls résidus
certains. Si un doute subsiste, elle signale les chemins et raisons et bloque la
fin de livraison jusqu’à résolution. Aucun doute ne doit entraîner une suppression.

La conformité tient compte des fichiers locaux utiles à chaque couche ; elle
n’impose pas une égalité aveugle de tous les fichiers locaux. Elle complète les
vérifications existantes des branches, commits et états Git.

## Contraintes et exclusions

- Préserver les `.env`, données, fichiers générés utiles et travaux en cours,
  y compris ignorés ou non suivis. Préserver les worktrees et les services.
- Ne pas supprimer globalement les fichiers ignorés ou les caches sans établir
  leur caractère obsolète. Aucun stash, reset destructif ou nettoyage Git global.
- Une couche occupée ne doit pas subir de nettoyage concurrent ; sa situation doit
  être signalée et résolue avant de déclarer le suivi terminé.
- L’évolution des conventions et contrôles doit suivre la boucle de consolidation
  du projet ; ce document conserve le besoin et ne vaut pas arbitrage technique.
- L’interview ne crée ni carte ni branche et ne déclenche pas le découpage,
  l’implémentation, un commit ou une livraison.

## Critères observables et preuves attendues

1. Un inventaire avant/après couvre le principal et les cinq couches, avec les
   chemins examinés, les éventuelles limites et le classement justifié des écarts.
2. Les résidus certains, dont les deux caches historiques observés s’ils sont
   toujours présents et obsolètes, sont retirés avec leurs dossiers devenus inutiles.
3. Les contenus locaux utiles et travaux en cours sont préservés ; la preuve ne
   repose pas uniquement sur `git status` ou l’identité des SHA.
4. La vérification réutilisable s’intègre au suivi de livraison et rend visibles
   ses résultats pour chaque arbre. Un doute empêche d’annoncer la fin de livraison.
5. Des essais démontrent le nettoyage d’un résidu certain, la préservation des
   fichiers utiles et le blocage sans suppression d’un contenu incertain.
6. Une seconde exécution après nettoyage ne produit aucun nouveau changement
   en l’absence de changement de contenu ou de contexte.
7. La documentation décrit le contrôle, les preuves et le traitement des cas
   incertains. Les README concernés et le guide de livraison sont à examiner ;
   leurs chemins précis seront arrêtés lors de l’analyse de consolidation.
8. Les contrôles pertinents du projet réussissent, notamment les tests d’outillage
   `python3 codebase-integrity/scripts/check.py` et la qualité
   `python3 codebase-integrity/scripts/quality.py`, selon le périmètre implémenté.

## Décisions humaines et confirmation

L’humain demande de tout vérifier : il ne souhaite pas devoir dresser la liste des
restes et refuse des couches non conformes. Il choisit « Audit, nettoyage et
vérification réutilisable », puis le nettoyage automatique des seuls résidus
identifiés avec certitude, avec blocage en cas de doute.

Le récapitulatif du périmètre, des protections, du comportement et des preuves,
ainsi que du passage par la consolidation pour les conventions et contrôles, a
été confirmé dans le chat par « oui », le 2026-10-27. Cette confirmation porte sur
le besoin, pas sur un résultat implémenté.

## Questions ouvertes

Aucune décision de besoin nécessaire ne reste ouverte. La définition déterministe
d’un résidu certain, les exceptions, les limites de parcours et l’intégration
technique au suivi de livraison restent à analyser et arbitrer en consolidation.
Aucune règle technique de suppression n’est inventée à cette étape.

## Tâches issues du découpage

| Besoin et critères | Carte | Couche | Prérequis |
| --- | --- | --- | --- |
| Audit complet, classement et protections (1, 3) | [OPS-055](../tasks/OPS-055-auditer-contenu-local-couches.md) | devops | Disponibilité et cadrage commité |
| Contrôle et nettoyage sûr, tests (2 à 6, 8) | [OPS-056](../tasks/OPS-056-verifier-nettoyer-residus-locaux.md) | devops | Audit commité et arbitrage de consolidation |
| Livraison, recette réelle et documentation (1 à 8) | [OPS-057](../tasks/OPS-057-integrer-recetter-conformite-livraison.md) | devops | Contrôle commité et validé, cibles disponibles |

Ordre séquentiel OPS-055 → analyse et arbitrage de consolidation → OPS-056 → OPS-057.
Aucun nouveau contrôle ni nettoyage autorisé avant l’arbitrage requis. Les cartes
qui dépendent de commits inexistants restent bloquées ; relever les SHA à leur
production. Ce découpage ne déclenche aucune de ces étapes.

## Réunion prévue

Branche dédiée `demands/DEM-007` et worktree `worktree/DEM-007`, à créer seulement
à la reconstitution depuis une base locale vérifiée. Ne pas utiliser une branche
de couche pour réunir la demande. Réunir les commits validés et leurs verdicts,
jamais du travail non commité.

## Preuve du découpage — 2026-10-27

Historique des cartes de toutes les références Git locales et fichiers des worktrees
examinés sans fetch : plus grand OPS observé OPS-054. Attribution OPS-055 à OPS-057,
sans collision observée. Demande préexistante conservée.

Worktree absolu résolu localement : dossier `worktree/devops` du dépôt principal ;
branche vérifiée `layers/devops` à `7511267`. Le develop local et les quatre autres
couches observées sont à `98932aa`. Devops
conserve des traces de DEM-006 différentes du develop actuel : aucun réalignement
ni rebase effectué. Son seul fichier non suivi avant écriture est DEM-007.
La disponibilité opérationnelle reste à confirmer avant exécution : état Git seul
insuffisant, suivi DEM-006 à clarifier. Aucun SHA de dépendance DEM-007 disponible.

Écriture documentaire limitée à DEM-007 et ses trois nouvelles cartes dans le
worktree devops ; branche existante conservée. Aucun commit, création de branche,
implémentation, nettoyage, test d’outillage, synchronisation distante ou délégation.
Les preuves attendues figurent dans les cartes ; elles ne sont pas annoncées réussies.

## Preuve d’enregistrement

Historique des demandes de toutes les références Git locales et fichiers des
worktrees examinés sans fetch : plus grand identifiant observé DEM-006. Aucun
doublon de ce besoin identifié ; attribution DEM-007.

Document enregistré seul dans `worktree/devops`, sur `layers/devops`, après lecture
des instructions, des couches et des README applicables. État Git propre avant
écriture ; DEM-006 et ses implémentations sont déjà commitées, dernier commit
observé `a001fa1`. Leur contenu est préservé. L’état des couches relevé pendant
l’interview est une observation datée et devra être revérifié avant toute action.

## Implémentation partielle — 2026-10-27

Cadrage et cartes : `e7e0c4f`. OPS-055 réalisée, preuve dans le
[rapport d’audit](../resources/audit-contenu-local-007.md) : six arbres parcourus,
dix caches sans source, contenus utiles préservés, deux familles de dossiers vides
à expliquer. Aucun nettoyage. L’absence de modification est observée par deux
relevés consécutifs de métadonnées, avec les limites décrites dans le rapport.

OPS-056 reste bloquée par l’arbitrage humain et sa trace commitée en consolidation.
OPS-057 reste bloquée par ce même arbitrage, le contrôle commité et validé et la
coordination des cibles. Le cadrage général ne remplace pas cet arbitrage. Aucun
contrôle affaibli ni nouveau contrôle implémenté. Demande non terminée ; aucune
validation humaine du résultat, livraison ou étape de consolidation déclenchée.

## Vérification humaine et reconstitution — 2026-10-27

Validation explicite « oui » de l’audit OPS-055 seul, au commit
`804459950e226d125736dfb07f71e94b40c1193b`, avec ses limites présentées.
Aucune correction demandée. OPS-056 et OPS-057 ne sont pas implémentées ni validées.
DEM-007 n’est donc pas entièrement validée.

L’invocation de reconstitution est examinée après ce verdict. La liste complète
des contributions validées manque : OPS-056 et OPS-057 restent bloquées par les
prérequis documentés. Aucune réunion partielle présentée comme complète ; branche
`demands/DEM-007` et worktree `worktree/DEM-007` non créés à cette étape.
Aucun contrôle de l’ensemble ni livraison annoncé ; aucune étape suivante lancée.

## Nettoyage ponctuel réalisé — 2026-10-27

Dix fichiers `.pyc` listés dans l’audit ont été revérifiés : sources absentes,
fichiers et parents directs non symboliques, en-tête CPython 3.12 reconnu.
Les dix fichiers sont supprimés, puis leurs seuls parents devenus vides.
`scripts/` et `tests/` ont ainsi disparu du principal ; `infra/` est conservé dans
chaque couche, seuls ses anciens `__pycache__/` vides sont retirés.
Les caches des sources encore présentes, dépendances, données, environnements,
`.agents/` et `.aws/` restent intacts. Aucun fichier suivi supprimé.
Les suppressions sont locales : Git ne versionnait pas ces caches.
L’audit initial est conservé comme preuve avant nettoyage, et non comme état actuel.

## Validation du périmètre corrigé — 2026-10-27

L’humain confirme « c’est validé » pour le nettoyage présenté au commit
`9b10d96`, après validation de l’audit `8044599`. OPS-055 et OPS-057 sont validées ;
OPS-056 est sans suite. Cette décision remplace les anciens blocages de
consolidation, abandonnés avec l’extension de périmètre. Reconstitution autorisée
sur `demands/DEM-007` dans `worktree/DEM-007`, depuis le develop local `98932aa`.

## Preuve de reconstitution — 2026-10-27

Branche `demands/DEM-007`, worktree `worktree/DEM-007`, créée depuis le develop
local `98932aa`. Merge sans conflit de `layers/devops` au commit `865d1da` ;
commit de réunion `c277f063e9ccaf7c2d6387171852794f6977963c`.
Ascendance vérifiée pour `e7e0c4f`, `8044599`, `0729ff4`, `9b10d96` et `865d1da`.
Aucun fichier non commité copié. Diff face à develop limité aux cinq documents
DEM-007 ; les contributions DEM-006 de develop sont préservées.

Vérifications : `git diff develop --check`, liens locaux des cinq documents et
ascendance des SHA acceptés réussis. Le changement réuni est documentaire ; aucun
code applicatif ou contrôle modifié, aucune preview ni test applicatif exécuté.
Les suppressions de caches sont des opérations locales déjà réalisées et validées,
non des suppressions Git à propager. Aucun push, PR, fusion vers develop ni
réalignement de couche effectué. Contrôles de livraison restant à exécuter à cette étape.

## Préparation de livraison — 2026-10-27

Qualité exécutée avec succès sur la branche réunie `771da3d` :
`python3 codebase-integrity/scripts/quality.py --root <depot>/worktree/devops`.
23 tests d’outillage, test du contrat API, lint du conteneur, validation du schéma,
comparaison OpenAPI, typecheck et build web/backoffice réussis (code retour 0).
Les dépendances applicatives sont celles de devops ; égalité du code `app/` avec
la branche réunie vérifiée par `git diff --exit-code layers/devops HEAD -- app`.
Les contrôles d’outillage proviennent du worktree de réunion. Parcours navigateur
prévus par la CI GitHub ; leur résultat sera vérifié avant fusion.

Principal et cinq couches propres, sans mission concurrente observée ; toutes
leurs têtes sont ancêtres de la réunion. Aucun commit étranger à rattacher.
Le distant develop observé est `98932aa154eb92f82b9b8583d72c67fe5e154959`.
Le diff à livrer se limite aux cinq documents DEM-007. Les caches supprimés
étaient ignorés : la PR conserve la preuve du nettoyage, sans suppression Git.
Fusion prévue par merge commit, puis avances rapides et suppression de la seule
branche temporaire DEM-007 ; worktrees et fichiers locaux conservés.
