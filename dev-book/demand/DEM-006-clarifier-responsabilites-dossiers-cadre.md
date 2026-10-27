# DEM-006 — Clarifier les responsabilités des dossiers du cadre AIDE

- Date : 2026-10-27.
- État : validée et reconstituée ; prête pour livraison, non livrée.
- Référence de session : référence de session indisponible.
- Carte externe : aucune fournie.

## Besoin, contexte et utilisateurs

Les contributeurs humains et les agents doivent comprendre rapidement le rôle des
dossiers du cadre, savoir où ranger les documents et retrouver les configurations.
Les README actuels mêlent responsabilités, procédures et détails techniques. Le
chapitre 02 de l’index documentaire place les environnements locaux au même niveau
que les quatre piliers. La configuration des couches est située dans `config/`,
alors que l’humain souhaite la regrouper dans l’infrastructure.

## Résultat attendu

### README des dossiers

Réécrire uniquement les README suivants avec une description courte et non exhaustive
des responsabilités essentielles :

- `codebase-integrity/README.md` : fournir les contrôles déterministes des conventions
  techniques, leurs configurations et les tests des vérificateurs ; rendre visibles
  les conventions sans contrôle. Les tests applicatifs restent dans les applications.
- `design/README.md` : références graphiques, maquettes, prototypes et vérification
  visuelle des parcours. Les composants applicatifs appartiennent aux couches web et
  backoffice.
- `dev-book/README.md` : journal opérationnel du projet ; `demand/` conserve les besoins,
  le contexte et les décisions de cadrage ; `tasks/` décrit les tâches, leurs critères
  et leurs preuves ; `resources/` rassemble les ressources d’appui à la réalisation
  et à la vérification. Les guides et références durables restent dans `docs/`.
- `infra/README.md` : configuration et outils des environnements d’exécution,
  environnements locaux, isolation des services et ressources des couches, pilotage
  et vérification, conteneurs témoins du cadre. Aucun déploiement applicatif n’est
  actuellement configuré.

Ces quatre fichiers suivent exactement cette structure :

```markdown
# Nom du dossier

Description courte.

## Rôle et responsabilités

## Conventions techniques
```

La rubrique « Conventions techniques » reste vide pour le moment. Aucun chapitre
supplémentaire, inventaire exhaustif ou procédure détaillée n’est attendu.
Cette décision porte sur ces quatre README, sans migration générale des autres README.

### Responsabilité de runbooks/

Dans le README parent de `dev-book/`, définir un runbook comme une opération
exceptionnelle et ponctuelle à appliquer après le déploiement d’une livraison
précise. La procédure est conservée avec son état d’exécution et sa preuve.
Ne pas imposer de contenu minimal : remplacer la définition actuelle et la rubrique
« Rubriques d’une procédure » par cette responsabilité, dans la structure retenue.

### Hiérarchie documentaire

Dans `docs/index.md`, remplacer « 02 — Cadre » par « 02 — Les quatre piliers ».
Conserver Consolidation, Couches, IA Engineering et Documentation au même niveau ;
placer le lien « Environnements de développement locaux » sous « Couches ».
Les chemins documentaires restent inchangés pour cette réorganisation.

### Configuration dans l’infrastructure

Déplacer le dossier `config/` vers `infra/config/`, notamment `layers.json` et son README.
Adapter ses consommateurs directs :

- `codebase-integrity/scripts/worktrees.py` ;
- `codebase-integrity/scripts/process.py` ;
- `infra/stack-env.sh`, utilisé par le Makefile.

Adapter les tests et les références documentaires actives concernés. Préserver le
contenu de la configuration et le comportement des outils : correspondances entre
couches et branches, identifiants, calcul des ports et identité des environnements.
Les preuves historiques doivent rester identifiables comme historiques.

## Critères observables et preuves attendues

1. Les quatre README utilisent uniquement la structure retenue, décrivent les
   responsabilités essentielles et laissent les conventions techniques vides.
2. La responsabilité de `runbooks/` correspond à la décision humaine, sans modèle
   de procédure imposé.
3. Le chapitre 02 présente quatre piliers et rattache les environnements locaux aux couches.
4. La configuration se trouve dans `infra/config/` ; les outils et leurs tests lisent
   le nouvel emplacement sans dépendre de l’ancien.
5. Les liens et références actives concernés restent valides. Une recherche des
   anciennes références distingue les erreurs des traces historiques.
6. Les tests pertinents des worktrees, des témoins et du pilotage Make réussissent.
   Exécuter les contrôles du projet adaptés au changement, notamment
   `python3 codebase-integrity/scripts/check.py`, et conserver leurs résultats.
7. La preuve documentaire comprend la relecture du diff et la vérification des liens ;
   elle ne nécessite pas de test artificiel reproduisant le texte des README.

## Contraintes et exclusions

