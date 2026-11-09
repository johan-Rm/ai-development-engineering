# OPS-082 — Adapter le lanceur à apps

- Demande : DEM-031 ; type : consolidation.
- Création et reprise d’analyse : 2026-11-09 ; session : `01a1b040-6627-7b60-a2ec-ab2f985bf83d`.
- État : validée par l’humain ; commit local en cours.
- Couche : devops ; worktree : `worktree/devops` ; branche : `layers/devops`.
- Base locale : `d42251e1dca1c4efd700a6a453f4bec80a2634c3` ; index vide.
- Besoin, analyse et règle confirmée : `tmp/demande-adapter-lanceur-apps.md`
  dans le principal, référence unique avant reconstitution.
- Demande définitive prévue : `dev-book/demand/DEM-031-adapter-lanceur-apps.md` (absente).

## Objectif et périmètre

Implémenter la sélection d’organisation confirmée dans le brouillon.
Chemins autorisés : `codebase-integrity/scripts/apps.py`,
`codebase-integrity/tests/test_apps.py`, `codebase-integrity/README.md`, cette carte.
Documenter la règle dans la rubrique existante « Conventions techniques » ;
conserver rubriques et ordre. Aucun changement CI, Docker, application, données,
contrôle de contribution ou seuil ; aucun alias ni déplacement de dossier.
Le message de régénération OpenAPI doit désigner l’emplacement effectivement choisi.

## Critères et contrôles

- Tester les trois applications sur chaque organisation et via une racine distincte.
- Tester coexistence (priorité au nouveau), nouveau dossier incomplet sans repli,
  absence des deux dossiers et propagation des erreurs ; aucun lancement incorrect.
- Conserver les tests de préservation de `.env` et de non-écrasement OpenAPI ;
  vérifier la création exclusive de `.env` dans l’organisation sélectionnée.
- Commandes : `python3 -B -m unittest discover -s codebase-integrity/tests -p test_apps.py`,
  `python3 codebase-integrity/scripts/quality.py`, `python3 codebase-integrity/scripts/check_docs.py`,
  `git diff --check`, depuis ce worktree. Prévoir les sockets locales et les runtimes applicatifs.
- Prouver aussi le lanceur avec `--root` sur les couches API/Web/Backoffice déplacées,
  en utilisant leurs fichiers sur place, sans copier de travail non commité.

## Mission et dépendances

Aucune dépendance de réalisation ; reprise des seuls changements identifiés
ci-dessous. Couche disponible pour OPS-082, sans nouvelle affectation étrangère.
La compatibilité et ses tests restent à produire ; les preuves du transfert
ne valent pas validation de ce nouveau comportement.
Branches d’archive des sources préservées ; aucun commit de DEM-030 à embarquer.
Ordre de livraison et reconstitution : voir le brouillon de référence.

## Preuves et verdict à compléter

Consigner commandes, résultats, limites, HEAD, diff et fichiers non suivis.
Livrer la consolidation avant DEM-030, avec qualité réussie avant renommage.
L’implémentation ne crée aucun commit ; nouvelle validation humaine nécessaire.

## Preuve du transfert

Le 2026-11-09 : les deux fichiers sont identiques octet par octet à leur état
dans le commit source OPS-081. `python3 -B -m unittest discover -s
codebase-integrity/tests -p test_apps.py` : quatre tests réussis.
`git diff --check` réussi. Diff soumis : uniquement les deux fichiers suivis
et cette carte non suivie ; index vide, base develop indiquée ci-dessus.
Aucun nouveau commit, verdict de consolidation ou changement de compatibilité.

## Preuves d’implémentation

Le 2026-11-09, session de création conservée : sélection dynamique depuis la racine
appelante, priorité au nouveau dossier, absence de repli si celui-ci est incomplet ;
message OpenAPI correspondant au chemin sélectionné. Convention documentée dans
le README local sans modification de ses rubriques. Aucun alias ni donnée déplacée.

Résultats finaux depuis `worktree/devops` :
- Tests ciblés Apps : 10 tests réussis, comprenant les cas ancien/nouveau, coexistence,
  incomplétude, absence, racine distincte, actions, `.env` et dérive OpenAPI.
- `python3 codebase-integrity/scripts/quality.py` : réussi sur l’ancien emplacement
  `app/` ; 117 tests d’outillage, test API, Symfony, contrat OpenAPI, typechecks et builds.
- `python3 codebase-integrity/scripts/apps.py check <application> --root <worktree>` :
  API, Web et Backoffice réussis sur les trois couches déplacées sous `apps/`.
  Le lanceur de cette couche lit les fichiers en place ; aucun transfert intermission.
- `check_docs.py`, `git diff --check`, périmètre et ordre des rubriques : conformes.

Contrôles avec sockets locales exécutés hors restriction du bac à sable.
Limites : pas de nouvelle recette navigateur/runtime ; contribution par commits
non vérifiable avant validation et reconstitution de DEM-031. La nouvelle règle
reste à vérifier humainement ; l’ancien verdict de transfert ne la valide pas.
État soumis : HEAD `d42251e1dca1c4efd700a6a453f4bec80a2634c3`, index vide,
diff limité aux trois fichiers Codebase Integrity autorisés et cette carte non suivie.
Aucun commit, push ou passage automatique à la vérification.

## Verdict humain

Le 2026-11-09 : « validé », après présentation du nouveau comportement et des
preuves. Empreintes des quatre fichiers revérifiées avant commit : conformes
à `tmp/verification-implementation-DEM-031.json` du principal. Aucun changement
fonctionnel depuis la présentation ; périmètre limité à OPS-082.
