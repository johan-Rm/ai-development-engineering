# TASK OPS-045 — Donner un skill propre à chaque étape des deux boucles AIDE

- **Créée le** : 2026-10-26.
- **Session** : non disponible (Codex).
- **Statut** : clôturée — ✅ fait le 2026-10-26. Douze skills indépendants, outils transversaux, vue et documentation actualisés ; commit demandé par l’utilisateur après présentation.
- **Type** : outillage documentaire.
- **Tests** : validation de la structure et des liens des skills ; scénarios de lecture des entrées, sorties et arrêts ; vérification des douze correspondances dans la vue ; rendu et navigation clavier de la vue ; `git diff --check`. Contrôles existants pertinents et qualité avant PR. Pas de tests applicatifs : aucun comportement applicatif modifié.
- **Mission** : devops, `layers/devops`, `/home/johan/www/lab/ai-orchestrated-development/worktree/devops`.
- **Demande d’origine** : échange du 2026-10-26 ; proposition des douze skills validée, indépendance absolue des boucles exigée ; sources dans le dépôt, installation personnelle ensuite ; vue et documentation incluses.
- **Dépendances par commit** : base du worktree `7c35e0292f2cd3b2e5f2e46a5864a086ae5dd85d` (OPS-043), déjà intégrée dans `develop` à `aa8b856587058a5f71ec35c13d3cd319fb58b1ce`. Aucun travail non commité d’une autre mission requis.

## Contexte

Les huit premiers skills personnels de l’ancien workflow AIOD couvrent surtout le développement,
regroupent plusieurs étapes et ne fournissent pas de procédure propre à chaque case du schéma AIDE.
La consolidation doit pouvoir être conduite indépendamment du développement.

## Périmètre et chemins autorisés

Dans le worktree affecté uniquement :

- Créer `skills/` comme source versionnée, avec un README, les douze skills et leurs ressources nécessaires.
- Adapter et intégrer les outils transversaux issus des huit skills examinés, avec correspondance explicite entre anciens et nouveaux noms.
- Actualiser `AGENTS.md`, `README.md`, `SETUP.md`, `docs/` et leurs README existants concernés pour documenter le catalogue, les responsabilités et l’installation personnelle ultérieure.
- Actualiser `dev-book/resources/vue-d-ensemble-ai-development-engineering.html` et son README pour associer chaque case à son skill.
- Compléter la présente carte avec les preuves et les choix d’implémentation.

Lire les README applicables avant toute écriture. Utiliser le skill `skill-creator` lors de la création
ou modification des skills. Lire la charte officielle et sa synthèse avant les modifications graphiques.

## Décisions de cadrage

Douze skills distincts, six par boucle :

| Étape | Développement | Consolidation |
| --- | --- | --- |
| 01 | `interviewer-demande` | `interviewer-constat` |
| 02 | `decouper-demande` | `analyser-convention` |
| 03 | `implementer-tache` | `arbitrer-convention` |
| 04 | `verifier-tache` | `implementer-consolidation` |
| 05 | `reconstituer-demande` | `verifier-consolidation` |
| 06 | `livrer-demande` | `livrer-consolidation` |

Les noms suivent la proposition validée. Les deux boucles sont indépendantes : aucun skill d’une
boucle ne délègue son étape à un skill de l’autre et aucune entrée ne requiert d’avoir parcouru l’autre.
Elles peuvent lire les mêmes conventions du projet et utiliser des outils transversaux ; cela ne
crée pas de dépendance entre leurs parcours. Une demande de consolidation peut aussi venir directement
de l’humain. Un constat du développement peut l’alimenter sans la déclencher automatiquement.

Évolution des huit skills initiaux :

- `evoquer-un-sujet` : conserver avant les boucles.
- `creer-tache` : répartir interview et découpage entre les skills dédiés ; documenter son remplacement.
- `demarrer-tache` : recentrer l’implémentation dans les deux skills propres à chaque boucle.
- `commit-tache` : conserver comme outil transversal, un commit par tâche validée, sur demande explicite.
- `creer-pr` : conserver comme outil transversal appelé explicitement lors des livraisons autorisées ; les deux skills de livraison portent chacun leur procédure propre.
- `apres-pr-mergee` : conserver après les boucles.
- `etat-des-lanes` : conserver en lecture seule, hors des étapes.
- `configurer-worktrees-aiod` : adapter et renommer `configurer-worktrees-aide`, hors des étapes.

