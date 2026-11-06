# API-004 — Déplacer api vers apps

- Demande : DEM-030 ; type : développement.
- Création : 2026-11-06 ; session : `01a1b040-6627-7b60-a2ec-ab2f985bf83d`.
- Besoin de référence : `tmp/demande-renommer-app-apps.md` dans le dépôt principal.
- Demande définitive prévue à la reconstitution : `dev-book/demand/DEM-030-renommer-app-apps.md` (absente à cette étape).
- Couche : api ; worktree : `worktree/api` ; branche : `layers/api`.
- Base locale : `d42251e1dca1c4efd700a6a453f4bec80a2634c3` ; sans fetch ni rebase.

- État : implémentée, non commitée, à vérifier.
- Dépendance : aucune ; intégration complète par OPS-081 attendue pour les contrôles communs.

## Objectif et chemins autorisés

Déplacer `app/api/` vers `apps/api/`, en conservant le contenu et les chemins
internes. Chemins autorisés : ces deux sous-arbres et cette carte.
Ne modifier aucun fichier partagé ni comportement applicatif.
Préserver et déplacer sans perte les fichiers locaux ignorés nécessaires, `.env`
et données ; inventorier leur présence sans exposer leurs valeurs.

## Critères, contrôles et preuve

Même contenu suivi avant/après déplacement ; aucune perte locale, aucun alias.
Comparer les fichiers et relire `git diff --summary` et `git diff --check`.
Depuis `apps/api/app/`, exécuter `python3 tests/smoke.py`,
`php bin/console lint:container` et `php bin/console lint:yaml config`.
Les liens et contrôles globaux sont vérifiés par OPS-081 après réunion des déplacements.
Consigner résultats et limites ici ; aucun nouveau test miroir du déplacement.
Documentation interne déplacée avec son application ; documentation commune dans OPS-081.

## Vérification et suite

Implémentation du 2026-11-06, session de création conservée.
État soumis : HEAD de base ci-dessus, index vide ; suppressions sous `app/api/`,
fichiers non suivis sous `apps/api/` et cette carte non suivie.
35 fichiers suivis identiques octet par octet à HEAD après déplacement.
7130 fichiers ignorés présents avant déplacement ; les 9314 entrées
locales ont conservé inode, mode, taille, date et cible des liens au déplacement,
avant exécution des contrôles (caches régénérables ensuite).
Empreinte SHA-256 du manifeste des contenus suivis avant déplacement :
`ec5c8f1c750e86e1961ba13a12ad7c01b8742d00c7d37c9c94b7bfda307aa549`.
`git diff --check` réussi ; `git diff --summary` relu : suppressions attendues,
les destinations restant non suivies sans indexation à cette étape.
`python3 tests/smoke.py` : un test réussi ; première tentative bloquée par
l’interdiction des sockets du bac à sable, relance autorisée hors bac réussie.
`php bin/console lint:container` et `php bin/console lint:yaml config` : réussis
(13 fichiers YAML).
Limite : liens, lanceurs communs, CI et tests globaux attendent OPS-081.
Aucun changement fonctionnel ni nouveau test ajouté ; aucun verdict humain ni commit.
Reconstitution et ordre : voir la matrice du brouillon de référence.

## Verdict humain

Le 2026-11-06 : « validé » pour les quatre cartes présentées, avec les réserves
de la restitution. Contenu revérifié contre `tmp/verification-DEM-030.json`
du dépôt principal avant indexation ; aucune modification fonctionnelle.
Validation acquise ; commit local autorisé, livraison non réalisée.

État : validée et commitée localement ; à livrer.
Commit de réalisation validé : `0a68888028ac81d266c226af85fb796078bc2560`.
