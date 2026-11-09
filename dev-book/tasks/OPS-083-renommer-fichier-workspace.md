# OPS-083 — Renommer le fichier workspace

- Type : consolidation
- Demande : [DEM-019](../demand/DEM-019-renommer-fichier-workspace.md).
- Date : 2026-11-09 ; état : validée et commitée ; réserves de recette levées à la livraison.
- Session de création : `01a1c0bc-2805-70e1-a520-6daa5dd4d039`.
- Mission : devops ; worktree `worktree/devops` ; branche `layers/devops`.
- Base locale : `b93a9897c0a120e3f773308e7d356c2e993448fd`, commune avec develop.
- Besoin et analyse : [DEM-019](../demand/DEM-019-renommer-fichier-workspace.md),
  matérialisée depuis `tmp/demande-renommer-fichier-workspace.md` du principal.

## Objectif et périmètre

Appliquer le cadrage confirmé de DEM-019 et couvrir tous ses critères sans les
recopier. Le brouillon fait référence pour le nom exact et les exclusions.

Chemins autorisés : `aide.code-workspace` et
`ai-powered-development-engineering.vscode-worktree` pour le déplacement ;
`codebase-integrity/scripts/setup_worktrees.py`,
`codebase-integrity/tests/test_setup_worktrees.py`,
`codebase-integrity/README.md` pour la convention dans la rubrique existante ;
`docs/architecture/02-cadre/couches/organisation.md` pour la référence active ;
cette carte pour les preuves. Ne pas ajouter de rubrique aux README.

Hors dépôt : `/home/johan/.bash_aliases`, uniquement la cible de l’alias existant,
sous réserve des permissions de l’environnement. Préserver les autres octets ;
ne jamais copier les autres alias dans les preuves. Mettre à jour cette cible
avant la recette locale : le script refuse les alias incompatibles.

Exclusions : historiques du dev-book, SETUP dont la commande reste identique,
Makefile, applications, AGENTS.md, réglages du workspace, .env et données.
Aucune modification de la commande d’ouverture en cas d’incompatibilité sans
nouvelle décision humaine. Aucun commit à l’implémentation.

## Dépendances et ordre

Aucune dépendance de réalisation ni commit à importer. DEM-018 et DEM-031 sont
déjà intégrées dans la base ; leurs cartes historiques ne sont pas des missions
actives. Déplacement, script, tests et référence documentaire forment une seule
contribution cohérente. Vérifier à nouveau la disponibilité avant implémentation.

À l’étape 05, réunir les commits validés sur `demands/DEM-019` dans le principal
(`.`), depuis develop local vérifié, libre et propre. Ne créer cette branche
qu’à cette étape ; conserver `layers/devops`. Retour du principal sur develop
après fusion distante. Qualité globale après réunion et avant PR.

## Contrôles et preuves attendus

- Comparer les octets du workspace à la base ; ancien fichier absent, JSON valide,
  chemins des six dossiers préservés. Chercher l’ancien nom dans les fichiers actifs
  sans parcourir les worktrees, dépendances ou .env ; distinguer les historiques.
- Adapter les tests existants sans importer la constante du script dans leurs
  attentes : nom exact généré, cible exacte de l’alias, relance sans altération,
  préservation des réglages et refus des configurations incompatibles. Vérifier
  aussi que la préparation ne recrée pas l’ancien fichier.
- Depuis ce worktree : `python3 -B -m unittest discover -s codebase-integrity/tests -p test_setup_worktrees.py`,
  `python3 codebase-integrity/scripts/check.py`,
  `python3 codebase-integrity/scripts/check_docs.py`, `git diff --check`.
  Ces contrôles existants restent bloquants ; pas de nouveau vérificateur global.
- Tester la préparation uniquement dans les dépôts et HOME jetables prévus par
  les tests ; ne pas lancer le setup réel depuis une couche non livrée, car sa
  racine cible est le principal. Vérifier l’alias personnel par `bash -n` puis
  chargement dans un Bash neuf et comparaison de la cible.
- Faire observer dans VS Code l’ouverture des six dossiers avec le nom final
  exact, en conservant la base des chemins relatifs. Une copie sous /tmp seule
  ne prouve pas la résolution des dossiers. Si nécessaire, effectuer cette recette
  après reconstitution ; elle ne bloque pas les éditions indépendantes, mais son
  résultat reste requis avant validation globale. Arrêter sur incompatibilité.
