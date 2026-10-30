# OPS-072 — Définir et contrôler les types de demandes

- Date : 2026-10-30 ; session de création : `01a18b94-1588-7021-869d-d11d9ff6ba72`.
- Demande et arbitrage : [DEM-022](../demand/DEM-022-types-demandes.md#arbitrage-humain--2026-10-30).
- Mission : devops ; worktree `worktree/devops` ; branche `layers/devops`.
- Base : `b40faca917b01074d078e49ad1cad6f7fb2ff7b6` ; aucune dépendance amont par commit.
- État : validée et commitée localement ; à livrer.

## Périmètre et critères

Appliquer l’arbitrage lié, sans le recopier : définition dans `dev-book/README.md`,
instruction directe dans AGENTS.md, typage intégré aux deux guides d’interview ; contrôle
et tests dans `codebase-integrity/`, intégration à quality.py et documentation
des commandes. Normaliser le seul champ Type de DEM-021 et DEM-022 ; préserver
les décisions et verdicts existants. Révision humaine : typer aussi les 18 demandes
historiques ; aucun inventaire ni exemption conservé.

Adapter séparément les seuls `interviewer-demande/SKILL.md` et
`interviewer-constat/SKILL.md` du répertoire personnel de skills. Aucun changement
applicatif, d’environnement, de données ou d’autorisation Git ; aucun rapport
d’analyse conservé. Une seule carte, le découpage découle de l’arbitrage.

Continuité de la session : DEM-021 et DEM-022 étaient les seuls changements
identifiés ; index vide, pas de mission étrangère. Identifiant OPS-072 vérifié
dans les références locales, cartes des worktrees et brouillons, sans fetch.

## Vérifications et preuves

Révision humaine du 2026-10-30, même session : suppression des exemptions et
migration immédiate de toutes les demandes. Les preuves du premier passage sont
remplacées par les contrôles de cette version corrigée, à consigner ci-dessous.
Le type classe le besoin ; il ne réécrit ni le parcours historique ni les verdicts.

- Les 20 demandes sont typées. Sur les 18 anciennes, comparaison à HEAD après
  retrait des deux seules métadonnées ajoutées (type et session intervenante) :
  contenu identique. Les besoins modifiant des conventions ou Codebase Integrity
  sont classés consolidation ; les réalisations ponctuelles restent développement.
- Inventaire d’exemptions supprimé ; aucun code de comparaison d’empreintes ni
  dépendance à Git dans le vérificateur.
- `python3 -B codebase-integrity/scripts/check_demands.py` : réussite sur tout le corpus.
- `python3 -B -m unittest discover -s codebase-integrity/tests -p test_demands.py` :
  9 tests réussis, dont obligation du type indépendamment de l’ancienneté ou du nom,
  doublons, format, exemples, erreurs de lecture et dossier absent.
- `python3 codebase-integrity/scripts/quality.py` : code 0, 39 tests d’outillage,
  contrôles API, types et builds web/backoffice réussis ; serveur HTTP temporaire
  autorisé. Journal : `/tmp/dem022-quality-uniform.log`.
- `git diff --check` réussi ; 44 liens locaux/ancres vérifiés dans les documents
  concernés, hors références historiques dont le contenu est inchangé.
- Les deux skills personnels restent adaptés et validés comme au premier passage ;
  aucun changement externe supplémentaire nécessaire. Ils restent hors de la PR.

Aucun parcours navigateur spécifique exécuté ; aucun code applicatif modifié.
Correction suivante : instruction directe de typage et de routage dans AGENTS.md,
sans renvoi documentaire, conformément à la demande humaine ; diff vérifié.
Ajout dans SETUP.md retiré à la demande humaine ; fichier identique à HEAD.
Pas de rapport d’analyse, de commit ou d’opération distante créé.

### Nouvelle présentation à la vérification

Corrections finales relues : consignes raccourcies, aucune modification de SETUP.md
ni d’IA Engineering, type intégré aux phrases des deux interviews, liste des contrôles
retirée du guide, point final facultatif. Les 9 tests ciblés et le contrôle des
20 demandes réussissent sur cette version ; `git diff --check` réussi.
La qualité complète ci-dessus précède la dernière adaptation de ponctuation,
couverte par les tests ciblés relancés. Métadonnées historiques et skills revérifiés.
Verdict humain du 2026-10-30, même session : « validé ». Puis correction demandée :
la validation déclenche les commits locaux sans autorisation séparée. Skills
`verifier-consolidation` et `implementer-consolidation`, AGENTS.md et guide alignés.
Vérification à reprendre à la demande humaine ; aucun commit créé ici.

## Vérification humaine attendue

Présenter la définition et le routage, le typage de tout le corpus et les échecs détectés. DEM-021 reste une demande distincte non commitée ;
aucun autre contenu de cette demande n’appartient à la carte. Attendre le verdict
avec `verifier-consolidation` ; aucune autorisation de commit déduite des tests.

## Verdict final et périmètre du commit

Après nouvelle présentation, réponse humaine : « validé », le 2026-10-30,
session d’origine. Validation du typage, du contrôle, des simplifications et des
autorisations corrigées. Commit local autorisé par cette validation.

Fichiers livrés : AGENTS.md, README du dev-book et de l’outillage, quality.py,
check_demands.py et ses tests, métadonnées des 18 demandes existantes, DEM-022,
cette carte et guides modifiés (points de contrôle, interviews, vérification).
DEM-021 reste hors commit ; les quatre skills personnels adaptés restent hors dépôt.
Les tests ciblés (9) et le contrôle du corpus ont réussi à la dernière présentation.

Commit validé : `fe09842309a98f05c804d3c0fcb0bb5966beaab6`. Contenu vérifié : 30 fichiers ;
seule DEM-021 reste non suivie, index vide après commit.
