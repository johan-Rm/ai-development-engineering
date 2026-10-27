# DEM-010 — Corriger le titre long AIDE

- Date : 2026-10-27.
- État : reconstituée et validée ; livraison bloquée par une assertion navigateur préexistante, non livrée.
- Identifiant de session de création : `01a17e4d-043f-7c71-9aa5-3754c3794e18`.
- Carte externe : aucune fournie.

## Besoin et utilisateurs

Le titre long actuel « AI Development Engineering » ne correspond plus à la
formulation voulue par l’humain. Les lecteurs de la documentation et du schéma
AIDE doivent retrouver un titre cohérent : **AI-powered Development Engineering**.
Le sigle reste **AIDE**.

## Périmètre et résultat attendu

Corriger tous les supports actuels du dépôt et le test associé. Les occurrences
repérées comprennent le README racine, les principes fondamentaux dans `docs/`,
la signature visible et son libellé accessible dans
`dev-book/resources/vue-d-ensemble-ai-development-engineering.html`, ainsi que
l’assertion correspondante dans `codebase-integrity/tests/browser/vue-aiod.cjs`.
L’implémentation devra vérifier les autres occurrences actuelles éventuelles.

Conserver les anciennes demandes et cartes comme traces historiques, y compris
leurs formulations anciennes. La carte OPS-040 documente une harmonisation
antérieure ; elle ne porte pas ce nouveau besoin et ne doit pas être réécrite.

## Contraintes et exclusions

- Conserver le sigle AIDE, les noms de fichiers et les chemins existants.
- Préserver les traces historiques, les .env, les données et les travaux étrangers.
- Conserver la présentation graphique ; vérifier que le titre plus long reste lisible.
- Ne modifier ni les conventions techniques ni la logique des contrôles : seule
  l’attente textuelle du test associé est concernée.
- Aucun changement fonctionnel applicatif, renommage du dépôt ou nouvelle identité graphique.

## Critères observables et preuves attendues

1. Tous les supports actuels utilisent exactement « AI-powered Development Engineering ».
2. La recherche des anciennes formulations distingue les traces historiques
   conservées et ne trouve plus d’ancien titre dans les supports actuels.
3. La signature du schéma et son libellé accessible portent le nouveau titre.
   Une vérification visuelle sur ordinateur et mobile confirme sa lisibilité.
4. Le test navigateur associé attend le nouveau titre et réussit.
5. Le diff confirme la préservation des anciennes demandes et cartes, du sigle,
   des chemins et des noms de fichiers.

Les commandes et prérequis précis du test navigateur seront relevés dans ses
README à l’implémentation. Les contrôles du projet sont
`python3 codebase-integrity/scripts/quality.py` avant PR et
`python3 codebase-integrity/scripts/check.py` pour l’outillage, selon le périmètre.

## Décisions humaines et confirmation

L’humain demande : « la version longue de notre titre AIDE doit etre :
AI-powered Development Engineering ».

À la question interactive de périmètre, il choisit : « Tous les supports actuels
et le test associé ; conserver les traces historiques ».

Le cadrage restitué précise le nouveau titre, la conservation du sigle et des
chemins, la préservation des anciennes demandes et cartes et la vérification
de cohérence et du rendu. L’humain le confirme dans le chat par « confirmé »
le 2026-10-27. Cette confirmation porte sur le besoin, pas sur un résultat implémenté.

## Questions ouvertes

Aucune question de besoin restante. Les prérequis d’exécution du test et les
occurrences supplémentaires éventuelles relèvent de l’examen technique ultérieur.
La correction étant éditoriale, elle n’introduit aucun parcours utilisateur ni
cas métier supplémentaire.

## Tâches issues du découpage

| Carte | Couche | Critères couverts | Dépendances | État |
| --- | --- | --- | --- | --- |
| [OPS-062](../tasks/OPS-062-corriger-titre-long-aide.md) | devops | 1 à 5 : supports, historique, accessibilité, rendu et test | Aucune tâche amont ; base `13d69361ae061a1fec27f039bb199160d4f5db30` | Validée et commitée avec réserve navigateur |

Mission dans `worktree/devops`, branche `layers/devops`, déjà existante et propre
avant création de la carte. Chemin absolu résolu dans cette session :
`/home/johan/www/lab/ai-development-engineering/worktree/devops`.
Aucune mission concurrente active identifiée dans les cartes consultées.
Le découpage est réalisé dans la session de création, sans commit ni implémentation.

Reconstitution prévue dans ce même worktree, après vérification de sa disponibilité,
sur `demands/DEM-010`, créée à cette étape depuis develop. Branche de retour :
`layers/devops`. Attendre le SHA du commit validé d’OPS-062, puis cherry-pick -x ;
aucun SHA de résultat n’est encore disponible. Le fichier définitif de DEM-010
sera créé sur cette branche avec les liens relatifs adaptés à son emplacement.
La branche demands/DEM-010 n’est pas créée au découpage.

## Contexte de travail de l’interview

Document créé dans `worktree/devops`, sur `layers/devops`, à partir du commit
`13d6936`. État Git propre avant création ; aucune mission concurrente active
identifiée dans les cartes consultées. Le maximum DEM observé dans l’historique
de toutes les références Git locales et dans les worktrees est DEM-009 ; aucune
demande existante correspondant à cette nouvelle formulation n’a été trouvée.
Aucun fetch, commit, découpage ou changement des supports à cette étape.

## Mise à jour du rangement — 2026-10-27

