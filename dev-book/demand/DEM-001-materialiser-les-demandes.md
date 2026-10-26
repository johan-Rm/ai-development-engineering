# DEM-001 — Matérialiser les demandes

- Date : 2026-10-26.
- État : cadrage confirmé ; résultat validé par l’humain ; commit autorisé, livraison non effectuée.
- Couche concernée : devops, maintenance du cadre AIDE.
- Session de chat : référence indisponible dans le contexte fourni.
- Carte externe : aucune référence fournie.

## Contexte et problème observé

Le cadre prévoit déjà `dev-book/demand/` pour les besoins, le contexte et les décisions
de cadrage. Il reste à expliciter comment l’interview produit et maintient cette trace,
indépendamment de la conversation et de l’outil de suivi.
Les humains et les agents doivent pouvoir retrouver une même référence de cadrage,
sans versions contradictoires entre le fichier, le chat et une carte externe.

## Résultat attendu

Après confirmation humaine du cadrage, le skill `interviewer-demande` crée ou reprend
un fichier Markdown sous `dev-book/demand/`, nommé `DEM-NNN-<sujet>.md`.
Ce fichier fait référence pour le besoin, le contexte, les critères observables,
les contraintes, les questions ouvertes et les décisions humaines.
Le chat sert à construire et préciser la demande ; une carte externe sert à son suivi.
Les références aux tâches sont ajoutées lors du découpage ; ces tâches restent
dans `dev-book/tasks/` et renvoient à la demande d’origine.

## Périmètre et contraintes

- Adapter la documentation du projet et le skill personnel `interviewer-demande`.
- Créer le fichier après confirmation du cadrage, sans création automatique de brouillon avant cet accord.
- Reprendre le fichier existant lorsqu’il correspond à la même demande.
- Conserver une référence au chat lorsqu’elle est disponible ; signaler explicitement son indisponibilité sinon, sans inventer d’identifiant.
- Permettre un lien facultatif vers une carte externe sans imposer de connexion à l’outil tiers.
- Exiger une instruction explicite pour créer ou modifier cette carte externe.
- Ne pas créer de tâches, de branches ou enchaîner une autre étape pendant cette interview.
- Le cadrage confirmé ne vaut pas validation d’un résultat implémenté.

## Critères observables et preuves attendues

1. La procédure et la documentation désignent le même emplacement, le même nommage
   et le même moment de création après confirmation humaine.
2. Une demande peut être reprise sans créer un second fichier pour le même besoin.
3. Le document contient le besoin, le contexte, les critères de réussite, les contraintes,
   les décisions et les questions restantes.
4. L’absence de référence de session est explicite et n’empêche pas le cadrage.
5. L’absence de carte externe n’empêche pas le cadrage ; un simple lien n’exige pas de connexion.
6. Le découpage prévoit des références réciproques entre demande et tâches.
7. La relecture de la documentation et du skill, appuyée sur les cas avec et sans
   références facultatives et sur la reprise d’une demande, établit leur cohérence.

Les contrôles documentaires pertinents seront déterminés lors de la préparation
du changement. Aucun test applicatif ou déploiement n’est requis par ce besoin documentaire.

## Décisions humaines

Le 2026-10-26, l’humain a choisi par questions interactives :

- création après confirmation du cadrage ;
- nommage `DEM-001-<sujet>.md`, généralisé en `DEM-NNN-<sujet>.md` dans la restitution ;
- périmètre couvrant la documentation du projet et le skill personnel.

L’humain a ensuite répondu « Je confirme ce cadrage » à la restitution regroupant
ces décisions, la responsabilité du fichier et les règles relatives aux références facultatives.

## Questions restantes

Aucune question de besoin bloquante. Les modalités d’attribution des numéros et les
emplacements documentaires sont précisés dans OPS-046 et les documents mis à jour.
L’évolution concerne le cadre AIDE : le traitement par consolidation a été proposé,
sans lancement ni arbitrage supplémentaire dans cette interview.

## Tâches issues du découpage

| Carte | Couche | Couverture | Ordre et dépendances |
| --- | --- | --- | --- |
| [OPS-046 — Matérialiser les demandes](../tasks/OPS-046-materialiser-les-demandes.md) | devops | Critères 1 à 7 : documentation et skill personnel, scénarios et preuves de cohérence | Carte unique ; aucune tâche amont distincte |

