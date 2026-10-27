# OPS-060 — Déplacer les anciennes copies et vérifier le rangement

- État : partiellement implémentée et commitée, à vérifier ; conservation locale de 002 non prouvée.
- Date : 2026-10-27.
- Demande : [DEM-008](../demand/DEM-008-reserver-noms-demandes.md).
- Couche : devops.
- Worktree : `worktree/devops`, relatif à la racine du dépôt principal.
- Branche : `layers/devops`, existante conservée.
- Session : référence de session indisponible ; mission définie dans ce chat.

Chemin absolu résolu localement ; vérifier branche, index, missions actives et
état Git avant chaque écriture. Un arbre propre ne prouve pas sa disponibilité.
Aucune délégation. Préserver .env, données, travaux en cours et historiques.

## Objectif, périmètre et chemins autorisés

Inventorier le principal, les cinq couches et les anciennes copies, y compris
fichiers ignorés ; distinguer les demandes légitimes de tous les autres noms DEM-*.
Déplacer hors du projet et renommer sans DEM- les copies de réunion DEM-002 à
DEM-007 si toujours présentes. Réparer les enregistrements pointant vers l’ancien
chemin avant déplacement, sans suppression de métadonnées à l’aveugle.

Chemins opérationnels autorisés : anciennes copies `worktree/DEM-002` à
`worktree/DEM-007`, métadonnées Git de ces seules copies pour réparation/déplacement,
et destinations `<temp>/aide-reunions/<projet>-reunion-002` à `-007`, à résoudre
et vérifier avant action. Ne pas déplacer les couches. Aucun écrasement si une
destination existe ; traiter la collision sans perte. Tout travail occupé est
préservé et coordonné. Les .env et contenus ignorés ou non suivis sont inclus.

Les copies anciennes peuvent contenir des rapports DEM-* : normaliser également
leurs noms et liens concernés sans changer leurs demandes ni perdre leur contenu.
Tracer tout diff local nécessaire dans ces anciennes copies, sans le confondre
avec un commit d’implémentation livré ou réécrire leur historique. Les fichiers
suivis des couches et du principal seront propagés uniquement à la livraison ;
consigner ce qui reste attendu jusqu’à leur alignement, sans modifier develop.

Chemins documentaires autorisés : cette carte, DEM-008 et
`dev-book/resources/migration-reunions-008.md`. Aucun changement de code applicatif,
aucun nettoyage global ou suppression de worktree.

## Dépendances par commit

Commits OPS-058 et OPS-059 à relever ; aucun SHA disponible au découpage.
Disponibilité de chaque copie à établir avant migration. Aucune livraison implicite.
La conformité finale des couches inclut leur alignement après fusion : la recette
pré-livraison doit distinguer cet état attendu de la migration locale déjà faite.

## Critères, contrôles et preuves

Comparer les inventaires et empreintes avant/après des fichiers suivis, ignorés
et non suivis, .env et données ; seules les modifications de noms/liens ciblées
sont admises. Vérifier git worktree list, les chemins enregistrés et git status
sur chaque copie déplacée. Prouver l’absence des anciens dossiers et inventorier
tous les noms DEM-* restant hors demand/, avec erreurs de lecture et limites.
Produire la preuve de reprise des copies sans nouvelle écriture parasite.
Contrôles qualité à la livraison : python3 codebase-integrity/scripts/quality.py ;
les tests de l’outillage sont inclus et doivent aller jusqu’à leur résultat final.
Ne pas créer de vérificateur permanent supplémentaire.

## Documentation et réalisation

Mettre à jour cette carte et DEM-008 avec les preuves et SHA avant vérification.
Lire les README applicables avant écriture. Aucun stash, reset destructif,
force-push ni rebase implicite. Aucun changement direct de tâche sur develop.
Non commencée ; aucun commit de réalisation ni verdict humain.

## Réalisation et limite — 2026-10-27

Dépendances : OPS-058 `caf3ad1`, correction `073ada7`, OPS-059 `619a84d`.
[Preuve détaillée](../resources/migration-reunions-008.md).
Six copies désormais extérieures sous un nom sans DEM-. Métadonnées anciennes
réparées. Contenus de 003 à 007 identiques au déplacement, preuves SHA-256
persistantes ; rapport et deux liens normalisés ensuite dans 007, diff local
explicite sans commit ni changement de son HEAD. Aucun worktree supprimé.

Incident : /tmp a été purgé pendant l’interruption, après déplacement de 002.
Ses fichiers suivis sont restaurés et Git fonctionne, mais la préservation des
anciens contenus ignorés ou locaux n’est pas démontrable. Ce critère reste ouvert.
Le stockage extérieur est corrigé vers un répertoire de mission persistant.
Les noms non conformes suivis du principal et des autres couches seront corrigés
à la livraison par le commit OPS-059 ; aucun changement direct de leur contenu.
Aucun verdict humain, push, PR, merge ou alignement à cette étape.
