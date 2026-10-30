# DEM-023 — Harmoniser les étapes des deux boucles

- Type : consolidation
- Date : 2026-10-30.
- Session de création : `01a18c38-1b13-7953-9118-aadc8cde8794`.
- Couche : devops ; worktree `worktree/devops` ; branche `layers/devops`.
- Base : `6a527151f01c097ed39b5f67791a7d6d52f8440c` ; arbre et index propres avant intervention.
- Statut : reconstituée ; contrôles de livraison réussis, PR à ouvrir.

## Décisions humaines

Deux boucles de six étapes : Interview → Analyse / découpage → Implémentation →
Vérification / arbitrage → Reconstitution → Livraison. Exactement un skill par
étape et par boucle : douze skills actifs pour les boucles. Supprimer le skill
`arbitrer-convention`, ajouter `reconstituer-consolidation` et répartir les décisions
initiales dans l’étape 02, le verdict sur le résultat dans l’étape 04.
Intégrer les prochaines PR par **Rebase and merge**, en conservant les commits
individuels, sans nouveau commit de fusion. L’historique existant reste intact.

## Périmètre et critères

Schéma interactif, skills personnels et guides/instructions associés cohérents.
Préserver les couleurs, interactions, accès clavier et rendu mobile. L’implémentation
ne crée pas de commit ; l’étape 04 crée les commits des cartes explicitement validées.
La reconstitution précède la livraison dans les deux boucles. Adapter les autorisations
et le suivi après rebase distant sans perte de travail ni réalignement de couche occupée.
Ne pas modifier les paramètres GitHub ni livrer une PR dans cette intervention.

Carte : [OPS-074](../tasks/OPS-074-harmoniser-boucles.md).
Le brief des conventions de commits DEM-024 reste distinct et hors du périmètre validé.

## Reconstitution et livraison — 2026-10-30

Instruction humaine ultérieure : « livre d'abord tes taches », autorisant la livraison
avant reprise de DEM-024. Branche `demands/DEM-023`, depuis develop `181f3cc` ;
retour prévu sur develop. Les couches restent sur leurs branches.

| Source validée | Commit reconstitué |
| --- | --- |
| `ce396be0d83f4d7d70ea4c94a645abc350aef1df` | `6bef6e8ece1f09857625b71da6a82a3521947b70` |
| `6aee39172aebb0539c0972ef98a59e3e0ec15dca` | `2dfceaba5eb0defe7e083700de492e985163e031` |

Deux conflits documentaires résolus par reprise exacte des fichiers validés
AGENTS et livraison de consolidation, sans changement de règles ni de comportement.
Qualité complète réussie : 66 tests de l’outillage, contrat API, conteneur et
mapping Symfony, contrat OpenAPI, typage et builds web/backoffice. Structure
documentaire et liens conformes après résolution ; aucun défaut d’espaces.
Rebase and merge autorisé sur GitHub ; aucune protection classique de develop
retournée par l’API. Les contrôles CI restent à vérifier avant fusion.
Le suivi ne pourra pas réaligner devops tant qu’il porte DEM-024 non livrée.

PR : https://github.com/johan-Rm/ai-development-engineering/pull/21.
HEAD présenté à l’ouverture : `cd9f1c127df4d162dbbc6fb265ae059cefded401`.
Ruleset develop actif : PR obligatoire, aucune approbation minimale ; Rebase and
merge autorisé. Contrôle CI qualité lancé ; fusion différée jusqu’à son succès.
