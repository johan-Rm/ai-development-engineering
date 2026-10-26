# Livraison

> Livrer les corrections et les contrôles qui renforceront les développements suivants.

## Entrée

Tâches validées et contributions réunies.

## Déroulement

L’IA exécute les contrôles de livraison, finalise les références documentaires et prépare les PRs. Chaque nouveau contrôle dispose d’une commande stable, de préconditions et d’un résultat attendu.

## Sortie

Des PRs de consolidation et des conventions techniques protégées par des vérifications reproductibles. Les contrôles bloquants doivent réussir avant la PR.

## Procédure associée

`livrer-consolidation`.

Le skill réalise directement le push, la création de PR, la fusion et le suivi après fusion
lorsque ces opérations sont demandées et autorisées. Une demande de PR n’autorise pas à elle seule
la fusion. Seules les branches confirmées libres sont réalignées sans perte de données.

## Livraison finale et nettoyage

La livraison se termine après la fusion vérifiée de la PR de la branche dédiée vers
`develop`, branche d’intégration et branche par défaut. Une promotion vers `master`
nécessite une demande explicite distincte. Attendre les contrôles et protections de la PR
et vérifier son SHA de fusion. Une fusion ne constitue pas une preuve de déploiement applicatif.

Après fusion vérifiée dans `develop`, supprimer les branches temporaires livrées locales et distantes,
libres et sans travail inédit ni autre PR ouverte, sans suppression forcée. Conserver les branches
`master`, `develop`, les couches locales `layers/*` et les branches occupées. Les couches ne sont
pas publiées sur le distant. Conserver les worktrees et leurs `.env` ; détacher uniquement celui
de la livraison s’il est propre et libre avant suppression de sa branche. Rapporter les suppressions
réelles et les exceptions. Une demande explicitement limitée conserve sa limite.
