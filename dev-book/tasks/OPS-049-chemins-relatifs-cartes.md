# OPS-049 — Rendre les chemins documentaires portables

- État : validée.
- Date : 2026-10-26.
- Demande d’origine : [DEM-004](../demand/DEM-004-chemins-relatifs-cartes.md).
- Couche : devops, maintenance documentaire du cadre.
- Session : référence de session indisponible.
- Worktree : `worktree/devops`, relativement à la racine du dépôt principal.
- Branche : `layers/devops`.

## Objectif et chemins autorisés

Remplacer les chemins personnels vers le dépôt par des chemins relatifs au dépôt principal.
Harmoniser les règles de rédaction avec la décision humaine de DEM-004, tout en conservant
la résolution et la vérification du chemin absolu à l’exécution.

Chemins autorisés, dans le seul worktree affecté :

- `dev-book/tasks/*.md` : toutes couches et tous statuts, en tant que documents du cadre ;
- `dev-book/demand/*.md` : références liées aux missions et preuves documentaires ;
- `AGENTS.md`, `dev-book/README.md` ;
- `docs/02-cadre/couches.md`, `docs/02-cadre/ia-engineering.md` ;
- `SETUP.md` : seulement si la relecture révèle une instruction contradictoire sur les cartes ;
- la présente carte et DEM-004 pour leur suivi et leurs preuves.

Lire avant écriture les README racine et dev-book, ainsi que tout README applicable
sur les chemins documentaires touchés. Appliquer la décision humaine sur les chemins
relatifs plutôt que recopier l’ancienne exigence de chemin absolu versionné.

## Exclusions

Ne pas réparer les liens Git, modifier Docker, les applications ou les fichiers `.env`.
Ne pas modifier les skills personnels, ni copier les fichiers non commités d’un autre
worktree. Ne pas modifier le Codebase Integrity, ses contrôles ou leurs configurations.
La décision documentaire est déjà confirmée par l’humain ; toute évolution supplémentaire
d’une convention technique ou d’un contrôle relève de la consolidation.
Ne pas rouvrir les cartes historiques ni modifier leurs dates, SHA, verdicts ou résultats.
Les chemins historiques hors du dépôt ne sont pas transformés en faux chemins relatifs
à ce dépôt ; leur éventuelle neutralisation doit conserver leur signification.

## Dépendances et préparation

Base locale existante : `ce9fca295d748188c03f65e0d056011a036a621b`, tête observée
de `layers/devops`. Aucun commit amont distinct nécessaire, aucune dépendance graphique
ou applicative. DEM-004 et cette carte appartiennent à la même mission et au même worktree.
Une seule carte, sans délégation ni parallélisation.

Prérequis opérationnel non satisfait : le fichier `.git` référence l’ancien emplacement.
La réparation est exclue de DEM-004 ; avant démarrage, vérifier à nouveau le chemin absolu
résolu localement, la branche, l’état Git et la disponibilité réelle de la couche.
La branche existante est conservée, sans rebase. Aucun fetch requis ni effectué.

## Critères d’acceptation

1. Les affectations et références documentaires au dépôt utilisent des chemins relatifs
   à sa racine principale : `worktree/devops`, `app/...`, `.git/...`, ou `.` selon le cas.
2. Aucun chemin personnel absolu vers le dépôt ne subsiste dans les documents autorisés.
   Les références génériques existantes au dépôt sont harmonisées lorsqu’elles désignent
   une affectation ou une preuve concernée ; ne pas faire de remplacement aveugle.
3. Les consignes et guides concernés précisent l’origine des chemins relatifs et réservent
   la résolution du chemin absolu à l’exécution, avec contrôle de branche et d’état Git.
4. Le sens des commandes et preuves historiques reste lisible ; dates, SHA, états et
   verdicts restent identiques. Les originaux demeurent disponibles dans l’historique Git.
5. Les preuves couvrent les cinq critères de DEM-004 et les contrôles pertinents réussissent,
   ou leurs limites sont explicitement rapportées sans affaiblissement des règles.

## Vérifications et preuve attendues

- Inventorier avant correction les chemins personnels et les exigences de persistance
  d’un chemin absolu dans les documents autorisés ; conserver les fichiers et catégories.
- Rechercher après correction les préfixes personnels de type `/home/`, `/Users/` et
  chemins Windows, ainsi que les anciens noms du dossier. Examiner les occurrences
  restantes pour distinguer les références au dépôt des chemins externes.
- Relire chaque substitution : origine relative explicite, commandes historiques intelligibles,
  absence de modification de date, SHA, état, verdict ou lien documentaire.
- Exécuter `git diff --check`, `python3 codebase-integrity/scripts/check.py` et
  `python3 codebase-integrity/scripts/quality.py` depuis le worktree affecté, en rapportant
  leurs résultats et les limites éventuelles. Aucun nouveau test applicatif prévu pour
  ce changement documentaire ; aucun contrôle de convention nouveau dans cette carte.

## Documentation, réalisation et preuve du découpage

Documentation prévue : consignes, README du dev-book, guides des missions, cartes et
demandes concernées. Résultats de recherche, relecture et contrôles à consigner ici lors
de l’implémentation ; aucune correction de ces documents n’est réalisée à cette étape.

