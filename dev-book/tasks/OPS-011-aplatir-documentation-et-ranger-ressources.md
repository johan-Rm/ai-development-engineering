# OPS-011 — Mettre la documentation à plat et ranger ses ressources

- **Créée le** : 2026-10-23.
- **Session** : non disponible (Codex).
- **Statut** : ✅ fait le 2026-10-23.
- **Type** : docs.
- **Demande** : ne conserver que des fichiers `.md` dans `docs/`, retirer le niveau redondant `aiod/` et ranger les ressources dans le dossier prévu.
- **Mission** : devops, branche `layers/devops`, worktree `worktree/devops`.
- **Dépendance par SHA** : OPS-010, `10e158a1fcddd21cfd7345d0f63a9f32eb042186`.
- **Tests** : inventaire avant/après et empreintes des ressources, contrôle des liens et références actives, `python3 codebase-quality-control/scripts/check.py`, test navigateur `codebase-quality-control/tests/browser/vue-aiod.cjs` et `git diff --check`. Aucun nouveau test applicatif : migration documentaire ; adapter uniquement les chemins du test existant.
- **Réf** : `docs/README.md`, `docs/aiod/README.md`, `docs/aiod/sources/README.md`, `dev-book/resources/README.md`, `dev-book/README.md`.

## Contexte

Le dossier `docs/aiod/` ajoute un niveau redondant dans un projet consacré à AIOD.
Il mélange des guides Markdown, deux représentations HTML et des sources PDF, HTML et PNG.
Le dossier de ressources prévu par le projet est `dev-book/resources/`.

## Périmètre

- Déplacer les guides Markdown de `docs/aiod/` directement sous `docs/`.
- Fusionner les deux index de documentation en un seul `docs/README.md`, sans perdre les entrées utiles.
- Déplacer les cinq ressources non Markdown (les deux schémas HTML, le carrousel HTML, le PDF et le PNG) directement dans `dev-book/resources/`, sans modifier leur contenu.
- Intégrer les informations de provenance et les liens du README des sources dans le README des ressources.
- Retirer les dossiers `docs/aiod/` et `docs/aiod/sources/` après récupération de leur contenu.
- Corriger les liens relatifs, références actives et consignes qui utilisent les anciens chemins, y compris les références du test navigateur.
- Documenter la convention : guides Markdown directement dans `docs/`, ressources dans `dev-book/resources/`.

Chemins autorisés : `docs/`, `dev-book/resources/`, la présente carte,
les fichiers Markdown suivis du dépôt qui référencent les chemins déplacés (dont `AGENTS.md`,
`CLAUDE.md`, `ia-engineering/` et les README), et
`codebase-quality-control/tests/browser/vue-aiod.cjs` pour adapter les chemins uniquement.
Les fichiers des autres worktrees sont exclus.

## Hors périmètre

Aucun changement fonctionnel des applications, aucun remaniement des schémas ou de la charte.
La charte officielle dans `design/` et les ressources déjà rangées ailleurs ne sont pas déplacées.
Aucun changement des couches, des environnements, des dépendances ou des branches.
Aucune suppression de contenu de référence, aucune réécriture des preuves historiques.
Aucun commit, push ou PR au titre de ce cadrage.

## Décisions de cadrage

- Structure explicitement demandée par l’utilisateur : documentation à la racine de `docs/`, exclusivement en Markdown.
- Destination résolue à partir du README existant : `dev-book/resources/` ; conserver les noms des ressources, sans recréer un sous-dossier `aiod/`.
- Fusionner les README plutôt que provoquer une collision ou perdre des informations de provenance.
- Adapter le test navigateur existant au nouveau chemin pour maintenir la preuve d’ouverture de la vue.
- Les mentions d’anciens chemins dans des preuves historiques peuvent rester si leur nature historique est claire ; les liens de navigation doivent fonctionner.
- Session fiable non fournie : repli explicite `non disponible (Codex)`.

## Règles et cas limites

Inventorier les destinations avant déplacement et arrêter en cas de collision imprévue.
Comparer les empreintes des cinq ressources avant et après migration ; conserver les sources sans modification.
Vérifier les dépendances locales des HTML avant déplacement et signaler tout conflit entre conservation
à l’identique et fonctionnement ; ne pas retoucher silencieusement les originaux.
Les aspects API, données, permissions applicatives, états d’interface, performance et traduction
sont sans objet. Le risque principal est la rupture de liens ou du test navigateur.
Aucun aval fonctionnel prévu.

