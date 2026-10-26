# OPS-039 — Renommer le cadre de contrôle en Codebase Integrity

- **Créée le** : 2026-10-24.
- **Session** : non disponible (Codex).
- **Statut** : ✅ fait le 2026-10-24.
  Renommage complet en Codebase Integrity, références actives et tests adaptés.
- **Type** : refactor.
- **Tests** : inventaire des références avant/après, vérification des liens et ancres, tests existants de l’outillage, contrôle navigateur du schéma AIDE et commande qualité existante depuis les nouveaux chemins ; `git diff --check`. Adapter les tests affectés sans affaiblir leurs assertions. Aucun nouveau contrôle de domaine demandé.
- **Demande** : nom `codebase-integrity` retenu par l’utilisateur ; périmètre complet de renommage validé le 2026-10-24 dans la conversation.
- **Mission** : devops, `layers/devops`, `worktree/devops`.
- **Dépendances par commit** : base locale `7bf59d6ef3cd2307ba7a9a20acd8a4591ae65c7e`, commune à `develop` et `layers/devops` au cadrage ; aucun autre commit amont requis, aucune tâche aval imposée.
- **Réf** : `README.md`, `codebase-quality-control/README.md`, `docs/01-codebase-quality-control/`, `docs/02-cadre/couches.md`, `.github/workflows/quality.yml`.

## Contexte

Le nom Codebase Quality Control ne représente pas suffisamment, pour l’utilisateur,
la portée du dispositif : sécurité, UX/UI, métier, comportement, architecture,
fiabilité, conformité, compatibilité, construction et rendu. Le nom Codebase Integrity
a été retenu pour désigner ce même dispositif transversal.

## Périmètre

- Renommer `codebase-quality-control/` en `codebase-integrity/`.
- Renommer `docs/01-codebase-quality-control/` en `docs/01-codebase-integrity/`.
- Employer « Codebase Integrity » dans les contenus actifs, titres, libellés et ancres.
- Adapter les chemins, imports éventuels, commandes, configurations, tests, liens et
  références du dépôt qui dépendent de ces noms, notamment la CI et le schéma AIDE.
- Chemins autorisés dans le worktree affecté : les deux répertoires et leurs destinations,
  `README.md`, `SETUP.md`, `AGENTS.md`, `worktree/README.md`, `docs/`, `.github/`, les configurations du cadre
  contenant des références concernées, `dev-book/runbooks/`, `dev-book/resources/`,
  la présente carte, ainsi que les README concernés sous `app/`, `design/` et `infra/`.
  Dans ces fichiers partagés, seules les adaptations liées au renommage sont autorisées.

## Hors périmètre

- Ajout de contrôles de sécurité, UX/UI, métier ou de tout autre domaine.
- Modification des conventions, seuils, exceptions, niveaux de blocage ou comportements.
- Réécriture des cartes clôturées, preuves datées et historique Git.
- Modification fonctionnelle des applications, contrats d’API, données, services,
  environnements, permissions ou infrastructure de déploiement.
- Modification des skills personnels ou des autres worktrees ; commit, push, PR et merge.

## Décisions de cadrage

- Le README suivi `worktree/README.md` contient deux commandes actives : il est inclus
  dans les adaptations documentaires du cadre ; aucun worktree imbriqué n’est modifié.
- Renommage complet validé, comprenant nom affiché, dossier d’outillage et chapitre documentaire.
- Une seule carte devops : les adaptations des README applicatifs concernent les liens
  vers le cadre commun, sans changement de responsabilité applicative.
- Conserver les noms des commandes `check.py` et `quality.py` et le comportement existant.
- Préserver les traces historiques ; les distinguer explicitement des références actives
  lors de la recherche des anciennes occurrences, plutôt que les remplacer globalement.
- Aucun identifiant fiable de session Codex n’est disponible ; ce champ ne prouve pas
  l’occupation ou la disponibilité de la couche. Vérifier sa coordination avant implémentation.
- Le cadrage reprend la branche existante, propre et alignée sur `develop`, sans fetch,
  rebase ni autre opération distante.

## Règles et cas limites

- Lire les README applicables avant chaque modification et la charte officielle avant
  toute adaptation du schéma. Conserver les interactions et vérifier que le nouveau
  libellé reste lisible sans débordement.
- Rechercher aussi les variantes typographiques, ancres HTML et chemins codés en dur,
  y compris dans les fichiers cachés suivis ; exclure `.git/`, les dépendances et `worktree/`.
- Ne pas ajouter d’alias vers les anciens chemins : les consommateurs actifs du dépôt
  doivent utiliser le nouveau nom. Signaler tout consommateur externe découvert.
- Une référence historique restante doit être identifiable comme telle ; les nouveaux
  liens actifs ne doivent pas pointer vers un chemin supprimé.
- Les états applicatifs, migrations de données, rôles métier, traduction et contraintes
  de performance sont sans objet pour ce renommage ; seule la lisibilité du schéma
  nécessite une vérification de rendu.
- Si une commande requise est empêchée par une dépendance ou l’environnement,
  consigner le blocage et ne pas déclarer sa réussite.

## Documentation impactée

README racine, `SETUP.md`, `AGENTS.md`, README de l’outillage déplacé,
chapitre documentaire déplacé, index et guides des boucles, guide des couches,
runbook de recette, schéma AIDE et README de ses ressources, README applicatifs,
de design et d’infrastructure contenant les références concernées. Inventorier
les occurrences exactes avant modification ; la carte ne remplace pas ces documents.

