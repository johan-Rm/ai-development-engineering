# OPS-052 — Mettre à disposition et vérifier les cinq stacks

- État : implémentée et commitée, à vérifier.
- Date : 2026-10-26.
- Demande d’origine : [DEM-005](../demand/DEM-005-dockeriser-applications-worktrees.md).
- Couche : devops.
- Session : référence de session indisponible ; mission confiée dans ce chat.
- Worktree : `worktree/devops`, relatif à la racine du dépôt principal.
- Branche : `layers/devops` ; conserver la branche existante, sans rebase.

Le chemin absolu du worktree sera résolu et vérifié avant exécution. Au découpage, les liens Git
obsolètes empêchaient les commandes ordinaires ; le découpage avait vérifié
la branche et l’état via le gitdir réel. Lire les README applicables avant toute écriture.

## Objectif et chemins autorisés

Rendre la stack disponible aux cinq couches par commits identifiés, puis prouver son
fonctionnement dans les cinq worktrees successivement et dans deux simultanément.
Rédaction et coordination depuis devops : cette carte, la demande, runbooks de recette
et preuves sous `dev-book/`, corrections documentaires sous `infra/` et `SETUP.md`.
Les autres worktrees sont uniquement des destinations d’application des commits autorisés
et d’exécution de la recette ; aucune copie de fichiers non commités ni écriture de tâche
sur develop. Une correction technique relève d’OPS-051 ou d’une carte complémentaire adaptée.

## Dépendances par commit

OPS-050 : `b041cab9031eee89d7cd40e8c2b7a90bbeb17a7c`.
OPS-051 : `d076aecd78c7bfe110758ef35055b42e0af35084` et correction documentaire
`ec0e27bd1b8e19bddf073139fcc6b95ede035136`, puis correction du cas sans `.env`
`c70975474d656c74fb3f88ec7419953221a38922`. Ces commits sont présents sur devops ;
leurs tests et preuves techniques passent, sans préjuger du verdict humain.
L’implémentation de DEM-005 confiée dans ce chat inclut leur mise à disposition locale
par commits dans les cinq couches, sans push, rebase ou merge.
Préparer les cinq branches seulement après vérification de disponibilité, de leurs états et
compatibilités ; préserver tout travail. Ne pas avancer arbitrairement les branches vers
la branche devops divergente. Un conflit ou une dépendance historique non cadrée bloque
la destination concernée jusqu’à résolution explicite.

## Critères d’acceptation

- Les cinq worktrees utilisent le même contenu autorisé de stack, issu des commits
  identifiés ; leurs applications sont celles de leur propre branche.
- Vérifier chacun à tour de rôle : domaines locaux, sélection web ou backoffice et option
  deux interfaces, lecture web et CRUD backoffice/API, code rechargé automatiquement.
- Observer une base neuve vide et migrée puis la conservation des articles après arrêt/relance.
- Faire tourner deux stacks ensemble : observer ports/domaines distincts, projets, réseaux,
  volumes, montages, dépendances et caches/builds distincts ; les articles restent propres
  à leur stack et une modification de code n’affecte que son worktree.
- Vérifier que les `.env`, données, services préexistants et fichiers locaux sont préservés,
  et que les fichiers générés restent utilisables par l’utilisateur de l’hôte.
- Restituer l’état final des services et ressources de test ; ne pas supprimer des volumes
  préexistants ni présenter une configuration seule comme preuve de fonctionnement.

## Tests, documentation et preuve

Consigner la matrice des cinq worktrees, branches, SHA consommés, URLs et résultats,
les observations navigateur, requêtes CRUD, montages et destinations d’écriture, rechargement,
isolation et persistance. Les données de preuve sont temporaires et identifiées ; préserver
les données étrangères au test. Vérifier l’accès réel au moteur Docker avant la recette.
Exécuter `python3 codebase-integrity/scripts/quality.py` et les tests propres à la stack ;
ne pas affaiblir les contrôles en cas d’échec. Documenter les limites et le verdict technique,
sans inventer le verdict humain de l’étape de vérification.

