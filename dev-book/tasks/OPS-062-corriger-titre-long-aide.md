# OPS-062 — Corriger le titre long AIDE dans les supports actuels

- Date : 2026-10-27.
- État : validée par l’humain avec réserve navigateur ; commit local en cours.
- Identifiant de session de création : `01a17e4d-043f-7c71-9aa5-3754c3794e18`.
- Demande : DEM-010, cadrage confirmé dans le chat.
- Brouillon de référence : `tmp/demande-corriger-titre-long-aide.md`, depuis la racine du dépôt principal (hors worktrees).
- Document définitif à créer à la reconstitution : [DEM-010](../demand/DEM-010-corriger-titre-long-aide.md). Ce lien reste en attente jusqu’à cette étape, conformément à la décision humaine de rangement.
- Couche : devops ; worktree : `worktree/devops` ; branche : `layers/devops`.
- Base locale vérifiée : `13d69361ae061a1fec27f039bb199160d4f5db30`, commune à develop et layers/devops au découpage ; aucun fetch effectué.
- Dépendances par commit : aucune tâche amont ; la base contient les supports et le test existants.

## Objectif

Présenter partout dans les supports actuels le titre long exact
**AI-powered Development Engineering**, avec le sigle AIDE inchangé, et adapter
l’attente textuelle du test navigateur existant.

## Chemins autorisés

- `README.md`.
- `docs/01-codebase-integrity/principes-fondamentaux.md`.
- `dev-book/resources/vue-d-ensemble-ai-development-engineering.html` : titre
  visible, libellé accessible et autres occurrences actuelles du titre uniquement.
- `codebase-integrity/tests/browser/vue-aiod.cjs` : attente textuelle du titre uniquement.
- La présente carte, pour les preuves et le verdict humain ultérieur.

Rechercher les autres anciennes formulations dans le dépôt en excluant worktree/.
Si un support actuel supplémentaire est trouvé hors de ces chemins, documenter
le chemin et ajuster explicitement le périmètre de la carte avant de l’éditer.
Lire les README applicables avant chaque écriture ; pour le rendu, consulter
la charte officielle `design/Brand Guidelines - Graines Digitales (standalone).html`
et `design/charte-graphique.md` sans les modifier.

## Exclusions

Anciennes demandes, cartes et preuves historiques ; noms de fichiers, chemins,
liens cibles, sigle AIDE, applications et environnements. Ne pas modifier les
conventions techniques, la logique des contrôles ou ajouter un nouveau contrôle
permanent. La modification de workflow documentée séparément dans tmp ne fait
pas partie de DEM-010. Aucun changement de mise en page prévu ; signaler un
problème de lisibilité nécessitant une adaptation hors du remplacement textuel.

## Critères et documentation

1. Le README, les principes fondamentaux et le schéma affichent le titre exact.
2. La signature visible et son aria-label sont cohérents.
3. La recherche des anciennes formulations ne trouve plus d’ancien titre dans
   les supports actuels ; les occurrences historiques conservées sont expliquées.
4. La signature reste lisible sur ordinateur et mobile, sans débordement nouveau.
5. Le test navigateur existant attend le nouveau titre et réussit.
6. Le diff préserve les exclusions et ne contient aucune modification de workflow.

La documentation modifiée est le résultat attendu lui-même ; aucun nouveau
guide ni README de convention n’est nécessaire pour cette correction éditoriale.

## Vérifications et preuve attendue

Depuis le worktree affecté :

- Inventaire des occurrences avant/après avec rg, en distinguant les historiques.
- `node codebase-integrity/tests/browser/vue-aiod.cjs app/web/targets/app`.
  Prérequis : Playwright résolu depuis la cible web et Chromium disponible ;
  constater et rapporter toute indisponibilité sans inventer une réussite.
- Relire les captures ordinateur et mobile produites par le test et consigner
  leurs chemins ainsi que les dimensions observées dans cette carte.
- `git diff --check` et contrôle du diff pour les exclusions.
- `python3 codebase-integrity/scripts/quality.py` avant PR ;
  `python3 codebase-integrity/scripts/check.py` pour les contrôles de l’outillage
  pertinents. Ne pas étendre les tests au-delà des besoins de la correction.

