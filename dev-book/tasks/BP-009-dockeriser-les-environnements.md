# BP-009 — Dockeriser les environnements de travail

- **Créée le** : 2026-10-06.
- **Session** : non disponible (Codex).
- **Statut** : à cadrer — choix de stack demandé à l’utilisateur.
- **Type** : outillage.
- **Tests** : résolution Compose, builds et démarrage de deux environnements simultanés ;
  observation des endpoints et des destinations d’écriture.
- **Réf** : BP-003 à BP-008 ; `docs/aiod/parallel-work.md`.
- **Rattachement** : devops pour les fichiers d’infrastructure, coordination blueprint
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

## Questions ouvertes

- Runtimes du backoffice, API et web ; base de données et proxy éventuels.
- Type d’exemple applicatif à construire, s’il dépasse de simples environnements de travail.
- Services réellement nécessaires à design et devops.

Ces réponses doivent précéder les fichiers spécifiques à une technologie.

## Hors périmètre

DNS public, comptes fournisseurs, déploiement en production et secrets réels.
Aucun environnement ne sera annoncé fonctionnel sur la seule base de ports théoriques.

## Documentation impactée

`docs/aiod/parallel-work.md`, documentation de l’exemple choisi, README des couches concernées
et procédure de démarrage/arrêt dans `dev-book/runbooks/`.

## Définition de terminé

- [ ] La stack et les services sont définis explicitement.
- [ ] Les configurations Compose se résolvent depuis les worktrees concernés.
- [ ] Deux environnements tournent simultanément sans collision de ports ou de données.
- [ ] Leurs endpoints et destinations effectives d’écriture sont observés et consignés.
- [ ] Une relance conserve les environnements et données préexistants.
- [ ] Les commandes et limites de chaque couche sont documentées.
- [ ] Aucun secret n’est commité et aucune ressource distante n’est modifiée.

## Preuves initiales

2026-10-06 : Docker Engine 29.7.2 et Docker Compose v5.5.0 disponibles.
Accès au moteur local vérifié après autorisation ; aucune pile lancée à ce stade.
