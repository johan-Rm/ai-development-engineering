# DEM-005 — Dockeriser les applications dans les cinq worktrees

- Date : 2026-10-26.
- État : cadrage confirmé ; découpée, dépendances à résoudre avant les cartes consommatrices.
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

Aucune décision de besoin bloquante après confirmation. Restent à déterminer au
découpage et à l’implémentation : ports exacts, noms des commandes, images adaptées
aux runtimes existants, ressources persistantes et méthode de réparation des liens Git.
Ces choix doivent respecter les critères confirmés et préserver l’existant.

## Tâches issues du découpage

Découpage du 2026-10-26, sans implémentation ni commit.

| Ordre | Carte | Critères DEM-005 couverts | Dépendances et état |
| --- | --- | --- | --- |
| 1 | [OPS-050 — Réparer les liens Git](../tasks/OPS-050-reparer-liens-worktrees.md) | 1, 7 | Prête ; réparation locale à exécuter et preuve à committer sous autorisation |
| 2 | [OPS-051 — Stack applicative commune](../tasks/OPS-051-stack-applicative-worktree.md) | 2 à 7, documentation | Non prête : OPS-050 sans SHA, liens et divergence à traiter |
| 3 | [OPS-052 — Recette des cinq stacks](../tasks/OPS-052-recette-cinq-stacks.md) | 1 à 8, preuves finales | Non prête : OPS-050 et OPS-051 sans SHA, mise à disposition par commits à autoriser |

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

Les dépendances futures sans SHA sont volontairement non résolues ; aucune copie de
travail non commité d’une autre mission ne peut les remplacer. L’implémentation et les
opérations Git nécessaires restent des étapes ultérieures selon leurs autorisations.
