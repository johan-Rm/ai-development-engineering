# OPS-056 — Vérifier et nettoyer les résidus locaux certains

- État : sans suite — extension de périmètre abandonnée par décision humaine.
- Date : 2026-10-27.
- Demande : [DEM-007](../demand/DEM-007-conformite-contenu-local-couches.md).
- Couche : devops.
- Worktree : `worktree/devops`, relatif à la racine du dépôt principal.
- Branche : `layers/devops`, existante conservée sans rebase.
- Session : référence de session indisponible ; mission définie dans ce chat.

Le chemin absolu est résolu et vérifié localement avant exécution. La disponibilité
de la couche doit être confirmée ; aucun agent délégué ni travail concurrent autorisé.

## Objectif

Implémenter uniquement les règles approuvées en consolidation pour inventorier,
classer et nettoyer les résidus certains, avec résultats par arbre et erreurs
explicites. Prévoir une consultation sans suppression et le nettoyage automatique
retenu. Préserver les contenus utiles ; tout doute bloque la fin de livraison.
Revérifier la cible et sa disponibilité avant mutation ; protéger les liens et
les chemins sortant du périmètre selon l’arbitrage. Ne pas nettoyer les six arbres
réels pendant cette carte : utiliser des dépôts et fichiers jetables.

## Chemins autorisés

`codebase-integrity/scripts/`,
`codebase-integrity/tests/` (hors tests navigateur), leurs README et le README
`codebase-integrity/README.md` ; cette carte et DEM-007. Limiter les changements
aux fichiers du nouveau contrôle et à son raccordement aux lanceurs pertinents.
Toute configuration supplémentaire doit être identifiée avant extension du périmètre.

## Dépendances et ordre

Commit d’audit OPS-055 à relever après réalisation ; aucun SHA disponible.
Arbitrage humain de consolidation et sa trace commitée obligatoires : définition
exacte du résidu certain, exceptions, protections et contrôles. Ne pas considérer
le cadrage DEM-007 comme cet arbitrage. Si l’implémentation est portée par des
cartes de consolidation, référencer leurs commits et éviter toute réalisation en double.

## Critères, tests et preuve attendue

Tests sur dépôts jetables : suppression d’un résidu approuvé, conservation de
sources et caches utiles, .env, données et travail non suivi ; cas incertain sans
suppression avec résultat bloquant ; cible occupée, lien et erreur d’accès selon
les règles arbitrées. Vérifier la seconde exécution sans changement et l’absence
d’effet hors cible. Exécuter `python3 codebase-integrity/scripts/check.py` et
`python3 codebase-integrity/scripts/quality.py` ; consigner résultats et limites.

## Documentation et exclusions

Conserver dans cette carte et DEM-007 les preuves, commandes, SHA et limites.
Lire les README applicables avant chaque écriture. Préserver les travaux existants,
.env, données et worktrees. Aucun nettoyage Git global, suppression de worktree,
stash, reset destructif, force-push ou rebase implicite. Aucun verdict humain inventé.

## Réalisation

Non commencée. Aucun commit d’implémentation ni verdict humain.

## Correction de périmètre — 2026-10-27

L’humain demande uniquement le nettoyage des résidus évoqués. La création d’un
contrôle réutilisable est abandonnée ; les objectifs précédents restent une trace
historique et ne constituent plus une mission. Aucun code ni contrôle modifié.
