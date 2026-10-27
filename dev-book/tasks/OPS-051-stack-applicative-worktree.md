# OPS-051 — Fournir la stack applicative autonome par worktree

- État : implémentée et commitée, à vérifier — correction Make directe.
- Date : 2026-10-26.
- Demande d’origine : [DEM-005](../demand/DEM-005-dockeriser-applications-worktrees.md).
- Couche : devops.
- Session : référence de session indisponible ; mission confiée dans ce chat.
- Worktree : `worktree/devops`, relatif à la racine du dépôt principal.
- Branche : `layers/devops` ; conserver la branche existante, sans rebase.

Le chemin absolu du worktree sera résolu et vérifié avant exécution. Les liens Git
obsolètes empêchent actuellement les commandes ordinaires ; le découpage a vérifié
la branche et l’état via le gitdir réel. Lire les README applicables avant toute écriture.

## Objectif et chemins autorisés

Fournir une stack locale réutilisable dans chacun des cinq worktrees, inspirée de cap-nour.
Chemins autorisés : `infra/` (Compose, Dockerfiles, Caddy, lanceur, configuration et tests
propres à la stack), `SETUP.md`, `docs/02-cadre/couches.md`, `dev-book/runbooks/`
(procédures de cette stack), cette carte et la demande pour les liens et preuves.
Placer les Dockerfiles et les tests de la stack dans `infra/`, sans modifier les applications.
Lire les README des applications pour respecter les runtimes et contrats existants.

## Dépendances par commit

OPS-050 : `b041cab9031eee89d7cd40e8c2b7a90bbeb17a7c`, présent dans la branche ;
liens réparés et commandes Git ordinaires vérifiées dans les cinq worktrees.
Base observée de devops : `ffd216fb6997f8e8e78a4e89b153c8b02653a780`.
Comparer le contenu utile avec `develop` (`aa8b856587058a5f71ec35c13d3cd319fb58b1ce`)
avant exécution : divergence observée de 1 commit côté develop et 25 côté devops.
Ne pas réintroduire dans la demande les différences historiques de workflow hors périmètre.

## Critères d’acceptation

- Une commande depuis le worktree démarre API et interface choisie ; une option lance
  web et backoffice ensemble. Fournir préparation, état/adresses et arrêt conservant les données.
- API compatible PHP >= 8.4, extensions SQLite/PDO et dépendances Composer verrouillées ;
  interfaces compatibles Node >= 22.12 et installation npm verrouillée.
- Caddy route des domaines locaux propres au worktree vers les services ; le proxy Nuxt
  utilise l’API de sa stack. Les ports publiés restent sur la boucle locale.
- Identifier les projets par dépôt et couche ; isoler réseaux, données SQLite persistantes,
  dépendances, caches et builds. Les montages source visent exclusivement le worktree appelant.
- Choisir et documenter les ports après recherche des collisions ; une collision doit produire
  un diagnostic exploitable sans arrêter un service tiers.
- Une base neuve est migrée et vide ; arrêt/relance la préservent. Aucun `.env` existant
  n’est remplacé, aucun secret n’est copié implicitement. Éviter les sorties root sur l’hôte.
- Les modifications du code sont prises en compte automatiquement, y compris pour Nuxt.
- La recette BusyBox reste distincte ; aucun changement des conventions ou contrôles
  du Codebase Integrity n’est requis pour cette stack.

## Tests, documentation et preuve

Résolution Compose pour les cinq identités et modes web/backoffice/deux interfaces ;
contrôles ciblés du lanceur sur mauvais worktree/branche, collisions et préservation des
fichiers. Tester les comportements avec les outils adaptés à l’implémentation, dans `infra/`.
Faire une première exécution réelle sur devops : accès via Caddy, CRUD, rechargement,
base initialement vide puis persistante, montages et propriétaires des sorties.
Exécuter `python3 codebase-integrity/scripts/check.py` sans en modifier les règles.
Documenter prérequis, préparation, commandes, adresses, ressources et limites dans
`infra/README.md`, `SETUP.md`, le guide des couches et les runbooks pertinents.

## Exclusions