- Consigner ici commandes, résultats, limites, état Git et verdict humain réel.
  Le test exploratoire et ses limites restent dans le brouillon de référence.

## État au découpage

Maximum OPS observé : 082 dans toutes les références Git locales et les fichiers
concernés ; 083 libre avant création, sans fetch. Session vérifiée par les deux
variables Codex concordantes. Index vide et arbre propre avant cette carte ;
branche existante conservée. Disponibilité établie par les traces de clôture de
DEM-030 et DEM-031 dans les brouillons du principal, en plus de l’état Git.
Aucun test d’implémentation exécuté, aucun code ou convention modifié, aucun commit.

## Implémentation et preuves — 2026-11-09

Base et session de création inchangées ; reprise limitée à cette carte non suivie,
seul changement présent au démarrage, index vide. Workspace déplacé à contenu
strictement identique à `HEAD:aide.code-workspace` ; JSON valide, six dossiers
conservés. Constante de préparation, attentes indépendantes et guide adaptés ;
convention ajoutée au README sans changement de rubriques ni d’ordre.

- Tests ciblés : sept réussis, sortie 0, création et relance sans ancien fichier,
  alias exécuté avec binaire simulé, préservation et incompatibilités couvertes.
- `python3 codebase-integrity/scripts/check.py` : 117 tests réussis, sortie 0 ;
  journal `/tmp/dem019-check.log`. Premier essai bloqué par la socket HTTP locale ;
  nouvelle exécution autorisée, sans modification des contrôles.
- Contrôle documentaire et `git diff --check` : réussis.
- Recherche dans les fichiers actifs hors historiques et copies : seules restent
  deux assertions négatives sur l’ancien nom dans `test_setup_worktrees.py` ;
  elles vérifient qu’il ne réapparaît pas. Historiques conservés.

Limite de réalisation : alias personnel inchangé, syntaxe Bash valide. Sa cible
actuelle existe dans le principal ; sa future cible y est absente tant que la
contribution n’est pas reconstituée. Changer maintenant sa cible casserait
l’ouverture existante. La bascule personnelle et sa preuve en Bash neuf sont donc
différées jusqu’à la présence du nouveau fichier dans le principal ; réaliser
cette opération avant la recette locale de préparation. Aucun alias temporaire,
aucune copie de travail non commité vers le principal et aucun setup réel lancé.

Limite de vérification globale : ouverture réelle du nom final non observée.
Les chemins relatifs du workspace de couche ne désignent pas les worktrees du
principal. Faire cette recette après reconstitution ; le test exploratoire de
l’interview ne valide pas ce nom final. Aucun verdict humain inventé.

État soumis : suppression de l’ancien workspace, nouveau workspace et cette carte
non suivis ; quatre fichiers suivis modifiés (README de Codebase Integrity,
script de setup, ses tests, guide des couches). Index vide ; aucun commit,
changement de branche, push, PR ou fusion. Qualité applicative complète différée
avant PR ; seuls les contrôles proportionnés ci-dessus ont été exécutés ici.

Empreinte SHA-256 du contenu présenté hors carte (chemins triés, séparateurs NUL) :
`f0925175bbee17ffaa8d3bb22be6128df5ff6a9e4131b43c6a292fac2384b8b4`.

## Verdict humain — 2026-11-09

Réponse exacte : « validé », après présentation du résultat et des réserves
sur la bascule de l’alias personnel et l’ouverture réelle après reconstitution.
Validation de la contribution de couche avec ces réserves ; elle ne prouve pas
leur réalisation et ne clôt pas DEM-019. Le suivi reste obligatoire avant clôture.

HEAD de base et empreinte du contenu présenté revérifiés identiques après verdict ;
index vide, aucun changement étranger. Contrôles et limites ci-dessus inchangés.
Seuls ce verdict et l’état de la carte sont ajoutés avant le commit local autorisé.

## Recette finale — 2026-11-09

Après reconstitution, cible personnelle de l’alias basculée vers le fichier final
présent dans le principal. Comparaison avant/après : seule cette cible a changé,
les autres octets sont identiques ; syntaxe `bash -n` valide, définition exacte
confirmée après chargement dans un Bash neuf. Aucun changement de commande ni de
nom d’alias. Ouverture `code --new-window` du fichier final : sortie 0.
L’humain répond « Oui, les six dossiers sont ouverts » à la recette de ce nom
exact. Les deux réserves précédentes sont levées ; aucun changement fonctionnel
supplémentaire dans le dépôt. Les shells déjà ouverts doivent recharger l’alias.
