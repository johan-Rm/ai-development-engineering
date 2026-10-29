# DEM-018 — Préparer le dépôt par un SETUP exécutable

- Date : 2026-10-29.
- Session de création : `01a18808-fc0b-7aa0-b084-441015c3c7ad`.
- État : cadrage confirmé par « confirmé » ; reconstituée sur `demands/DEM-018` ; à livrer, avec réserve Ubuntu neuf.
- Couche concernée : devops ; mission définie au découpage ci-dessous.

## Besoin et utilisateurs

Permettre à un développeur sous Ubuntu avec VS Code et Codex de préparer ce dépôt,
de démarrer ses applications puis de commencer une première demande avec les agents.
SETUP présente les commandes à exécuter, sans explications ; seul le dernier
chapitre renvoie vers la documentation. Les courtes actions manuelles nécessaires
restent indiquées. Ne plus employer le sigle dans le texte courant.

## Périmètre et décisions

Réécrire SETUP selon le contenu validé ci-dessous. Créer la cible Make
`setup-worktrees` en réutilisant `codebase-integrity/scripts/worktrees.py` :
préparer les cinq worktrees par défaut sur leurs branches `layers/*` depuis
`develop`, générer le workspace avec le principal et ces cinq worktrees, et
installer l’alias Bash `vscode-worktree-ai-powered-development-engineering`.
L’alias doit être utilisable à l’étape suivante ; inclure son activation nécessaire.
Préserver worktrees, configurations, autres alias, `.env` et données existants.

Le nom d’alias remplace la proposition de commande `code <workspace>` ; le nom
technique du fichier workspace reste à résoudre à l’implémentation en tenant
compte de l’existant. La génération et l’installation réutilisent une configuration
existante compatible sans l’écraser. Maintenir les références affectées par la
réécriture, sans recopier la documentation dans plusieurs fichiers.

L’alias personnel existe déjà selon [DEM-015](DEM-015-renommer-alias-workspace.md) ;
cette demande rend sa préparation disponible aux nouveaux clones.
Le dépôt privé de skills n’a pas pu être inspecté dans cette session : vérifier
son accès et l’installation réelle avant de conclure à la réussite.

## Contenu validé de SETUP

Les sept chapitres et leur contenu ont été approuvés un à un dans le chat avant
confirmation du cadrage. Référence du résultat : [SETUP](../../SETUP.md), livré par
les commits validés ; ne pas en conserver de copie dans cette demande.
Le commentaire préparatoire « à créer » est retiré une fois la commande réalisée.

## Critères et preuves attendues

- Respect des sept chapitres et de leur ordre, du titre et de l’introduction validés.
- Aucune création imposée de `~/projets` ; aucun renvoi documentaire avant le chapitre 7.
- Installation courte de Docker par les paquets Ubuntu ; choisir et relever la
  version Ubuntu de recette où les paquets requis et Python sont disponibles.
- Sur clone neuf, une commande Make prépare les cinq worktrees, le workspace
  et son alias ; la commande du chapitre 5 ouvre le workspace attendu.
- Une relance préserve les éléments existants et n’écrase pas une configuration
  incompatible ; une impossibilité est signalée sans altérer le travail présent.
- Parcours complet obligatoire sur un Ubuntu neuf : installation, clone, skills,
  worktrees, workspace, applications accessibles aux trois adresses et démarrage
  de l’interview dans Codex. Conserver les résultats et limites dans les futures cartes.
