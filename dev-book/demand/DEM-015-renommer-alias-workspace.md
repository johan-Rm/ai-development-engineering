# DEM-015 — Renommer l’alias d’ouverture du workspace

- Type : développement
- Session intervenante (typage DEM-022) : `01a18b94-1588-7021-869d-d11d9ff6ba72`.
- Date : 2026-10-29.
- Session de création : `01a1869b-17bd-7292-a890-d6785556af2c`.
- Cadrage confirmé dans le chat par « go » avant documentation.
- État : reconstituée sur `demands/DEM-015` ; à livrer.

## Besoin et périmètre

Pour l’utilisateur du shell local, remplacer dans `~/.bash_aliases` l’alias
`aide-code-workspace` par `vscode-worktree-ai-powered-development-engineering`.
Le nouveau nom explicite l’outil et le projet visés.
Conserver exactement la commande actuelle et son workspace cible.

## Décisions et critères d’acceptation

- Supprimer la définition de l’ancien alias, sans compatibilité.
- Le nouvel alias exécute `code /home/johan/www/lab/ai-development-engineering/aide.code-workspace`.
- La syntaxe de `~/.bash_aliases` est valide ; dans un shell neuf chargé avec ce fichier,
  le nouvel alias est défini et l’ancien absent.
- Vérifier humainement l’ouverture du même workspace dans VS Code.

## Contraintes et exclusions

Préserver les autres alias. Ne modifier ni le workspace ni les fichiers du dépôt.
Le fichier cible est personnel et extérieur au dépôt : sa modification reste
soumise aux permissions de l’environnement lors de l’implémentation.
Aucune documentation durable du dépôt ne référence cet alias selon la recherche locale.
Aucun changement d’interface ou de service applicatif n’est concerné.

## Questions ouvertes

Aucune sur le besoin confirmé.

## Tâches issues du découpage

| Carte | Couche / branche | Couverture | Dépendances |
| --- | --- | --- | --- |
| [OPS-068](../tasks/OPS-068-renommer-alias-workspace.md) | devops / `layers/devops` | Tous les critères | Aucune |

OPS-068 validée par « validé » le 2026-10-29 ; preuves et limites dans la carte.
Commit local des traces : `e885f489f1f542c8b1f3056dd77775854be90d1e`.
Couche propre et sans mission active
identifiée avant création ; branche existante conservée, sans fetch ni rebase,
sur la base locale `69a709acb15f10a5390867380a88b9cd11fade75`, commune avec develop.

Reconstitution prévue après validation humaine et commit des traces d’OPS-068 :
créer `demands/DEM-015` depuis develop local vérifié dans le principal (`.`),
libre et propre, puis cherry-pick du commit validé. Le fichier personnel reste
hors Git. Après fusion distante, retour du principal sur develop ; la couche
conserve `layers/devops`. Aucune branche de demande créée au découpage.

## Reconstitution

Principal libre et propre sur develop avant création ; base locale vérifiée
`69a709acb15f10a5390867380a88b9cd11fade75`. Branche `demands/DEM-015`
créée dans le principal ; cherry-picks avec provenance, sans conflit ni fetch.

| Commit source validé | Commit obtenu |
| --- | --- |
| `e885f489f1f542c8b1f3056dd77775854be90d1e` | `b37aae43103068a822215810afe3a2e8f62274f7` |
| `0d27b4b70c269460008f969bc4caf5f37a50423c` | `46e31d906404bcb1f3176cbfaf1ab378ede594d2` |

La demande matérialise le brouillon conservé sous `tmp/` ; la carte porte les
preuves du changement personnel hors Git. Retour du principal sur develop
prévu après fusion distante. Aucun push ni livraison à cette étape.

Contrôles de reconstitution : carte cherry-pickée identique à la source validée,
liens locaux demande/carte résolus, `git diff --check` et `bash -n` réussis.
Seules la demande matérialisée et l’actualisation du lien de la carte restent
non commitées pour la livraison. Aucun contrôle applicatif exécuté : changement
personnel et traces documentaires uniquement.

## Livraison

Qualité complète : `python3 codebase-integrity/scripts/quality.py`, code 0,
journal `/tmp/dem015-quality.log` ; tests d’outillage, contrat API, types et builds
web/backoffice réussis. Premier essai limité par le sandbox (socket HTTP refusée),
puis réussite avec permissions adaptées, sans modifier les contrôles.

Historique devops rattaché par `c1983643fb8259866e409fd361d2b23f9cf1c3a6` :
seuls les deux commits validés d’OPS-068 étaient divergents. Conflit documentaire
résolu en conservant la carte reconstituée ; arbre strictement identique au premier
parent vérifié. Les cinq couches sont propres, sans nouvelle mission identifiée.
Base distante develop vérifiée identique à la base locale ; merge commit permis.
Le fichier personnel n’est pas livré par Git : seuls la demande et ses preuves le sont.

PR : https://github.com/johan-Rm/ai-development-engineering/pull/15 ; source
`demands/DEM-015`, cible `develop`. Fusion par merge commit après réussite des
checks et protections distants. Suivi effectif de fusion et d’alignement à
consigner dans le brouillon conservé sous tmp/.
