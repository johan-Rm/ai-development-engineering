# OPS-059 — Renommer les rapports et corriger leurs liens

- État : bloquée par le commit OPS-058.
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
`dev-book/resources/DEM-007-audit-contenu-local.md` est une occurrence connue,
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
Non commencée ; aucun commit de réalisation ni verdict humain.
