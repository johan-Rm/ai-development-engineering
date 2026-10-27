# DEM-009 — Simplifier le workflow de développement

- Date : 2026-10-27.
- État : validée, commitée et reconstituée ; non livrée.
- Identifiant de session : `01a17c9e-d8e8-7833-805b-fe7a84cfecd0`.
- Carte externe : aucune fournie.

## Besoin et périmètre courant

L’humain souhaite un workflow simple, sans conservation ni gestion de copies de
réunion. Les contributeurs doivent assembler une demande par une branche et des
cherry-picks, puis livrer cette branche. Les modifications demandées dans cette
session aux étapes de commit et à la traçabilité sont intégrées à DEM-009.

## Résultat attendu

- Implémenter les cartes sans commit à l’étape 03 ; créer leurs commits distincts
  à l’étape 04 seulement après validation humaine explicite du contenu présenté.
- Exiger un ID réel de session dans toute nouvelle demande et carte. Conserver
  l’origine et ajouter la session intervenante en cas de reprise ; ne rien inventer.
- Bloquer une nouvelle mission sur couche sale ou occupée, mais permettre la reprise
  des changements identifiés de la même mission sans travail étranger.
- Reconstituer la demande dans un worktree existant libre et propre : créer
  `demands/<identifiant>` depuis develop, puis `git cherry-pick -x` des seuls
  commits validés, verdicts compris, dans l’ordre des dépendances.
- Ne créer aucune copie, aucun dossier ou emplacement de réunion supplémentaire.
- Après livraison, rendre le worktree à sa branche de couche et le conserver avec
  ses .env et données ; supprimer seulement les branches temporaires livrées.
- Consigner les SHA et les preuves utiles dans demande et carte, sans rapport séparé.

## Critères observables et preuves

1. Skills, AGENTS et guides sont cohérents avec ces règles. Les instructions de
   copie extérieure, d’archivage et de suppression de copie ont disparu du parcours.
2. La reconstitution utilise une branche dédiée depuis develop et des cherry-picks,
   sans merge de branches de couche à cette étape ni copie de fichiers non commités.
3. L’essai sur dépôt jetable démontre la création de branche, l’application de deux
   commits avec provenance, le contenu attendu, l’absence de nouveau worktree et
   la préservation de develop et de la branche de couche.
4. Une reprise vérifie les commits déjà appliqués pour ne pas les rejouer ; garder
   la correspondance SHA source → obtenu dans la demande ou les cartes.
5. Avant validation, aucun commit à l’implémentation. Après verdict, la vérification
   compare le contenu à celui présenté et ne committe que les cartes acceptées.
6. Les IDs de DEM-009 et OPS-061 sont réels ; les skills de création exigent cet ID.
7. Le chapitre « Conventions techniques » du README dev-book reste vide ; aucun
   rapport de clôture séparé n’est conservé. Liens et validateurs des skills passent.

## Contraintes

Préserver les .env, données, principal, couches et travaux étrangers. Aucun stash,
reset destructif, force-push, rebase implicite ou suppression de worktree réel.
Pas de modification de Codebase Integrity ni de nouveau contrôle permanent.
Les dépendances entre cartes restent fondées sur les commits issus de leur
validation ; aucune consommation de contribution non commitée d’une autre mission.
Les contrôles de livraison et protections GitHub restent applicables. La livraison
conserve l’alignement des couches prévu par le projet, sans changer les commits
sources validés. Les archives historiques ne sont pas réécrites.

## Décisions humaines

L’humain avait d’abord demandé la suppression des copies après livraison, sans
archive. Il a ensuite demandé les commits à l’étape 04, l’ID réel de session et
l’intégration de ces changements dans DEM-009 (« inclut ça dans DEM-009 »).
Il a demandé de supprimer le rapport séparé puis de laisser vide le chapitre
« Conventions techniques » du README dev-book ; ces corrections sont appliquées.

Dernière décision, prioritaire sur le nettoyage précédemment envisagé :
« la reconstitution consiste simplement à créer un branche et à cherry pick les
commits associés », avec demande de simplification du processus. Le périmètre
courant ne crée donc plus de copies à supprimer et conserve les worktrees existants.
Cette décision de fonctionnement ne vaut pas validation de l’implémentation corrigée.

## Carte et réunion de la demande

[OPS-061](../tasks/OPS-061-supprimer-copies-livrees.md) porte le périmètre cohérent,
les corrections et leurs preuves. Branche prévue : `demands/DEM-009`, depuis
develop local vérifié, dans `worktree/devops` lorsqu’il sera libre et propre après
validation/commit de la carte. Branche de retour : `layers/devops`.
Aucun autre worktree ni dossier prévu ; création de branche seulement à l’étape 05.

## Réalisation et preuve

Base : `da44ac36942165786b969c37e9b91de1f0158a23` sur layers/devops.
Modifications de cette session explicitement rattachées à la même mission,
non étrangères ; aucun commit, push, PR, reconstitution réelle ou livraison.
Essai jetable de branche/cherry-picks réussi ; détails dans OPS-061.
Skills personnels modifiés hors dépôt, disponibles dans la session et validés.
Aucun verdict humain acquis sur cette dernière version.

## Références et attribution

Historique local et worktrees examinés sans fetch à l’attribution : DEM-008 et
OPS-060 étaient les plus grands identifiants ; DEM-009 et OPS-061 conservés.
Le blocage initial de maintenance séparée a été levé par le rattachement humain.
Référence de chat : lien indisponible ; ID réel de session renseigné ci-dessus.
Aucune décision de besoin nécessaire ouverte ; la vérification de cette version reste attendue.

## Verdict humain — 2026-10-27

L’humain répond « ok c’est validé » à la présentation de la version simplifiée :
branche demands/<identifiant> depuis develop puis cherry-picks des commits validés
dans un worktree existant libre et propre, sans copie supplémentaire. Le verdict
couvre le périmètre courant de DEM-009 et OPS-061, y compris les commits à l’étape
04 après validation, la session obligatoire et les corrections demandées (README
dev-book sans conventions et absence de rapport séparé).

Les six skills personnels sont validés par skill-creator ; ils restent hors Git.
L’essai de reconstitution jetable et les liens sont vérifiés. Aucun changement
fonctionnel supplémentaire introduit pendant la consignation de ce verdict.
Commit local de carte créé à cette étape 04 ; reconstitution et livraison restent
à effectuer. Aucun push, PR ou merge autorisé par cette seule vérification.

Commit de carte validée créé à l’étape 04 : `5d69599f86b0ac1ea84be16761f1ed6cba082fdd`.

## Reconstitution — 2026-10-27

Branche `demands/DEM-009` créée depuis develop local
`da44ac36942165786b969c37e9b91de1f0158a23`, dans le worktree existant
`worktree/devops`, libre et propre avant opération. Branche de retour : layers/devops.
Aucun nouveau worktree ni dossier de réunion, aucun fetch implicite.

Cherry-picks avec -x, sans conflit :

- `5d69599f86b0ac1ea84be16761f1ed6cba082fdd` → `f94260f6c5022ce7976d4271b128a9e841ae276e`.
- `f524cfd` → `9cfa94b7f1a238d515712a368154efb12afadf20`.

Contenu final identique à layers/devops avant la présente trace documentaire,
contrôlé par `git diff --exit-code layers/devops HEAD`. Liens locaux et
`git diff develop --check` réussis ; chapitre Conventions techniques de dev-book
vide. 23 tests d’outillage réussis avec `python3 codebase-integrity/scripts/check.py`.
Aucun push, PR, merge de livraison ou alignement effectué. Livraison à venir.
