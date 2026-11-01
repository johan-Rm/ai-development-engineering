# OPS-079 — Contrôler les contributions selon leur boucle

- Demande : [DEM-028](../demand/DEM-028-proteger-contributions-codebase-integrity.md).
- Date : 2026-11-01
- Session de création : `01a195af-a030-75c2-9958-a8e2307d9447`
- État : validée humainement ; commit local autorisé.
- Couche : devops ; worktree `worktree/devops` ; branche `layers/devops`.
- Base : `531f4db38c93f4fab61bc190ec4d26c46062e57b`.
- Dépendance amont : aucune ; ne transférer aucun travail non commité.

## Objectif et chemins autorisés

Appliquer le périmètre et les décisions de DEM-028, qui restent leur source unique.
Une mission réunit documentation, déclaration structurée, vérificateur Python,
tests et raccordement local/CI, distincts des tests d’isolation des processus.

Chemins : `codebase-integrity/`, `.github/workflows/`,
`docs/git-workflow/README.md`, `docs/git-workflow/regles-de-pr.md`,
`docs/architecture/01-codebase-integrity/conventions-et-domaines.md`,
`docs/architecture/03-developpement-loop/06-livraison.md`,
`docs/architecture/04-consolidation-loop/06-livraison.md`,
`dev-book/README.md`, la demande et cette carte.
`AGENTS.md` uniquement si une adaptation des consignes existantes est nécessaire,
sans extension des autorisations Git. Conserver rubriques et ordre des README.

## Exclusions

Aucun changement applicatif, graphique, d’infrastructure d’exécution, de données,
de `.env`, de skill personnel ou d’autre worktree. Ne pas réécrire les demandes
historiques ni imposer rétroactivement les nouvelles déclarations.
Ne pas changer les protections distantes à cette étape. Aucun commit.

## Réalisation attendue

- Définir les conventions de contribution dans le README Git ; documenter le
  format de déclaration dans le README du dev-book, avec renvois sans duplication.
  Documenter commande stable, paramètres, préconditions et limites dans les
  README applicables ; ne pas créer de sections supplémentaires.
- Porter une seule déclaration structurée dans la demande : corrections,
  références aux conventions et contrôles, accompagnements motivés ou motif
  d’absence de correction. Définir et tester un schéma strict ; aucun copier-coller
  des règles locales. DEM-028 doit elle-même satisfaire le nouveau format.
- Exploiter les références des commits et les métadonnées des demandes dans
  les objets Git visés ; réutiliser les vérificateurs existants sans modifier
  leurs garanties. Déterminer base, ancêtre commun, commits nouveaux et diff
  de contribution sans inclure les changements propres à la cible.
- Vérifier les chemins par commit et dans le diff final, avec gestion des deux
  côtés des déplacements, suppressions, changements de mode et liens symboliques.
  Les déclarations couvrent les changements de la consolidation ; l’adéquation
  sémantique et la qualification des accompagnements restent humaines.
- Refuser l’absence ou l’ambiguïté des références, types contradictoires,
  changement de type destiné à contourner la règle et mélange des deux boucles.
  Une plage vide ne doit pas produire de fausse preuve de contrôle d’une PR.
- Charger le vérificateur et ses dépendances depuis la base de confiance,
  en lisant le candidat comme données, avant toute exécution applicative.
  Le point d’entrée accepte explicitement le dépôt candidat : ne pas déduire
  celui-ci du dossier d’une extraction temporaire du vérificateur.
- Raccorder au contrôle avant PR et à la CI existante ; séparer la vérification
  par la base des tests de la nouvelle version. Base invalide, historique incomplet
  ou vérificateur de base absent : diagnostic bloquant, aucun repli silencieux.

## Critères, tests et preuves

- Développement : accepter un changement hors dossier protégé ; refuser ajout,
  modification, suppression, déplacement entrant/sortant et changement annulé
  dans un commit ultérieur du dossier protégé.
- Consolidation : accepter les associations valides, conventions nouvelles ou
  existantes, et le motif sans correction ; refuser déclaration absente/invalide,
  chemins non couverts, convention ou ancre absente, contrôle absent ou inchangé.
- Références : tester type absent/invalide/dupliqué, carte contradictoire,
  documents ambigus, type modifié, mélange des boucles, fichiers locaux sales,
  tête demandée différente de HEAD et chemins atypiques sans interpolation shell.
- Confiance : prouver qu’un vérificateur candidat neutralisé ne fait pas accepter
  une contribution interdite ; tester branche cible avancée, historique incomplet,
  base absente, première installation et propagation des échecs avant l’applicatif.
- Exécuter tests ciblés, `python3 codebase-integrity/scripts/check.py`,
  `python3 codebase-integrity/scripts/check_docs.py`,
  `python3 codebase-integrity/scripts/check_demands.py` et `git diff --check`.
  Vérifier les nouveaux fichiers non suivis ; consigner commandes, résultats,
  cas couverts et limites ici. Qualité complète et plage de commits à la livraison.
- Avant présentation, vérifier qu’aucune modification applicative ou règle de
  processus sans lien n’a été introduite ; maintenir les 81 tests préexistants.

## Reconstitution et mise en service prévues

Après verdict et commits de l’étape 04, prévoir `demands/DEM-028` depuis develop
dans le principal libre et propre, à l’étape 05. Aucune branche créée ici.
L’amorçage du vérificateur et la preuve des protections distantes relèvent de la
limite de mise en service consignée dans la demande ; ne pas annoncer un blocage
de fusion garanti sur la seule réussite des tests locaux.

## Réalisation et preuves — 2026-11-01