## Exclusions

Aucun déploiement, merge, push, PR ni suppression de worktree ; aucune stack develop.
Les autorisations Git nécessaires ne sont pas acquises par l’invocation du découpage.

## Réalisation et preuves

Recette réalisée le 2026-10-26, sans verdict humain de validation.

## Distribution locale — 2026-10-26

Les quatre branches consommatrices étaient propres et aucune mission concurrente en
cours n’a été trouvée dans leurs cartes. Les branches existantes ont été conservées,
sans rebase ni réunion avec l’historique divergent de devops. Application par cherry-pick
des seuls commits ci-dessous, sans conflit ni copie de travail non commité.
Les quatre couches ont la même base et ont reçu les mêmes commits résultants.
Les patch-id stables des quatre paires source/copie sont identiques.

| Carte | Commit source devops | Commit consommé par API, web, backoffice et design |
| --- | --- | --- |
| OPS-050 | `b041cab9031eee89d7cd40e8c2b7a90bbeb17a7c` | `cba710e9dc4074b774e8b8ba51b6662e407988f9` |
| OPS-051 | `d076aecd78c7bfe110758ef35055b42e0af35084` | `3e46eceaeba6701ac095423bb3ae35e8f61948a1` |
| OPS-051, chapitres README | `ec0e27bd1b8e19bddf073139fcc6b95ede035136` | `3f1de3a986d19cae02da4c5a491410a1425b328b` |
| OPS-051, absence de .env | `c70975474d656c74fb3f88ec7419953221a38922` | `0a0c512312547930f66ca7038010478628e4f515` |

Le contenu des fichiers `infra/` est identique dans les cinq couches. Les différences
historiques d’instructions, documentation ou workflow ne sont pas reprises par ces patches.
La présente preuve documentaire et la demande actualisée sont également destinées aux
quatre branches par le seul commit OPS-052, sans changement de code supplémentaire.

## Matrice de recette réelle — 2026-10-26

Version PHP observée : 8.4.27 ; Node : v22.23.4. Les cinq couches ont été vérifiées
successivement sur la version corrigée sans montage `.env`, en arrêtant chaque stack
avant la suivante. Devops a aussi vérifié les trois modes web/backoffice/both séparément.

| Couche | Branche | Port | Articles au premier contrôle | CRUD navigateur + lecture web | Rechargement web/BO/PHP | Persistance après arrêt/relance |
| --- | --- | --- | --- | --- | --- | --- |
| devops | `layers/devops` | 19304 | 0 | réussi | réussi | réussie |
| api | `layers/api` | 19302 | 0 | réussi | réussi | réussie |
| web | `layers/web` | 19303 | 0 | réussi | réussi | réussie |
| backoffice | `layers/backoffice` | 19301 | 0 | réussi | réussi | réussie |
| design | `layers/design` | 19305 | 0 | réussi | réussi | réussie |

Pour chaque couche :

- `python3 infra/apps.py up --interface both` a démarré sa stack ;
- `python3 infra/browser.py --reload` a créé/modifié/supprimé son article via le
  backoffice et vérifié la lecture réelle dans le web, puis observé le rechargement
  automatique des deux interfaces et de PHP, sans redémarrage ;
- `python3 infra/test-runtime.py --expect-empty` a vérifié la base vide, les montages
  du bon worktree en lecture seule, les utilisateurs 1000:1000, les volumes privés,
  l’absence de fichiers générés root et la conservation d’un article après arrêt/relance ;
- les `.env` observés ont gardé leurs empreintes, les trois fichiers temporairement
  modifiés ont été restaurés exactement et le diff applicatif initial a été conservé ;
- les seuls articles créés par les recettes ont été supprimés, puis `down` a arrêté
  cette stack en conservant ses volumes avant le passage à la couche suivante.

## Deux stacks simultanées