Historique de toutes les références locales et fichiers des worktrees inspectés sans fetch :
maximum OPS-048 avant attribution. État observé via les métadonnées Git explicitement
désignées : branche `layers/devops`, seul DEM-004 non suivi avant découpage.
Les cartes consultées n’indiquent aucune autre mission devops en cours ; disponibilité à
revérifier avant implémentation. Les commandes Git ordinaires échouent sur l’ancien chemin :
préparation opérationnelle bloquée, branche conservée au commit de base ci-dessus.
Réunion prévue dans DEM-004 sur `demands/DEM-004`, à créer à la reconstitution.
Aucune implémentation, aucun commit et aucune opération distante effectués.

## Réalisation et preuves — 2026-10-26

Avant écriture, branche `layers/devops` et base prévue confirmées ; index vide,
seuls DEM-004 et OPS-049 non suivis, aucune autre modification préexistante.
Aucune autre mission en cours identifiée dans les cartes consultées.
La branche et le worktree affectés sont conservés. Pour les commandes Git, utiliser
`git --git-dir="$DEM004_GIT_DIR" --work-tree="$DEM004_WORKTREE" ...` après résolution
locale des deux variables : métadonnées `.git/worktrees/devops` et `worktree/devops`
depuis la racine principale. Aucun lien Git modifié, aucune réparation incluse.

Inventaire : 36 occurrences personnelles du chemin du dépôt, dans les affectations,
preuves, commandes historiques et demandes liées. Toutes sont remplacées par leur
chemin relatif au dépôt principal. Les affectations et preuves préfixées par le
placeholder historique du dépôt sont harmonisées également ; la mention d’une ancienne
neutralisation dans OPS-006 reste une trace historique, sans affectation à exécuter.
Les trois références personnelles au dossier de skills hors dépôt utilisent désormais
`<skills-personnels>`, défini dans le README ; aucun fichier de skill modifié.
Les préfixes de chemins temporaires historiques hors dépôt sont conservés.

Documentation harmonisée : `AGENTS.md`, `dev-book/README.md`, guides des couches
et de l’IA Engineering. Le guide d’installation ne demande pas de persister un chemin
absolu dans les cartes ; son alias personnel reste un exemple local, sans modification.

Preuves ponctuelles exécutées, sans ajout de contrôle ni de test au dépôt :

- Recherche dans les cartes et demandes : aucun chemin personnel vers le dépôt restant,
  aucun chemin personnel de l’utilisateur restant ; les préfixes génériques de recherche
  dans la présente carte ne désignent pas un emplacement personnel.
- Comparaison exhaustive des documents historiques modifiés à `HEAD` : contenu égal
  aux seules substitutions attendues ; listes des SHA sur 40 caractères, dates et lignes
  de statut/verdict identiques. Relecture des guides et de la commande historique OPS-011.
- `git diff --check` : réussi. Liens Markdown existants conservés ; liens DEM-004/OPS-049
  réciproques vérifiés.
- `python3 codebase-integrity/scripts/check.py` : 23 tests, un échec d’environnement
  dans le sandbox (socket HTTP local interdit). Les 23 tests réussissent lors de la
  relance incluse dans `quality.py` hors sandbox.
- `python3 codebase-integrity/scripts/quality.py` : code de sortie 0 hors sandbox ;
  23 tests d’outillage, test CRUD API, lint du conteneur Symfony, validation du mapping
  Doctrine et génération OpenAPI réussis ; typecheck et build web et backoffice réussis.
  La synchronisation du schéma de base est exclue par le contrôle existant `--skip-sync`.

Couverture : critères 1 et 2 par inventaire/nettoyage ; critère 3 par harmonisation des
consignes ; critère 4 par comparaison exhaustive ; critère 5 par recherches, relecture
et qualité complète. Aucun test ou contrôle affaibli. Aucun changement applicatif ou `.env`.
Le lien Git ordinaire reste cassé et sa réparation demeure séparée.

L’invocation explicite d’`implementer-demande` autorise le commit local de cette carte,
de ses documents et preuves. SHA communiqué après création dans le chat ; cette carte
accompagne ce commit. Résultat à vérifier par l’humain, sans verdict anticipé.
Aucun push, PR, merge ou démarrage de l’étape suivante.

## Verdict humain — 2026-10-26

Verdict explicite dans le chat : « validé », après présentation des cinq critères,
des preuves et de la limite du lien Git cassé, hors périmètre.
La validation globale couvre DEM-004 et sa seule carte OPS-049, sur le commit
d’implémentation `60ccb2acdc9436eefc709845b49a6174c96ac181`.
Les cinq critères sont acceptés ; aucune correction demandée.

Branche `layers/devops` et arbre propre vérifiés avant consignation, en désignant
explicitement les métadonnées Git actuelles. Seules DEM-004 et OPS-049 sont modifiées
pour ce verdict et son commit documentaire. Aucun code modifié, aucune réparation Git,
aucun push, PR ou merge. Reconstitution et livraison restent à lancer séparément.
