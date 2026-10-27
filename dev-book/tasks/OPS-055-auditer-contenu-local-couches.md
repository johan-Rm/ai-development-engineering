# OPS-055 — Auditer le contenu local des six arbres

- État : validée ; non livrée.
- Date : 2026-10-27.
- Demande : [DEM-007](../demand/DEM-007-conformite-contenu-local-couches.md).
- Couche : devops.
- Worktree : `worktree/devops`, relatif à la racine du dépôt principal.
- Branche : `layers/devops`, existante conservée sans rebase.
- Session : référence de session indisponible ; mission définie dans ce chat.

Le chemin absolu est résolu et vérifié localement avant exécution. La disponibilité
de la couche doit être confirmée ; aucun agent délégué ni travail concurrent autorisé.

## Objectif

Produire un inventaire en lecture seule du principal et des cinq couches configurées,
y compris les contenus ignorés, non suivis, dépendances, caches et dossiers vides.
Ne pas suivre les liens hors des arbres ni entrer dans les métadonnées Git ; rendre
visibles les limites et erreurs de lecture sans les assimiler à une conformité.
Comparer aux fichiers suivis, sources actuelles et usages ; justifier chaque
classement : résidu certain proposé, contenu utile ou doute. Ne rien supprimer.
Préparer les éléments pour l’analyse et l’arbitrage de consolidation : critères de
certitude, exceptions, liens symboliques, concurrence, accès refusés et protections.

## Chemins autorisés

Cette carte et DEM-007 ; rapport nouveau
`dev-book/resources/DEM-007-audit-contenu-local.md`. Les six arbres sont des cibles
de lecture uniquement ; aucun fichier applicatif, cache ou environnement modifié.

## Dépendances et ordre

Aucun commit amont DEM-007 n’existe. Enregistrer son cadrage et cette carte par
un commit autorisé à l’étape d’implémentation avant de produire la preuve.
Résoudre d’abord la disponibilité devops et le suivi DEM-006. Aucun transfert de
travail non commité entre couches.

## Critères, tests et preuve attendue

Inventaire des six arbres avec chemins, motifs de classement, limites et état des
missions. Couvrir les exemples scripts/tests et rechercher les autres occurrences.
Vérifier que l’audit ne modifie aucun contenu ; consigner les états Git et les
protections observées sans exposer les secrets. Ce rapport prépare la consolidation,
sans inventer son verdict humain ni implémenter de nouvelle règle.

## Documentation et exclusions

Conserver dans cette carte et DEM-007 les preuves, commandes, SHA et limites.
Lire les README applicables avant chaque écriture. Préserver les travaux existants,
.env, données et worktrees. Aucun nettoyage Git global, suppression de worktree,
stash, reset destructif, force-push ou rebase implicite. Aucun verdict humain inventé.

## Réalisation

Audit effectué le 2026-10-27 :
[rapport](../resources/DEM-007-audit-contenu-local.md), script reproductible inclus.
Cadrage et cartes commités en `e7e0c4f` avant l’audit. Devops ne présente aucun
travail étranger non commité ; son dernier commit DEM-006 est ancêtre du develop
local. Branche conservée ; aucune écriture concurrente observée pendant le relevé.

Les six arbres, dépendances et caches compris, ont été parcourus deux fois :
aucune erreur de lecture ni variation des métadonnées. Dix caches Python sans
source correspondante proposés comme résidus. `.agents/` et `.aws/` restent à
expliquer ; les dépendances, montages, données, preuves et environnements sont
préservés. Aucun nettoyage effectué et aucune conformité globale annoncée.

Vérification : script Python ponctuel en lecture seule, analyse des usages dans
README, fichiers ignorés et pilotage Docker ; contrôle des liens documentaires et
des espaces du diff. Aucun test de vérificateur ni outil durable modifié, donc
pas de nouvelle suite de tests artificielle. Aucun verdict humain recueilli.
La preuve et cette carte sont portées par le commit OPS-055, SHA relevé après commit.

## Verdict humain — 2026-10-27

L’humain répond « oui » à la présentation explicite de l’audit OPS-055 seul.
Commit d’implémentation accepté : `804459950e226d125736dfb07f71e94b40c1193b`.
Le verdict couvre l’inventaire des six arbres, les dix caches sans source proposés
comme résidus, le classement et les limites annoncées (comparaison des métadonnées,
sans vérification intégrale des contenus). Aucune correction demandée.
Il ne valide ni une règle technique de suppression, ni OPS-056, ni OPS-057.
Aucun nettoyage effectué ; livraison à venir.
