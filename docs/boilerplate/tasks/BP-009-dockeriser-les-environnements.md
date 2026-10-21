# BP-009 — Dockeriser les environnements de travail

- **Créée le** : 2026-10-06.
- **Session** : non disponible (Codex).
- **Statut** : clôturée le 2026-10-06 — outillage commun testé en dépôt jetable.
- **Type** : outillage.
- **Tests** : résolution Compose, builds et démarrage de deux environnements simultanés ;
  observation des endpoints et des destinations d’écriture.
- **Réf** : BP-003 à BP-008 ; `docs/aiod/parallel-work.md`.
- **Rattachement** : devops pour les fichiers d’infrastructure, coordination de la maintenance du cadre
  pour l’outillage commun. Les changements applicatifs éventuels font l’objet de tâches distinctes.

## Contexte

L’utilisateur demande désormais de créer les worktrees et leur dockerisation. Les cartes
d’initialisation Git ne couvrent ni les services ni les runtimes.
Le blueprint reste indépendant de la stack ; le premier exemple concret doit être choisi.

## Périmètre

Préparer une configuration Docker Compose utilisable depuis les worktrees, avec des identifiants
stables par couche et une identité de projet. Définir les cibles backoffice, API, web multi-cibles,
et les outils utiles à devops et design. Une couche sans service n’a pas besoin d’un conteneur
permanent ; son environnement de travail doit être explicitement décrit.

Isoler les ports, réseaux, données de développement, caches et fichiers de build.
Les volumes et montages doivent viser les chemins du worktree concerné, jamais ceux d’un voisin.
La création du worktree ne démarre pas automatiquement les services.

## Décisions déjà prises

- Cinq couches, branches `layers/<couche>`, intégration `develop`, référence publique `master`.
- Aucune copie automatique de secrets ; conserver les `.env` existants.
- Aucune opération sur les domaines publics ou serveurs distants.
- Commandes de démarrage et d’arrêt distinctes de la création Git.

## Arbitrage humain du 2026-10-06

Aucune stack produit, aucune application : seule la mécanique AIOD est testée.
Un conteneur BusyBox sert une page témoin par couche. Son runtime n’est pas une stack applicative.
Chaque couche possède un port stable, un réseau et un volume distincts. Les tests observent
les pages, les montages et des écritures dans les volumes. Aucun build applicatif à tester.
Un commit d’initialisation par couche est autorisé ; le socle commun est commité au préalable
pour que les worktrees consomment un contenu identifié.

## Hors périmètre

DNS public, comptes fournisseurs, déploiement en production et secrets réels.
Aucun environnement ne sera annoncé fonctionnel sur la seule base de ports théoriques.

## Documentation impactée

`docs/aiod/parallel-work.md`, documentation de l’exemple choisi, README des couches concernées
et procédure de démarrage/arrêt dans `dev-book/runbooks/`.

## Définition de terminé

- [x] La stack et les services sont définis explicitement.
- [x] Les configurations Compose se résolvent depuis les worktrees concernés, sans build applicatif.
- [x] Deux environnements tournent simultanément sans collision de ports ou de données.
- [x] Leurs endpoints et destinations effectives d’écriture sont observés et consignés.
- [x] Une relance conserve les environnements et données préexistants.
- [x] Les commandes et limites de chaque couche sont documentées.
- [x] Aucun secret n’est commité et aucune ressource distante n’est modifiée.

## Preuves initiales

2026-10-06 : Docker Engine 29.7.2 et Docker Compose v5.5.0 disponibles.
Accès au moteur local vérifié après autorisation ; aucune pile lancée à ce stade.

## Vérification

Recette en dépôt jetable `/tmp/aiod-docker-trial-tqo6vjkp` : API et web simultanés,
ports 18102 et 18103, réseaux et volumes `aiod-8e0aadc5-api` et `aiod-8e0aadc5-web` distincts.
Les montages /proof pointent sur chaque arbre, en lecture seule. Les marqueurs de données
api et web sont différents et conservés après relance. Les ressources de test ont été retirées.
Douze tests Python valident la mécanique Git, l’identité et la préservation des fichiers.
Les cinq environnements du dépôt seront démarrés et observés pendant BP-004 à BP-008.

## Livré

Compose commun, outils process/check_docker, identifiants stables, exclusions et procédure de recette.
Aucune stack applicative, aucun build produit, aucun secret ni ressource distante.
