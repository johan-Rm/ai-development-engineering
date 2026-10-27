# OPS-057 — Intégrer la conformité locale au suivi de livraison

- État : Bloquée : contrôle commité, arbitrage et disponibilité des cibles manquants.
- Date : 2026-10-27.
- Demande : [DEM-007](../demand/DEM-007-conformite-contenu-local-couches.md).
- Couche : devops.
- Worktree : `worktree/devops`, relatif à la racine du dépôt principal.
- Branche : `layers/devops`, existante conservée sans rebase.
- Session : référence de session indisponible ; mission définie dans ce chat.

Le chemin absolu est résolu et vérifié localement avant exécution. La disponibilité
de la couche doit être confirmée ; aucun agent délégué ni travail concurrent autorisé.

## Objectif

Documenter et raccorder le contrôle au suivi de livraison selon l’arbitrage.
Recetter le principal et les cinq couches, nettoyer uniquement les résidus certains
avec l’outil validé et conserver une preuve avant/après. Un doute ou une couche
occupée bloque la conclusion de livraison. Vérifier la conservation des fichiers
utiles et une seconde exécution sans changement. Le nettoyage local approuvé est
une opération de recette traçable, pas un changement de tâche sur develop.

## Chemins autorisés

`docs/03-developpement-loop/06-livraison.md`,
`docs/01-codebase-integrity/points-de-controle.md`,
`docs/02-cadre/couches/index.md`, `SETUP.md`, README de l’outil,
`dev-book/resources/DEM-007-recette-conformite.md`, cette carte et DEM-007.
`AGENTS.md` seulement si une consigne du projet doit changer après arbitrage.
Les six arbres ne sont des cibles de nettoyage que pour les chemins explicitement
reconnus par les règles approuvées ; aucun changement de leurs fichiers suivis,
.env, données ou travaux en cours. Ne pas modifier les skills personnels.

## Dépendances et ordre

Commit OPS-056 et trace de son verdict humain à identifier avant recette réelle ;
aucun SHA disponible. Commit d’arbitrage de consolidation requis. Coordination
explicite des six arbres avant toute mutation ; le SHA seul ne prouve pas leur
disponibilité. Le mode d’accès à l’outil depuis les cibles doit être documenté,
sans copie de travail non commité ni synchronisation Git implicite.

## Critères, tests et preuve attendue

Le guide de livraison exige le résultat de chaque arbre et interdit d’annoncer
le suivi terminé si une cible reste incertaine ou occupée. Fournir l’inventaire
avant/après, les actions exactes et leurs motifs, la préservation des contenus
utiles et la seconde exécution sans changement. Rejouer les contrôles pertinents
si leur raccordement évolue, vérifier liens et diff documentaire. Ne lancer ni
push, PR, merge ni réalignement des branches dans cette carte.

## Documentation et exclusions

Conserver dans cette carte et DEM-007 les preuves, commandes, SHA et limites.
Lire les README applicables avant chaque écriture. Préserver les travaux existants,
.env, données et worktrees. Aucun nettoyage Git global, suppression de worktree,
stash, reset destructif, force-push ou rebase implicite. Aucun verdict humain inventé.

## Réalisation

Non commencée. Aucun commit d’implémentation ni verdict humain.
