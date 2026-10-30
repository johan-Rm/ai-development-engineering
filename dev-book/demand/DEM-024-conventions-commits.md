# DEM-024 — Clarifier les conventions des commits

- Type : consolidation
- Date : 2026-10-30.
- Session de création : `01a18c38-1b13-7953-9118-aadc8cde8794`.
- Session intervenante : `01a18cd5-5286-75e0-bd7f-b86c292bcf63`.
- Statut : OPS-075 validée humainement et commitée localement ; reconstitution à effectuer.

## Besoin

Rendre l’historique lisible et les commits compréhensibles après l’intégration par
Rebase and merge, qui conserve les commits individuels sur develop.

## Cadrage confirmé le 2026-10-30

Confirmation humaine : « perfect, confirmé ».

- Préfixes usuels (`feat`, `fix`, `docs`, `chore`…), titres et descriptions en français.
- Titre : `type(CARTE): changement`, verbe à l’infinitif, précis, sans point final.
  Utiliser `DEM-*` pour les commits documentaires portant sur la demande entière.
- Corps facultatif : expliquer le changement, sa motivation ou une contrainte ;
  rattacher le commit de carte à sa demande. Ne pas recopier les preuves ni lister
  les fichiers déjà visibles dans Git.
- Écarter les titres `wip`, `fixup` et « corrections diverses » ; nommer précisément
  les corrections et les traces complémentaires autorisées.
- Le titre de PR résume le résultat de la demande, distinct du titre des commits.
- Piste de contrôle : vérifier chaque commit de la PR, son format et ses références ;
  la pertinence du texte reste soumise à la relecture.

Exemples de forme (identifiants illustratifs, sans création de cartes) :

```text
fix(OPS-075): préserver les couches occupées après livraison

Éviter leur réalignement tant qu’une mission est en cours.

Demande : DEM-024
```

```text
docs(OPS-075): consigner le SHA du commit validé
docs(DEM-024): consigner les contrôles de livraison
```

## Éléments pour l’analyse

- L’historique consulté présente plusieurs placements de références :
  `dc77d7a` (`docs(DEM-018): …`), `fe09842` (`… (OPS-072)`),
  `06cfa71` (`… DEM-022`). Les commits de traces restent à examiner globalement.
- Source d’inspiration consultée : guide de workflow Git externe fourni dans la conversation.
  Retenir la lisibilité individuelle des commits, le corps motivé et la distinction
  commit/PR ; ne pas importer son architecture, son cycle, son versionnement,
  ses règles d’attribution ou ses commandes de réécriture.
- Préserver les décisions de [vérification](../../docs/architecture/03-developpement-loop/04-verification-arbitrage.md) :
  commits distincts des cartes validées, corrections et traces documentaires.
- À préciser en analyse : liste des types, références obligatoires selon le commit,
  cas particuliers, exemples non conformes et contrôles utiles dans l’outillage existant.

## Analyse du 2026-10-30

### Couverture et constats

Analyse sur `layers/devops`, HEAD `6aee39172aebb0539c0972ef98a59e3e0ec15dca`.
Reprise du seul fichier non suivi de cette demande ; index vide. Les autres
worktrees ne sont consultés que pour les branches et les identifiants des cartes.

- Recherche des mentions Git dans les fichiers du dépôt non ignorés, y compris
  instructions, guides, configuration, outillage, applications et ressources HTML.
  Lecture des procédures de vérification, reconstitution et livraison des deux
  boucles, des README concernés et des six skills personnels correspondants.
- `git log --all` : 270 commits accessibles, dont 56 merges ; 47 titres utilisent
  déjà la forme avec identifiant en scope. Ce chiffre mesure seulement la syntaxe,
  pas la conformité complète. Types rencontrés : `docs`, `feat`, `chore`,
  `refactor`, `fix`, ancien `merge` ; 76 titres sans préfixe reconnu.
- Exemples : `d17b1af` utilise `refactor(OPS-054): …` ; `fe09842` place la carte
  en suffixe ; `2112742` utilise un scope technique ; `6aee391` consigne un SHA.
  Les traces historiques du dev-book et les ressources originales sont à préserver.
- Aucun commitlint, hook de message ou contrôle équivalent repéré. Lecture de
  `.github/workflows/quality.yml`, `quality.py`, `check.py` et `check_demands.py` :
  la qualité vérifie le contenu, pas les messages. Le checkout CI actuel ne prévoit
  pas explicitement la profondeur nécessaire à une plage de commits.
- Les skills de vérification renvoient déjà à la convention du projet ; ceux de
  livraison n'imposent pas de format. Aucun changement de leurs autorisations requis.
- Limites : références Git locales uniquement, sans fetch ni inspection distante
  des protections ou PR. Dépendances ignorées, `.env`, objets Git inaccessibles et
  destinations réseau exclus. La syntaxe ne prouve ni la langue ni la pertinence.