Aucune modification de `codebase-integrity/`, des règles AGENTS, des contrats applicatifs,
des fichiers sources ou README sous `app/`. Si une adaptation applicative devient nécessaire,
signaler le besoin et compléter le découpage dans sa couche avant d’y écrire.
Aucun PostgreSQL, service métier de cap-nour, domaine public, déploiement ou stack develop.

## Réalisation et preuves

2026-10-26 : stack implémentée dans `infra/`, sans modification de `app/`,
`config/` ou `codebase-integrity/`. Ajout des Dockerfiles API et Chromium, Compose,
Caddy, lanceur, scripts de démarrage et recettes/tests propres à la stack.
Le runbook décrit les commandes, ports, volumes et diagnostics ; SETUP et le guide
des couches pointent vers cette procédure.

Preuves sur devops, port 19304, projet `aide-app-ec4e123090-devops` :

- `python3 infra/test_apps.py` : 9 tests réussis, dont 15 résolutions Compose,
  refus des branches inadaptées, préservation des `.env`, collision réelle, relance
  après fermeture TCP, droits des points de montage et montages limités du navigateur.
- Les trois modes réellement lancés après arrêt : web donne api/caddy/web ; backoffice
  donne api/caddy/backoffice ; both donne api/caddy/web/backoffice.
- `python3 infra/browser.py --reload` : Chromium réel, accès Caddy, création/modification/
  suppression via le backoffice et lecture dans le web réussis. Les deux interfaces
  se mettent à jour automatiquement ; modification PHP observée sans redémarrage.
  Les trois fichiers temporaires sont restaurés exactement ; `git diff -- app` est vide.
- Base SQLite initialement vide ; article retrouvé après arrêt/relance puis supprimé.
  Les montages observés visent le seul worktree devops, les sources sont en lecture seule,
  les services applicatifs tournent en 1000:1000 et les volumes portent le préfixe du projet.
  Aucun fichier généré des volumes inspectés n’appartient à root ; les `.env` sont inchangés.
- `python3 codebase-integrity/scripts/check.py` : 23 tests réussis.
  `python3 codebase-integrity/scripts/quality.py` : code 0, outillage, contrat API,
  lint Symfony, mapping Doctrine, comparaison OpenAPI, types et builds des deux interfaces.
- Syntaxes Python, shell et JavaScript vérifiées ; `git diff --check` réussi.

Les sockets des tests et Docker exigent ici une exécution hors sandbox ; aucun contrôle
n’a été affaibli. Les essais ont révélé deux corrections : SO_REUSEADDR pour ne pas
confondre TIME_WAIT avec un service actif, et désactivation explicite d’OPcache pour
le serveur PHP de développement. Chromium a été construit dans une image dédiée
pour éviter une installation système sur l’hôte. Ses seuls montages sont le script,
les captures et les trois fichiers ciblés lors du test de rechargement ; aucun `.env`.
La tentative de montage large dans une image locale a été rejetée automatiquement et
remplacée par cette recette limitée, testée avec succès.

Journaux locaux : `/tmp/DEM-005-tests-stack.log`, `/tmp/DEM-005-check.log`,
`/tmp/DEM-005-quality.log`, `/tmp/DEM-005-selective.log`,
`/tmp/DEM-005-browser-devops.log` et `/tmp/DEM-005-runtime-devops.log`.
Captures : `/tmp/DEM-005-browser-artifacts/DEM-005-devops-{web,backoffice}.png`.
La stack devops reste disponible pour la recette OPS-052. Aucun verdict humain inventé.
Le SHA de ce commit sera référencé par OPS-052 et dans le bilan final.

Correction documentaire OPS-051 : les responsabilités et conventions de la nouvelle stack
utilisent les chapitres `## Rôle et responsabilités` et `## Conventions techniques`
attendus pour la revue locale. `git diff --check` réussi ; aucun changement exécutable.

Correction OPS-051 pendant OPS-052 : le worktree web sans `.env` a révélé un point
de montage impossible sous le bind source en lecture seule. Suppression de ce montage ;
le runtime Symfony existant supporte `APP_RUNTIME_OPTIONS` JSON et `dotenv_path`,
maintenant fixé à `.env.example`. Aucun `.env` hôte créé ou modifié. Les 15 résolutions
Compose et le test de préparation sans `.env` couvrent ce cas. La recette réelle des
cinq couches sera rejouée sur ce commit de correction et consignée dans OPS-052.