- Ne pas modifier les README des sous-dossiers de `dev-book/` ni les procédures existantes.
- Ne pas ajouter de conventions techniques dans les quatre README concernés.
- Ne pas modifier le comportement fonctionnel des outils lors du déplacement de configuration.
- Préserver les modifications préexistantes, les `.env`, les données et les worktrees.
- Les changements de conventions et de contrôles restent soumis au processus de
  consolidation du projet ; ce cadrage n’autorise pas leur affaiblissement.
- Cette étape crée uniquement la demande : ni cartes, ni branche, ni implémentation,
  ni commit, push, PR ou merge.

## Décisions humaines et confirmation

L’humain a demandé des README non exhaustifs respectant la structure ci-dessus,
puis a demandé de laisser leurs conventions techniques vides. Il a précisé le rôle
ponctuel des runbooks après déploiement et leur conservation avec état et preuve.
Il a limité les changements de `dev-book/` à son README parent.

Il a approuvé la hiérarchie « Les quatre piliers », avec les environnements locaux
sous Couches, puis demandé le rattachement de `config/` à l’infrastructure.

Le cadrage récapitulant les quatre README, les runbooks, l’index documentaire, le
déplacement de configuration, les preuves et les exclusions a été confirmé dans le
chat par « oui », le 2026-10-27. Cette confirmation valide le besoin, pas un résultat implémenté.

## Questions ouvertes

Aucune décision de besoin nécessaire ne reste ouverte. Le découpage devra préciser
les chemins autorisés, les dépendances par commit, les commandes de preuve et la
coordination des couches avant toute implémentation.

## Tâches issues du découpage

| Besoin | Carte | Couche | État au découpage |
| --- | --- | --- | --- |
| README du cadre, runbooks et index | [OPS-053](../tasks/OPS-053-clarifier-readme-cadre-index.md) | devops | Validée (OPS-053) |
| Configuration dans infra, consommateurs et tests | [OPS-054](../tasks/OPS-054-deplacer-config-infra.md) | devops | Validée (OPS-054) |
| README design | [UX-001](../tasks/UX-001-clarifier-readme-design.md) | design | Validée (UX-001) |

Ordre : OPS-053 puis OPS-054, séquentiellement en devops. UX-001 peut être réalisée
séparément après transmission par commit identifié du cadrage et de sa carte ;
aucune délégation automatique. Aucun transfert de travail non commité.

## Réunion prévue

Branche dédiée : `demands/DEM-006`. Worktree prévu : `worktree/DEM-006`, relatif à
la racine du dépôt principal. Création uniquement à la reconstitution, depuis une
base locale explicitement vérifiée à cette étape. Réunir les commits validés des
cartes et leurs verdicts ; jamais la branche de couche comme branche de réunion.

## Preuve du découpage — 2026-10-27

Historique de toutes les références Git locales et cartes des worktrees examinés,
sans fetch : plus grands identifiants observés OPS-052 et aucun UX. Attribution
OPS-053, OPS-054 et UX-001, sans collision identifiée.
Branches existantes layers/devops et layers/design conservées à
`779ce88da0a8e1945061cd2805bd0005ce01c13b`, identique au develop local observé.
Aucune synchronisation distante annoncée. Devops ne contient initialement que
DEM-006 non suivie, issue de cette session ; design est propre. Les dernières
missions OPS-050 à OPS-052 sont clôturées ; aucune mission concurrente identifiée.
La disponibilité doit être revérifiée à l’exécution.

Les chemins absolus résolus et vérifiés localement correspondent à worktree/devops
et worktree/design dans ce dépôt ; les affectations versionnées conservent leurs
chemins relatifs selon les README applicables. Aucune branche créée, aucun commit,
aucune implémentation et aucun test fonctionnel à cette étape. Les dépendances
sans commit restent explicitement bloquantes dans les cartes.

## Preuve d’enregistrement

Demande enregistrée dans `worktree/devops`, branche `layers/devops`, après lecture
des instructions et README applicables et vérification de l’état Git. Les demandes
présentes dans les worktrees et l’historique de toutes les références Git locales
ont été examinés, sans fetch : plus grand numéro observé, DEM-005 ; aucun doublon
correspondant à ce besoin identifié. DEM-006 est attribué à cette demande.

## Implémentation devops — 2026-10-27

OPS-053 : `56c8a954cc5ad2073b336e7d73b6622ebfcdb87f`.
OPS-054 est réalisée dans le commit portant sa carte et cette preuve ; SHA à relever
après commit. 23 tests d’outillage et tous les contrôles Make réussissent.
UX-001 reçoit le cadrage par cherry-pick identifié dans sa carte, sans copie non commitée.
Les verdicts humains et la réunion restent à effectuer aux étapes correspondantes.

## Couverture et SHA d’implémentation — 2026-10-27

- OPS-053 : `56c8a954cc5ad2073b336e7d73b6622ebfcdb87f` sur layers/devops.
- OPS-054 : `d17b1af9ecc673dcee4839c3bff5b4a326ea87f1` sur layers/devops.
- Transmission d’OPS-053 sur design : `8dafce6` (cherry-pick du commit identifié).
- UX-001 : `396e014a5f5742ef7114c93e6abfd220de3323e2` sur layers/design.