Consigner commandes, résultats réels et limites dans cette carte. Pas de nouveau
test qui répète simplement le remplacement. Le verdict humain sera recueilli
à la vérification ; l’implémentation reste non commitée jusque-là.

## Ordre et reconstitution prévus

Une seule carte couvre tous les critères de DEM-010 ; aucune dépendance entre couches.
Après validation humaine, la vérification créera le commit local de cette carte
avec code, documentation, preuves et verdict ; son SHA reste à renseigner.
La reconstitution attend ce SHA identifié : elle est non prête avant cela.

Worktree prévu : `worktree/devops`, à revérifier libre et propre à la reconstitution.
Créer alors `demands/DEM-010` depuis le develop local vérifié, appliquer le commit
validé avec `git cherry-pick -x` et matérialiser la demande définitive depuis son
brouillon local, avec session, décisions, liens et correspondance des SHA.
Branche à retrouver après livraison : `layers/devops`. Aucun dossier de réunion,
nouveau worktree ou copie de travail non commité d’une autre mission.

## État observé au découpage

Worktree devops propre avant création, index vide, aucune mission concurrente
active identifiée dans les cartes consultées. Branche existante conservée sans
rebase ; branche demands/DEM-010 absente et réservée à la reconstitution.
Maximum OPS observé : 061 dans les références Git locales et les cinq worktrees.
L’état propre seul ne garantit pas l’absence d’une mission externe ; revérifier
la disponibilité avant implémentation. Aucun support ni test modifié au découpage.

## Preuves d’implémentation — 2026-10-27

Reprise de la même mission : seul ce fichier de carte était non suivi avant
écriture, conformément au découpage ; index vide et aucun changement étranger.
Base HEAD inchangée : `13d69361ae061a1fec27f039bb199160d4f5db30`.

Six occurrences remplacées : une dans README.md, une dans les principes,
trois dans la vue (signature, aria-label et texte des détails) et une dans
l’assertion navigateur. Comparaison automatisée au contenu de HEAD : les quatre
fichiers sont exactement le résultat du seul remplacement du titre, sans autre
modification. Sigle, chemins, CSS, logique et historiques préservés.

- `rg -n -o 'AI Development Engineering' --glob '!worktree/**'` : seules
  quatre cartes historiques conservent l’ancien titre : OPS-002, OPS-026,
  OPS-027 et OPS-040. Aucun support actuel restant.
- `git diff --check` : réussite.
- `node --check codebase-integrity/tests/browser/vue-aiod.cjs` : réussite.
- `python3 codebase-integrity/scripts/quality.py` : réussite, code 0 après
  exécution hors sandbox pour permettre les sockets locales. Comprend les
  23 tests de l’outillage, le contrat API, les contrôles Symfony et les
  typechecks/builds web et backoffice. Première tentative sandbox arrêtée
  par PermissionError sur la socket du test d’identité ; aucun contrôle modifié.
- `node codebase-integrity/tests/browser/vue-aiod.cjs app/web/targets/app` :
  échec avant chargement de la page, y compris hors sandbox : Chromium ne
  trouve pas `libnspr4.so`. Aucun résultat navigateur ni capture de cette
  exécution disponible ; captures ordinateur/mobile non relues. Critères
  de rendu et réussite du test navigateur restent à vérifier après résolution
  de ce prérequis système. Aucune installation système effectuée.

État présenté : quatre fichiers suivis modifiés ci-dessus et cette carte non
suivie ; index vide. Aucun commit créé, aucun verdict humain recueilli.
Les critères textuels sont couverts ; la carte reste à vérifier avec la limite
explicite du navigateur et ne constitue pas un résultat validé.

## Verdict humain — 2026-10-27

À la restitution d’OPS-062 et de ses preuves, incluant la réserve explicite sur
le test navigateur et le rendu non vérifiés faute de libnspr4.so, l’humain répond
« validé ». Ce verdict couvre uniquement OPS-062, dans l’état présenté sur la
base `13d69361ae061a1fec27f039bb199160d4f5db30` : quatre fichiers suivis modifiés
et cette carte. Les cinq empreintes SHA-256 ont été revérifiées identiques avant
l’ajout de cette trace. La réserve navigateur demeure ; aucun test navigateur
réussi ni contrôle visuel ne sont déduits de ce verdict. La carte reste à livrer.
