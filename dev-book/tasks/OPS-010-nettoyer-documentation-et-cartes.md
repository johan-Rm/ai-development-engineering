# OPS-010 — Séparer la documentation durable et les cartes de tâches

- **Créée le** : 2026-10-23.
- **Session** : non disponible (Codex).
- **Statut** : ✅ fait le 2026-10-23.
- **Type** : docs.
- **Demande** : analyser puis rectifier le rangement de `docs/`, les cartes qui y figurent et les traces de l’ancienne couche de maintenance ; cadrage accepté dans la conversation.
- **Mission** : couche devops, branche `layers/devops`, worktree `worktree/devops`.
- **Dépendance par SHA** : `e90631fc77fae1a7519f1059f58c0c396c5473c9`, état local commun à `develop` et `layers/devops` lors du cadrage.
- **Tests** : inventaire avant/après des cartes, vérification des liens locaux et des références aux anciens chemins, `python3 codebase-quality-control/scripts/check.py` et `git diff --check`. Pas de nouveaux tests applicatifs : aucun code exécutable ni comportement applicatif modifié.
- **Réf** : OPS-001, OPS-023 ; `docs/README.md`, `docs/boilerplate/README.md`, `docs/aiod/adoption.md`, `dev-book/README.md`, `docs/aiod/couches.md`.

## Contexte

La configuration actuelle contient déjà les cinq couches attendues. OPS-001 a rattaché
la maintenance du cadre à devops. Pourtant, treize cartes de construction restent dans
`docs/boilerplate/tasks/`, séparées des cartes suivantes placées dans `dev-book/tasks/`.
Les guides recommandent encore cet archivage documentaire et présentent le dev-book
comme réservé aux tâches courantes. Ce rangement brouille la distinction entre méthode,
historique des réalisations et travail restant.

## Périmètre

- Migrer les treize cartes OPS-013 à OPS-022, API-001, WEB-001 et BO-001 vers `dev-book/tasks/`.
- Conserver toutes les cartes ensemble, ouvertes ou clôturées, distinguées par leur statut.
- Réintégrer l’inventaire utile des exemples de `docs/boilerplate/README.md` dans le guide d’adoption, puis retirer `docs/boilerplate/` devenu vide de contenu utile.
- Actualiser les liens entrants, les liens relatifs des cartes déplacées, les index et la procédure d’adoption.
- Examiner les mentions historiques susceptibles d’être prises pour du travail encore en cours ; les qualifier comme preuves datées sans inventer une nouvelle vérification ou un état Git.
- Confirmer que les documents courants rattachent la maintenance à devops et ne présentent aucune sixième couche.

Chemins autorisés : `docs/` (Markdown uniquement), `dev-book/README.md`,
`dev-book/tasks/`, `README.md`, `infra/README.md`, `design/README.md` et les fichiers
Markdown de `ia-engineering/` uniquement si leurs liens ou conventions sont directement concernés.

## Hors périmètre

Applications, dépendances, scripts, configuration des cinq couches, infrastructure exécutée,
charte et schémas graphiques, sources originales, environnements et `.env`.
Aucune suppression de carte, renumérotation BP vers OPS, réécriture Git, suppression de branche,
publication ou création de tâches applicatives. Aucun commit, push ou PR dans cette étape de cadrage.

## Décisions de cadrage

- Choix explicite de l’utilisateur : toutes les cartes dans `dev-book/tasks/`, sans sous-dossier d’archives.
- `docs/` contient les guides et références durables ; le dev-book porte les cartes et leurs preuves.
- Les identifiants BP sont historiques et ne prouvent pas qu’une tâche était injustifiée.
- Préserver les anciennes missions dans leur contexte ; ne pas les réattribuer rétroactivement à devops.
- Le terme « boilerplate » peut désigner un exemple applicatif ; seules ses utilisations qui entretiennent une couche ou une destination de cartes erronée doivent disparaître.
- L’état local suffit au cadrage : aucune synchronisation distante ou réécriture de branche nécessaire.

## Règles et cas limites

