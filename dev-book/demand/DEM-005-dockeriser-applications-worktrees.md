# DEM-005 — Dockeriser les applications dans les cinq worktrees

- Date : 2026-10-26.
- État : implémentée et commitée, à vérifier — commandes Docker contextualisées et guide des couches.
- Confirmation humaine : « confirmé », le 2026-10-26, après restitution du cadrage dans le chat.
- Session : référence de session indisponible.
- Carte externe : aucune.
- Couche de rédaction : devops ; worktree `worktree/devops`, branche `layers/devops`.

## Contexte et problème observé

Les conteneurs BusyBox d’OPS-021 vérifient la mécanique d’isolation AIDE, mais ne
servent pas les applications. L’API Symfony/API Platform, le web et le backoffice
Nuxt se lancent actuellement sur l’hôte. L’humain et les agents doivent pouvoir
lancer et vérifier les applications d’une branche sans perturber une autre couche.

Les cinq worktrees existent sur disque, mais leurs liens Git référencent encore
l’ancien chemin du dépôt. Leur remise en état est nécessaire avant leur utilisation.

Le projet cap-nour sert de référence locale : `docker-compose.dev.yml` et
`dev-book/tasks/OPS-003-une-stack-docker-par-worktree.md` dans ce projet décrivent
une stack par worktree, des domaines locaux derrière Caddy et le démarrage sélectif
des interfaces. Ses services métier et sa configuration de production ne sont pas
à recopier. La référence sera résolue localement, sans chemin personnel versionné.

## Utilisateurs et résultat attendu

L’humain consulte et vérifie dans le navigateur le résultat d’une branche ; les agents
disposent de commandes reproductibles pour démarrer les services et produire les preuves.

Chacun des cinq worktrees API, web, backoffice, design et devops dispose d’une stack
autonome pouvant servir l’API, le web et le backoffice depuis son propre code.
Design et devops peuvent ainsi lancer les applications pour leurs vérifications.

## Décisions humaines et comportement attendu

- Une stack autonome par worktree, avec ses dépendances et données ; aucune API partagée
  entre couches.
- Caddy fournit des domaines locaux par worktree et un port propre à chaque stack,
  par exemple `web.wt-api.localhost` et `backoffice.wt-api.localhost`.
- Une commande exécutée depuis le worktree lance l’API et l’interface choisie ; une
  option permet de lancer les deux interfaces. Le code se recharge automatiquement.
- SQLite est conservée : base persistante isolée par worktree, vide au premier
  lancement, avec le schéma nécessaire ; aucun jeu de données injecté automatiquement.
- La remise en état des cinq worktrees sous le chemin actuel appartient à cette demande,
  en préservant branches, modifications et fichiers locaux existants.
- Les cinq stacks sont testées à tour de rôle, puis deux simultanément.

## Contraintes

Isoler ports, réseaux, bases, volumes, dépendances, caches et fichiers générés.
Les montages et destinations d’écriture doivent viser le worktree concerné.
Préserver les `.env`, les services préexistants et le travail local ; éviter les fichiers
générés appartenant à root sur l’hôte. Les domaines et ports sont destinés à l’accès local.
Les ports exacts seront choisis après vérification des disponibilités et collisions locales.

Respecter les procédures AIDE, les périmètres par couche et les dépendances par commits
identifiés. Aucun transfert de travail non commité entre missions. La confirmation du
besoin ne vaut ni validation du résultat ni autorisation de commit, push, PR ou merge.

## Critères observables et preuves attendues

1. Les cinq worktrees sont utilisables sous le chemin actuel sur leurs branches
   `layers/<couche>`, sans perte de travail, de fichiers locaux ou de données existantes.
2. Depuis chacun, les commandes documentées préparent et lancent l’API avec l’interface
   choisie ; l’option deux interfaces fonctionne. Les montages correspondent à sa branche.
3. Les domaines Caddy donnent accès aux applications ; la lecture et le CRUD des articles
   fonctionnent via les interfaces et l’API selon leurs capacités existantes.
4. Une modification de code dans le worktree est visible par rechargement automatique.
5. Deux stacks fonctionnent simultanément : ports, domaines, ressources Docker et
   destinations d’écriture sont distincts. Les articles créés dans l’une n’apparaissent
   pas dans l’autre ; les caches et builds ne s’écrasent pas.
6. L’arrêt puis la relance conservent les données de chaque stack. Le premier lancement
   d’une nouvelle base présente une collection vide et un schéma opérationnel.
7. Les `.env` et fichiers locaux préexistants sont préservés ; les écritures générées
   sur l’hôte restent utilisables par son utilisateur.
8. Les preuves consignent les cinq stacks vérifiées successivement et deux simultanément :
   accès navigateur, CRUD, rechargement, isolation et persistance. La résolution Compose
   seule ne constitue pas une preuve de fonctionnement.

