# OPS-069 — Regrouper la documentation du cadre sous architecture

- Date : 2026-10-29 ; état : validée et commitée avec réserve ; à livrer.
- Session de création : `01a18804-42eb-7d20-8dbc-7430446e4350`.
- Demande : `tmp/demande-regrouper-docs-architecture.md`, relativement au dépôt principal ; référence du besoin et des critères d’acceptation.
- Demande définitive prévue : `dev-book/demand/DEM-017-regrouper-docs-architecture.md`, absente avant reconstitution.
- Mission : devops ; worktree `worktree/devops` ; branche `layers/devops`.
- Base locale : `ec6efd5`, commune avec develop ; aucune dépendance amont ni import de commit.

## Objectif et périmètre

Réaliser tous les critères de DEM-017 dans une seule contribution : déplacement,
organisation des index et correction des références actives, sans état intermédiaire
où la navigation serait cassée.

Chemins autorisés : `docs/`, `AGENTS.md`, `README.md`, `SETUP.md`,
`infra/`, `.codex/`, `.github/`, les README du cadre sous `codebase-integrity/`,
`dev-book/README.md`, les ressources et procédures actives sous `dev-book/resources/`
et `dev-book/runbooks/`, pour les seules adaptations de références nécessaires ;
cette carte pour les preuves et le verdict.

Exclusions : demandes et preuves historiques, autres cartes, applications, données,
`.env`, skills personnels et réécriture de fond. Ne modifier ni conventions techniques
ni contrôles. Si un contrôle impose les anciens chemins, signaler le blocage plutôt
que l’affaiblir. Lire les README applicables avant de toucher chaque périmètre.

## Vérifications et documentation

- Comparer les fichiers avant/après : les quatre dossiers sont déplacés sans perte ;
  les écarts de contenu se limitent aux index et aux références nécessaires.
- Rechercher les anciens chemins dans les fichiers actifs suivis ; qualifier les
  occurrences restantes en distinguant les traces historiques conservées.
- Vérifier les destinations des liens relatifs et des ancres modifiés, depuis les
  deux index et les points d’entrée actifs ; consigner les limites de la vérification.
- Exécuter `git diff --check` et `python3 codebase-integrity/scripts/check.py`
  depuis le worktree. `python3 codebase-integrity/scripts/quality.py` reste requis
  avant PR ; aucun test applicatif supplémentaire propre au déplacement.

Les documents déplacés et les entrées existantes portent la documentation durable ;
aucun guide parallèle. Consigner ici les résultats, les limites et le verdict humain
à l’étape appropriée. Aucun verdict ni résultat implémenté à ce stade.

## Préparation observée

Avant création : branche attendue présente, index vide, arbre propre ; même base
que develop. Les traces consultées ne révèlent pas de mission active concurrente.
Les anciens états « à livrer » de cartes historiques ne sont pas réécrits ; les
livraisons intégrées sont présentes dans l’historique local. Disponibilité à revérifier
avant implémentation. Identifiant attribué après examen des références locales,
de leur historique et des fichiers locaux : maximum antérieur OPS-068 ; aucun fetch.

Après validation humaine et commit local à l’étape 04, reconstituer selon le plan
du brouillon. Aucun commit créé au découpage.

## Résultat présenté — 2026-10-29

Reprise de la même mission : seule cette carte non suivie était présente au démarrage,
conforme au découpage ; index vide, branche et base inchangées. Aucun travail étranger identifié.

Les 22 documents des quatre dossiers sont sous `docs/architecture/`, avec le sommaire
transféré dans son index ; `docs/index.md` devient l’entrée générale. Références actives
adaptées dans `AGENTS.md`, `SETUP.md`, `infra/config/README.md`,
`codebase-integrity/scripts/README.md` et `dev-book/README.md`.

Preuves :

- Comparaison avec `git show HEAD:<ancien chemin>` : les 22 documents sont présents
  au nouveau chemin et identiques après neutralisation des destinations Markdown.
- Inspection Python des liens Markdown des deux index, des documents et des points
  d’entrée ci-dessus, README racine inclus : 97 liens locaux examinés, destinations
  et ancres Markdown présentes. Vérification statique, sans navigation dans un navigateur.
- Recherche des quatre anciens préfixes `docs/<dossier>/` dans les fichiers actifs :
  aucune occurrence ; demandes et cartes historiques exclues, laissées intactes.
- `git diff --check` : réussi.
- `python3 codebase-integrity/scripts/check.py` : 23 tests réussis après autorisation
  du serveur HTTP local temporaire ; première exécution bloquée par les sockets du bac à sable.

Le contrôle complet `quality.py` reste à exécuter avant PR. Aucun contrôle ni test
de vérificateur modifié ; aucun test ajouté pour ce déplacement documentaire.

État soumis : HEAD `ec6efd554d16459536233c43f824617df4db2dea`, index vide ;
diff suivi limité aux cinq fichiers actifs listés, à l’index général et aux suppressions
des anciens chemins. Fichiers non suivis : `docs/architecture/**` (23 fichiers) et
cette carte. Le brouillon ignoré du principal contient le suivi de la demande.
Les anciens liens historiques peuvent rester non résolus conformément au cadrage.
Aucun commit, verdict humain ni branche de demande créé à cette étape.

## Vérification — 2026-10-29

Écart détecté par `git grep` sur les fichiers suivis, hors demandes et cartes historiques :
`worktree/README.md:13` et `:17` conservent deux liens actifs vers les anciens chemins
des guides des couches et de reconstitution. La recherche précédente excluait trop
largement `worktree/`, masquant son README suivi ; sa conclusion d’absence d’occurrence
active était incomplète.

Le critère des références actives reste non satisfait. Correction à réaliser à
l’implémentation, en incluant ce README dans le périmètre de la carte, puis nouvelle
présentation ; aucune correction effectuée durant la vérification. Les 22 documents
déplacés restent conformes à la comparaison de contenu. Aucun verdict humain acquis.
Relevé des 52 chemins soumis (empreintes et suppressions) conservé dans
`tmp/verification-ops-069.json` du principal avant ajout de cette trace.

## Verdict humain — 2026-10-29

Réponse « validé », réitérée après la question explicite sur l’acceptation des deux
liens cassés comme réserve : validation avec cette réserve conservée. Aucun correctif
inclus. Avant commit : branche et HEAD inchangés, index vide ; comparaison des
52 chemins au manifeste conforme, hors trace documentaire de vérification de cette carte.

Commit local validé avec réserve : `c305cf2dffe8c562a04e112468dcdc87b701d859`.
