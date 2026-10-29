# OPS-067 — Retirer le sigle des supports actuels

- Date : 2026-10-29 ; état : validée avec réserve navigateur ; commit local à créer.
- Session de création : `01a18693-b0a7-7651-8d7c-9197f32ab602`.
- Demande : DEM-014 ; référence du besoin : `tmp/demande-retirer-sigle.md`, relative au dépôt principal, hors de ce worktree.
- Future demande : `dev-book/demand/DEM-014-retirer-sigle.md` dans le principal ; fichier à créer à la reconstitution, absent à ce stade.
- Mission : devops ; worktree `worktree/devops` ; branche `layers/devops`.
- Base locale : `93c392bb78289097bf9c73b9553b890358f75696`, commune avec develop.
- Dépendances : aucune carte amont ni commit à importer.

## Objectif et critères

Couvrir les critères 1 à 4 de DEM-014 dans une contribution cohérente : appliquer
la règle éditoriale confirmée aux supports actuels, au schéma et à son test.
Le brouillon fait référence pour les formulations, exclusions et décisions.

## Chemins autorisés

- `README.md`, `SETUP.md`, `AGENTS.md`, `.codex/config.toml`.
- `docs/index.md`, `docs/01-codebase-integrity/principes-fondamentaux.md`,
  `docs/02-cadre/documentation.md`, `docs/02-cadre/ia-engineering.md`.
- `infra/README.md`, `infra/config/README.md`, `app/README.md`.
- `dev-book/README.md`, `dev-book/resources/README.md`,
  `dev-book/resources/vue-d-ensemble-ai-development-engineering.html`.
- `design/charte-graphique.md` : reformulation éditoriale seulement.
- `codebase-integrity/tests/browser/README.md`,
  `codebase-integrity/tests/browser/vue-aiod.cjs` : attente textuelle associée seulement.
- Cette carte : état, preuves et verdict à venir.

Les chemins correspondent à l'inventaire initial du mot entier sensible à la
casse. Signaler toute occurrence actuelle supplémentaire hors de ces chemins
avant d'étendre le périmètre. Aucun renommage, changement de convention, de
logique de contrôle, de comportement applicatif ou d'identité graphique.
Préserver les traces historiques, sources originales et travaux étrangers.

## Vérifications et preuves attendues

- Refaire l'inventaire par `rg --hidden -n -w 'AIDE'`, en excluant `.git/`,
  `worktree/`, `tmp/`, les demandes et cartes historiques ; distinguer les
  éventuelles occurrences techniques conservées. Consigner résultat et limites.
- Relire les reformulations et le diff ; vérifier les liens et ancres concernés,
  l'absence de renommage et la préservation du sens des consignes.
- Lire les références graphiques prescrites par AGENTS.md avant de toucher au
  schéma. Vérifier sa lisibilité sur ordinateur et mobile ainsi que les libellés
  accessibles ; conserver les preuves utiles dans cette carte.
- Depuis ce worktree : `git diff --check`,
  `python3 codebase-integrity/scripts/check.py`, puis
  `node codebase-integrity/tests/browser/vue-aiod.cjs app/web/targets/app`
  selon son README (dépendances web, Playwright et Chromium requis).
  Distinguer les échecs préexistants ou prérequis manquants du résultat attendu,
  sans affaiblir les assertions étrangères à la demande.
- Qualité complète requise avant PR :
  `python3 codebase-integrity/scripts/quality.py`.
  Aucun nouveau test de jugement rédactionnel.

## Disponibilité et suite

Index et arbre propres avant création ; branche existante conservée, sans fetch
ni rebase. La clôture de DEM-013 dans son brouillon confirme la libération de
devops ; les anciens états « à livrer » des cartes historiques ne constituent
pas une nouvelle mission active. Maximum OPS observé dans toutes les références
Git locales et les documents des worktrees : 066.

Après implémentation, vérification humaine et commits validés : reconstitution
dans le principal (`.`), libre et propre, sur `demands/DEM-014`, créée seulement
à cette étape depuis develop local vérifié. Réunir les commits validés par SHA,
sans copie non commitée ; retour du principal sur develop après fusion distante.
Devops conserve `layers/devops`. Aucun commit ni implémentation à ce découpage.

## Résultat et preuves — 2026-10-29

Les 17 fichiers suivis du périmètre sont modifiés : nom long aux présentations,
reformulations contextuelles ailleurs. Le schéma présente uniquement le nom long
dans sa signature, son titre et ses libellés ; son test attend ce texte.
Styles et dessin du pictogramme inchangés. Références graphiques du dépôt lues,
dont le contenu embarqué de la charte officielle ; aucune refonte graphique.

Contrôles depuis le worktree affecté :

- `git diff --check` : réussi.
- Inventaire `rg --hidden -n -w --glob '!.git/**' --glob '!worktree/**'
  --glob '!tmp/**' --glob '!dev-book/tasks/**' --glob '!dev-book/demand/**'
  'AIDE' .` : aucune occurrence (code 1 normal pour absence de résultat).
  Les traces de demandes/cartes et brouillons restent exclues ; noms techniques
  inchangés. Les fichiers ignorés restent exclus par défaut par cette commande.
- Vérification Python ponctuelle : 81 liens locaux et ancres Markdown des
  documents modifiés valides ; aucun lien entrant trouvé vers les trois titres
  dont l'ancre change. Blocs CSS du schéma identiques à HEAD ; sigle absent
  de tout son HTML, y compris les libellés accessibles.
- `python3 codebase-integrity/scripts/check.py` : 23 tests réussis, hors sandbox
  pour permettre le serveur HTTP temporaire.
- Commande navigateur prévue : échec au lancement Chromium, avant toute
  assertion, bibliothèque système `libnspr4.so` absente ; même résultat hors
  sandbox. Test et rendu ordinateur/mobile non vérifiés. Aucune assertion
  étrangère à la demande modifiée pour contourner cette limite.
- Qualité complète non lancée à cette étape éditoriale ; reste requise avant PR.

État présenté : même HEAD de base, `layers/devops`, index vide ; les 17 fichiers
suivis listés dans le périmètre et cette seule carte non suivie. Empreinte
SHA-256 de leur contenu (chemins triés, chemin puis octet nul, contenu puis
octet nul) : `01d169d054c8b1a553a2e0eea76fc839a65a99306845ebd05846842491846dde`.
Seule la carte préexistante de cette mission était présente à la reprise,
conforme à l'état laissé au découpage. Aucun travail étranger rencontré ; aucun
commit, verdict humain ou changement de branche.

## Verdict humain — 2026-10-29

L'humain répond « validé » à la restitution d'OPS-067 avec réserve explicite :
test navigateur et rendu ordinateur/mobile non vérifiés, qualité complète
restant requise avant PR. Empreinte des 17 fichiers revérifiée identique avant
commit ; branche et HEAD conformes, index vide. Validation limitée à cette carte.
