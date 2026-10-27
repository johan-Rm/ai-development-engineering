# OPS-059 — Renommer les rapports et corriger leurs liens

- État : validée ; non livrée.
- Date : 2026-10-27.
- Demande : [DEM-008](../demand/DEM-008-reserver-noms-demandes.md).
- Couche : devops.
- Worktree : `worktree/devops`, relatif à la racine du dépôt principal.
- Branche : `layers/devops`, existante conservée.
- Session : référence de session indisponible ; mission définie dans ce chat.

Chemin absolu résolu localement ; vérifier branche, index, missions actives et
état Git avant chaque écriture. Un arbre propre ne prouve pas sa disponibilité.
Aucune délégation. Préserver .env, données, travaux en cours et historiques.

## Objectif, périmètre et chemins autorisés

Inventorier les fichiers/dossiers DEM-* hors des demandes dans le contenu du
dépôt, puis renommer les rapports avec un nom adapté à leur rôle. Le rapport
`dev-book/resources/audit-contenu-local-007.md` est une occurrence connue,
non une liste exhaustive. Conserver son contenu et corriger tous ses liens actifs.
Les mentions historiques restent identifiables comme historiques.

Chemins autorisés : rapports concernés de `dev-book/resources/` et leurs liens
locaux dans `dev-book/demand/`, `dev-book/tasks/`, `dev-book/resources/README.md`
et les guides qui les référencent. Nom proposé pour le rapport connu :
`dev-book/resources/audit-contenu-local-007.md`. Ne pas renommer les demandes.
Ne pas modifier les copies d’autres couches : propagation des fichiers suivis
par commits et livraison, jamais copie de travail non commité.

## Dépendances par commit

Commit OPS-058 à identifier après réalisation ; aucun SHA disponible au découpage.
Ne pas utiliser les changements non commitées de la carte amont.

## Critères, contrôles et preuves

Inventaire des noms avant/après, preuve de contenu identique avant et après
renommage, recherche des liens et contrôle de leur résolution. Distinguer contenu
suivi et anciennes copies de réunion traitées par OPS-060. Vérifier diff --check ;
pas de test artificiel reproduisant le texte documentaire.

## Documentation et réalisation

Mettre à jour cette carte et DEM-008 avec les preuves et SHA avant vérification.
Lire les README applicables avant écriture. Aucun stash, reset destructif,
force-push ni rebase implicite. Aucun changement direct de tâche sur develop.
Réalisation décrite dans les preuves ci-dessous ; verdict humain consigné en fin de carte.

## Preuve OPS-059 — 2026-10-27

Dépendance OPS-058 : `caf3ad1`. Parcours de tout le worktree devops, fichiers
ignorés compris, hors métadonnées Git et copies imbriquées : un seul nom DEM-*
hors demand, le rapport d’audit. Renommé en `audit-contenu-local-007.md` sans
modification de contenu ; SHA-256 avant/après : `e369c7dd13330902cd5480860ba1aa801684cb918c788324cfad301281c72283`.
Références locales des demandes et cartes corrigées ; demandes non renommées.
Les autres copies sont traitées par OPS-060 ou propagées à la livraison.

## Verdict humain — 2026-10-27

L’humain répond « oui validé » après présentation des trois cartes et demande
explicite d’acceptation de la réserve OPS-060. Commits présentés et acceptés : `619a84d`.
Validation du renommage du rapport avec contenu préservé et liens corrigés.
Aucune correction fonctionnelle demandée. Ancienne mention « Non commencée »
rectifiée dans cette trace documentaire. Livraison non effectuée.
