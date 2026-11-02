# UX-003 — Intégrer le schéma v5 et ses variantes

- Demande : DEM-029 ; type : développement.
- Création : 2026-11-01 ; reprise : 2026-11-02.
- Session de création et de reprise : `01a191fd-85e2-7582-b808-fe2d2089afb6`.
- État : validée et commitée localement ; à livrer.
- Besoin et critères : [DEM-029](../demand/DEM-029-integrer-schema-v5.md).
- Couche : design ; worktree : `worktree/design` ; branche conservée : `layers/design`.
- Base locale observée : `531f4db38c93f4fab61bc190ec4d26c46062e57b` ; aucun fetch ni alignement.

## Objectif et chemins autorisés

Préparer la v5 comme référence et conserver les autres versions comme essais.
Les seuls travaux préexistants repris sont les huit HTML ci-dessous et cette carte.

- `design/drafts/vue-d-ensemble-ai-development-engineering-v3.html`.
- `design/drafts/vue-d-ensemble-ai-development-engineering-v4-a-material-doux.html`.
- `design/drafts/vue-d-ensemble-ai-development-engineering-v4-b-plan-architectural.html`.
- `design/drafts/vue-d-ensemble-ai-development-engineering-v5.html`.
- `design/drafts/vue-d-ensemble-ai-development-engineering-v6-essai-critique.html`.
- `design/drafts/vue-d-ensemble-ai-development-engineering-v7-b-motion-signature.html`.
- `design/drafts/vue-d-ensemble-ai-development-engineering-v7-essai-motion.html`.
- `design/drafts/vue-d-ensemble-ai-development-engineering-v8-hallmark-statique.html`.

Autoriser aussi `design/charte-graphique.md` pour les adaptations validées.
Préserver v1/v2 et la charte officielle ; exclure vidéo, applications, outillage et AGENTS.md.

## Référence graphique et cohérence

Documenter les adaptations de la v5 : bleu acier IA, olive du socle et des sorties,
finition satinée, motifs, logo et positions des badges. Les essais restent distincts.
Vérifier les douze chemins de skills dans les panneaux et corriger les noms obsolètes,
sans modifier les étapes ni les autorisations. Préserver les contrôles pré-PR du projet
et distinguer leur rôle de celui du CI/CD.

## Dépendances et transmission

Aucun commit amont requis : reprise des essais de cette session, sans travail étranger.
Après vérification humaine, transmettre à OPS-080 le SHA du commit UX-003 validé,
encore absent. Aucun transfert de fichiers non commités ni rebase implicite.

## Critères, contrôles et preuves

Appliquer les critères du brouillon. Consigner le rendu v5 aux trois résolutions,
les interactions, les flèches et l’absence d’erreur JavaScript ; vérifier l’inversion
des badges et leurs panneaux. Vérifier syntaxe, ressources et chemins des huit HTML.
Pour les v7, contrôler aussi replay et réduction des mouvements ; la v8 reste statique.
Exécuter `python3 codebase-integrity/scripts/check_docs.py` et `git diff --check`.
Relire le diff graphique, sans nouveau test navigateur persistant (DEM-027).

## Réalisation et verdict

Implémentation du 2026-11-02, sur le HEAD indiqué ci-dessus ; index resté vide.
Diff soumis : les huit HTML non suivis listés, cette carte et `design/charte-graphique.md`.
Skills et textes des panneaux corrigés ; focus, Tab et retour au déclencheur assurés.
Les adaptations v5 sont documentées, sans nouvelle conception graphique.

Preuves :

- Chromium via `aide-app-browser:ec4e123090`, script temporaire `/tmp/ux003-browser.cjs` : 23 panneaux par HTML, clavier, contenu sans JS, aucune erreur JS ni requête réseau ; deux fontes chargées par document.
- V5 aux trois formats prévus : aucun texte hors bloc ni défilement, slogan de deux lignes ; bandes égales de 64 / 68,30 / 80px, badges haut/bas de 34px, écart des huit flèches aux blocs de 0px. Badges Documentation et Consolidation vérifiés avec leurs panneaux.
- Deux v7 : replay fonctionnel, animations terminées et réduction des mouvements respectée ; v8 sans animation.
- `node --check` sur les scripts exécutables extraits : réussi. SVG analysables, IDs uniques, deux fontes embarquées décodées et douze chemins de skills existants dans chacun des huit HTML.
- `python3 codebase-integrity/scripts/check_docs.py` et `git diff --check` : réussis ; limites documentaires dans `docs/README.md`. v1/v2 et charte officielle inchangées.

Captures et rapport temporaires : `/tmp/ux003-v5-{1280,1366,1920}.png`,
`/tmp/ux003-browser.json` et `/tmp/ux003-static.json` ; aucun test persistant ajouté.
Empreinte SHA-256 des huit HTML concaténés en ordre lexicographique :
`a7f348cf2de1a1e19964e79e31131d2359058cc9366739219d140d9d7caf1642`.
Limites : revue Chromium desktop, sans audit exhaustif WCAG ni validation graphique des essais.
Verdict humain du 2026-11-02 : « validé », après présentation d’UX-003 seule.
Empreinte du lot revérifiée avant commit ; aucune modification fonctionnelle depuis la présentation.
La validation couvre UX-003 ; OPS-080 reste à implémenter après consommation du commit.

Commit validé UX-003 : `ca13ecb669469facedb6d7fed761439c9c1dd83d`.