Base HEAD inchangée ; index vide. Les seuls changements préexistants repris
étaient DEM-028 et cette carte, créées dans la même session. Aucun travail étranger.
Périmètre présenté : 15 fichiers, identifiés par la déclaration de DEM-028
et ses deux traces automatiques (demande et carte), dont cinq fichiers nouveaux.
Aucun fichier applicatif, environnement ou skill modifié ; AGENTS inchangé.

`check_contributions.py` contrôle les objets Git ; `contribution.py` extrait ses
dépendances depuis la base et les exécute avec isolation Python. La qualité locale
appelle ce lanceur avant les autres contrôles. La CI conserve ses déclencheurs
et sépare le job `Contribution de confiance` du job applicatif dépendant,
avec checkouts sans conservation des identifiants et permissions en lecture seule.
Les règles et le format sont documentés à leurs sources, avec renvois depuis
les procédures ; aucune rubrique de README ajoutée ou réordonnée.

- Suite ciblée : 20 tests de contribution réussis ; 15 tests de commits réussis.
- `python3 codebase-integrity/scripts/check.py` : 101 tests réussis, dont les
  81 préexistants. Premier passage limité par le refus du serveur HTTP local
  existant dans le bac à sable ; relance autorisée hors bac à sable, sortie 0.
- `check_docs.py` et `check_demands.py` : réussis. Notice documentaire connue
  conservée : référence dynamique dans `docs/README.md`.
- `git diff --check`, espaces des nouveaux fichiers et comparaison des titres
  des README avec HEAD : conformes.
- Validation YAML locale : syntaxe, dépendance entre jobs, permissions et absence
  de conservation des identifiants vérifiées. Aucune exécution GitHub revendiquée.
- Déclaration réelle de DEM-028 : couverture des 15 fichiers vérifiée par lecture
  locale avec le validateur de consolidation et comparaison des contenus à HEAD,
  sans créer de commit. Ce résultat ne remplace pas le contrôle de la plage commitée.
- `contribution.py --repo . --base HEAD --head HEAD` : échec attendu, code 1,
  diagnostic « vérificateur de base absent ou non régulier ; amorçage requis ».
  La base ne contient effectivement pas le nouveau vérificateur ; aucun repli ajouté.

Limites : qualité applicative complète, plage finale commitée, CI distante,
protection du workflow et statut obligatoire restent à vérifier à la livraison.
La qualification des accompagnements, du type et du renforcement réel des tests
reste humaine. Aucune exception ni autorisation Git supplémentaire introduite.
Résultat implémenté, non commité, à vérifier ; aucun verdict humain inventé.

## Vérification / arbitrage — 2026-11-01

Relecture des dix diffs suivis et des cinq fichiers nouveaux ; base et index
inchangés. Empreinte SHA-256 avant cette trace, calculée sur les 15 chemins triés,
leurs modes et contenus séparés par NUL :
`40b39bbe975100c875c6c57e2c1b06f47c251d32e234dca60614d3baa0324241`.
Contrôles documentaires, typage et espaces revérifiés : conformes.
Les 101 tests réussis à l’implémentation ne couvrent pas le défaut ci-dessous.

Défaut reproduit sans modifier l’implémentation : un README contenant un titre
`### Contrat` dans ses responsabilités, puis un autre dans ses conventions,
possède les ancres réelles `contrat` et `contrat-1`. La fonction `convention()`
recalcule les ancres sur la seule section des conventions : elle accepte
`README.md#contrat`, qui vise les responsabilités, et refuse la vraie référence
de convention `README.md#contrat-1`. La preuve de localisation est donc incorrecte
dans ce cas, au-delà des limites sémantiques réservées à la revue humaine.

Correction nécessaire à l’étape 03 : conserver le calcul des ancres du document
entier tout en vérifiant leur appartenance à la section des conventions ; ajouter
un test de non-régression prouvant le refus de la mauvaise ancre et l’acceptation
de la bonne. Le périmètre et les règles confirmés restent inchangés.
Aucune correction de code ni aucun commit pendant cette vérification.
Verdict humain non reçu ; la carte n’est pas présentée comme validée.

## Correction après revue — 2026-11-01

Retour à l’étape 03 autorisé explicitement : « DEM-028, ok corrige ».
`convention()` conserve désormais les titres précédents dans le calcul des ancres
et ne retient que celles introduites dans la section des conventions. Les sections
suivantes sont exclues. Aucun changement de règle ni extension de périmètre.

Test de non-régression ajouté avec trois titres identiques : avant, dans et après
les conventions. Avant correction, il reproduit l’acceptation erronée de `contrat`
et le refus de `contrat-1` ; après correction, seule `contrat-1` est acceptée,
`contrat` et `contrat-2` sont refusées.

`python3 codebase-integrity/scripts/check.py` : 102 tests réussis, sortie 0,
hors bac à sable pour le serveur HTTP temporaire existant. Contrôles documentaires,
typage et espaces : conformes. Base et index inchangés ; toujours 15 fichiers
modifiés/nouveaux. Les limites de mise en service déjà consignées restent applicables.
Résultat corrigé, non commité, à vérifier ; aucun verdict humain du résultat.

## Verdict humain — 2026-11-01

Verdict exact : « validé », après nouvelle vérification de la correction.
Les 15 fichiers présentés ont été revérifiés identiques avant consignation :
SHA-256 `f57847d961370e9167e51216ed7f7e4d8e5e4f29cb8b5429fc2d4b87e4c9a346`,
base HEAD indiquée en tête. Les 21 tests ciblés sont repassés à la vérification ;
les 102 tests complets ont réussi après correction. Aucun changement fonctionnel
depuis présentation. Les limites de mise en service restent applicables.
La validation autorise le commit local de cette carte, preuves et documentation
comprises ; aucun push, PR ou fusion à cette étape.