Le catalogue comprend donc douze skills d’étapes et les outils transversaux conservés.
Les anciennes installations personnelles servent de références en lecture ; leurs remplacements
et retraits sont documentés sans les appliquer dans cette tâche.

## Règles et cas limites

Chaque skill définit ses conditions d’entrée, sa responsabilité, sa sortie, ses preuves et ses
conditions d’arrêt. Une invocation n’enchaîne pas automatiquement les étapes ni les boucles.
Les skills d’arbitrage et de vérification présentent les éléments et recueillent un verdict humain ;
ils ne peuvent ni l’inventer ni le remplacer. Tests pertinents et documentation accompagnent
l’implémentation avant présentation. La boucle de développement n’affaiblit pas les règles pour
faire passer ses changements. La consolidation recherche les occurrences à l’échelle concernée,
formalise l’arbitrage et produit des contrôles exécutables sans IA.

La préparation des branches, les cartes, les commits et les PR doivent avoir un responsable explicite
à l’intérieur de chaque parcours ; aucune opération ne doit disparaître dans le découpage.
La reconstitution utilise uniquement des commits identifiés et autorisés.
Préserver les autorisations explicites exigées pour commit, push, PR et merge ; préserver les travaux
existants et les `.env`. Un arbre propre ne prouve pas la disponibilité d’une couche.
Les skills restent génériques et lisent les conventions du projet plutôt que figer les chemins personnels.

## Hors périmètre

Installation, écrasement ou suppression dans `~/.codex/skills` ; modification des autres skills personnels
(`creer-socle`, `vulgariser`, `create-readme`, `documentation-writer`) ; applications, infrastructure
et environnements ; refonte graphique générale ; modification des documents originaux ou cartes historiques.
Pas de commit, push, PR, merge ni opération distante dans le seul cadre de cette demande de cadrage.
Pas de changement des règles ou contrôles sans lien avec la refonte validée.
Permissions, données applicatives, chargement, référencement et migrations : sans objet.

## Documentation impactée

`skills/README.md` décrit le catalogue et la migration ; les SKILL.md portent les procédures.
`AGENTS.md`, les guides AIDE de `docs/`, le README racine et `SETUP.md` référencent les sources versionnées
et distinguent disponibilité des sources et installation effective. La vue interactive identifie le
skill de chaque étape sans substituer l’IA aux décisions humaines. Les liens vers les sources doivent
fonctionner depuis le mode de consultation documenté, y compris si le serveur ne sert que les ressources.

## Définition de terminé

- [x] Les douze cases ont chacune un skill distinct, présent dans le dépôt et correctement nommé.
- [x] Chaque boucle fonctionne sans invoquer ni exiger un skill de l’autre boucle.
- [x] Les entrées, sorties, preuves, arrêts et décisions humaines de chaque étape sont explicites.
- [x] Les huit anciens skills ont tous une correspondance documentée : remplacement, conservation ou renommage.
- [x] Les opérations transversales et l’installation ultérieure sont documentées sans modifier l’installation personnelle.
- [x] Vue interactive, instructions et documentation concordent sur les douze étapes et leurs skills.
- [x] Structure des skills, liens, scénarios de parcours et rendu de la vue ont été vérifiés ; preuves consignées.
- [x] Les contrôles pertinents passent sans affaiblissement des règles existantes.

## Réalisation et preuves

Lors du cadrage : branche `layers/devops` reprise sans changement de référence, sans fetch ni rebase ;
aucun commit de cette branche absent de `develop` à l’inventaire. Numéro vérifié dans l’historique de toutes
les références et les cartes des worktrees : dernier OPS observé, OPS-044. Aucun identifiant de session
fiable exposé par l’environnement ; repli explicite ci-dessus. Implémentation et vérifications réalisées ci-dessous.


