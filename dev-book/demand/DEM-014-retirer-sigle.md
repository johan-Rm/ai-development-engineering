# DEM-014 — Retirer le sigle des supports actuels

- Date : 2026-10-29.
- État : validée et commitée avec réserve navigateur ; reconstituée, à livrer.
- Session de création : `01a18693-b0a7-7651-8d7c-9197f32ab602`.

## Besoin et utilisateurs

Le sigle « AIDE » se confond avec le mot français « aide ». Les lecteurs des
supports actuels doivent identifier le cadre sans cette ambiguïté ni répétition
inutile de son nom long : **AI-powered Development Engineering**.

## Décisions et périmètre

Retirer le sigle des textes actuels du dépôt : documentation, consignes,
commentaires de configuration, schéma et libellés accessibles. Adapter le test
associé au schéma. Employer le nom long dans les titres et premières
présentations ; ailleurs, supprimer le sigle ou employer une formulation
contextuelle telle que « le cadre », « le projet » ou « le schéma ».

Conserver les noms techniques et chemins, notamment `aide.code-workspace`, les
anciennes demandes et cartes historiques et les brouillons antérieurs. Les
skills personnels hors dépôt restent hors périmètre. Aucun changement
fonctionnel applicatif ni nouvelle identité graphique n'est demandé.

Cette décision remplace, pour les supports actuels, la conservation du sigle
prévue par [DEM-010](DEM-010-corriger-titre-long-aide.md).

## Critères observables et preuves

1. La recherche sensible à la casse du mot entier `AIDE` ne trouve plus de
   sigle dans les textes actuels concernés ; les occurrences historiques et
   techniques conservées sont distinguées dans la preuve.
2. Les reformulations restent naturelles, précises et sans répétition inutile
   du nom long ; les noms techniques et chemins restent identiques.
3. Le schéma et ses libellés accessibles sont cohérents ; sa lisibilité est
   vérifiée sur ordinateur et mobile.
4. L'attente textuelle du test associé est adaptée et son résultat consigné.
   Appliquer les contrôles proportionnés selon les
   [points de contrôle](../../docs/01-codebase-integrity/points-de-controle.md).

## Confirmation humaine

L'humain choisit de conserver les noms techniques puis d'adapter chaque
occurrence au contexte. Il confirme la restitution du cadrage par « go » dans
le chat le 2026-10-29. Cette confirmation porte sur le besoin, pas sur une
implémentation.

## Questions ouvertes

Aucune question de besoin restante. L'inventaire définitif des textes et les
commandes de vérification seront précisés aux étapes suivantes.

## Tâches issues du découpage

| Carte | Couche / branche | Critères | Dépendances | État |
| --- | --- | --- | --- | --- |
| [OPS-067](../tasks/OPS-067-retirer-sigle-supports-actuels.md) | devops / `layers/devops` | 1 à 4 | Aucune | Validée et commitée ; réserve navigateur |

Une seule contribution éditoriale couvre la demande. La carte fait référence
pour les chemins, contrôles et preuves. Reconstitution réalisée dans le principal
(`.`), sur `demands/DEM-014`. Retour prévu du principal sur develop après fusion
distante ; les worktrees de couche conservent layers/*.

Verdict du 2026-10-29 : « validé », sur OPS-067 et ses réserves présentées.
Commit d'implémentation : `700d22f51695598536ab274cc5cc316973da2e9f`.
La carte conserve les preuves et limites ; sa trace de SHA est commitée séparément.

## Trace de création

Brouillon créé dans le `tmp/` ignoré du dépôt principal, sur `develop`, index
et arbre suivis propres avant écriture. Aucun besoin identique trouvé dans les
brouillons et documents des worktrees ; maximum DEM observé : 013 dans les
références Git locales et fichiers consultés. Aucun fetch ni changement de
branche ; aucune carte ni implémentation créée.


## Reconstitution — 2026-10-29

Principal libre, index et arbre propres sur develop avant création de branche.
Base locale vérifiée : `93c392bb78289097bf9c73b9553b890358f75696`.
Aucun fetch ; cherry-picks avec provenance, sans conflit :

| Source validée | Commit obtenu |
| --- | --- |
| `700d22f51695598536ab274cc5cc316973da2e9f` | `b7ace0e882a0aef34696d8dd36a48febaf1214b6` |
| `b1d2fd24dd244c1af87227d208095ec346b3182a` | `c7869c48210d057073a0801341c63f16dcadb086` |

Brouillon matérialisé après cherry-picks, identité et session conservées ; liens
adaptés. Document définitif inclus dans le commit documentaire de livraison. Aucune copie de contribution non commitée d'une couche.

Contrôles de reconstitution : arbres commités de HEAD et layers/devops
identiques (`git diff --exit-code layers/devops HEAD`), `git diff --check`
réussi ; trois liens locaux du document définitif valides ; 23 tests
d'outillage réussis via `python3 codebase-integrity/scripts/check.py` hors
sandbox. Réserve navigateur conservée ; qualité complète restant requise avant
PR. Aucune nouvelle exécution navigateur justifiée : contenu identique à la
carte validée. Aucun push, PR ou fusion à cette étape.


## Préparation de livraison — 2026-10-29

Les cinq couches sont libres, propres et sans mission nouvelle identifiée dans
cette session. Seule devops porte les deux commits validés de cette demande.
Après vérification d'égalité des arbres, historique rattaché par merge ciblé
`8b89f630ffcf6c66210b71106e9d37bd1f203f0c` : aucun changement de contenu,
avances rapides finales possibles. develop local et origin/develop pointent
sur la base de reconstitution après fetch. Fusion par merge commit, permise
par GitHub et conforme aux livraisons précédentes.

Qualité complète locale : `python3 codebase-integrity/scripts/quality.py`
réussie (code 0), journal `/tmp/dem014-quality.log` : 23 tests d'outillage,
contrat et contrôles API, types et builds web/backoffice. Réserve navigateur du
schéma maintenue selon le verdict humain ; aucun contrôle affaibli.

PR : https://github.com/johan-Rm/ai-development-engineering/pull/14
Source `demands/DEM-014`, cible `develop` ; fusion par merge commit après
réussite des checks et protections distants. Suivi de fusion et d'alignement
à consigner dans le brouillon conservé sous tmp/.
