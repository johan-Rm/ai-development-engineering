# OPS-074 — Harmoniser schéma, skills et procédures

- Demande : [DEM-023](../demand/DEM-023-harmoniser-boucles.md).
- Session de création : `01a18c38-1b13-7953-9118-aadc8cde8794`.
- Couche : devops ; worktree `worktree/devops` ; branche `layers/devops`.
- Statut : validée humainement le 2026-10-30 ; commit local à créer.
- Base : `6a527151f01c097ed39b5f67791a7d6d52f8440c` ; aucune dépendance de code.

## Mission

Appliquer les décisions de la demande dans le schéma puis dans les douze skills.
Chemins : `dev-book/resources/vue-d-ensemble-ai-development-engineering.html`,
`docs/architecture/`, `README.md`, `AGENTS.md`, liens Markdown entrants, test navigateur
du schéma, demande et carte ; skills correspondants sous `~/.codex/skills/`.
Supprimer uniquement le skill d’arbitrage autonome. Préserver les autres skills,
le code applicatif, environnements, données et sources graphiques.

## Vérifications et résultat

Vérifier les douze étapes, acteurs et skills ; navigation et liens ; tests du schéma
sur ordinateur/mobile, interactions et clavier ; validation des skills ; contrôles
documentaires et tests de l’outillage. Résultats du 2026-10-30 :

- Test navigateur du schéma réussi : douze actions, six étapes et six skills uniques
  par boucle, un acteur humain à l’étape 04 ; panneaux, clavier, tactile, focus,
  fermetures et dimensions 1918×924, 1366×768, 1280×614 et 390×844. Captures relues dans
  `/tmp/dem023-browser/` ; le mobile conserve la navigation horizontale interne.
- Correction après capture humaine : mêmes espacements internes et hauteurs de
  sortie pour les deux boucles ; grille rétractable et typographie compacte. Test
  des hauteurs et positions correspondantes, absence de recouvrement des sorties
  et de débordement du texte, réussi aux quatre dimensions ci-dessus.
- Douze skills installés vérifiés par `quick_validate.py`, avec contrôle des numéros
  01 à 06 et des libellés dans chaque boucle ; nouveau `reconstituer-consolidation`,
  suppression effective d’`arbitrer-convention`. Les autres skills sont préservés.
- `python3 codebase-integrity/scripts/check.py` : 66 tests réussis (socket locale autorisée).
- `python3 codebase-integrity/scripts/check_docs.py`,
  `python3 codebase-integrity/scripts/check_demands.py` et `git diff --check` : réussis.

Chromium sur l’hôte manque de `libnspr4.so` ; test réussi dans l’image existante
`aide-app-browser:ec4e123090`, sans réseau ni montage des environnements. Le premier
essai Docker a révélé les droits insuffisants du dossier temporaire pour Chromium ;
correction limitée à ce dossier. Une attente olive obsolète du test a été corrigée
vers la terre cuite `#C07040` déjà présente dans le schéma et prescrite par la charte ;
aucun style de couleur modifié.

Commande navigateur utilisée, depuis la racine du worktree (image déjà disponible) :

```sh
task_root="$PWD"
task_artifacts=/tmp/dem023-browser
mkdir -p "$task_artifacts"
chmod 1777 "$task_artifacts"
docker run --rm --network none --shm-size=256m \
  --mount "type=bind,source=$task_root/codebase-integrity/tests/browser/vue-aiod.cjs,target=/repo/codebase-integrity/tests/browser/vue-aiod.cjs,readonly" \
  --mount "type=bind,source=$task_root/dev-book/resources/vue-d-ensemble-ai-development-engineering.html,target=/repo/dev-book/resources/vue-d-ensemble-ai-development-engineering.html,readonly" \
  --mount "type=bind,source=$task_artifacts,target=/tmp" \
  aide-app-browser:ec4e123090 node /repo/codebase-integrity/tests/browser/vue-aiod.cjs /opt/aide-browser
```

Les skills personnels sont hors Git ; leurs versions précédentes sont conservées
hors du catalogue dans `/tmp/dem023-skills-before/`. La cohérence des autorisations
avec AGENTS.md et les guides a été relue : pas de commit à l’étape 03, commits après
verdict à l’étape 04, réunion à l’étape 05 et Rebase and merge à l’étape 06. Le
repositionnement local après réécriture des SHA reste conditionné à la preuve
d’intégration, aux correspondances et à l’absence de travail inédit ou partagé.
Ce suivi Git est documenté, pas exécuté sur un distant dans cette intervention.

Qualité applicative complète non exécutée : aucun code applicatif modifié ;
elle reste requise avant PR. Aucun réglage GitHub modifié ni push. Le brief DEM-024
reste distinct et hors du commit d’OPS-074.

Empreinte SHA-256 des douze skills installés (noms triés et contenus) :
`0942843446a3b3f46bd1527a8f190e31959a3bae046a3e1ce7e6317d52bf644f`.

Contenu présenté : base en tête, 26 chemins modifiés/supprimés/non suivis.
Empreinte SHA-256 des chemins triés et contenus, hors cette carte :
`1e136e94f0df2bfb66679006faeaae0a03e204da7b775d63b914f267707c79b4`. Index vide. Les skills personnels sont identifiés séparément ci-dessus.

## Verdict humain

Le 2026-10-30, même session de création : réponse exacte « validé » à la
présentation d’OPS-074, incluant la correction d’alignement du schéma. Les deux
empreintes ci-dessus ont été vérifiées identiques avant consignation du verdict.
Les seules adaptations suivantes sont les traces de validation et de commits.

Périmètre du commit : 25 chemins de la carte, documentation, test et preuves inclus.
Le brief non suivi DEM-024 est explicitement exclu. Les douze skills personnels
restent hors du dépôt ; leur installation effective est identifiée par l’empreinte
ci-dessus. Leur suppression/création et leurs étapes ont été vérifiées.