## Implémentation du 2026-10-26

- `skills/` contient douze skills d’étapes et six outils transversaux, tous autonomes.
  Les procédures des douze étapes ont été écrites pour leurs responsabilités respectives ;
  les outils transversaux ont été adaptés pour supprimer les enchaînements de l’ancien workflow.
  Le skill de configuration conserve sa référence historique datée, sous le nom AIDE.
- La consolidation prépare ses cartes et branches dans son implémentation et réunit ses
  contributions dans sa livraison. Elle n’invoque aucun skill du développement.
  Le découpage du développement prépare ses propres cartes et branches ; les verdicts humains
  précèdent les commits explicitement demandés dans les deux parcours.
- Les deux skills de livraison possèdent leur procédure ; `creer-pr` est uniquement leur outil
  transversal optionnel. Les résultats réutilisés doivent couvrir le même HEAD et environnement.
- Catalogue, migration des huit anciens noms, installation ultérieure, AGENTS.md, README,
  SETUP, IA Engineering et douze pages d’étapes mis à jour.
- La vue affiche le skill et son chemin source en tête des détails de chacune des douze cases.
  Le texte reste consultable si seul le dossier de ressources est servi, sans lien HTTP hors
  racine. Aucun changement de CSS, palette, typographie, formes ou acteur ; conservation du
  cadre olive, des actions IA terre cuite et des étapes humaines olive observée en capture.

## Vérifications et preuves

- Validation `quick_validate.py` fourni par `skill-creator`, appliquée aux dix-huit dossiers :
  **18 réussites**. Frontmatter, noms et structure valides.
- Contrôle ponctuel des liens Markdown de `skills/`, `docs/`, AGENTS.md, README, SETUP et
  README des ressources : **toutes les destinations locales existent**.
- Inspection des données de la vue : **12 associations uniques**, sources présentes ; contrôle
  de l’absence de noms des skills de l’autre boucle dans chacun des douze SKILL.md : réussi.
  Cette vérification structurelle ne prouve pas à elle seule le comportement futur d’un agent.
- Scénarios examinés par lecture des procédures : constat direct sans demande de développement
  (interview de consolidation) ; arbitrage différé (aucune implémentation) ; contrôle rouge
  (aucune PR ni affaiblissement) ; verdict absent (aucune validation ni commit) ; contribution
  sans SHA (aucune reconstitution) ; branche propre mais occupée (aucun réalignement).
  Ces scénarios sont une revue des instructions, pas des simulations exécutées par un autre agent.
- `python3 codebase-integrity/scripts/check.py` : **23 tests réussis**.
  Le premier passage était limité par l’interdiction d’ouvrir le serveur HTTP temporaire ;
  le passage autorisé avec ce serveur local s’est terminé par `OK`.
- `node codebase-integrity/tests/browser/vue-aiod.cjs app/web/targets/app` : **réussi**,
  avec `LD_LIBRARY_PATH=/tmp/ops045-browser-libs/extracted/usr/lib/x86_64-linux-gnu`.
  Chromium nécessitait trois paquets Ubuntu extraits sous `/tmp` (libnspr4, libnss3,
  libasound2t64), sans installation système ni changement des dépendances du projet.
  Vérifie les douze actions, clic/clavier/tactile, focus, fermeture, panneau superposé et
  dimensions ordinateur/mobile. Les tests existants du Codebase Integrity restent inchangés.
- Vérification navigateur complémentaire `/tmp/ops045-view.cjs` : **12 skills distincts**,
  ouverture par Entrée, nom et chemin source dans les détails, fichier existant, fermeture
  par Échap et retour du focus ; mention du verdict humain vérifiée sur l’arbitrage.
- Captures : `/tmp/ops045-overview.png`, `/tmp/ops045-skill-panel.png` (arbitrage relu visuellement),
  ainsi que les captures ordinateur/mobile du test existant sous `/tmp/aiod-html-*.png`.
