# WEB-004 — Déplacer web vers apps

- Demande : DEM-030 ; type : développement.
- Création : 2026-11-06 ; session : `01a1b040-6627-7b60-a2ec-ab2f985bf83d`.
- Besoin de référence : `tmp/demande-renommer-app-apps.md` dans le dépôt principal.
- Demande définitive prévue à la reconstitution : `dev-book/demand/DEM-030-renommer-app-apps.md` (absente à cette étape).
- Couche : web ; worktree : `worktree/web` ; branche : `layers/web`.
- Base locale : `d42251e1dca1c4efd700a6a453f4bec80a2634c3` ; sans fetch ni rebase.

- État : implémentée, non commitée, à vérifier.
- Dépendance : aucune ; intégration complète par OPS-081 attendue pour les contrôles communs.

## Objectif et chemins autorisés

Déplacer `app/web/` vers `apps/web/`, en conservant le contenu et les chemins
internes. Chemins autorisés : ces deux sous-arbres et cette carte.
Ne modifier aucun fichier partagé ni comportement applicatif.
Préserver et déplacer sans perte les fichiers locaux ignorés nécessaires, `.env`
et données ; inventorier leur présence sans exposer leurs valeurs.

## Critères, contrôles et preuve

Même contenu suivi avant/après déplacement ; aucune perte locale, aucun alias.
Comparer les fichiers et relire `git diff --summary` et `git diff --check`.
Depuis `apps/web/targets/app/`, exécuter `npm run typecheck` et `npm run build`.
Les liens et contrôles globaux sont vérifiés par OPS-081 après réunion des déplacements.
Consigner résultats et limites ici ; aucun nouveau test miroir du déplacement.
Documentation interne déplacée avec son application ; documentation commune dans OPS-081.

## Vérification et suite

Implémentation du 2026-11-06, session de création conservée.
État soumis : HEAD de base ci-dessus, index vide ; suppressions sous `app/web/`,
fichiers non suivis sous `apps/web/` et cette carte non suivie.
13 fichiers suivis identiques octet par octet à HEAD après déplacement.
14133 fichiers ignorés présents avant déplacement ; les 16319 entrées
locales ont conservé inode, mode, taille, date et cible des liens au déplacement,
avant exécution des contrôles (caches régénérables ensuite).
Empreinte SHA-256 du manifeste des contenus suivis avant déplacement :
`3d7501552ca1c37857002644d8ceb6174414dd1f68292d69a1e7235f486bdf19`.
`git diff --check` réussi ; `git diff --summary` relu : suppressions attendues,
les destinations restant non suivies sans indexation à cette étape.
`npm run typecheck` et `npm run build` depuis le nouvel emplacement : réussis.
Limite : liens, lanceurs communs, CI et tests globaux attendent OPS-081.
Aucun changement fonctionnel ni nouveau test ajouté ; aucun verdict humain ni commit.
Reconstitution et ordre : voir la matrice du brouillon de référence.

## Verdict humain

Le 2026-11-06 : « validé » pour les quatre cartes présentées, avec les réserves
de la restitution. Contenu revérifié contre `tmp/verification-DEM-030.json`
du dépôt principal avant indexation ; aucune modification fonctionnelle.
Validation acquise ; commit local autorisé, livraison non réalisée.

État : validée et commitée localement ; à livrer.
Commit de réalisation validé : `633bb0bbbf4c127108b6c93c5505de2bd5834b03`.
