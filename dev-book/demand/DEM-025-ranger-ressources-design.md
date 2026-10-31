# DEM-025 — Ranger les ressources graphiques

- Type : développement
- Date : 2026-10-30
- Session de création : `01a18c1a-ab5a-7940-b95d-8e44ac3b92fc`
- État : reconstituée ; livraison reprise sur dérogation humaine explicite.
- Confirmation humaine : « oui » dans la session de création, après restitution du cadrage.

## Besoin et utilisateurs

Ranger les ressources pour faciliter leur consultation par l’auteur et les contributeurs :
regrouper les références graphiques et les brouillons dans design, retirer deux rapports devenus inutiles.
Typage selon [le dev-book](../README.md#types-de-demandes).

## Résultat attendu et critères d’acceptation

Depuis `dev-book/resources/` :

| Source | Action ou destination |
| --- | --- |
| `audit-contenu-local-007.md` | Supprimer |
| `migration-reunions-008.md` | Supprimer |
| `Picto-fond-noir-1000x1000.svg` | Déplacer vers `design/Picto-fond-noir-1000x1000.svg` |
| `cadre-aiod.html` | Déplacer vers `design/drafts/vue-d-ensemble-ai-development-engineering-v1.html` |
| `vue-d-ensemble-ai-development-engineering.html` | Déplacer vers `design/drafts/vue-d-ensemble-ai-development-engineering-v2.html` |

- Conserver le JPG, le carrousel, le PDF et le schéma PNG à leur emplacement actuel.
- Conserver les contenus déplacés à l’identique, sans copie résiduelle à l’ancien emplacement.
- Maintenir `design/drafts/`, `design/mockups/` et `design/wireframes/` versionnables,
  avec un `.gitkeep` lorsque nécessaire.
- Actualiser les liens actifs, index, responsabilités documentaires et chemins des tests ;
  préserver les traces historiques sans liens actifs cassés vers les rapports supprimés.

## Contraintes et exclusions

Aucune refonte graphique ni modification des sources originales conservées.
Respecter les couches [design et devops](../../docs/architecture/02-cadre/couches/organisation.md),
leurs travaux préexistants et les transmissions par commits identifiés.
La disponibilité des couches sera vérifiée à l’affectation ; l’interview n’en réserve aucune.
Le déplacement ne définit pas une convention générale de rangement des futures ressources.

## Vérifications attendues

Comparer les empreintes avant/après des trois fichiers déplacés ; vérifier les destinations,
les suppressions, les liens actifs et la conservation des autres sources.
Exécuter le contrôle navigateur existant de la vue interactive depuis son nouveau chemin.
Appliquer les [contrôles du dépôt](../../codebase-integrity/README.md)
proportionnés aux changements ; qualité complète avant PR.

## Questions ouvertes

Aucune sur le besoin confirmé.

## Cartes et verdicts

| Carte | Verdict | Commit source | Commit reconstitué |
| --- | --- | --- | --- |
| [UX-002](../tasks/UX-002-accueillir-ressources-graphiques.md) | « validé » après correction du README | `1faf42c` | `d2ed24a` |
| [OPS-076](../tasks/OPS-076-rappeler-structure-readme.md) | « validé » | `f14ada8` | `66fc8c4` |
| [OPS-077](../tasks/OPS-077-finaliser-rangement-ressources.md) | « validé » avec limite navigateur connue | `7cfedb9` | `a68ac96` |

Traces également reconstituées : `e015fd7` → `d1e6d78` (UX-002),
`005b207` → `ffa9f84` (cartes devops). Provenances conservées par cherry-pick `-x`.
Les preuves et verdicts détaillés restent dans les cartes.

## Décisions complémentaires

- Ajout explicite demandé par l’humain : rattacher le rappel de structure des README
  dans AGENTS à une petite tâche ; OPS-076 porte ce changement, sans nouvelle section
  de README ni modification des autorisations Git.
- La carte de rangement envisagée sous OPS-075 devient OPS-077 : OPS-075 a été
  attribuée à DEM-024 avant sa matérialisation.
- Décision humaine « recommandation validé » : reprendre la source actuelle comme v2,
  pour préserver les évolutions d’OPS-074 absentes de la première copie UX-002.
  OPS-077 applique cette correction ; le SVG et la v1 conservent leurs contenus.
- Transmission de UX-002 à devops explicitement autorisée : `1faf42c` → `82a79f6`,
  `e015fd7` → `50a4d34`. Ces copies ne sont pas rejouées une seconde fois.

## Reconstitution — 2026-10-31

Principal libre et propre sur develop, base locale vérifiée
`cf68451f0a1f4054b1aca4bb075dce6a64fbec19`. Branche `demands/DEM-025`
créée dans le principal (`.`), sans fetch ni nouveau worktree. Les cinq commits
ci-dessus ont été appliqués sans conflit, dans l’ordre. Les couches restent sur layers/*.
Le principal retrouvera develop après intégration distante autorisée.
Le brouillon `tmp/demande-ranger-ressources-design.md` est conservé, sans copie
non commitée d’une mission de couche. La demande et les liens documentaires de
reconstitution restent non commités pour la livraison.

## Contrôles et limites

Contrôle documentaire et `git diff --check` réussis après actualisation des liens.
Comparaison des trois ressources avec leurs sources dans le develop de base :
identiques ; les quatre originaux restants sont inchangés. Les chemins du test
navigateur ciblent la v2.
La limite navigateur
préexistante acceptée à la vérification demeure ; elle ne constitue pas un contrôle
réussi. La qualité complète et les contrôles de commits restent requis avant PR.

## Préparation de livraison — 2026-10-31

Cible distante vérifiée par fetch : `origin/develop` et develop local identiques
à la base de reconstitution. Inventaire : les cinq couches propres ; design conserve
`e015fd7`, devops `005b207`, les autres couches sont sur la base develop.
Aucune couche déplacée, aucun push effectué.

`python3 codebase-integrity/scripts/quality.py` : réussi hors bac à sable après
un premier échec d’ouverture du serveur HTTP temporaire dans celui-ci. Types des
demandes, liens documentaires, 81 tests de l’outillage, contrat API, conteneur, mapping,
OpenAPI, types et builds web/backoffice réussis. Le contrôle des commits est exécuté
séparément après ce commit documentaire, contre la cible distante vérifiée.

Le contrôle navigateur propre à OPS-077 reste en échec préexistant (voir sa carte).
La validation humaine avec cette limite ne vaut pas réussite du contrôle requis.
Livraison arrêtée avant push/PR ; correction à implémenter puis à faire valider
avant reprise, sans affaiblissement du test. Aucun alignement après intégration
ni suppression de branche effectué.

## Dérogation humaine de livraison — 2026-10-31

Instruction explicite : « tu doit outre passé ça et ensuite nous devons supprimer
ce test ». L’humain autorise la poursuite de DEM-025 malgré le seul échec navigateur
préexistant décrit dans OPS-077. Cet échec demeure consigné ; aucun succès
ni exception de contrôle automatique inventé. Les autres contrôles et protections
GitHub restent applicables. La suppression du test est demandée pour la suite,
après cette livraison.