Toutes les cartes sont implémentées et commitées, à vérifier. La preuve UX-001
est dans sa version commitée sur design ; la copie de sa carte sur devops reste
celle du cadrage jusqu’à la réunion autorisée, sans copie de travail non commité.
Les deux worktrees sont propres après leurs commits d’implémentation.
La branche demands/DEM-006 n’est pas créée à cette étape ; ni réunion, ni push,
ni PR, ni merge effectué. La vérification humaine n’a pas encore eu lieu.

## Verdict humain — 2026-10-27

Après présentation des trois cartes, des résultats observables, des preuves et de
la limite quality.py avant PR, l’humain a répondu « validé » dans le chat.
Cette validation globale couvre explicitement :

- OPS-053 : `56c8a954cc5ad2073b336e7d73b6622ebfcdb87f` ;
- OPS-054 : `d17b1af9ecc673dcee4839c3bff5b4a326ea87f1` ;
- UX-001 : `396e014a5f5742ef7114c93e6abfd220de3323e2`.

Aucune correction demandée. Couverture : trois cartes validées sur trois.
La trace UX-001 est commitée dans son worktree design ; sa copie sur devops reste
historique jusqu’à reconstitution par les commits identifiés. Aucun changement de
code, nouvelle exécution de tests, reconstitution ou livraison à cette étape.
La demande DEM-007 non suivie, présente avant cette consignation, reste intacte et
exclue du commit documentaire de DEM-006.

## Preuve de reconstitution — 2026-10-27

Branche `demands/DEM-006`, worktree `worktree/DEM-006`, créés depuis la base locale
`779ce88da0a8e1945061cd2805bd0005ce01c13b`. Aucun fetch ni modification de develop.
Deux merges conservent l’ascendance des commits validés :

- `6c57c93` réunit devops jusqu’au verdict `7511267` ;
- `b40f8de` réunit design jusqu’au verdict `fc3a24b`.

Ascendance vérifiée pour `56c8a95`, `d17b1af`, `396e014`, `7511267` et `fc3a24b`.
Le cherry-pick antérieur `8dafce6` est également conservé dans l’historique design.
Les conflits add/add des seuls documents de cadrage ont été résolus depuis les
versions commitées : demande et cartes OPS de `7511267`, carte UX de `fc3a24b`.
Aucun conflit de comportement, aucune copie de travail non commité.
Les quatre README et le JSON ont été comparés aux versions validées : identiques.
Les cartes réunies contiennent les trois verdicts humains.

Contrôles de l’ensemble dans le worktree de réunion :

- `python3 codebase-integrity/scripts/check.py` : 23 tests réussis ;
- `make test` : tous les contrôles réussis, 5 identités et 15 configurations Compose,
  préservation des .env, collisions et paramètres invalides refusés ;
- liens locaux de l’index documentaire et du README de configuration : valides ;
- `git diff --check` : réussi ; état propre avant ajout de cette preuve.

Les contrôles à sockets locales ont été exécutés avec les permissions nécessaires.
Pas de preview ni de démarrage de stack applicative : cette branche de réunion ne
correspond pas à une couche d’exécution. quality.py reste requis avant PR lors de la
livraison avec ses prérequis. Les parcours applicatifs ne sont pas modifiés par DEM-006.

DEM-007 non suivie dans devops reste intacte et absente de la réunion. Design reste
propre. Aucun push, PR, merge vers develop ou réalignement des couches à cette étape.

## Préparation de livraison — 2026-10-27

Livraison complète demandée par invocation de livrer-demande. Cible origin/develop
vérifiée à `779ce88`, branche par défaut develop, merge commit autorisé par GitHub.
Historique limité aux contributions DEM-006 et verdicts validés ; branches de couche
ancêtres de la réunion, sans divergence inédite identifiée.

`python3 codebase-integrity/scripts/apps.py install all` puis
`python3 codebase-integrity/scripts/quality.py` : réussis dans worktree/DEM-006,
avec PHP, Composer et Node locaux ; 23 tests d’outillage, smoke API, lint conteneur,
schéma et contrat OpenAPI, typechecks et builds web/backoffice. Aucun contrôle
modifié pour obtenir ces résultats. Les contrôles Make de reconstitution restent
réussis et couvrent les fichiers techniques inchangés depuis cette exécution.
Index et diff vérifiés, aucun fichier étranger ni .env inclus.

Avant PR, inventaire local : develop, API, web, backoffice et design propres ;
devops contient DEM-007 non suivie. La règle impose de laisser cette couche intacte.
La PR peut être livrée, mais le suivi restera incomplet tant que devops ne pourra
pas être réalignée sans toucher à cette mission. Aucun stash, reset ou rebase prévu.

Les installations et builds ne démarrent aucune stack applicative ni déploiement.
Les contrôles GitHub de la PR restent à attendre avant fusion ; cette preuve ne
prétend pas que la PR est déjà créée ou fusionnée.
