# Vérifier les cinq stacks applicatives

## Objectif et préconditions

Vérifier DEM-005 sur les cinq branches puis sur deux stacks simultanément, avec
les commits de stack identifiés dans OPS-052. Coordonner les couches : le test de
rechargement modifie temporairement trois fichiers puis les restaure exactement.
Préserver les fichiers locaux, les données et les services étrangers à la recette.
Vérifier le moteur Docker local, les registres et les ports avec `make info`.

## Recette successive

Depuis la racine de chaque worktree, successivement pour devops, API, web,
backoffice et design :

```sh
git status --short --branch
make up INTERFACE=both
make test-browser RELOAD=1
make test-runtime EXPECT_EMPTY=1
make down
git status --short --branch
```

Ne lancer la couche suivante qu’après succès et arrêt de la précédente. Sur une
base déjà utilisée, omettre `EXPECT_EMPTY=1` ; ne pas effacer ses données pour satisfaire
une assertion. La preuve de base vide exige une première observation sur une base neuve.
Comparer l’état Git final à l’état initial, qui peut inclure les documents de la mission.

Le test navigateur vérifie le CRUD via le backoffice et la lecture web, capture les deux
interfaces, observe le rechargement Nuxt et PHP, et supprime son article. Le test runtime
observe montages, UID/GID et volumes, vérifie l’absence de fichiers générés root,
crée son article puis arrête/relance la stack et vérifie la persistance avant suppression.
Les `.env` et le diff applicatif initiaux sont comparés après exécution.

## Deux stacks simultanées

1. Démarrer `make up INTERFACE=both` depuis `worktree/api` puis `worktree/web`.
   Les ports attendus par défaut sont 19302 et 19303.
2. Observer avec Docker les deux projets annoncés par `info` : réseaux, volumes,
   ports et sources des montages distincts. Les montages `/app` doivent viser
   exclusivement leurs propres worktrees et rester en lecture seule.
3. Créer un article avec un titre unique dans chaque backoffice. Vérifier via les
   deux API et les deux interfaces que chaque article reste dans sa stack. Supprimer
   seulement les deux articles de cette preuve après observation.
4. Sauvegarder les octets du composant web `app/web/targets/app/app/app.vue` de la
   couche API et l’empreinte du même fichier de la couche web. Insérer temporairement
   un texte unique dans le premier `<h1>` côté API. Attendre sa présence dans le HTML
   rendu par `web.wt-api.localhost:19302` ; vérifier son absence dans le HTML de
   `web.wt-web.localhost:19303` et l’empreinte inchangée du fichier de la couche web.
   Restaurer les octets sauvegardés, y compris en cas d’erreur, sans reset global.
5. Comparer les états Git et les empreintes des `.env` à l’inventaire initial.
   Consigner les résultats, les SHA et l’état final des services dans OPS-052.

Pour les requêtes HTTP d’un outil qui ne résout pas `*.localhost`, utiliser par exemple
`curl --resolve api.wt-api.localhost:19302:127.0.0.1 http://api.wt-api.localhost:19302/api/articles`.
La recette navigateur définit ces résolutions dans son propre conteneur, sans changer
le DNS ou les fichiers de résolution de l’hôte.

## Contrôles et preuves

Exécuter `make test`, puis les contrôles existants
`python3 codebase-integrity/scripts/check.py` et
`python3 codebase-integrity/scripts/quality.py` depuis devops avec leurs dépendances.
Consigner la matrice des cinq couches et la paire simultanée, les résultats navigateur,
les observations des ressources et les limites. Les captures sont sous
`/tmp/DEM-005-make-browser-artifacts/` et les observations runtime sous
`/tmp/DEM-005-make-runtime-<couche>.json` ; les preuves durables sont dans la carte.
Le succès technique ne constitue pas le verdict humain.

## Arrêt en cas d’erreur et retour arrière

Conserver le diagnostic et l’identifiant du seul article temporaire concerné. Si le service
est indisponible, annoncer le nettoyage différé au lieu de supprimer des volumes.
Restaurer les fichiers temporairement modifiés et arrêter seulement la stack concernée
avec `down`. Aucun prune global, suppression de données, contournement de contrôle,
rebase, push ou merge n’appartient à cette recette.
