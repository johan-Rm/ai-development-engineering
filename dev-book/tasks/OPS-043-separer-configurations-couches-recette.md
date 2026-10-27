# TASK OPS-043 — Séparer la configuration des couches et de la recette

- **Créée le** : 2026-10-24.
- **Session** : non disponible (Codex).
- **Statut** : clôturée — ✅ fait le 2026-10-26. Configurations séparées, consommateurs, tests et documentation adaptés.
- **Type** : refactor.
- **Tests** : tests de création et préservation des worktrees ; lecture des configurations depuis le worktree appelant ; tests de l’outillage via `python3 codebase-integrity/scripts/check.py` ; comparaison JSON complète de la configuration Compose avant/après sans démarrage ; `git diff --check`.
- **Mission** : devops, `layers/devops`, `worktree/devops`.
- **Demande d’origine** : échange du 2026-10-24, séparation des responsabilités proposée puis validée par l’utilisateur.
- **Réf** : OPS-041, OPS-042 ; `docs/02-cadre/couches.md`, `codebase-integrity/README.md`, `infra/README.md`.
- **Dépendances par commit** : base locale `a100043dcc7bc0ebca7c44296b4c3b7b46c8ea34` (OPS-042), sur `develop` au commit `bd95c1c` ; aucune dépendance non commitée, aucun aval imposé.

## Contexte

`codebase-integrity/scripts/aiod.json` mélange la définition des couches du cadre
et la configuration de ses témoins Docker. Son emplacement présente les scripts
consommateurs comme propriétaires de ces configurations.

## Périmètre et chemins autorisés

- Créer `config/layers.json` avec la section `layers` actuelle, branches, rôles et identifiants stables inchangés.
- Créer `infra/process-check.json` avec la section `process` actuelle, image et base de ports inchangées.
- Supprimer `codebase-integrity/scripts/aiod.json`.
- Adapter `codebase-integrity/scripts/worktrees.py` pour lire uniquement la configuration des couches.
- Adapter `codebase-integrity/scripts/process.py` pour lire les deux configurations.
- Adapter les fixtures et vérifications dans `codebase-integrity/tests/test_worktrees.py` et `codebase-integrity/tests/test_process.py`.
- Créer `config/README.md` pour préciser la responsabilité de la configuration commune ; actualiser `infra/README.md` et `codebase-integrity/scripts/README.md`.
- Actualiser les références documentaires actives dans `SETUP.md`, `docs/02-cadre/couches.md` et, si nécessaire, `README.md` ; présente carte.

Lire les README existants applicables avant toute écriture. Si un autre consommateur
actif est découvert, le signaler et examiner son rattachement avant extension.

## Hors périmètre

Applications, cartes et preuves historiques, ressources originales ; renommage des
couches, branches, identifiants Docker ou paramètres `PROCESS_CHECK_*` ; évolution
des ports, images ou contrats. Aucun `.env`, artefact d’identité, conteneur, volume
ou réseau modifié. Aucun déploiement, démarrage de conteneur, push, PR ou merge.
Commit seulement sur demande explicite.

## Décisions de cadrage

L’utilisateur valide la séparation selon les responsabilités : le cadre définit les
couches, l’infrastructure définit les témoins, les outils consomment ces fichiers.
Conserver les enveloppes JSON `layers` et `process` minimise le changement de
structure. Aucun mécanisme de repli vers l’ancien fichier : configurations,
consommateurs, tests et documentation sont livrés ensemble.
Le déplacement et l’adaptation des contrôles sont explicitement autorisés dans ce
cadrage ; aucune convention ni contrôle hors périmètre ne doit être affaibli.
La suppression du guide de recette a été isolée dans OPS-042 avant cette carte.

## Règles et cas limites

Chaque outil doit lire la configuration du worktree appelant, y compris lorsque
la disposition du dépôt principal diffère. L’outil de création des worktrees doit
fonctionner sans fichier de configuration Docker. La recette nécessite les deux
fichiers ; leur absence ou leur invalidité ne doit pas déclencher de création
implicite, de repli sur une autre configuration ou de perte des protections existantes.
Conserver validation des branches, unicité des identifiants, protection des chemins,
préservation des fichiers et identités, et options de lancement Compose.
Les environnements déjà générés restent compatibles puisque les valeurs ne changent
pas. Aucune modification des rôles applicatifs, permissions, données, états
d’interface, accessibilité ou performance : dimensions sans objet ici.

