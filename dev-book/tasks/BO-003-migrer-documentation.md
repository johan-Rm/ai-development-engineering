# BO-003 — Migrer la documentation backoffice

- Demande : [DEM-021](../demand/DEM-021-conventions-documentaires.md#arbitrage-humain--2026-10-30).
- Session de création : `01a18c38-1b13-7953-9118-aadc8cde8794`.
- Couche : backoffice ; worktree `worktree/backoffice` ; branche `layers/backoffice`.
- Statut : en attente des commits amont validés.
- Dépendance : WEB-003 et OPS-073, commits à renseigner après validation humaine.

## Mission et périmètre

Déplacer le contenu utile de `app/backoffice/README.md` vers `docs/applications/backoffice.md`, puis supprimer ce README et adapter les liens entrants, sans duplication du contrat API ni des règles communes.

Chemins autorisés : `app/backoffice/README.md`, `docs/applications/backoffice.md`, lien backoffice de `app/README.md`, navigation `docs/index.md`, références Markdown entrantes vers ce README et cette carte. Ces fichiers partagés sont réservés séquentiellement pour cette mission.

Exclusions : code applicatif, données, `.env`, sources graphiques et autres worktrees.
Une carte à la fois ; aucun transfert de travail non commité. Les cartes sont préparées
dans devops et ne seront disponibles ailleurs qu’après commit validé.

## Critères et preuves

Appliquer l’arbitrage de la demande sans étendre les exceptions. Informations utiles
conservées à une seule source ; liens migrés ; contrôles conformes, cas d’écart et
exceptions couverts pour le vérificateur. Préserver les preuves historiques.

Vérifications : Contrôle documentaire et `git diff --check` ; confronter les commandes déplacées aux scripts et manifestes applicatifs, sans démarrer ni modifier les données.

## Résultat et verdict

À renseigner après réalisation. Aucun verdict humain d’implémentation ni commit.