- Contrôles documentaires et tests adaptés à l’outillage modifié selon les
  [points de contrôle](../../docs/architecture/01-codebase-integrity/points-de-controle.md#exécuter-dans-ce-dépôt),
  dont `python3 codebase-integrity/scripts/check.py` et qualité avant PR.

Aucune installation ni recette Ubuntu neuf effectuée à l’interview.
Le cadrage confirmé ne vaut pas validation d’une implémentation.

## Exclusions et points restant à résoudre

Exclus : autres systèmes, autres outils IA, onboarding de couches personnalisées,
publication du dépôt de skills, modification fonctionnelle des applications.
Pas de question de besoin ouverte. Version Ubuntu de recette, moyen de fournir
cet environnement neuf et détails d’installation de l’alias restent à résoudre
lors de la préparation technique ; ne pas déclarer le parcours vérifié sans preuve.

## Tâches issues du découpage

| Carte | Mission | Dépendances | État |
| --- | --- | --- | --- |
| [OPS-070](../tasks/OPS-070-setup-commandes.md) | devops / `layers/devops` | Aucune | Validée et commitée avec réserve Ubuntu neuf |

Une carte couvre l’outillage, les sept chapitres et la recette ; aucune dépendance
intermédiaire non commitée. Branche existante conservée sur la base locale
`57ae8c5623a9610e70a40f5589bcdaac977e1b21`, commune avec develop ; index et arbre
propres avant création de la carte, aucune autre mission active identifiée.
Maximum OPS observé : 069 dans toutes les références locales et fichiers concernés,
sans fetch. Session de découpage identique à la session de création.

Reconstitution prévue dans le principal (`.`), libre et propre, sur
`demands/DEM-018` créée depuis develop local vérifié après validation humaine et
commit d’OPS-070 ; cherry-pick du commit validé, puis matérialisation de
`dev-book/demand/DEM-018-setup-commandes.md`. Retour du principal sur develop après
fusion distante. Aucune branche créée, aucun commit ni implémentation au découpage.


## Suivi d’implémentation — 2026-10-29

OPS-070 réalisée dans son worktree et sa branche affectés, sans commit.
Preuves, fichiers présentés et limites : voir la carte ci-dessus. Les tests locaux
réussissent ; la recette complète sur Ubuntu neuf reste non exécutée, empêchant
la satisfaction de tous les critères. Aucune validation humaine du résultat.

## Vérification humaine — 2026-10-29

Verdict « validé » sur OPS-070, avec la réserve Ubuntu neuf présentée explicitement.
Commit local : `856defdd41224150dc5a0c33d79cdbb135038576`. Empreintes vérifiées avant commit ;
preuves et réserve conservées dans la carte. Demande à reconstituer, non livrée.

## Reconstitution — 2026-10-29

Principal libre sur develop, index et arbre propres avant création ; base locale
`57ae8c5623a9610e70a40f5589bcdaac977e1b21`. Aucune mission active identifiée dans
le principal ; DEM-017 clôturée. Aucun fetch ni copie de travail d’une couche.
Session intervenante identique à la session de création.

| Source validée | Commit obtenu par cherry-pick avec provenance |
| --- | --- |
| `856defdd41224150dc5a0c33d79cdbb135038576` | `2112742ef4eee5512555b465342053378555ce15` |
| `02e64ef21e2a157bba448a7ebd40e027541ff03d` | `a90b6243cd85c88bc06e862e9a4faed0e5bceb26` |

Cherry-picks sans conflit ; arbre commité identique à `layers/devops`, vérifié
par `git diff --exit-code layers/devops HEAD`. Brouillon matérialisé après les
cherry-picks et conservé dans tmp/. Carte reliée à cette demande définitive.
Seules ces traces documentaires restent non commitées pour la livraison.
Principal maintenu sur `demands/DEM-018`, retour prévu sur develop après fusion ;
worktrees de couche conservés sur `layers/*`. Aucun push, PR ni fusion effectué.
Réserve Ubuntu neuf acceptée à la vérification et toujours ouverte.

Contrôles de reconstitution : 30 tests d’outillage réussis, 5 liens locaux
valides et `git diff --check` réussi. Qualité complète restant à exécuter avant PR.

## Préparation de livraison — 2026-10-29

Les cinq couches sont propres et sans nouvelle mission active identifiée ;
DEM-016 reste cadrée sans carte affectée observée. Base origin/develop vérifiée
après fetch : `57ae8c5623a9610e70a40f5589bcdaac977e1b21`. Merge commit permis
par GitHub, cible et branche par défaut develop.

Les deux seuls commits divergents de devops sont ceux d’OPS-070 validée, appliqués
par cherry-pick à la reconstitution. Rattachement ciblé de cet historique prévu
pour permettre les avances rapides finales, avec contrôle d’égalité de l’arbre.

Rattachement effectué : `435a3b9b3753ad1471d8657885ac775f28f21c90`. Conflit
limité à la carte documentaire, résolu avec la version reconstituée ; arbre
strictement identique au premier parent, vérifié avant commit.

Qualité complète locale réussie : `python3 codebase-integrity/scripts/quality.py`,
code 0 ; journal `/tmp/dem018-quality.log` : 30 tests d’outillage, contrat API,
types et builds web/backoffice. Aucun changement fonctionnel depuis ces contrôles ;
seules les traces documentaires de livraison sont ajoutées. Réserve Ubuntu neuf
acceptée maintenue. PR vers develop, fusion par merge commit après checks requis.

PR : https://github.com/johan-Rm/ai-development-engineering/pull/17 ; source
`demands/DEM-018`, cible `develop`. Fusion par merge commit après checks et
protections satisfaits ; SHA de fusion et alignement effectifs à consigner
dans le brouillon conservé sous tmp/.