Les stacks API et web ont ensuite tourné ensemble sur 19302 et 19303. Observation
Docker : projets `aide-app-ec4e123090-api` et `aide-app-ec4e123090-web`, chacun avec
son réseau `_default` et neuf volumes privés. Aucun volume, réseau ou port commun.
Les montages `/app` visent respectivement `worktree/api/app/` et `worktree/web/app/`.
Les seuls ports publiés sont ceux de Caddy, liés à `127.0.0.1`.

Un article distinct a été créé dans chaque API : chacune n’expose que son article.
Une modification temporaire du composant web de la couche API est apparue dans le HTML
servi sur `web.wt-api.localhost:19302` et est restée absente sur
`web.wt-web.localhost:19303` ; l’empreinte du fichier de la couche web n’a pas changé.
Les octets du fichier modifié ont été restaurés et les deux articles supprimés.
Les deux recettes Chromium ont ensuite repassé le CRUD et la lecture, pendant que
les deux stacks restaient actives. Elles ont aussi supprimé leurs articles de preuve.

## Contrôles, documentation et limites

- `python3 infra/test_apps.py` : 9 tests réussis, incluant les 15 résolutions Compose
  et les régressions de port TIME_WAIT, montages limités et démarrage sans `.env`.
- `python3 codebase-integrity/scripts/check.py` : 23 tests réussis.
- `python3 codebase-integrity/scripts/quality.py` : code 0 ; outillage, contrat API,
  lint Symfony, mapping Doctrine, comparaison OpenAPI, types et builds des deux interfaces.
  Les applications et les contrôles sont inchangés ; aucune règle affaiblie.
- Syntaxes Python/shell/JavaScript et `git diff --check` vérifiés.
- [Runbook quotidien](../runbooks/stacks-applicatives.md) et
  [recette reproductible](../runbooks/recette-stacks-applicatives.md) disponibles.

Les tests localhost et Docker ont nécessité l’exécution autorisée hors sandbox.
La recette navigateur utilise une image construite depuis le Dockerfile inspectable du
dépôt et uniquement les montages ciblés, après rejet automatique de l’essai de montage
large dans une image locale. Aucun changement de paquets système hôte n’a été nécessaire.
Les tags d’images ne sont pas des digests immuables ; le lanceur de recette Chromium
utilise le réseau hôte Linux. Aucun déploiement, service métier de cap-nour ou stack develop.

## Preuves et état final

Les preuves durables sont la matrice et les observations ci-dessus. Les artefacts locaux
complémentaires sont `/tmp/DEM-005-runtime-<couche>.json`,
`/tmp/DEM-005-browser-<couche>.log`, `/tmp/DEM-005-browser-dual-{api,web}.log`,
`/tmp/DEM-005-isolation.json`, `/tmp/DEM-005-distribution.json`,
`/tmp/DEM-005-tests-stack.log`, `/tmp/DEM-005-quality-final.log` et les captures sous
`/tmp/DEM-005-browser-artifacts/`. La procédure durable permet de rejouer la recette
sans dépendre des scripts temporaires ayant orchestré ces passages.

API et web restent actives avec leurs deux interfaces pour la vérification humaine.
Backoffice, design et devops sont arrêtées ; leurs volumes et dépendances restent présents.
Les bases Docker sont revenues à zéro article après suppression des seules données de preuve.
Le conteneur MySQL préexistant `kazen_garden_db` reste actif sur son port initial 3307 ;
aucun de ses services, volumes ou données n’a été modifié par cette mission.
Les liens des seuls cinq worktrees demandés sont réparés ; les anciens arbres DEM-002/003
hors périmètre restent inchangés. `develop` reste à
`aa8b856587058a5f71ec35c13d3cd319fb58b1ce`, sans modification de tâche.
Aucune branche de réunion créée, aucun push, PR, merge ou fetch. Les divergences
historiques des branches sont conservées et restent à traiter selon les autorisations
ultérieures de reconstitution/livraison. Les trois cartes restent à vérifier par l’humain.
Le SHA du commit documentaire OPS-052 se lit dans son historique et dans le bilan final.