Les tests pertinents accompagnent l’implémentation. Les contrôles du projet à prendre
en compte sont `python3 codebase-integrity/scripts/check.py` pour l’outillage et
`python3 codebase-integrity/scripts/quality.py` pour la qualité avant PR.
L’accès au moteur Docker était refusé dans la session de diagnostic ; son accès effectif
devra être vérifié pour produire les preuves d’exécution, sans annoncer de services actifs
sur la seule base de la configuration.

## Documentation concernée

Mettre à jour les README d’infrastructure et des applications concernés, ainsi que les
guides d’installation et de travail par couche pertinents. Documenter les prérequis,
la préparation des worktrees, les adresses, le choix des interfaces, les commandes
de démarrage et d’arrêt, la persistance et les limites. Les procédures reproductibles
et preuves ont leur place dans le dev-book. Actualiser les règles locales concernées
si elles changent, avec leurs contrôles pertinents.

## Exclusions

- Production, préproduction, déploiement distant et domaines publics.
- Stack supplémentaire sur `develop`.
- Migration vers PostgreSQL, services métier de cap-nour et données de démonstration.
- Évolution fonctionnelle des applications ou ajout d’authentification.
- Suppression de worktree, écrasement de `.env` ou remise à zéro des données existantes.

## Questions ouvertes et choix d’implémentation

Aucune question de besoin ouverte. Choix réalisés : ports 19301 à 19305 suivant les
identifiants des couches, lanceur `infra/apps.py`, images PHP 8.4 et Node 22 avec les
locks existants, Caddy local et SQLite dans des volumes privés. Les liens Git ont été
réparés avec `git worktree repair`. Les runbooks détaillent les commandes et ressources.
Les cinq stacks et leur isolation ont été observées, sans changement de périmètre.

## Tâches issues du découpage

Découpage du 2026-10-26, sans implémentation ni commit.

| Ordre | Carte | Critères DEM-005 couverts | Dépendances et état |
| --- | --- | --- | --- |
| 1 | [OPS-050 — Réparer les liens Git](../tasks/OPS-050-reparer-liens-worktrees.md) | 1, 7 | Implémentée et commitée : `b041cab`, à vérifier |
| 2 | [OPS-051 — Stack applicative commune](../tasks/OPS-051-stack-applicative-worktree.md) | 2 à 7, documentation | Correction Make directe implémentée et commitée : `a46ac38`, à vérifier |
| 3 | [OPS-052 — Recette des cinq stacks](../tasks/OPS-052-recette-cinq-stacks.md) | 1 à 8, preuves finales | Implémentée et commitée, à vérifier ; dépendances et copies identifiées dans la carte |

Les trois cartes sont séquentielles et relèvent de devops. Aucune mission d’écriture
applicative ni délégation n’est créée. Les Dockerfiles, le lanceur et leurs tests propres
sont prévus sous `infra/` ; aucun changement du Codebase Integrity n’est autorisé.

## Réunion prévue

Branche dédiée : `demands/DEM-005` ; worktree prévu : `worktree/DEM-005`, relatif
à la racine du dépôt principal. Création à la reconstitution uniquement, depuis une base
locale explicitement identifiée à cette étape ; aucune branche de couche ne sert de réunion.
Réunir uniquement les commits autorisés de la demande, sans différences historiques hors périmètre.

## État des branches au découpage

Observation locale, sans fetch, sans promesse de synchronisation distante. Les chemins
absolus ont été résolus sous le dépôt principal et les états vérifiés au moyen des gitdirs
réels, car les liens ordinaires pointent encore vers l’ancien emplacement.

| Worktree | Branche | HEAD observé | État |
| --- | --- | --- | --- |
| `worktree/devops` | `layers/devops` | `ffd216fb6997f8e8e78a4e89b153c8b02653a780` | DEM-005 non suivie avant découpage ; aucune mission concurrente en cours repérée |
| `worktree/api` | `layers/api` | `6477c51f6428bccdd81c08be20edf644e94fee31` | Propre, lien Git cassé |
| `worktree/web` | `layers/web` | `6477c51f6428bccdd81c08be20edf644e94fee31` | Propre, lien Git cassé |
| `worktree/backoffice` | `layers/backoffice` | `6477c51f6428bccdd81c08be20edf644e94fee31` | Propre, lien Git cassé |
| `worktree/design` | `layers/design` | `6477c51f6428bccdd81c08be20edf644e94fee31` | Propre, lien Git cassé |

Branches existantes conservées, aucune créée ou déplacée. Elles ne sont pas annoncées
comme préparées pour la recette : OPS-050 doit réparer les liens, puis OPS-052 vérifier
la disponibilité de chaque couche et les commits consommables. La disponibilité ne se
déduit pas de la seule propreté Git. `develop` observée à
`aa8b856587058a5f71ec35c13d3cd319fb58b1ce` reste inchangée. Sa divergence avec
`layers/devops` est de 1 commit côté develop et 25 côté devops ; aucun rebase ni merge
implicite. La base commune est `7c35e0292f2cd3b2e5f2e46a5864a086ae5dd85d`.

