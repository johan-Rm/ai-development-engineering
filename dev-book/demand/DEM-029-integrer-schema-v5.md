# DEM-029 — Intégrer le schéma v5

- Type : développement
- Création : 2026-11-01 ; cadrage actualisé le 2026-11-02.
- Session de création et de reprise : `01a191fd-85e2-7582-b808-fe2d2089afb6`.
- Confirmation humaine : cadrage actualisé confirmé le 2026-11-02 par « parfait / validé ».
- État : cartes validées ; livraison par la PR référencée ci-dessous, suivi post-fusion dans le brouillon local.

## Besoin

Faire de la v5 le schéma interactif de référence pour les lecteurs du cadre.

## Périmètre

- Conserver tous les essais HTML v3 à v8 de `design/drafts/`, dont les deux v7 ; préserver v1 et v2.
- Garder la v5 comme référence : Documentation à gauche, Consolidation en bas, avec leurs détails associés.
- Actualiser les liens documentaires et les adaptations graphiques validées.
- Exclure la vidéo, déjà supprimée, les évolutions applicatives et toute modification de la charte officielle.

## Critères et preuves

- Liens actifs vers la v5 ; variantes consultables comme essais, sans présumer leur validation graphique.
- V5 sans défilement, texte tronqué ni chevauchement à 1280 × 720, 1366 × 768 et 1920 × 1080 ; slogan sur deux lignes et cadre symétrique.
- Numéros séparés des titres ; flèches homogènes et liaisons horizontales au contact des blocs.
- Panneaux, fermeture et clavier utilisables ; preuves visuelles et contrôles proportionnés consignés dans les cartes.
- Ne pas réintroduire le test navigateur supprimé par DEM-027. Le cadrage ne vaut pas validation du résultat.

## Tâches issues du découpage

| Carte | Couche / branche | Dépendance | État |
| --- | --- | --- | --- |
| [UX-003](../tasks/UX-003-integrer-schema-v5.md) | `worktree/design` / `layers/design` | Aucune | Validée et commitée |
| [OPS-080](../tasks/OPS-080-referencer-schema-v5.md) | `worktree/devops` / `layers/devops` | Commit UX-003 consommé, voir carte | Validée et commitée |

Reconstitution dans le principal (`.`), depuis develop local vérifié
`d365b712c92e60fad5e4f0965c376c5018719eb4` ; aucun fetch ni branche de couche déplacée.
Retour prévu sur develop après fusion distante.

## Questions ouvertes

Aucune sur le besoin. Reconstitution et livraison selon la procédure du projet, après validation des cartes.

## Reconstitution

Les verdicts et preuves restent dans les cartes. Les quatre cherry-picks sont sans conflit :

| Source validée | Commit obtenu | Rôle |
| --- | --- | --- |
| `ca13ecb669469facedb6d7fed761439c9c1dd83d` | `1b2702e10c0212aa83dcf6a097abca71e3e79b85` | UX-003 |
| `e496661a329b7cec5c0c71020c0d3e590cd718c4` | `8f3274ea3fb88cbde93858cf6b373f458ca24bb6` | Trace UX-003 |
| `5791aaea3d22cbed97741cd4f9187f26859f5d91` | `9ef9e23ade1a6b5b203edee42a835b91ab698747` | OPS-080 |
| `82d1b86a939c8855cc178505e08d7a9e9407396d` | `89edaf967450a361075c2a6eda94dfd720845e0d` | Trace OPS-080 |

Sur instruction humaine « stash le et continue », seule la modification locale de concision
d’AGENTS.md est conservée dans le stash `d3cc79fc9f3308c9fb5122ccc0ac47629abd3b99`.
Elle reste hors DEM-029, à restaurer après retour sur develop ; le stash antérieur est préservé.

Contrôles de reconstitution du 2026-11-02 : quatre patch-id identiques aux sources,
empreintes des deux cartes conformes, contrôle documentaire et `git diff --check` réussis.
AGENTS.md, v1/v2 et charte officielle inchangés par rapport à develop.
Les preuves navigateur d’UX-003 restent applicables aux HTML identiques ; aucun nouvel audit visuel.
La demande définitive et les liens des cartes ont été intégrés au commit documentaire
`f17f2d06a56089e7143413f754ccc75ea71c25b2`.

## Livraison

Cible distante vérifiée le 2026-11-02 : `origin/develop` sur
`d365b712c92e60fad5e4f0965c376c5018719eb4`, identique à la base locale.
Rebase and merge autorisé par GitHub ; aucune PR DEM-029 existante.
L’API de protection classique retourne « Branch not protected » ; aucune protection modifiée.
Ruleset actif : PR requise, discussions résolues, suppression et réécriture de develop protégées ; aucune revue obligatoire. Aucune règle modifiée.

PR : [#26](https://github.com/johan-Rm/ai-development-engineering/pull/26), vers develop.
HEAD vérifié avant ouverture : `f17f2d06a56089e7143413f754ccc75ea71c25b2`.
`python3 codebase-integrity/scripts/quality.py --commit-base d365b712c92e60fad5e4f0965c376c5018719eb4 --commit-head HEAD` : réussi (contribution et cinq commits, demandes, liens, 111 tests d’outillage, contrôles API, typechecks et builds web/backoffice).
Le test HTTP local exige une exécution hors bac à sable ; la relance complète a réussi sans modifier les contrôles.
Preuve temporaire : `/tmp/dem029-quality.log`. Les preuves UX-003 couvrent les mêmes HTML.

La présente trace ne change que ce document ; contrôler à nouveau contribution, commits et liens avant push.
Attendre la CI du HEAD final et vérifier la PR exacte avant Rebase and merge.
Correspondances réécrites et égalité des SHA des couches à consigner dans le brouillon
après preuve d’intégration distante ; ne pas modifier directement develop.