- `git diff --check` : réussi. La suite qualité applicative complète reste pour la livraison
  avant PR ; aucun changement applicatif dans cette mission.

## État de livraison

Résultat présenté, puis validé pour clôture par la demande explicite `commit-tache` de l’utilisateur.
Carte et changements réunis dans le commit OPS-045. Aucun push, PR, merge ni installation personnelle. La vue modifiée est celle du worktree devops ; un serveur
servant les ressources du dépôt principal ne reflète pas ces changements avant intégration.


## Livré

- Dix-huit SKILL.md, le catalogue et la référence historique de configuration dans `skills/`.
- Les douze associations de la vue interactive et son README.
- Instructions du projet, guides des deux boucles, IA Engineering, index, README et SETUP actualisés.
- Carte clôturée avec les preuves de validation et la migration des huit anciens skills.

## Tests ajoutés et exemption

Sans objet pour de nouveaux tests versionnés : procédures et contenu documentaire uniquement,
y compris les données textuelles de la vue ; aucun changement de logique exécutable.
La validation des skills, les tests existants et le contrôle navigateur complémentaire décrits
ci-dessus couvrent le résultat. Aucune modification des vérificateurs du Codebase Integrity.

## Reste à faire (hors périmètre)

Installation personnelle des skills et retrait des anciens noms sur demande distincte.
Qualité complète et PR, puis intégration, uniquement sur demande de livraison.


## Correction demandée après le commit initial — 2026-10-26

L’utilisateur demande que les skills soient opérationnels dans le répertoire personnel avant
livraison et retire la conservation de leurs sources dans le dépôt. Cette instruction remplace
le choix initial des sources versionnées et de l’installation ultérieure, conservé ci-dessus
comme historique du premier commit.

Les dix-huit skills ont été installés et validés dans `/home/johan/.codex/skills/` ; les trois
anciens noms remplacés ont été retirés. Les autres skills personnels ont été préservés par
comparaison SHA-256. Les huit anciens dossiers ont été sauvegardés sous
`/tmp/aide-skills-avant-refonte-huuypil4`. La session expose désormais les dix-huit nouveaux skills.
Le dossier `skills/` du projet est retiré et les références actives corrigées pour désigner
les skills personnels. Correction non commitée ; aucun changement de l’historique Git.


## Simplification complémentaire demandée — 2026-10-26

Suppression personnelle de `evoquer-un-sujet`, `commit-tache`, `creer-pr` et `apres-pr-mergee`.
Les deux skills de vérification exécutent eux-mêmes les commits autorisés après verdict humain.
Les deux skills de livraison exécutent eux-mêmes push, PR, fusion et suivi selon la demande,
sans dépendance aux skills supprimés ni aux skills de l’autre boucle. Les autorisations du projet,
les checks et revues avant fusion, la preuve de fusion et la préservation des branches occupées
restent explicites. Les quatorze skills restants passent quick_validate ; les quatre dossiers
supprimés sont absents et aucune référence à ces noms ne subsiste dans les douze skills d’étape.
Sauvegarde préalable : `/tmp/aide-avant-integration-git-iyw7kz8y`.
Documentation active mise en cohérence ; aucune opération Git de livraison effectuée.


## Vérification et clôture des corrections — 2026-10-26

Après présentation du résultat et demande de validation/commit, l’utilisateur invoque
`verifier-tache OPS-045` : accord de clôture et de commit retenu dans ce contexte.
Les quatorze skills personnels ont été validés ; les suppressions et l’indépendance des
boucles sont vérifiées. Les modifications du dépôt sont documentaires et retirent les copies
des skills ; aucun nouveau comportement applicatif ni contrôle modifié. Les tests existants
et preuves de la première implémentation restent référencés ci-dessus ; `git diff --check`
est réussi sur les corrections. Aucun fichier hors OPS-045 observé dans l’index ou le diff.
La correction remplace les critères initiaux de sources versionnées et d’outils transversaux
supprimés ; les décisions initiales restent historiques. Les skills personnels opérationnels
ne font pas partie du commit du dépôt. Aucun push, PR ni merge demandé à cette étape.
