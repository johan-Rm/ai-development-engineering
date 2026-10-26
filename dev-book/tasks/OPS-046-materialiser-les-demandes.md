# OPS-046 — Matérialiser les demandes après leur cadrage

- État : validée — résultat accepté par l’humain ; commit autorisé le 2026-10-26.
- Date : 2026-10-26.
- Demande d’origine : [DEM-001](../demand/DEM-001-materialiser-les-demandes.md).
- Couche : devops.
- Session : identifiant fiable indisponible.
- Worktree : `/home/johan/www/lab/ai-orchestrated-development/worktree/devops`.
- Branche : `layers/devops`, existante, conservée sans rebase.
- Base locale observée : `0ca44922ba429652d6f9874f2e1ed888c17bdc0f`.
- Dépendances par commit : aucune tâche amont distincte. DEM-001 est un document
  non commité de cette même mission et de ce même worktree ; aucune copie inter-worktrees.

## Objectif

Rendre cohérentes la documentation du projet et la procédure personnelle d’interview
sur la création et la reprise d’une demande durable après confirmation humaine.
Une carte unique garde ensemble ces textes et leurs preuves de cohérence.

## Périmètre et chemins autorisés

Dans le worktree affecté :

- `dev-book/README.md` : responsabilités du fichier, rubriques, nommage et attribution
  des numéros après examen des références locales et des worktrees concernés, sans fetch implicite.
- `docs/03-developpement-loop/01-interview.md` : création ou reprise après accord,
  références facultatives et absence explicite de référence de session.
- `docs/03-developpement-loop/02-decoupage.md` : références réciproques demande/tâches.
- `dev-book/demand/DEM-001-materialiser-les-demandes.md` : suivi de cette demande.
- La présente carte : réalisation, preuves et documentation effectivement modifiée.

Hors dépôt : `/home/johan/.codex/skills/interviewer-demande/SKILL.md`, modification
explicitement comprise dans le besoin confirmé. Lire les instructions applicables et utiliser
`skill-creator` lors de cette modification. Ce chemin requiert une écriture hors des racines
autorisées par le sandbox ; traiter l’autorisation technique au moment de l’implémentation.
Le skill personnel ne sera pas contenu dans un commit du dépôt : conserver une preuve lisible de sa modification.

## Exclusions

Applications, infrastructure, graphisme, connecteurs tiers, création ou modification de cartes
externes, modification d’autres skills et migration des anciennes cartes.
Ne pas ajouter de contrôle bloquant ni élargir une convention technique dans cette carte
sans le traitement de consolidation applicable. Aucun commit, push, PR ou merge implicite.

## Critères d’acceptation

1. Documentation et skill situent la demande sous `dev-book/demand/DEM-NNN-<sujet>.md`
   et imposent la confirmation humaine du cadrage avant création.
2. La reprise conserve l’identité d’une demande existante et ne produit pas de doublon.
3. Le fichier fait référence pour le besoin, le contexte, les critères observables,
   les contraintes, les décisions et les questions ouvertes ; chat et carte externe ont des rôles explicites.
4. La référence de session est conservée si disponible, explicitement indisponible sinon,
   sans inventer d’identifiant ni empêcher le cadrage.
5. La carte externe est facultative ; conserver son lien n’impose pas de connexion,
   et sa création ou sa modification requiert une instruction explicite.
6. Le découpage ajoute les liens vers les tâches dans la demande et la demande d’origine
   dans chaque carte, sans lancer automatiquement l’implémentation.
7. Les textes concordent, y compris sur l’attribution d’un numéro disponible et la distinction
   entre confirmation du besoin et validation du résultat.

## Tests et preuve attendue

- Relecture croisée des trois documents et du skill, avec matrice des sept critères.
- Scénarios de lecture : nouvelle demande avant/après confirmation, reprise, références
  chat/carte présentes ou absentes, simple lien externe sans connexion, découpage et liens réciproques.
