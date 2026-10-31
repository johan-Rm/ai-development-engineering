# DEM-027 — Supprimer le test navigateur du schéma

- Type : consolidation
- Date : 2026-10-31
- Session de création : `01a18c1a-ab5a-7940-b95d-8e44ac3b92fc`
- État : OPS-078 validée et commitée ; à reconstituer.
- Confirmation humaine : « oui » après restitution du périmètre.

## Constat

Le test navigateur du schéma interactif échoue sur « Aucun contenu masqué verticalement »
(ligne 213), avec le même échec avant et après le déplacement des ressources de DEM-025.
La livraison de DEM-025 a été explicitement autorisée malgré cette limite, puis intégrée
par PR #23 au SHA `b916a7d87e7f58e8ced927951420607adcb3cc41`.
L’humain demande désormais le retrait de tout ce test, pas seulement de l’assertion.

## Proposition et périmètre confirmés

Retrait ponctuel de `codebase-integrity/tests/browser/vue-aiod.cjs` et de son
`README.md` dédié. Examiner et retirer les références actives éventuelles ;
préserver les chemins et résultats servant de preuves historiques.
Aucune convention générale excluant les tests de schémas n’est proposée.

Le schéma HTML et les tests navigateur des applications sont conservés.
Aucun remplacement du test, changement de rendu ou suppression d’un autre contrôle.
La confirmation du besoin ne vaut pas validation du résultat implémenté.

## Critères observables et vérifications attendues

- Les deux fichiers sont absents, sans commande ni lien actif les référençant.
- Les ressources HTML et les tests applicatifs restent inchangés.
- Le contrôle documentaire, `git diff --check` et la qualité restante réussissent.
- Les traces historiques et verdicts ne sont pas réécrits.

## État préexistant à reprendre

Dans `worktree/devops`, branche `layers/devops`, base `b916a7d`, les deux suppressions
non commitées ont déjà été réalisées dans cette session sur instruction explicite.
Contrôle documentaire et `git diff --check` réussis ; recherche dans .github,
codebase-integrity, app, docs, README et AGENTS : aucune référence active restante.
Ces changements sont identifiés et conservés, sans modification à l’interview.
DEM-025 reste livrée et n’est pas rouverte.

## Analyse globale — 2026-10-31

Périmètre : fichiers suivis et non ignorés de cette copie de travail, sans parcourir
les worktrees imbriqués, les dépendances ignorées, les fichiers binaires ni les `.env`.
Recherche `vue-aiod` et chemins `codebase-integrity/tests/browser` ou ancien nom
`codebase-quality-control/tests/browser` dans 270 fichiers texte. Les deux fichiers
supprimés ont également été relus depuis le HEAD, ainsi que quality.py et la CI.

- Avant suppression : seul le README dédié donnait une commande active pour ce test.
  Aucun appel depuis quality.py, les scripts applicatifs ou le workflow GitHub.
- Après suppression : occurrences restantes limitées aux demandes et cartes,
  servant de décisions ou preuves historiques ; aucune référence active à retirer.
- Les commandes `test:e2e` web et backoffice utilisent Playwright et restent exécutées
  séparément en CI. Conserver les dépendances et l’installation Chromium.
- Perte de couverture assumée par le retrait complet confirmé : interactions,
  géométrie et rendu du schéma ne seront plus vérifiés par ce script.
- Aucun autre écart ni zone essentielle inaccessible identifié dans le périmètre Git.
  Les ressources ignorées et les appels externes au dépôt ne sont pas audités.

## Options et décision acquise

Le retrait complet (deux fichiers, faible coût, couche devops seule) est retenu
sur décision humaine « Tout le test navigateur du schéma », puis confirmation « oui ».
Retirer seulement l’assertion ou réparer le rendu conserverait le test ; ces options
ne correspondent pas au périmètre choisi. Aucune exception automatique, règle générale
ou nouveau contrôle permanent n’est proposé. Les traces historiques sont conservées
comme preuves, pas comme instructions actives.

Les contrôles ponctuels de la carte vérifient l’absence des fichiers et appels actifs,
la conservation des ressources et tests applicatifs, puis la qualité existante.
Cas conforme : absence des deux fichiers et de leurs appels ; écarts : fichier résiduel,
lien actif cassé ou modification des tests applicatifs. Les occurrences historiques
ne constituent pas des écarts. Le contrôle documentaire existant reste bloquant ;
la recherche et le diff complètent la preuve, sans test reflétant seulement la suppression.

## Carte et intégration

| Carte | Couche | Mission | Dépendance | État |
| --- | --- | --- | --- | --- |
| [OPS-078](../tasks/OPS-078-supprimer-test-navigateur-schema.md) | devops | Finaliser le retrait confirmé | Aucune carte amont | Validée et commitée : `b287eca` |

Worktree `worktree/devops`, branche existante `layers/devops`, base locale
`b916a7d87e7f58e8ced927951420607adcb3cc41`, sans fetch ni alignement.
Les seuls changements préexistants sont la présente demande non suivie et les deux
suppressions identifiées de cette session. Aucun travail étranger constaté.
Identifiant OPS-078 attribué après examen de l’historique de toutes les références
locales et des cartes des worktrees : maximum OPS-077.

Prévoir `demands/DEM-027` depuis develop local vérifié dans le principal (`.`),
libre et propre, uniquement à la reconstitution après validation et commit de la carte.
Conserver les worktrees de couche sur layers/* ; retour du principal sur develop
après intégration distante autorisée. Aucune branche créée à cette étape.

## Suivi d’implémentation

OPS-078 réalisée ; preuves et limites dans la carte. Aucun commit, aucun verdict
humain sur le résultat ; vérification / arbitrage à effectuer.

## Verdict du résultat

Validation explicite « validé » d’OPS-078 le 2026-10-31. Preuves et verdict
conservés dans la carte ; la livraison reste à effectuer.

Commit local validé d’OPS-078 : `b287eca1bdbcf04bdaaa63fe19bcbb6e32ba58b7`.