## Documentation impactée

`config/README.md` explique la propriété des couches et la coordination avec la
table documentaire ; `infra/README.md` documente les paramètres des témoins ;
`codebase-integrity/scripts/README.md` précise les sources consommées.
Les guides d’installation et des couches indiquent les nouveaux chemins.
Les références dans les cartes historiques restent conservées comme traces datées.

## Définition de terminé

- [x] Les deux configurations contiennent les valeurs antérieures sans altération.
- [x] L’ancien fichier est supprimé et aucun consommateur actif ne dépend encore de son chemin.
- [x] La création des worktrees ne dépend pas de la configuration Docker et les lectures respectent le worktree appelant.
- [x] Les tests de l’outillage passent avec les fixtures adaptées et les protections existantes conservées.
- [x] La configuration Compose résolue est strictement identique avant/après, sans démarrage de conteneur.
- [x] Responsabilités et nouveaux chemins sont documentés ; `git diff --check` réussit.
- [x] Les preuves sont consignées pour relecture humaine et aucune ressource active n’est modifiée.

## Réalisation et preuves

Implémentation terminée le 2026-10-26 ; résultat présenté avec ses preuves, puis
clôture et commit demandés explicitement par l’utilisateur via `commit-tache OPS-043`.

- Branche `layers/devops` avancée sans rebase ni perte de fichiers sur `develop`
  au commit `a4b450a` (fusion locale de OPS-042 et OPS-044). Aucun commit de tâche
  restant à intégrer avant le démarrage ; la dépendance OPS-042 est présente.
- `config/layers.json` contient uniquement l’enveloppe `layers` ;
  `infra/process-check.json` contient uniquement l’enveloppe `process`.
  Leur réunion JSON a été comparée à `git show HEAD:codebase-integrity/scripts/aiod.json` :
  toutes les valeurs sont strictement identiques.
- `worktrees.py` lit uniquement `config/layers.json`. `process.py` lit les deux
  configurations dans le worktree appelant. Ancien fichier supprimé, aucun repli ajouté.
- Fixtures migrées et quatre tests ajoutés : création sans configuration Docker,
  configurations absentes ou invalides sans repli, lecture des deux fichiers du
  worktree secondaire lorsque ceux du dépôt principal sont absents.
- `python3 codebase-integrity/scripts/check.py` : **23 tests réussis**.
  Premier passage bloqué uniquement par l’interdiction du serveur HTTP local dans
  le bac à sable ; second passage autorisé avec ce serveur temporaire : `OK`.
- Comparaison avant/après via `process.settings(Path.cwd())` puis
  `process.compose(info, 'config', '--format', 'json', capture=True)` :
  identité et configuration Compose JSON complète strictement identiques.
  Captures locales : `/tmp/ops043-before.json` et `/tmp/ops043-after.json`.
  Aucun appel `up`, `down` ou `prepare` sur l’environnement réel.
- `git diff --check` : aucune erreur.
- Recherche des références actives avec `rg -n 'aiod\.json' SETUP.md docs infra codebase-integrity config` :
  seules subsistent les fixtures testant explicitement le refus de repli et la
  mention historique de ce refus dans le README de configuration. Aucun
  consommateur actif supplémentaire découvert ; cartes historiques préservées.
- Documentation mise à jour : `config/README.md`, `infra/README.md`,
  `codebase-integrity/scripts/README.md`, `SETUP.md`, `docs/02-cadre/couches.md`.
  Pas de changement nécessaire au README racine.
- Aucun `.env`, artefact réel d’identité, conteneur, volume ou réseau modifié.
  Les dépôts et identités créés par les tests sont jetables, sous `/tmp`.
  Carte, configurations, scripts, tests et documentation réunis dans le commit de
  cette tâche. Aucun push, PR ou merge de la tâche effectué.

## Livré

- Configuration du cadre : `config/README.md` et `config/layers.json`.
- Configuration de recette : `infra/process-check.json` et `infra/README.md`.
- Consommateurs : `worktrees.py`, `process.py` et README de l’outillage ; ancien `aiod.json` supprimé.
- Tests : fixtures migrées et cas de non-régression dans `test_worktrees.py` et `test_process.py`.
- Guides : `SETUP.md` et `docs/02-cadre/couches.md`.

## Reste à faire (hors périmètre)

Livraison et intégration sur demande explicite ; aucune tâche d’implémentation restante pour OPS-043.