## Documentation impactée

Index `docs/README.md`, guides déplacés, `dev-book/resources/README.md`,
`dev-book/README.md`, consignes des assistants et README qui pointent vers ces documents.
La carte conserve les preuves ; les conventions durables sont écrites dans les README concernés.

## Définition de terminé

- [x] `docs/` contient uniquement des fichiers `.md` directement à sa racine, sans sous-dossier `aiod/`.
- [x] Tous les guides et toutes les entrées utiles des deux index sont conservés.
- [x] Les cinq ressources sont dans `dev-book/resources/` avec les mêmes empreintes.
- [x] La provenance et les liens des sources sont conservés dans le README des ressources.
- [x] Les liens locaux et références actives utilisent les nouvelles destinations ; les mentions historiques restent contextualisées.
- [x] Les chemins du test navigateur sont actualisés et la vue s’ouvre depuis sa nouvelle destination.
- [x] Les contrôles prévus sont exécutés et leurs résultats ou limites sont consignés.

## Réalisation et vérification — 2026-10-23

- Worktree devops repris sur le commit OPS-010 prévu ; seule la carte OPS-011 était non suivie. Aucun fetch ni changement de branche.
- Neuf fichiers Markdown directement sous `docs/`, aucun sous-dossier ; index fusionnés et provenance des originaux conservée dans le README des ressources.
- Cinq ressources déplacées sans modification ; aucune dépendance locale `src` ou `href` dans les trois HTML déplacés.
- 77 liens Markdown locaux vérifiés : aucune cible absente (fragments internes non contrôlés).
- Recherche dans les guides, consignes et README courants : aucune référence restante à `docs/aiod/`. Les anciennes mentions des cartes restent historiques selon la convention du dev-book.
- `python3 codebase-quality-control/scripts/check.py` : 17 tests réussis ; `git diff --check` réussi.
- Le test navigateur référence les deux nouvelles adresses (bureau et mobile). Premier essai : Playwright absent du worktree ; réutilisation des dépendances déjà installées à la racine, puis constat de Chromium absent. Installation temporaire tentée séparément.

### Empreintes SHA-256 préservées

- `dev-book/resources/cadre-aiod.html` : `a298d5a4038ccfa10b5b1b2bffcf793b6d4014b94a8c33de0f78910e6f9b17c0`.
- `dev-book/resources/vue-d-ensemble-ai-development-engineering.html` : `cf7738f347eb1a2a2320d80f8614a0f25496b4fcddbf8b735f9fd055d53e85ed`.
- `dev-book/resources/aiod-approche_1.png` : `7ee50e6853bcb098f81b5f377c3295380215b853876fd810dff465ff08d836df`.
- `dev-book/resources/AIOD-carrousel-v1.html` : `2f97871ede64898d4e95f738baf4d5c5e57cefcac713fc9bb279804dbfa21f41`.
- `dev-book/resources/AIOD.pdf` : `8be76b159b0698b3f8a2d25e8b5d09908747754885886f8c344d11ac4262cb4b`.

### Vérification navigateur terminée

- Chromium téléchargé dans `/tmp/ops011-playwright` après expiration puis nouvelle acceptation de la revue automatique ; bibliothèques libnspr4, libnss3 et libasound2t64 extraites dans `/tmp/ops011-libs/root`, sans installation système.
- Commande réussie hors bac à sable (celui-ci bloque le démarrage de Chromium) :

```sh
LD_LIBRARY_PATH=/tmp/ops011-libs/root/usr/lib/x86_64-linux-gnu PLAYWRIGHT_BROWSERS_PATH=/tmp/ops011-playwright node codebase-quality-control/tests/browser/vue-aiod.cjs app/web/targets/app
```

- Résultat : 12 actions, ouverture au clic/clavier/tactile, fermeture, focus, dimensions bureau/mobile et panneau superposé vérifiés. Dépendances Playwright existantes de l’arbre principal utilisées en lecture seule ; aucun changement des dépendances du projet.
- Aucun écart au cadrage, aucun point croisé restant. Aucun commit, push ou PR.

## Clôture — 2026-10-23

Résultat validé par la demande de commit de l’utilisateur. Guides et ressources migrés,
index fusionnés, références actives et test navigateur adaptés. Preuves réunies dans
le commit OPS-011 ; aucune publication ni travail restant dans ce périmètre.