Au découpage, les dépendances futures sans SHA restaient volontairement non résolues ;
aucune copie de travail non commité ne pouvait les remplacer. Elles ont ensuite été
réalisées et commitées pendant l’implémentation confiée, selon le bilan ci-dessous.


## Bilan d’implémentation — 2026-10-26

Les trois cartes sont implémentées et commitées avant vérification humaine. Les huit
critères sont couverts par les preuves d’OPS-050/051/052 : cinq liens Git réparés,
cinq stacks autonomes réellement testées successivement et deux simultanément,
CRUD navigateur, lecture web, rechargement automatique, isolation et persistance.
Les bases Docker étaient vides au premier contrôle et sont revenues à zéro article
après les recettes ; les `.env` et le travail local ont été préservés.

Les commits propres à la demande ont été appliqués aux quatre autres couches par
cherry-pick identifié, sans reprendre l’historique divergent de devops. La table des
SHA source/consommateur est dans OPS-052 ; le contenu de stack est identique partout.
Les neuf tests de stack et la qualité complète existante passent, sans changement
des applications, de leurs locks ou du Codebase Integrity.

Les [commandes quotidiennes](../../docs/02-cadre/couches/dockerisation.md) et la
[procédure de recette](../runbooks/recette-stacks-applicatives.md) sont documentées.
Les stacks API et web restent disponibles sur les ports 19302 et 19303 avec leurs
deux interfaces ; les trois autres sont arrêtées, leurs volumes conservés.
Aucun push, PR, merge, fetch ou début de reconstitution. La branche et le worktree
de réunion restent seulement prévus. Aucun verdict humain n’est déduit des tests.


## Verdict humain — 2026-10-27

Après présentation des trois cartes, l’humain répond « je demande des corrections »,
puis demande des commandes `make` pour piloter la stack « à la place de python3 ».
La demande n’est pas validée sur les SHA présentés : OPS-050 `b041cab`,
OPS-051 `d076aec`, `ec0e27b`, `c709754` et OPS-052 `61797d6`.

La correction porte sur l’interface de commande d’OPS-051 : fournir des cibles Make
pour préparer, démarrer (web, backoffice ou les deux), afficher les informations et
l’état, arrêter la stack et lancer ses recettes/tests. Les commandes à saisir et la
documentation doivent utiliser `make` ; les scripts Python peuvent rester internes.
Cette demande ne requiert pas de réécrire le lanceur dans un autre langage ni de
modifier les contrôles du Codebase Integrity. Le Makefile racine rejoint le périmètre
explicitement demandé pour cette correction ; les noms exacts des cibles seront
choisis à l’implémentation et documentés avec les paramètres d’interface.

OPS-051 retourne à l’implémentation et produira de nouveaux commits avec ses preuves.
OPS-052 devra vérifier et documenter ces commandes Make dans les cinq couches après
identification des nouveaux commits. OPS-050 reste sans verdict favorable explicite ;
aucune validation partielle n’est déduite de l’absence de correction à son sujet.
Les preuves du 2026-10-26 restent historiques. La présente étape ne modifie pas le code,
ne relance pas les services et n’enchaîne pas automatiquement l’implémentation.


## Précision humaine et correction d’implémentation — 2026-10-27

L’humain précise ensuite que Make doit appeler directement les commandes Docker,
puis demande « supprime python du pilotage » et invoque `implementer-demande` pour
DEM-005. Cette précision remplace la possibilité de garder un lanceur Python interne.
Le Makefile porte les actions Docker Compose ; le contexte de couche est préparé en
shell avec Git et le parseur JSON standard de Perl. Aucun lanceur Python ne participe
au pilotage applicatif, y compris indirectement. Les outils du cadre hors de cette
stack restent hors périmètre et inchangés.

Les cibles prévues sont `help`, `info`, `config`, `prepare`, `up`, `status`, `down`,
`test`, `test-browser` et `test-runtime`. `INTERFACE=web|backoffice|both` sélectionne
les interfaces. Les recettes navigateur utilisent Docker et les assertions de
persistance utilisent Node ; elles ne réintroduisent pas Python dans le pilotage.
L’identité des projets, ports et volumes existants doit être conservée.


## Bilan de correction — 2026-10-27

Python est supprimé du pilotage applicatif. Le Makefile appelle directement Docker
Compose ; le contexte Git et JSON est préparé en shell avec Perl/JSON::PP.
`make up`, `make status`, `make down`, `make prepare` et les recettes
Make remplacent les anciens appels. Les quatre scripts Python propres à cette stack
sont supprimés ; les outils du cadre hors pilotage Docker sont inchangés.

