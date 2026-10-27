# OPS-061 — Simplifier la reconstitution et aligner le workflow

- État : validée et commitée ; non livrée.
- Date : 2026-10-27.
- Demande : [DEM-009](../demand/DEM-009-supprimer-copies-apres-livraison.md).
- Identifiant de session : `01a17c9e-d8e8-7833-805b-fe7a84cfecd0`.
- Couche : devops ; worktree `worktree/devops` ; branche `layers/devops`.
- Base : `da44ac36942165786b969c37e9b91de1f0158a23`.

## Objectif

Mettre en œuvre le périmètre courant de DEM-009 : commits à l’étape 04 après
validation, session obligatoire, arrêt avant nouvelle mission sale/occupée,
reconstitution par branche et cherry-picks dans un worktree existant. Aucun dossier
de réunion, rapport séparé, archive ou suppression de copie à organiser.

## Chemins autorisés

- `AGENTS.md`, `README.md`, `dev-book/README.md` (chapitre Conventions techniques vide).
- `docs/03-developpement-loop/01-interview.md`, `02-decoupage.md`,
  `03-implementation.md`, `04-verification.md`, `05-reconstitution.md`,
  `06-livraison.md`, `index.md`.
- `docs/02-cadre/couches/index.md`, `worktree/README.md` pour retirer les copies extérieures.
- Cette carte et DEM-009 ; aucun rapport séparé.
- Skills personnels `interviewer-demande`, `decouper-demande`, `implementer-demande`,
  `verifier-demande`, `reconstituer-demande`, `livrer-demande` : cohérence des règles
  et simplification demandées, sans élargir push/PR/merge hors livraison.

Les skills restent hors Git : leurs validations sont présentées séparément.
Aucun élément Codebase Integrity ni test applicatif modifié.

## Dépendances et affectation

Aucune dépendance amont supplémentaire. L’humain a intégré les changements déjà
présents de la session dans DEM-009 : reprise de cette même mission, pas démarrage
sur un travail étranger. Vérifier chemin absolu, branche, index et disponibilité.
Pas de délégation, rebase, nettoyage ou commit artificiel pour obtenir un arbre propre.

## Réalisation et contrôles

Les six skills et les consignes du dépôt appliquent le nouveau parcours :
`git switch -c demands/<identifiant> develop`, puis `git cherry-pick -x <sha>`
des seuls commits validés dans l’ordre. Les SHA sources et obtenus sont conservés
dans les documents existants ; une reprise contrôle la provenance avant rejeu.
Le worktree revient à sa branche de couche après fusion distante, puis est aligné
et conservé. Seules les branches temporaires livrées sont supprimées.

Essai exécuté dans un dépôt jetable :

- Initialisation de develop et d’un worktree layers/devops ; deux commits sources
  (résultat validé et trace de verdict).
- Création de demands/DEM-009 depuis develop dans ce même worktree.
- Deux cherry-picks avec -x : contenus et provenance des SHA sources vérifiés.
- Nombre de worktrees inchangé, aucun dossier supplémentaire ; develop et la
  référence layers/devops inchangés, branche de demande propre avec deux commits.

L’ancien essai de suppression de copie ne définit plus le comportement courant :
il était lié au périmètre remplacé par la simplification demandée.
Les cas de mission sale, de reprise identifiée, de dépendance non commitée, de
verdict absent/refusé et d’ID absent sont vérifiés par revue des instructions,
sans prétendre à une évaluation autonome d’agent.

Validateurs skill-creator des skills modifiés, liens locaux et `git diff --check`
vérifiés. Le README dev-book a son chapitre Conventions techniques vide.
La qualité globale sera exécutée à la livraison, sans résultat anticipé.

## Corrections humaines et validation

Les changements de cette session ont été inclus explicitement dans DEM-009.
Le rapport de clôture a été supprimé sur demande ; aucune preuve séparée créée.
Les conventions ajoutées au README dev-book ont été retirées sur demande.
La dernière simplification remplace les copies extérieures et leur nettoyage par
une branche et des cherry-picks dans un worktree existant. Le nom historique du
fichier de carte est conservé pour ses liens, son titre décrit le périmètre courant.

Aucun commit d’implémentation ni verdict favorable sur cette version corrigée.
Présenter le contenu à l’étape 04 ; seulement après validation, committer cette
carte avec les modifications acceptées et leurs preuves, puis relever le SHA.
Ne pas pousser, ouvrir une PR, fusionner ou reconstituer réellement dans cette étape.

## Verdict humain — 2026-10-27

L’humain répond « ok c’est validé » à la présentation de la version simplifiée :
branche demands/<identifiant> depuis develop puis cherry-picks des commits validés
dans un worktree existant libre et propre, sans copie supplémentaire. Le verdict
couvre le périmètre courant de DEM-009 et OPS-061, y compris les commits à l’étape
04 après validation, la session obligatoire et les corrections demandées (README
dev-book sans conventions et absence de rapport séparé).

Les six skills personnels sont validés par skill-creator ; ils restent hors Git.
L’essai de reconstitution jetable et les liens sont vérifiés. Aucun changement
fonctionnel supplémentaire introduit pendant la consignation de ce verdict.
Commit local de carte créé à cette étape 04 ; reconstitution et livraison restent
à effectuer. Aucun push, PR ou merge autorisé par cette seule vérification.

Commit de carte validée créé à l’étape 04 : `5d69599f86b0ac1ea84be16761f1ed6cba082fdd`.