## Définition de terminé

- [x] Les dossiers et le nom affiché utilisent Codebase Integrity conformément au cadrage.
- [x] Aucun consommateur actif du dépôt ne dépend des anciens chemins ou libellés.
- [x] Les liens et ancres concernés pointent vers des cibles existantes.
- [x] La CI, les outils et leurs tests utilisent les nouveaux chemins sans changement de règles.
- [x] `python3 codebase-integrity/scripts/check.py` réussit.
- [x] Le contrôle navigateur existant du schéma réussit ; le nouveau libellé et les interactions sont vérifiés visuellement.
- [x] `python3 codebase-integrity/scripts/quality.py` réussit avec ses prérequis disponibles.
- [x] Les cartes clôturées et preuves historiques sont préservées, les anciennes occurrences restantes sont expliquées.
- [x] La documentation concernée est cohérente et `git diff --check` réussit.

## Réalisation et preuves

Implémentation du 2026-10-24 dans le seul worktree devops, sur `layers/devops`,
sans commit, fetch, rebase ni modification des autres worktrees.

- Deux dossiers renommés ; 34 fichiers actifs adaptés, y compris les deux commandes
  du README suivi `worktree/README.md`. Scripts, CI, documentation, ancres et schéma
  utilisent les nouveaux chemins et libellés. Aucun alias créé.
- Recherche insensible à la casse des anciens noms, variantes avec espaces ou tirets
  et acronyme CQC dans les fichiers suivis : aucune occurrence active restante.
  Vingt-huit cartes historiques conservent les anciens noms ; toutes les cartes
  préexistantes ont été comparées octet par octet à HEAD et sont inchangées.
  Les mentions d’origine dans la présente carte décrivent la migration.
- Comparaison des fichiers suivis avec HEAD : seules les substitutions du nom et du
  chemin, plus la correction d’assertion décrite ci-dessous, ont été effectuées.
  Configurations, seuils et comportements conservés ; aucun fichier applicatif
  fonctionnel ou verrou de dépendances modifié.
- Vérification de 65 liens locaux et ancres Markdown dans les documents concernés :
  aucune rupture introduite. Le lien `../ia-engineering/parallel-work.md` dans
  `worktree/README.md` était déjà absent dans HEAD ; il reste hors périmètre.
- `python3 codebase-integrity/scripts/worktrees.py list` : réussi depuis le nouveau
  chemin ; les six arbres sont identifiés, seul devops porte les changements.
- `python3 codebase-integrity/scripts/quality.py` : code de sortie 0.
  Il exécute les 18 tests de l’outillage (`check.py`), le test du contrat API,
  la validation du conteneur et du schéma Symfony, la comparaison OpenAPI,
  puis le typage et les builds des deux applications Nuxt.
- `LD_LIBRARY_PATH=/tmp/ops039-browser-libs/root/usr/lib/x86_64-linux-gnu node
  codebase-integrity/tests/browser/vue-aiod.cjs app/web/targets/app` : code de sortie 0.
  Vérifications des libellés Codebase Integrity, des interactions souris/clavier/tactile,
  du focus et des dimensions ordinateur/mobile. Captures relues :
  `/tmp/aide-codebase-integrity.png` (panneau et bandeau renommés, lisibles) et
  `/tmp/aiod-html-390.png` (rendu mobile). Palette et typographie existantes conservées.
- `git diff --check` : réussi. Les nouveaux fichiers ont également été examinés
  par comparaison avec leur contenu avant déplacement.

### Ajustement de test

Le test navigateur échouait sur « Chaque convention appartient à un seul domaine »,
alors que le HTML de HEAD contenait déjà « Chaque convention technique appartient
à un seul domaine ». L’assertion a été alignée sur cette formulation existante,
sans suppression ni assouplissement de la vérification. Aucun texte de règle n’a changé.

### Environnement de vérification

Les premiers essais ont révélé des dépendances applicatives absentes et le blocage
par le bac à sable des sockets de test. Les commandes finales ont été exécutées
avec autorisation d’ouvrir les serveurs locaux. Les dépendances verrouillées ont été
installées dans ce worktree ; l’outil d’installation API a créé uniquement le `.env`
manquant depuis `.env.example`. Aucun `.env` préexistant n’a été remplacé.
Chromium a été téléchargé dans le cache Playwright et ses bibliothèques manquantes
extraites dans `/tmp/ops039-browser-libs/`, sans installation système.
Les journaux temporaires sont `/tmp/ops039-quality.log`, `/tmp/ops039-browser.log`
et `/tmp/ops039-links.txt`. Ces fichiers et captures sont des preuves locales temporaires.

## Vérification

Les résultats et preuves de la réalisation ci-dessus ont été relus avant clôture.
La demande explicite de commit OPS-039 du 2026-10-24 autorise cette clôture.
Aucune modification fonctionnelle depuis les contrôles réussis ; aucune gate complète
relancée lors du commit.

## Livré

`codebase-integrity/` et `docs/01-codebase-integrity/` remplacent les anciens dossiers.
La CI, les instructions, les README, les guides et le schéma AIDE pointent vers ce nom.
Les tests adaptés et la présente carte accompagnent le renommage dans un seul commit.

## Reste à faire (hors périmètre)

Le lien préexistant absent `../ia-engineering/parallel-work.md` dans
`worktree/README.md` reste à traiter dans une demande distincte.
Push, PR et merge restent soumis à une demande explicite.
