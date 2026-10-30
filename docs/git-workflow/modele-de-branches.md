# Modèle de branches

> Comprendre le rôle des branches de couche, de demande, d’intégration et de production.

Le dépôt sépare le travail des couches, l'assemblage d'une demande et l'intégration.
`develop` rassemble les contributions livrées ; `master` représente la production ;
`main` reste historique.

Chaque couche possède une branche durable `layers/<couche>` et un worktree
`worktree/<couche>`. Le nom identifie la responsabilité de la couche, tandis que
la carte précise la tâche et son périmètre. Un seul agent y écrit à la fois.
La disponibilité dépend aussi des missions engagées : un arbre propre peut être occupé.

Les changements restent non commités pendant l'implémentation. Après validation
humaine, chaque carte produit son commit avec les changements, tests, documentation,
preuves et verdict. Une correction ultérieure validée ajoute un commit ; elle ne
remplace pas celui déjà accepté.

Une demande est ensuite reconstituée dans le dossier principal, sur une branche
`demands/<identifiant>` créée depuis develop. Les seuls commits validés y sont
appliqués par cherry-pick avec leur provenance, dans l'ordre des dépendances.
Cette branche rassemble le contenu de la future PR sans fusionner les branches
de couche ni copier leur travail non commité. Si un conflit modifie le résultat
validé, une décision humaine est nécessaire.