OPS-051 est corrigée dans `a46ac38f1445fb98d81bd30b076f22a67c2b1503` et distribuée par commits identifiés.
OPS-052 a vérifié les cinq couches successivement puis API/web simultanément, avec
CRUD navigateur, rechargement, isolation et persistance. Les mêmes noms de projets,
ports et volumes sont réutilisés, sans perte des données ou fichiers locaux.
Les sept groupes de contrôles Make et la qualité complète passent ; les commandes
et prérequis sont documentés. Les tables de SHA et preuves sont dans OPS-052.

Les corrections retournent à la vérification humaine ; aucun verdict favorable n’est
présumé, y compris pour OPS-050 qui reste sans validation explicite. Aucune opération
distante de livraison ou de réunion n’a été engagée. API et web restent consultables
sur 19302 et 19303 avec les deux interfaces ; les autres stacks sont arrêtées.

## Corrections complémentaires demandées

L’humain réserve `dev-book/runbooks/` aux mesures exceptionnelles lors des déploiements.
Les guides locaux de DEM-005 rejoignent `docs/02-cadre/`. Il demande également
le démarrage d’une couche sans `cd` et sans `make -C` : les cibles courtes
`make api|web|backoffice|design|devops`, `make stop-<couche>` et
`make status-<couche>` sont ajoutées au Makefile porté par OPS-051.
Elles seront accessibles depuis la racine principale après intégration du Makefile.
Ces corrections restent à vérifier ; les précédentes preuves ne constituent pas
une validation humaine de cette version.

## Corrections humaines lors de la vérification des raccourcis

L’humain indique : « les noms de commandes manque de contexte » à propos de
`make api`, `make web`, `make backoffice`, `make design` et `make devops`.
Remplacer ces noms par des commandes exprimant explicitement le pilotage Docker
local des couches, et appliquer ce vocabulaire au démarrage, à l’arrêt et à l’état.

L’humain refuse également le placement des trois fichiers dans `docs/02-cadre/` :
« tu dois laisser les 2 autres qui ne concernent pas cette tache ».
Conserver `recette-stacks-applicatives.md` et `reparer-liens-worktrees.md` à leurs
emplacements d’origine dans `dev-book/runbooks/`, en annulant leurs déplacements
sans perdre leur contenu. La correction de structure porte sur le guide d’usage.
Transformer `docs/02-cadre/couches.md` en sous-dossier `docs/02-cadre/couches/`,
conserver le contenu général des couches dans son point d’entrée et y ranger
un guide pour utiliser la dockerisation locale des couches. Mettre à jour les liens
concernés sans étendre la réorganisation aux deux autres procédures.

Version examinée : HEAD `df5ac29`, avec corrections non commitées des raccourcis
et de la documentation. Aucun SHA nouveau ne correspond à cette version de travail.
Verdict : corrections demandées ; aucune validation globale ou partielle acquise.
Retour à l’implémentation, sans modification de code ni déplacement supplémentaire
pendant cette vérification.

Précision humaine sur le nom du guide : utiliser
`docs/02-cadre/couches/dockerisation.md`, et non `dockerisation-locale.md`.
Le contenu reste consacré à l’environnement de développement local des couches.

## Résultat de la correction de contexte

Les cibles retenues sont `docker-up-<couche>`, `docker-stop-<couche>` et
`docker-status-<couche>`. Le guide est `docs/02-cadre/couches/dockerisation.md` ;
le contenu général des couches est conservé dans `docs/02-cadre/couches/index.md`.
Les deux autres procédures restent à leurs emplacements d’origine. Les tests Make
et la qualité complète passent. La correction est préparée sur `layers/devops`,
puis OPS-052 vérifie et référence son commit dans les cinq couches.
Aucun verdict humain favorable acquis ; la demande reste à vérifier.

## Bilan des dernières corrections

OPS-051 est commitée dans `8c1482eb1d1025e18b3f2b67ec592751f886da0c` et appliquée
aux quatre autres couches par commits identifiés (table dans OPS-052). Les noms
Docker contextualisés et le guide `couches/dockerisation.md` sont en place dans
les cinq worktrees. Les deux autres procédures sont conservées à leur emplacement
initial, sans modification de contenu.

OPS-052 a vérifié les nouveaux raccourcis sur les cinq couches successivement :
démarrage, état, HTTP 200 sur les deux interfaces et arrêt. API/web fonctionnent
ensuite ensemble, avec quatre accès HTTP à 200. Les tests Make et la qualité complète
passent ; les env et les fichiers applicatifs sont préservés. Les commandes courtes
depuis la racine principale seront disponibles après intégration du Makefile.
Les trois cartes restent sans validation humaine ; DEM-005 est à vérifier.