- Comparer les identifiants et noms avant déplacement ; arrêter en cas de collision sans écraser de carte.
- Conserver critères, décisions et preuves datées ; les anciennes commandes restent historiques lorsqu’elles ne sont plus exécutables telles quelles.
- Une mention historique d’un ancien chemin peut rester si son contexte est explicite ; un lien destiné à la navigation doit pointer vers la destination actuelle.
- Ne pas transformer une carte clôturée en tâche ouverte ni présenter un ancien résultat comme une preuve actuelle.
- Les aspects API, modèle de données, rôles applicatifs, états d’interface, accessibilité, performance et traduction sont sans objet pour cette migration documentaire.
- Le risque principal est la perte de traçabilité ou un lien cassé ; l’inventaire et la relecture du diff doivent le couvrir.
- Aucun aval ni report fonctionnel prévu ; toute anomalie hors périmètre est signalée sans correction opportuniste.

## Documentation impactée

`README.md`, `docs/README.md`, `docs/aiod/adoption.md`, `dev-book/README.md`,
`infra/README.md`, `design/README.md`, les cartes migrées et leurs références entrantes.
`docs/aiod/couches.md` et `ia-engineering/` sont à vérifier et à corriger seulement si nécessaire.

## Définition de terminé

- [x] Les treize cartes sont présentes dans `dev-book/tasks/`, sans perte ni doublon d’identifiant.
- [x] Toutes les cartes, ouvertes et clôturées, suivent la convention de rangement acceptée.
- [x] `docs/` ne contient plus de cartes de tâches et `docs/boilerplate/` a été retiré après migration du contenu utile.
- [x] Les index et le guide d’adoption décrivent la nouvelle convention et conservent l’inventaire des exemples.
- [x] Les liens de navigation touchés ciblent des fichiers existants ; les anciennes références historiques sont explicitement contextualisées.
- [x] La documentation courante décrit cinq couches et rattache la maintenance du cadre à devops.
- [x] Les mentions d’état ancien ne laissent pas croire à un travail actuellement non commité sans preuve.
- [x] L’inventaire avant/après, le contrôle des liens, les tests de l’outillage et le contrôle du diff sont consignés dans la carte lors de sa réalisation.

## Livré et vérification — 2026-10-23

- Branche `layers/devops` reprise sur la base locale prévue, sans fetch ni changement Git ; seule la carte OPS-010 était non suivie à l’ouverture.
- Treize cartes migrées ; comparaison de leur texte à l’inventaire avant déplacement : contenu identique après retrait des seules notes historiques ajoutées à OPS-022. Les 34 cartes présentes ont des identifiants uniques, OPS-010 comprise.
- `docs/boilerplate/` retiré après récupération de l’inventaire des exemples dans `docs/aiod/adoption.md`. Aucun autre dossier de cartes ne subsiste dans `docs/`.
- Index et liens d’initialisation design/devops actualisés ; convention des cartes ouvertes et clôturées explicitée dans le dev-book.
- Notes de contexte ajoutées aux cartes OPS-022, OPS-023, OPS-024, OPS-001, OPS-002, OPS-003, OPS-006 et OPS-008 pour qualifier les anciens états Git et chemins. Critères, affectations et preuves historiques préservés.
- Vérification des liens de fichiers Markdown locaux, sur les fichiers suivis existants et les cartes nouvellement présentes : 75 cibles vérifiées, aucune absente (fragments internes non contrôlés).
- Recherche de `boilerplate/` dans les guides courants, consignes et README d’accueil, design et infra : aucune occurrence. Les mentions restantes dans les cartes documentent le contexte historique ou le périmètre de migration.
- Configuration JSON vérifiée : exactement api, backoffice, web, design et devops ; tableau de routage et gouvernance déjà cohérents, sans modification nécessaire.
- `python3 codebase-quality-control/scripts/check.py` : 17 tests réussis.
- `git diff --check` : réussi ; contrôle séparé des espaces de fin de ligne des nouveaux fichiers réussi.
- Aucun code applicatif changé ; aucune nouvelle suite de tests nécessaire. Aucun commit, push ou PR. Aucun point croisé hors périmètre identifié.

## Clôture — 2026-10-23

Résultat validé par l’utilisateur. Migration documentaire et preuves réunies dans un commit
OPS-010 ; aucun changement applicatif ni publication. La mise à plat de `docs/aiod/`
et le rangement de ses ressources relèvent de la tâche suivante.
