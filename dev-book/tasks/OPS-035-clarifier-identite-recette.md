# OPS-035 — Clarifier les artefacts locaux de recette

- Date : 2026-10-23.
- Statut : ✅ fait le 2026-10-24.
- Type : refactor.
- Session : non disponible (Codex).
- Mission : devops, branche `layers/devops`, worktree `/home/johan/www/lab/ai-orchestrated-development/worktree/devops`.
- Décision humaine : remplacer `.aiod/runtime/index.html` contenant du JSON par `.local/process-check/identity.json`, servi à `/identity.json`.
- Périmètre : scripts de recette, tests, Compose, exclusions et documentation associée.
- Hors périmètre : changements OPS-034 conservés sans modification, applications, migration ou suppression des anciens artefacts locaux, volumes et conteneurs actifs.
- Tests : contrôle Python du dépôt ; réponse HTTP réelle avec serveur local temporaire ; validation Compose si Docker disponible.
- Critères : identité JSON explicite, vérification et healthcheck sur le nouvel endpoint, protections contre les liens symboliques et écrasements conservées, artefacts exclus de Git/recherche/build.
- Risque : les témoins déjà lancés nécessitent une relance après adoption du changement ; les anciennes données locales sont conservées.
- Écart de processus explicite : cette modification demandée est préparée sans committer OPS-034, dont les fichiers restent distincts ; aucun commit autorisé dans cet échange.

## Réalisation et preuves

- Chemin, extension JSON, vérificateur HTTP, montage Docker et healthcheck actualisés ; exclusions et documentation synchronisées.
- `python3 codebase-quality-control/scripts/check.py` : 18 tests réussis, dont une réponse HTTP réelle à `/identity.json` et le rejet d’une identité incorrecte. Le test HTTP nécessite l’accès aux sockets locales, interdit dans le bac à sable initial ; exécution avec permission étendue réussie.
- `python3 codebase-quality-control/scripts/process.py config` : configuration Compose valide, montage `.local/process-check` en lecture seule et healthcheck `/identity.json`.
- `git diff --check` : réussi.
- Aucun conteneur démarré ou relancé ; isolation Docker complète non réexécutée. Les anciens artefacts `.aiod/` restent conservés et ignorés, aucune migration destructive.
- OPS-034 reste intacte et non commitée.

## Nettoyage local demandé le 2026-10-24

Les cinq anciennes identités générées ont été vérifiées puis transférées vers
`.local/process-check/identity.json` dans leurs worktrees respectifs ; les cinq dossiers
`.aiod/` ont été supprimés une fois vides. Aucun conteneur témoin actif avant nettoyage
(vérification Docker) ; aucun volume ni autre service modifié. Les scripts des autres
branches restent à actualiser par intégration avant de relancer leur recette.

Le 2026-10-24, sur demande, les exclusions historiques `.aiod/` ont été retirées de `.gitignore`, `.ignore` et `.dockerignore` ; `.local/process-check/` reste exclu. Vérification par `git check-ignore` et `git diff --check`.

## Mise en commit — 2026-10-24

Autorisation explicite de l’utilisateur de committer le travail accumulé. 18 tests de l’outillage réussis le 2026-10-24, dont le test HTTP réel sur /identity.json. Exécution avec permission étendue pour les sockets locales ; aucun conteneur relancé. Exclusions et nettoyage local documentés.
`git diff --check` réussi. La relecture finale par l’utilisateur reste à venir ; la réalisation technique ne vaut pas son verdict éditorial.
