# OPS-036 — Centraliser les instructions propres au projet

- Date : 2026-10-23.
- Statut : ✅ fait le 2026-10-24.
- Type : docs.
- Session : non disponible (Codex).
- Mission : devops, `layers/devops`, `/home/johan/www/lab/ai-orchestrated-development/worktree/devops`.
- Demande validée : supprimer ia-engineering/, retirer les procédures déjà portées par les skills et conserver dans AGENTS.md les seules consignes spécifiques utiles, sans le rendre exhaustif.
- Périmètre : AGENTS.md, suppression des quatre documents ia-engineering/, liens actifs README/docs/configuration et précisions utiles dans les documentations existantes.
- Hors périmètre : audit complet de la documentation de l’écosystème, modification des skills, applications et cartes historiques.
- Tests : liens locaux, absence de référence active au dossier supprimé, parsing TOML et diff --check. Aucun nouveau test de code pour cette correction documentaire.
- Décisions : préserver les exceptions du dépôt aux procédures des skills ; garder les détails de recette dans sa documentation ; préserver les changements OPS-034 et OPS-035 non commités. Aucun commit demandé.

## Preuves

- ia-engineering/ supprimé ; les conventions propres au dépôt et les exceptions aux skills sont centralisées dans AGENTS.md, sans recopier les procédures de commit, PR et après-merge.
- README racine, index docs, adoption et commentaire de configuration actualisés.
- Liens locaux des quatre documents modifiés vérifiés ; TOML valide et vide de réglages.
- Recherche des références actives au dossier supprimé dans AGENTS.md, README.md, docs/, infra/, codebase-quality-control/ et .codex/ : aucune.
- `git diff --check` : réussi. Aucun test de code relancé pour ce changement documentaire.
- Les références dans les cartes et ressources historiques sont conservées. Aucun commit ni audit global de la documentation entrepris.

## Mise en commit — 2026-10-24

Autorisation explicite de l’utilisateur de committer le travail accumulé. Les quatre fichiers ia-engineering/ sont supprimés. Les règles utiles sont dans AGENTS.md, intégré avec ses liens définitifs au commit documentaire OPS-037. Les références historiques aux fichiers supprimés restent des traces de cadrage.
`git diff --check` réussi. La relecture finale par l’utilisateur reste à venir ; la réalisation technique ne vaut pas son verdict éditorial.
**Tests** : sans objet pour de nouveaux tests exécutables — instructions et documentation uniquement ; liens actifs et TOML vérifiés dans le lot final.