## Corrections humaines demandées — 2026-10-27

SHA présentés : `d076aecd78c7bfe110758ef35055b42e0af35084`,
`ec0e27bd1b8e19bddf073139fcc6b95ede035136` et
`c70975474d656c74fb3f88ec7419953221a38922`. Aucun de ces SHA n’est validé.
L’humain demande des commandes `make` pour piloter la stack, à la place des appels
explicites à `python3`. Fournir des cibles pour préparer, démarrer avec le choix
d’interface, afficher les adresses et l’état, arrêter et exécuter les tests/recettes.
Les scripts Python peuvent rester utilisés en interne. Le Makefile racine est ajouté
au périmètre de correction par cette demande explicite ; actualiser la documentation
et les preuves concernées sans modifier le Codebase Integrity.
De nouveaux commits d’implémentation sont nécessaires avant une nouvelle vérification.
Aucun code modifié à l’étape de consignation du verdict.


## Clarification et réalisation Make — 2026-10-27

L’humain demande explicitement de supprimer Python du pilotage et de faire appeler
Docker directement par Make ; la possibilité précédente de conserver Python comme
lanceur interne ne s’applique plus. Le Makefile racine contient les appels Compose,
la préparation et l’exécution Docker de Chromium. `infra/stack-env.sh` prépare
seulement les paramètres, les vérifications Git et les points de montage, avec Git,
Bash, Perl/JSON::PP et les outils Linux existants. Il ne distribue pas d’actions Docker.
Les anciens `apps.py`, `browser.py`, `test-runtime.py` et `test_apps.py` de `infra/`
sont supprimés. Les tests Make remplacent les tests du lanceur ; la recette de
persistance Node appelle Make pour le cycle de vie. Aucun changement de Compose,
contrat, lock, configuration de couche ou Codebase Integrity n’est nécessaire.


Preuves de la correction Make sur devops, 2026-10-27 :

- `make test` : sept groupes de contrôles réussis, dont les cinq identités et quinze
  configurations, le routage compact JSON, les paramètres invalides, la préservation
  des `.env`, les collisions réelles, le port détenu par Caddy, les montages symboliques,
  les cibles prepare/status/up/down et un `make -n` sans effet. Un faux exécutable
  Python échoue s’il est invoqué ; ces contrôles passent sans l’appeler.
- `make prepare`, `make status` et les démarrages réels web/backoffice/both réussis.
  Projets, ports et volumes conservent exactement leur identité précédente.
- `make test-browser RELOAD=1` : CRUD navigateur, lecture web, rechargement PHP/Nuxt
  réussis, avec restauration exacte des fichiers testés.
- `make test-runtime EXPECT_EMPTY=1` : cycle down/up via Make, article conservé puis
  supprimé, `.env` préservés, montages et UID/GID corrects, aucun fichier généré root.
  La recette utilise des connexions HTTP neuves après relance plutôt qu’une connexion
  persistante liée au conteneur arrêté.
- Qualité complète existante réussie, sans modification du Codebase Integrity.
  Syntaxes Bash/Node et `git diff --check` vérifiés ; aucun diff applicatif.

Les procédures quotidiennes et de recette, SETUP, le guide des couches et le README
infra présentent Make. Prérequis de pilotage Linux/WSL : GNU Make, Bash, Git, Docker
Compose, Perl/JSON::PP, coreutils et ss ; aucun Python ni Node hôte pour le pilotage.
Seule la recette d’assertions runtime utilise Node sur l’hôte.
Les journaux sont `/tmp/DEM-005-make-{test,prepare,status,modes,quality}.log`,
`/tmp/DEM-005-make-browser-devops.log` et `/tmp/DEM-005-make-runtime-devops.log`.
Cette correction reste à vérifier par l’humain ; OPS-052 vérifiera ses copies dans
les cinq couches après identification du nouveau SHA.

## Corrections supplémentaires — raccourcis et documentation locale