- Vérification des liens Markdown modifiés et `git diff --check` depuis le worktree affecté.
- Exécuter les contrôles documentaires existants pertinents ; `python3 codebase-integrity/scripts/quality.py`
  avant une éventuelle PR. `python3 codebase-integrity/scripts/check.py` si l’outillage change.
- Pas de tests applicatifs : aucun comportement applicatif modifié.

## Documentation à mettre à jour

Les trois documents du périmètre et le skill personnel, puis les preuves dans cette carte.

## Réalisation et preuves

Découpage uniquement. Le 2026-10-26 : branche et base ci-dessus observées ; seul
`dev-book/demand/` était non suivi avant création de la carte, sans modification suivie.
OPS-045 est clôturée ; aucune affectation concurrente repérée dans les cartes consultées.
L’historique de toutes les références locales et les fichiers des six worktrees ont été
examinés sans fetch : plus grand identifiant observé OPS-045.
L’utilisateur demande explicitement un découpage autonome, sans confirmation intermédiaire.

### Implémentation du 2026-10-26

Documentation mise à jour : `dev-book/README.md`, guides Interview et Découpage.
Skill personnel `interviewer-demande` modifié et validé par `quick_validate.py`.
Les changements préexistants du renommage en `implementer-demande` sont préservés.
Aucun changement d’outillage, de contrôle ou de convention technique du code.

### Matrice de couverture et scénarios relus

| Critère | Preuve par lecture des textes finaux |
| --- | --- |
| 1 | README, guide Interview et skill : emplacement DEM, création après confirmation ; avant confirmation, aucune création prescrite. |
| 2 | README, guide Interview et skill : recherche préalable puis reprise du même chemin et identifiant. |
| 3 | README et skill : rubriques de cadrage, fichier de référence, chat de clarification et carte de suivi. |
| 4 | Guide Interview et skill : référence disponible conservée ; indisponibilité explicite sinon, sans invention ni blocage. |
| 5 | Les trois textes d’interview distinguent lien facultatif sans connexion et mutation externe sur instruction explicite. |
| 6 | Guide Découpage et README : liens réciproques ; DEM-001 et OPS-046 en donnent un exemple vérifié. |
| 7 | Relecture croisée : attribution après inventaire local, absence de doublon, aucune étape suivante automatique et aucun verdict de résultat déduit du cadrage. |

Ces scénarios sont des vérifications documentaires ; aucune simulation d’une future
conversation n’a été exécutée. Le skill personnel hors dépôt contient désormais les
instructions de création/reprise, de numérotation AIDE, de contenu de référence, de références
facultatives et de liens futurs vers les tâches décrites ci-dessus ; il conserve ses limites Git.

### Contrôles exécutés

- `quick_validate.py /home/johan/.codex/skills/interviewer-demande` : réussi.
- Vérification des destinations des liens locaux des cinq fichiers documentaires concernés : 26 destinations existantes.
- `git diff --check` : réussi.
- `python3 codebase-integrity/scripts/check.py` : premier essai empêché par le sandbox
  lors de l’ouverture du serveur HTTP temporaire ; relance avec cette permission, 23 tests réussis.
- Qualité applicative complète non exécutée : aucun changement applicatif et aucune PR demandée.

### Verdict humain et état de reconstitution

Le 2026-10-26, l’utilisateur a répondu « validé » à la présentation de DEM-001 / OPS-046.
Les sept critères présentés sont acceptés. Les renommages des autres skills restent hors de ce verdict.

Le 2026-10-26, l’utilisateur a demandé explicitement « committe OPS-046 ».
Le commit contient la demande, cette carte, les règles de matérialisation du dev-book
et les guides Interview et Découpage. Les changements de workflow et de renommage
réalisés ensuite sont conservés hors de ce commit, y compris dans les fichiers partagés.
Le skill personnel `interviewer-demande`, validé, reste hors dépôt et hors commit.
Branche de réunion retenue : `layers/devops`, dans le worktree de la mission.
Contrôles : 23 tests de l’outillage réussis, validation du skill et liens locaux réussis ;
relecture du diff indexé et `git diff --cached --check` avant commit.
Aucun push, PR ou merge autorisé par cette demande de commit.
