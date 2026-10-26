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
