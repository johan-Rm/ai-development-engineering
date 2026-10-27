# DEM-005 — Dockeriser les applications dans les cinq worktrees

- Date : 2026-10-26.
- État : correction Make en cours ; non validée.
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
| 2 | [OPS-051 — Stack applicative commune](../tasks/OPS-051-stack-applicative-worktree.md) | 2 à 7, documentation | Implémentée et commitée : `d076aec`, `ec0e27b`, `c709754`, à vérifier |
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

Les [commandes quotidiennes](../runbooks/stacks-applicatives.md) et la
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