L’humain confirme que seules les demandes restent dans `tmp/` à la racine du
dépôt principal, ignoré par Git. Les cartes restent versionnées dans les
worktrees. Le document définitif sera créé à la reconstitution dans
`dev-book/demand/DEM-010-corriger-titre-long-aide.md`, sur `demands/<identifiant>`,
avec décisions, identifiant de session et liens vers les cartes. L’identité
DEM-010 déjà attribuée est conservée ; ce fichier est un brouillon local.
Le déplacement ne modifie pas le périmètre confirmé de la correction du titre.

## Vérification humaine et commits locaux — 2026-10-27

L’humain répond « validé » à la présentation d’OPS-062 avec réserve explicite :
test navigateur et rendu non vérifiés faute de libnspr4.so. Les cinq empreintes
des fichiers présentés ont été vérifiées identiques avant commit.

- Commit d’OPS-062 : `5737c74` (implémentation, test, documentation, preuves et verdict).
- Commit documentaire de traçabilité : `f041526b9edf8c108c11a4091f82557de065c632`,
  ne modifiant que la carte pour consigner son SHA et son état.

La reconstitution devra inclure ces deux commits dans cet ordre. Aucun push,
aucune branche de reconstitution créée et aucune livraison à cette étape.

## Reconstitution réalisée — 2026-10-27

Branche `demands/DEM-010` créée dans `worktree/devops` depuis le develop local
`13d69361ae061a1fec27f039bb199160d4f5db30`. Worktree propre et index vide avant
opération ; branche de retour : `layers/devops`. Aucun fetch effectué.

| Commit source validé | Commit obtenu par cherry-pick -x | Contenu |
| --- | --- | --- |
| `5737c74570b124c7d92cbefa0d3d36b22700b22a` | `580aae6b6996f8344cc4bd86090de3241992d1da` | OPS-062, correction et verdict |
| `f041526b9edf8c108c11a4091f82557de065c632` | `2bad2f069df7cffd4d52a1c5c72a2c065d4d780c` | Trace du SHA validé |

Les deux cherry-picks ont réussi sans conflit. L’arbre obtenu est identique à
celui de layers/devops avant la matérialisation documentaire. Les sections
précédentes décrivent l’historique des étapes ; le présent état les actualise.
Le brouillon local est conservé. Ce document définitif est créé à cette étape,
conformément au rangement explicitement confirmé par l’humain ; il reste non
commité pour la prochaine étape de livraison. Aucun push, PR ou merge effectué.

Contrôles de reconstitution : comparaison des arbres avec layers/devops sans
diff, git diff --check, syntaxe Node et existence du lien carte/demande.
Le contrôle qualité réussi à l’implémentation porte sur le même arbre de code.
La réserve navigateur validée reste inchangée : libnspr4.so absente, test
navigateur et rendu non vérifiés. Aucun succès supplémentaire n’est inventé.

## Préparation de livraison — 2026-10-27

Accès GitHub vérifié et fetch origin effectué ; origin/develop et develop
pointent sur `13d69361ae061a1fec27f039bb199160d4f5db30`. Aucune PR ouverte
au début de la préparation. Le dépôt autorise les merge commits, stratégie
prévue pour cette livraison. Les cinq couches et le principal sont propres,
hors cette demande définitive attendue dans le worktree de livraison ; aucune
mission concurrente active identifiée dans les cartes consultées.

Le problème de dépendances Chromium est contourné sans installation système :
paquets Ubuntu libnspr4, libnss3 et libasound2t64 téléchargés et extraits sous
`/tmp/dem010-browser-deps`, puis exécution avec
`LD_LIBRARY_PATH=/tmp/dem010-browser-deps/extracted/usr/lib/x86_64-linux-gnu`.
Le test `node codebase-integrity/tests/browser/vue-aiod.cjs app/web/targets/app`
démarre, mais échoue ligne 42 : couleur attendue rgb(168, 185, 122), couleur
observée rgb(192, 112, 64). Cette assertion est identique dans develop avant
DEM-010 ; le terre cuite observé correspond à la charte actuelle (DEM-003).
Aucun changement de cette assertion ni de la couleur n’est inclus dans DEM-010.

Contrôle ciblé séparé via Playwright : nouveau titre exact, aria-label exact,
absence de débordement de la signature et de la page vérifiés sur 1918 × 924
et 390 × 844. Captures `/tmp/dem010-desktop.png` et `/tmp/dem010-mobile.png`
relues : signature lisible dans les deux cas. Ce contrôle ne remplace pas le
test complet qui reste en échec. Le reste du schéma mobile est une zone
horizontale défilante préexistante, sans modification de mise en page.

La livraison est bloquée avant push et PR conformément au skill : un contrôle
requis échoué bloque l’ouverture. La correction du test dépasse l’attente
textuelle autorisée par OPS-062. La réserve initiale sur le navigateur est
complétée par ces constats, sans invention d’un nouveau verdict humain.

Alignement à prévoir à la reprise : layers/devops contient les deux SHA sources
validés et diverge de leurs cherry-picks. Vérifier leur équivalence, déjà constatée
sur les arbres de code, puis rattacher cet historique par merge ciblé avant PR
pour permettre l’avance rapide finale. Les quatre autres couches restent sur
la base develop. Aucun historique de couche modifié pendant cette préparation.

Contrôle final `python3 codebase-integrity/scripts/quality.py` : réussite,
code 0, sortie /tmp/dem010-quality.log. `git diff --check` : réussite.
La demande définitive et les preuves de préparation sont commitées localement ;
aucun code supplémentaire ni correction du test hors périmètre.
