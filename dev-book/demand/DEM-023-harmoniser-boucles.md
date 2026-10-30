# DEM-023 — Harmoniser les étapes des deux boucles

- Type : consolidation
- Date : 2026-10-30.
- Session de création : `01a18c38-1b13-7953-9118-aadc8cde8794`.
- Couche : devops ; worktree `worktree/devops` ; branche `layers/devops`.
- Base : `6a527151f01c097ed39b5f67791a7d6d52f8440c` ; arbre et index propres avant intervention.
- Statut : validée et commitée localement ; prête pour la reconstitution (étape 05).

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
