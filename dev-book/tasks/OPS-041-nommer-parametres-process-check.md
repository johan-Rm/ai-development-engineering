# TASK OPS-041 — Nommer les paramètres Compose selon leur rôle de recette

- **Créée le** : 2026-10-24.
- **Session** : non disponible (Codex).
- **Statut** : ✅ fait le 2026-10-24.
- **Livraison** : paramètres internes Python et Compose renommés en `PROCESS_CHECK_*`, test et documentation synchronisés.
- **Type** : refactor.
- **Tests** : contrôler la transmission des paramètres et la préservation de l’environnement appelant ; exécuter `python3 codebase-integrity/scripts/check.py` ; valider la configuration Compose résolue sans démarrer de conteneur ; `git diff --check`.
- **Réf** : OPS-040 ; `infra/README.md`, `codebase-integrity/scripts/README.md`, `codebase-integrity/tests/README.md`.
- **Demande d’origine** : échange du 2026-10-24 ; remplacement du préfixe lié à l’écosystème par un nom fonctionnel, cadrage validé par l’utilisateur.
- **Couche et branche** : devops, `layers/devops`.
- **Worktree** : `worktree/devops`.
- **Chemins autorisés** : `codebase-integrity/scripts/process.py`, `infra/compose.process.yaml`, `infra/README.md`, `codebase-integrity/tests/test_process.py`, présente carte.
- **Dépendances par commit** : base `ed715efb57b780305138ee814891bcb1e0334077`, incluant OPS-040 ; aucune dépendance aux travaux BO-002, WEB-002 et API-002, aucun aval imposé.

## Contexte

Les variables internes transmises par le script de recette à Docker Compose portent
encore le préfixe `AIOD_`. Leur rôle concerne le conteneur témoin ; un nom fonctionnel
reste compréhensible indépendamment du nom de l’écosystème.

## Périmètre

Modifier ensemble le producteur Python et le consommateur Compose :

| Ancien nom | Nouveau nom |
| --- | --- |
| `AIOD_IMAGE` | `PROCESS_CHECK_IMAGE` |
| `AIOD_PORT` | `PROCESS_CHECK_PORT` |
| `AIOD_PROOF_DIR` | `PROCESS_CHECK_PROOF_DIR` |

Documenter ces paramètres internes dans `infra/README.md` et vérifier leur
transmission ainsi que la configuration résolue.

## Hors périmètre

Noms des projets, réseaux et volumes Docker ; `aiod.json` ; `.env` ; applications ;
artefacts locaux et identités existantes. Aucun démarrage ou arrêt de conteneur,
déploiement, migration, suppression de données ou modification des ports effectifs.
Commit, push, PR, merge et opérations distantes seulement sur demande explicite.

## Décisions de cadrage

L’utilisateur a validé `PROCESS_CHECK_`, cohérent avec `.local/process-check/`,
plutôt qu’un préfixe dépendant du nom AIDE. Aucun alias des anciens noms : le script
fournit lui-même les valeurs et les deux fichiers changent dans la même tâche.
Le changement et sa vérification dans l’outillage sont explicitement autorisés ;
aucune autre convention technique ni aucun contrôle existant ne doit être affaibli.

## Règles et cas limites

Conserver les valeurs calculées, le chemin des preuves relatif au dépôt principal (chemin absolu résolu à l’exécution), l’environnement
appelant et les options de lancement, notamment `--env-file` pointant sur le fichier
nul. Ne pas modifier `os.environ` ni lire ou écrire les `.env` pour cette recette.
Les nouveaux paramètres doivent être fournis explicitement même si l’environnement
appelant contient d’autres valeurs. Les anciens noms ne sont plus utilisés par
le script ou le fichier Compose ; ne pas nettoyer l’environnement de l’utilisateur.
Les variables Compose restent obligatoires. Aucun comportement applicatif, état
d’interface, permission métier ou contrainte graphique n’est concerné.

## Documentation impactée

`infra/README.md` : nom, rôle et alimentation interne des trois paramètres ;
absence de migration des `.env` dans le fonctionnement piloté par le script.
Les commandes publiques restent inchangées.

## Définition de terminé

- [x] Les trois noms sont synchronisés entre Python et Compose ; aucune référence `AIOD_` ne reste dans ces deux fichiers.
- [x] Les valeurs image, port et montage résolues sont identiques à celles attendues avant renommage.
- [x] La transmission des paramètres est vérifiée, sans altérer l’environnement appelant ni lancer Docker dans le test unitaire.
- [x] Les tests de l’outillage et la validation Compose sans démarrage réussissent ; leurs résultats sont consignés.
- [x] Le README d’infrastructure est à jour et `git diff --check` réussit.
- [x] Aucune donnée, ressource active, autre couche ou convention hors périmètre n’est modifiée.

## Vérification

Implémentation le 2026-10-24 sur `layers/devops`, base inchangée
`ed715efb57b780305138ee814891bcb1e0334077`. Seule la carte non suivie était
présente au démarrage ; aucun travail tiers touché.

- Producteur `process.py` et consommateur `compose.process.yaml` synchronisés
  sur `PROCESS_CHECK_IMAGE`, `PROCESS_CHECK_PORT`, `PROCESS_CHECK_PROOF_DIR`.
- README d’infrastructure : rôle des paramètres internes et absence de migration
  des `.env` documentés.
- Nouveau test unitaire sans Docker : valeurs héritées contradictoires remplacées
  dans la copie transmise au sous-processus ; variable tierce préservée ;
  environnement appelant inchangé ; commande, options et résultat vérifiés.
- `python3 codebase-integrity/scripts/check.py` : 19 tests réussis. Le premier
  passage dans le bac à sable bloquait le test HTTP existant (socket locale) ;
  relance avec permission étendue réussie, sans affaiblir le test.
- `python3 -B codebase-integrity/scripts/process.py config` : réussi, image
  `busybox:1.37.0`, port local `18104`, montage absolu `.local/process-check`
  du worktree devops, lecture seule conservée.
- Comparaison JSON complète des configurations résolues avant/après : strictement
  identiques. Ancien Compose extrait de `HEAD` dans un dossier temporaire et
  résolu avec les anciennes variables, même projet et mêmes valeurs ; comparaison
  avec le nouveau Compose via `process.compose` réussie.
- Aucune référence `AIOD_` restante dans le producteur et le consommateur.
- `git diff --check` : réussi ; uniquement les quatre fichiers prévus et la carte.

Aucun conteneur démarré ou arrêté, aucun artefact d’identité ni `.env` modifié,
aucun nom de projet/réseau/volume changé. Le serveur HTTP du test tourne uniquement
dans son environnement temporaire. Mise en commit explicitement demandée par
l’utilisateur le 2026-10-24 après présentation du résultat ; aucun push.

## Livré

- `codebase-integrity/scripts/process.py` : nouveaux paramètres fournis à Compose.
- `infra/compose.process.yaml` : mêmes paramètres consommés, toujours obligatoires.
- `codebase-integrity/tests/test_process.py` : transmission et préservation de l’environnement couvertes.
- `infra/README.md` : paramètres internes documentés.
- Présente carte : cadrage, preuves et clôture.

## Reste à faire (hors périmètre)

Aucun reliquat pour OPS-041. Les commits applicatifs BO-002, WEB-002 et API-002
restent sur leurs branches respectives, hors de ce commit.