### Décisions complémentaires confirmées

Verdict humain : « sorry, oui confirmé », en réponse aux cinq compléments proposés.
La demande d'implémentation reste active après cette confirmation.

1. Types autorisés : `feat`, `fix`, `docs`, `refactor`, `test`, `perf`, `build`,
   `ci`, `style`, `chore`. Choisir selon le changement principal ; réserver `style`
   au formatage sans changement de comportement. Pas de versionnement automatique
   ni de syntaxe `!` obligatoire ; expliquer une incompatibilité dans le corps.
2. Carte en scope : préfixe existant `API`, `WEB`, `BO`, `UX` ou `OPS`, suivi
   d'au moins trois chiffres ; ligne `Demande : DEM-NNN` obligatoire dans le corps,
   même sans paragraphe explicatif. Scope `DEM-*` réservé au type `docs` et aux
   seuls changements documentaires de la demande. Vérifier en livraison l'existence
   unique des documents et le rattachement de la carte à la demande.
3. Titre de PR : résultat global en français, référence `DEM-*` en suffixe ;
   aucun préfixe Conventional Commit imposé. Exemple :
   `Clarifier les conventions des commits (DEM-024)`.
4. Contrôle bloquant Python, sans dépendance ajoutée : message avant commit via
   fichier, puis chaque commit de la plage explicite base → HEAD avant PR et en CI.
   Contrôler types, scope, description non vide sans point final, références,
   titres provisoires et absence de merges dans les nouvelles contributions.
   L'examen du contenu pour `docs(DEM-*)` accepte seulement les fichiers Markdown
   de `dev-book/demand/` et `dev-book/tasks/` ; tout autre cas exige arbitrage.
5. Application prospective : uniquement les nouveaux commits à livrer, sans reprise
   des commits passés ni mécanisme d’exception historique (correction humaine :
   « pas ebsoin on ne reprendra pas les commits passés »).

La langue, l'infinitif, la précision, l'adéquation du type, la portée réelle et le
verdict humain restent des critères de relecture. Accepter les corps avec trace
`cherry picked from commit` ; ne pas imposer de liste de fichiers ou de règle
d'attribution. Une correction validée garde la même carte et produit un nouveau
commit descriptif ; une trace de SHA reste un commit documentaire autorisé.

### Options, coûts et vérification envisagée

| Option | Coût et portée |
| --- | --- |
| Documentation seule | Faible ; les formats divergents restent possibles. |
| Python intégré aux contrôles existants, recommandé | Modéré ; tests de dépôts jetables, plage Git explicite et adaptation CI. |
| commitlint et hooks | Dépendance et configuration supplémentaires ; les références aux cartes demandent encore une logique spécifique. |

Cas à tester : message de carte conforme, trace documentaire, corps facultatif
hors ligne de rattachement, trace de cherry-pick ; rejeter
type inconnu, scope technique, référence absente ou contradictoire, carte inexistante,
doublon d'identifiant, titre provisoire, merge nouveau et plage Git inaccessible.
Tester un commit invalide au milieu d'une série, une base absente et un historique
superficiel ; aucune erreur d'exécution ne doit être annoncée comme conformité.

### Impact et découpage prévu

Une mission devops cohérente suffit : convention à source unique dans le guide dédié des commits
(après correction humaine du placement initial), liens depuis AGENTS et les procédures concernées ; vérificateur, tests,
intégration qualité/CI. Les explications Git sont organisées dans leur thématique ;
le guide architectural des contrôles reste consacré au système.
Aucun code applicatif, modèle de branches, ressource graphique ou skill personnel
à modifier. La règle touche les futurs commits de toutes les couches.

Les identifiants ont été vérifiés dans l'historique local et les noms de cartes
des six copies : dernier OPS observé `OPS-074`. Revérifier avant réservation.
Carte : [OPS-075](../tasks/OPS-075-conventions-commits.md).
Reconstitution prévue : `demands/DEM-024` dans le dossier principal libre et propre,
depuis develop, avec les seuls commits validés ; aucune branche créée à cette étape.

## Limites

Ne pas réécrire l’historique ni modifier l’architecture ou les règles établies.
Le choix Rebase and merge est acquis. Le cadrage et l'analyse n'ont pas modifié
les conventions ; leur implémentation suit la carte, sans adoption finale avant
vérification humaine. Aucune carte n'a été préparée à l'interview.

## Vérification finale

Verdict humain : « validé ». Résultats : 81 tests réussis ; contrôles documentaires,
typage et espaces conformes. Exceptions historiques abandonnées et anciennes
propositions de placement remplacées par une thématique Git autonome.
Les trois corrections de liens signalées à la revue font partie de l’état accepté.
Les preuves détaillées et l’identité du contenu présenté sont conservées dans OPS-075.

Commit validé d’OPS-075 : `29f6a8dcd677e803cdcf808375f83a2cafda729d`.
