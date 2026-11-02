# OPS-080 — Référencer le schéma v5

- Demande : DEM-029 ; type : développement.
- Création : 2026-11-01 ; reprise : 2026-11-02.
- Session de création et de reprise : `01a191fd-85e2-7582-b808-fe2d2089afb6`.
- État : validée par l’humain ; commit local à créer.
- Besoin et critères : `tmp/demande-schema-v5.md`, dans le dépôt principal.
- Demande définitive future : `dev-book/demand/DEM-029-integrer-schema-v5.md`, à la reconstitution.
- Couche : devops ; worktree : `worktree/devops` ; branche conservée : `layers/devops`.
- Base locale observée : `e1ad28338cdc77c3ba00759c462afd7f6d7bef2e` ; aucun fetch ni alignement.

## Objectif et chemins autorisés

Faire pointer les trois liens actifs vers la v5 préparée par UX-003.
Chemins : `README.md`, `dev-book/README.md`, `docs/architecture/index.md` et cette carte.
Conserver rubriques, ordre, références historiques et rôle de sommaire de l’index.
Aucun changement des schémas, de la charte, du workflow, des tests ou d’AGENTS.md.

## Disponibilité et dépendance

Reprise de cette carte seule ; aucun fichier étranger modifié, index vide.
Préserver intégralement les commits existants de DEM-028, dont la tête observée.
Dépendance consommée par cherry-pick tracé :
`ca13ecb669469facedb6d7fed761439c9c1dd83d` → `eeda1fa2afa5f12c4748d6db2b7dded4c1169703`.
Cette dernière tête est la base de l’implémentation OPS-080 ; les commits de DEM-028
restent intacts. Aucun fichier non commité transféré, aucun rebase ni fetch.

## Critères, contrôles et preuve

Les trois liens actifs ciblent la v5 et se résolvent ; les essais restent conservés.
Exécuter `python3 codebase-integrity/scripts/check_docs.py` et `git diff --check`.
Vérifier les rubriques des README et l’absence d’explication ajoutée à l’index.
Consigner résultats et limites ici ; aucun nouveau test persistant.

## Reconstitution et verdict

Voir le brouillon pour l’ordre et la branche de réunion.
Implémentation du 2026-11-02 : trois liens actifs vers la v5 ; liens historiques v1/v2 conservés.
Diff soumis : `README.md`, `dev-book/README.md`, `docs/architecture/index.md` et cette carte non suivie.
Verdict humain du 2026-11-02 : « oui », après restitution de vérification d’OPS-080.
Empreinte revérifiée avant commit ; aucun changement fonctionnel depuis la présentation.

Contrôles du 2026-11-02 : `python3 codebase-integrity/scripts/check_docs.py` et
`git diff --check` réussis ; trois cibles présentes et titres Markdown inchangés.
Index relu : aucun contenu explicatif ajouté. Ascendance de la base initiale vérifiée.
Empreinte SHA-256 des trois documents concaténés en ordre lexicographique :
`ca0884b1003dd3b0ac4febdfb0dc4bad5436a7a8eb44d3c2bfd4e94e8563fb95`.
Limites : contrôle documentaire et relecture du diff ; pas de nouvel audit visuel,
les HTML sont ceux du commit UX-003 validé.