L’humain demande des commandes simples par couche, sans `cd` ni option `-C`.
Le Makefile propose `make api`, `make web`, `make backoffice`, `make design` et
`make devops`, avec les deux interfaces par défaut, ainsi que `stop-<couche>` et
`status-<couche>`. Les appels sont transmis au Makefile du worktree cible, dont
les vérifications Git et Docker restent actives. Aucun environnement n’est lancé
sur develop. La racine du dépôt principal disposera de ces cibles après intégration ;
pendant la correction, elles sont vérifiables depuis le worktree devops.

L’humain précise aussi que `runbooks/` est réservé aux mesures exceptionnelles
lors des déploiements. Les trois procédures de DEM-005 sont déplacées dans
`docs/02-cadre/`, avec actualisation des liens et de l’index. Elles concernent
uniquement le développement local. Aucun déploiement distant n’est configuré.

`infra/test-shortcuts.sh` vérifie les cinq destinations, leurs commandes de démarrage,
arrêt et état, l’interface par défaut et sa surcharge, ainsi que l’absence d’action
avec `make -n`. Aucun verdict favorable n’est déduit de ces contrôles.

## Verdict sur les raccourcis et la structure documentaire

Corrections humaines demandées : les cibles `make api|web|backoffice|design|devops`
manquent de contexte. Les noms doivent expliciter la dockerisation locale des
couches, y compris pour l’arrêt et l’état. Le guide d’utilisation doit rejoindre
un sous-dossier `docs/02-cadre/couches/` remplaçant `couches.md`, avec conservation
du contenu général et mise à jour des liens. Les deux autres documents de recette
et de réparation restent à leur emplacement d’origine ; annuler leur déplacement.
Version concernée : modifications non commitées sur HEAD `df5ac29`, sans nouveau
SHA d’implémentation. Aucune validation ; corrections à réaliser à l’implémentation.

Nom du guide précisé par l’humain :
`docs/02-cadre/couches/dockerisation.md` ; abandonner le nom proposé
`dockerisation-locale.md`. Ce fichier reste à créer lors de la correction de structure.

## Réalisation de la correction de contexte

Les commandes deviennent `make docker-up-<couche>`, `make docker-stop-<couche>`
et `make docker-status-<couche>` pour api, web, backoffice, design et devops.
Le démarrage sélectionne les deux interfaces par défaut ; `INTERFACE=web` ou
`INTERFACE=backoffice` reste possible. Les anciennes cibles sans contexte ne sont
pas conservées. Le routage appelle le Makefile du worktree cible ; Compose reste
appelé directement par ses recettes, sans Python dans le pilotage.

`docs/02-cadre/couches.md` devient `docs/02-cadre/couches/index.md`, avec
adaptation des chemins relatifs. Le guide d’usage est
`docs/02-cadre/couches/dockerisation.md`. Les deux autres procédures de recette
et de réparation sont conservées, octet pour octet, à leurs emplacements initiaux
dans `dev-book/runbooks/`. Les liens actifs de SETUP, AGENTS, des README et des
index sont actualisés ; les règles et contrôles du Codebase Integrity sont inchangés.
Les modifications des README config/design et d’AGENTS portent uniquement sur
le lien du document déplacé, sans changement de responsabilité ou de convention.

Preuves : `make test` réussi (sept groupes existants dont quinze configurations
Compose, plus les tests des cinq raccourcis, arrêt/état, interface et aperçu).
`git diff --check` et syntaxe Bash réussis. Journaux locaux :
`/tmp/DEM-005-corrections-tests.log` et `/tmp/DEM-005-corrections-quality.log`.
La disponibilité depuis la racine principale attend l’intégration du Makefile ;
aucune modification sur develop. OPS-052 vérifie ensuite le commit identifié.

Qualité complète réussie (code 0) : outillage, contrat API, lint Symfony,
mapping Doctrine, comparaison OpenAPI, types et builds Nuxt. Les tests refusent
aussi les anciennes cibles sans contexte et une couche inconnue. Vérification des
liens locaux des guides et points d’entrée modifiés réussie. Les deux procédures
conservées ont été comparées avec HEAD par `cmp`, sans différence.
