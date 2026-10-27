# OPS-054 — Déplacer la configuration des couches dans infra

- État : implémentée et commitée, à vérifier.
- Date : 2026-10-27.
- Demande : [DEM-006](../demand/DEM-006-clarifier-responsabilites-dossiers-cadre.md).
- Couche : devops.
- Worktree : `worktree/devops`, relatif à la racine du dépôt principal.
- Branche : `layers/devops` ; branche existante conservée.
- Session : référence de session indisponible ; mission définie dans ce chat.
- Base locale vérifiée : `779ce88da0a8e1945061cd2805bd0005ce01c13b` ; aucun fetch.

Le chemin absolu du worktree est résolu localement et sa branche, son état et sa
 disponibilité sont revérifiés avant exécution. Aucune délégation n’est autorisée.

## Objectif et chemins autorisés

Déplacer `config/README.md` et `config/layers.json` vers `infra/config/`.
Adapter `codebase-integrity/scripts/worktrees.py`, `process.py`, leur README,
`codebase-integrity/tests/test_worktrees.py`, `test_process.py`,
`infra/stack-env.sh`, `infra/test-make.sh`, `SETUP.md` et
`docs/02-cadre/couches/index.md` pour le nouvel emplacement.
Corriger les liens relatifs du README déplacé en conservant ses conventions existantes.
Mettre à jour cette carte et DEM-006 pour les preuves. Si la recherche révèle un
consommateur actif supplémentaire, identifier son chemin et compléter la carte avant correction.

## Exclusions

Aucun changement de valeurs JSON, de calcul des ports, d’identité des environnements,
de comportement des outils, de recette Docker ou de convention de contrôle.
Ne pas réécrire les preuves historiques pour prétendre qu’elles utilisent déjà le nouveau chemin.
Ne pas remplir les conventions du README infra simplifié par OPS-053.

## Dépendances et ordre

Après OPS-053 : commit d’implémentation absent à ce découpage, SHA à identifier et
vérifier dans layers/devops avant démarrage. Ne pas utiliser sa copie non commitée
comme dépendance. La mission reste bloquée jusqu’à cette résolution.
Base locale commune déjà présente. Aucun transfert vers une autre couche nécessaire.

## Critères et preuve

L’ancien dossier config racine est remplacé par infra/config ; contenu JSON inchangé.
Les trois consommateurs directs et leurs fixtures lisent le nouvel emplacement.
Absence ou invalidité de configuration conserve le comportement d’erreur existant.
Les ports, branches, domaines et identités restent identiques à configuration égale.
Les liens du README déplacé et les références actives sont valides.

Exécuter `python3 codebase-integrity/scripts/check.py`, `make test`,
`git diff --check`, puis rechercher les anciennes références avec
`rg -n 'config/layers\.json' --glob '!worktree/**'` et classer les occurrences :
le nouveau chemin inclut aussi ce suffixe ; distinguer nouveau chemin, erreur et historique.
Les tests de création worktree, de configuration absente et d’isolation existants
servent de non-régression ; adapter leurs fixtures sans affaiblir leurs assertions.
Consigner commandes, résultats et SHA amont. Aucun démarrage applicatif supplémentaire requis
si les tests réussissent sans divergence fonctionnelle.
Avant PR, la livraison exécutera `python3 codebase-integrity/scripts/quality.py`
avec ses prérequis applicatifs, selon les règles du projet.

## Contraintes communes

Lire AGENTS.md, les couches, la demande et les README applicables avant écriture.
Préserver le travail existant et les `.env`. Aucun changement sur develop ou master,
aucun rebase implicite, aucun déploiement. Ne pas affaiblir les conventions ou contrôles.
Les README simplifiés ont une description courte, puis uniquement
« Rôle et responsabilités » et « Conventions techniques », cette dernière rubrique vide.
Ne pas ajouter de tests qui reproduisent seulement le texte documentaire.
La validation humaine et la livraison restent des étapes distinctes.

## Réalisation et verdict

Réalisée le 2026-10-27. Configuration déplacée et consommateurs/fixtures adaptés,
sans modification des assertions ni des valeurs JSON (identité octet par octet vérifiée).
Liens relatifs du README déplacé : valides. Recherche des références : tous les usages
actifs utilisent infra/config/layers.json ; les occurrences historiques de dev-book
restent historiques, notamment OPS-043 et DEM-005.
`python3 codebase-integrity/scripts/check.py` : 23 tests réussis.
`make test` : tous les contrôles réussis, dont 5 identités, 15 configurations Compose,
préservation .env, refus des collisions et paramètres invalides.
Première exécution : fixture de dossier corrigée ; restriction sandbox sur les sockets
locales résolue en relançant avec les permissions nécessaires, sans affaiblir les tests.
`git diff --check` : réussi. Aucun déploiement ni recette applicative démarrée.
quality.py reste à la livraison avec ses prérequis. Aucun verdict humain à ce stade.

## Dépendance résolue

OPS-053 : `56c8a954cc5ad2073b336e7d73b6622ebfcdb87f`, présent sur layers/devops avant démarrage.
