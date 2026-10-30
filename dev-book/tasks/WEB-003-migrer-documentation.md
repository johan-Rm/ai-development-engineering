# WEB-003 — Migrer la documentation web

- Demande : [DEM-021](../demand/DEM-021-conventions-documentaires.md#arbitrage-humain--2026-10-30).
- Session de création : `01a18c38-1b13-7953-9118-aadc8cde8794`.
- Périmètre applicatif : web.
- Couche exécutante : devops ; worktree `worktree/devops` ; branche `layers/devops`.
- Base : `cb3336b1389d32c0a3118c7870393a3d3f5349bc`.
- Statut : validée humainement le 2026-10-30 ; commit local à créer.
- Dépendance : commit validé d’[OPS-073](OPS-073-conventions-documentaires.md#commit-local),
  présent dans la branche ; aucune dépendance de code aux deux autres cartes.
- Organisation : [prise en charge globale](../demand/DEM-021-conventions-documentaires.md#prise-en-charge-globale-des-cartes-restantes).

## Mission et périmètre

Déplacer le contenu utile de `app/web/README.md` vers `docs/applications/web.md`, puis supprimer ce README et adapter les liens entrants, sans duplication du contrat API ni des règles communes.

Chemins autorisés : `app/web/README.md`, `docs/applications/web.md`, lien web de `app/README.md`, navigation `docs/index.md`, références Markdown entrantes vers ce README et cette carte. La documentation commune des interfaces (`docs/applications/interfaces.md`) et son index sont également autorisés ; leur édition est coordonnée au sein de cette mission unique.

Exclusions : code applicatif, données, `.env`, sources graphiques et autres worktrees.
Les trois cartes documentaires sont réalisées dans la même mission, conformément
à l’instruction humaine référencée ci-dessus ; aucun transfert entre worktrees.

## Critères et preuves

Conserver les informations utiles à une seule source, migrer les liens et préserver
les preuves historiques. Respecter l’arbitrage sans modifier les applications ni
le vérificateur documentaire.

Vérifications : Contrôle documentaire et `git diff --check` ; confronter les commandes déplacées aux scripts et manifestes applicatifs, sans démarrer ni modifier les données.

## Résultat et verdict

Le README web est supprimé et son contenu utile déplacé vers le guide prévu.
Les liens de navigation sont adaptés ; les références littérales historiques sont
conservées. Aucun code, manifeste, verrou de dépendances, test ou contrôle modifié.
La procédure commune des interfaces évite de répéter les instructions npm et la
configuration de connexion. Le contrat détaillé reste dans OpenAPI.

Commandes et préconditions confrontées aux manifestes, configurations et scripts
locaux. Correction du lancement backoffice : le dossier depuis la racine est
`app/backoffice/`. Les constats npm anciens ne sont pas présentés comme actuels.

Contrôles et identification du contenu : voir les
[preuves de la reprise](../demand/DEM-021-conventions-documentaires.md#preuves-de-la-reprise-documentaire).
Validation et périmètre du commit : voir le
[verdict humain](../demand/DEM-021-conventions-documentaires.md#verdict-sur-les-trois-cartes-restantes).
Le commit local est autorisé par cette validation.
