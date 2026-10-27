# DEM-007 — Vérifier la conformité du contenu local des couches

- Date : 2026-10-27.
- État : cadrage confirmé ; découpée, missions bloquées par leurs prérequis.
- Référence de session : référence de session indisponible.
- Carte externe : aucune fournie.

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
