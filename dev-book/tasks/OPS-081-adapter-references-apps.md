# OPS-081 — Adapter les références communes à apps

- Demande : DEM-030 ; type : développement.
- Création : 2026-11-06 ; session : `01a1b040-6627-7b60-a2ec-ab2f985bf83d`.
- Besoin de référence : `tmp/demande-renommer-app-apps.md` dans le dépôt principal.
- Demande définitive prévue à la reconstitution : `dev-book/demand/DEM-030-renommer-app-apps.md` (absente à cette étape).
- Couche : devops ; worktree : `worktree/devops` ; branche : `layers/devops`.
- Base locale : `d42251e1dca1c4efd700a6a453f4bec80a2634c3` ; sans fetch ni rebase.

- État : périmètre hors Codebase Integrity validé ; transfert humain des deux fichiers vers DEM-031.

## Objectif et chemins autorisés

Sans consommer de travail amont non commité, déplacer
`app/README.md` vers `apps/README.md` et adapter les références actives.
Chemins autorisés : `README.md`, `Makefile`, `.github/workflows/quality.yml`,
`app/README.md`, `apps/README.md`, `infra/`, `docs/`,
`dev-book/` pour les liens actifs et cette carte ; `.gitignore` et
`aide.code-workspace` seulement si une référence concernée y est découverte.
Les contenus applicatifs sont réservés aux trois cartes amont.
Conserver les preuves historiques, les chemins internes `api/app`, `web/targets/app`
et les chemins `/app` propres aux conteneurs. Préserver les rubriques des README.
Exclure les changements fonctionnels, les nouvelles conventions et les alias.
Instruction complémentaire : corriger la distinction des dépendances dans les skills
et les guides concernés ; AGENTS.md seulement si une autorisation Git change (aucune prévue).

## Critères, contrôles et preuve

Couvrir les critères du brouillon : références actives corrigées, liens valides,
applications et commandes opérationnelles, données et fichiers locaux conservés.
Exécuter `python3 codebase-integrity/scripts/quality.py`, `make test`,
`python3 codebase-integrity/scripts/check_docs.py` et `git diff --check`.
Sur une stack isolée disponible : `make test-runtime` et `make test-browser` ;
consigner prérequis, environnement et limites si un contrôle ne peut être exécuté.
Relire la CI, les sources des montages Compose et le routage documentaire des couches.
Rechercher les références résiduelles dans les fichiers suivis et non ignorés,
hors dépendances, worktrees et `.env` ; justifier les occurrences conservées.
Adapter les tests de chemins existants ; ne pas affaiblir les contrôles.
Consigner résultats, conservation des ressources et limites ici ; aucun verdict anticipé.

## Vérification et suite

Implémentation du 2026-11-06, même session. Instruction humaine : réaliser la carte
et corriger le skill ; aucune consommation ni copie de travail non commité.
Références actives adaptées dans CI, Make, lanceur applicatif et ses tests de chemins,
Compose, recettes locales et documentation. `apps/README.md` identique à HEAD
avant déplacement ; rubriques des README conservées. Chemins internes et conteneurs
inchangés ; preuves historiques conservées.

Contrôles : `check.py`, 111 tests réussis après relance autorisée hors bac à sable
(sockets interdites au premier essai) ; `make test` réussi (15 configurations Compose,
identités, ports, préservation des données et raccourcis). Syntaxes Bash et Node
et `git diff --check` réussis. Le lanceur corrigé `apps.py check <application>
--root <worktree de la couche>` réussit pour API, Web et Backoffice ; contrôle
OpenAPI inclus, sans transfert de fichiers entre missions.
`check_docs.py` et `quality.py` restent en échec sur l’unique lien vers
`apps/api/app/openapi.json`, absent de cette couche avant réunion des commits.
Tests runtime et navigateur sur stack réunie non exécutés à cette étape.

Correction des skills personnels `implementer-demande` et
`analyser-decouper-demande` : dépendances de réalisation distinctes de celles des
contrôles globaux ; validation `quick_validate.py` réussie pour chacun.
Guides des étapes 02 et 03 ajustés ; aucune autorisation Git changée, AGENTS.md intact.

Point à arbitrer avant livraison : le vérificateur intégré interdit une contribution
de développement touchant `codebase-integrity/` (`check_contributions.py`, règle
existante). L’adaptation nécessaire du lanceur et de ses chemins de tests entre
dans cette interdiction ; contrôle conservé sans exception ni affaiblissement.
La conformité de livraison ne peut donc pas être annoncée.

État soumis : HEAD de base inchangé, index vide ; diff suivi des chemins ci-dessus,
`app/README.md` supprimé, `apps/README.md` et cette carte non suivis.
Aucun verdict humain ni commit créé.
Reconstitution et ordre : voir la matrice du brouillon de référence.

## Verdict humain

Le 2026-11-06 : « validé » pour les quatre cartes présentées, avec les réserves
de la restitution. Contenu revérifié contre `tmp/verification-DEM-030.json`
du dépôt principal avant indexation ; aucune modification fonctionnelle.
Validation acquise ; commit local autorisé, livraison non réalisée.

État : validée et commitée localement ; à livrer.
Commit de réalisation validé : `48eab41ca24a990957f4e178135ea220378ee80e`.

## Séparation demandée le 2026-11-09

Sur instruction humaine « deux fichiers », les changements du lanceur
`codebase-integrity/scripts/apps.py` et de `codebase-integrity/tests/test_apps.py`
sont transférés à DEM-031 / OPS-082. Les preuves antérieures ci-dessus décrivent
le résultat combiné avant séparation ; elles ne prouvent pas le fonctionnement
autonome de DEM-030 après séparation. Le périmètre restant est repris sans
changement de comportement supplémentaire depuis le commit source validé.
La validation initiale et la décision de transfert sont conservées ; ordre
de livraison et contrôles combinés à résoudre avant publication.