Découpage réalisé le 2026-10-26. L’utilisateur a demandé explicitement de réaliser
cette étape de façon autonome, sans validation intermédiaire du découpage.
Branche existante conservée : `layers/devops`, dans
`/home/johan/www/lab/ai-orchestrated-development/worktree/devops`.
Implémentation réalisée dans OPS-046 ; preuves et contrôles consignés dans la carte,
résultat validé par l’humain le 2026-10-26 (« validé »).
Branche de réunion : `layers/devops`. Commit OPS-046 autorisé le 2026-10-26.


## Correction du workflow demandée après vérification

L’utilisateur a approuvé le déplacement des commits locaux dans l’implémentation,
le commit documentaire des verdicts à la vérification et le choix de la branche de réunion
au découpage. Les skills, AGENTS.md, le dev-book, les guides et les textes de la vue AIDE
ont été alignés. Le découpage est autonome ; le verdict humain se recueille dans le chat.
Les demandes explicites de push, PR et merge restent nécessaires.

Branche de réunion retenue pour cette demande à une seule couche : `layers/devops`,
worktree `/home/johan/www/lab/ai-orchestrated-development/worktree/devops`.
Les mentions précédentes de blocage décrivent l’ancien fonctionnement. Aucun SHA de
contribution n’a encore été créé dans cet échange ; la reconstitution reste à effectuer.
Validation des quatre skills modifiés et 23 tests de l’outillage réussis ; `git diff --check` réussi.


## Preuve de reconstitution — 2026-10-26

Carte unique OPS-046, validée par l’humain. Commit de contribution et trace du verdict :
`1cde387108f7db8e3c064ce578f8e90b0489e225`, présent à la tête de `layers/devops`.
Ascendance vérifiée : aucune intégration ni répétition de commit nécessaire.
Les cinq fichiers du commit correspondent au périmètre initial ; destinations des liens
locaux du commit vérifiées et contrôle du diff du commit réussi.
Les 23 tests déjà exécutés ont réussi ; aucun code ou contrat applicatif modifié.
Le skill personnel validé reste hors dépôt. Les corrections de workflow et renommages
non commités restent exclus de cette réunion. Livraison non engagée ; arbre de travail
non propre à cause de ces changements conservés. Aucun push, PR ou merge effectué.


## Reconstitution sur branche dédiée — 2026-10-26

La décision humaine ultérieure remplace le choix initial de réunion sur la branche de couche.
La branche dédiée `demands/DEM-001`, créée lors de la reconstitution, pointe sur
`1cde387108f7db8e3c064ce578f8e90b0489e225` (OPS-046 et trace de validation humaine).
Ascendance et absence de différence avec le commit validé vérifiées ; contrôle du diff réussi.
Aucun commit rejoué, aucun merge ni nouveau commit nécessaire. Les corrections locales
ultérieures restent sur `layers/devops`, hors de la branche dédiée. Cette dernière n’est
actuellement attachée à aucun worktree. La livraison n’a pas été lancée.
Le skill personnel d’interview reste hors Git ; les 23 tests exécutés précédemment ont réussi.


## Préparation de livraison — 2026-10-26

Qualité complète exécutée avec succès au SHA `1cde387108f7db8e3c064ce578f8e90b0489e225`
dans une copie locale temporaire isolée, après installation des dépendances :
23 tests d’outillage, contrôles API, types et builds web/backoffice. Parcours navigateur non exécutés.
Le diff cumulé vers `develop` comprend aussi OPS-045 (`7c6499d`, `0ca4492`),
soit trois commits et 23 fichiers au total. Cette inclusion n’a pas été autorisée pour DEM-001.
Publication en attente d’arbitrage du périmètre et d’autorisation explicite de push/PR.
Le constat de reconstitution précédente portait uniquement sur la présence d’OPS-046 ;
il ne prouvait pas l’exclusivité du diff vers l’intégration. Aucun push, PR ou merge effectué.


## Autorisation de livraison globale

L’utilisateur confirme que les travaux antérieurs sont validés et demande de tout aligner.
La livraison inclut le socle antérieur, OPS-046 et les corrections de workflow explicitement
demandées dans cet échange : commits pendant l’implémentation, verdict documentaire,
branche dédiée créée à la reconstitution et livraison autonome. Ces corrections sont réunies
par un commit documentaire distinct ; les skills personnels restent hors du dépôt.
