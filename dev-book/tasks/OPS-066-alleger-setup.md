# OPS-066 — Alléger SETUP

- Date : 2026-10-28.
- État : validée et commitée ; à livrer.
- Session de création : `01a182d3-1898-7e92-8fdc-c16b502fecbf`.
- Demande : DEM-013 ; source actuelle `tmp/demande-alleger-setup.md`, relative au dépôt principal.
- Demande définitive prévue : `dev-book/demand/DEM-013-alleger-setup.md` ; absente avant reconstitution. Ajouter alors le lien relatif.
- Mission : devops ; worktree `worktree/devops` ; branche `layers/devops`.
- Base observée : `92c64ba`, commune avec develop ; index et arbre propres avant création de cette carte, aucune mission active identifiée après clôture de DEM-012.
- Dépendances : aucune carte amont ni commit à importer.

## Objectif et critères

Réaliser les critères du brouillon DEM-013, référence du besoin : transformer
SETUP en parcours court sans perdre les informations utiles qui lui sont propres.
Vérifier les sources existantes avant de remplacer les répétitions par des liens.

## Périmètre autorisé

- `SETUP.md` : réécriture documentaire.
- `README.md`, `docs/**/*.md`, `infra/README.md`, `dev-book/resources/README.md` : seuls ajustements de liens entrants vers les sections de SETUP, si nécessaires.
- Cette carte : état, preuves et verdict humain à venir.

Exclus : changements fonctionnels, modification des skills, des conventions
techniques ou des contrôles, refonte des autres guides, cartes historiques.
Adapter les ancres entrantes à la structure convenue dans le chat.

## Vérification et preuves attendues

- Relecture avant/après : informations utiles préservées ; répétitions remplacées par leurs références ; commandes et comportements inchangés.
- Vérifier les fichiers et ancres des liens sortants et entrants concernés.
- Exécuter `git diff --check` et `python3 codebase-integrity/scripts/check.py` depuis le worktree ; qualité complète avant PR selon les [points de contrôle](../../docs/01-codebase-integrity/points-de-controle.md#exécuter-dans-ce-dépôt).
- Consigner ici les résultats, limites et références nécessaires, sans recopier le besoin ni les guides. Aucun test applicatif nouveau pour cette réécriture documentaire.

## Suite prévue

Après implémentation, validation humaine et commit de cette carte : reconstitution
sur `demands/DEM-013`, créée depuis develop local vérifié dans le principal (`.`)
libre et propre. Retour du principal sur develop après fusion distante ; devops
conserve `layers/devops`. Aucune branche de demande créée au découpage.

## Résultat et validation

La première proposition n’a pas été validée : l’humain l’a jugée incompréhensible.
Le cadrage a été repris dans le chat puis la nouvelle structure explicitement
approuvée avec invocation d’implementer-demande. Le brouillon fait référence
pour ces décisions ; la conservation du lancement sur l’hôte et de l’adoption
est remplacée par ce nouveau périmètre.

Résultat : cinq chapitres, skills dans les prérequis, création des worktrees
séparée de l’ouverture du workspace, démarrage Docker, lien vers le workflow.
Les libellés et ancres entrants ont été ajustés ; le lien des points de contrôle
vers l’installation supprimée renvoie désormais à la recette Docker.

Vérifications du 2026-10-28 :

- `git diff --check` réussi.
- Script Python local : 58 liens vérifiés dans les documents modifiés, et ancres
  entrantes Markdown vers SETUP valides.
- `python3 codebase-integrity/scripts/check.py` : 23 tests réussis hors sandbox
  pour permettre le serveur HTTP local temporaire.
- Aucun changement de code ; qualité applicative complète non relancée pour
  cette correction documentaire, reste requise avant PR.

État soumis : base `92c64ba4893cbda4818e349c54bb997e296730fc`, index vide.
Fichiers suivis modifiés : `SETUP.md`, `README.md`, `docs/index.md`,
`docs/01-codebase-integrity/points-de-controle.md`, `docs/02-cadre/documentation.md`,
`docs/02-cadre/couches/index.md`, `docs/03-developpement-loop/index.md`.
Cette carte reste non suivie. SHA-256 de SETUP :
`8bba950f3efe303250c96a56eba7e9eb5f193ce17214f7a391459f9677c6f8a2`.
Verdict humain du 2026-10-28 : « validé », après présentation de la correction finale d’OPS-066. Validation limitée au contenu présenté et à ses preuves ; qualité complète restant requise avant PR.

Dernières corrections humaines appliquées : titre et références alignés, nom complet
et description du blueprint sous le H1, prérequis sans puces. Décisions dans le
brouillon ; contenu de SETUP conforme, empreinte ci-dessus revérifiée.

Commit local créé après validation : `1d2c5bb9031e5237260d3ae4a2fb42d5a6b7f3ee`.
