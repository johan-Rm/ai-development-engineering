# DEM-028 — Protéger les contributions au Codebase Integrity

- Type : consolidation
- Date : 2026-11-01
- Session de création : `01a195af-a030-75c2-9958-a8e2307d9447`
- État : correction d’amorçage et documentation d’OPS-079 validées ; commit local autorisé.
- Domaine proposé : Fiabilité des vérifications.
- Confirmation humaine du cadrage : « oui ».

## Constat

Les tests existants vérifient notamment l’isolation des processus et des worktrees,
mais aucun contrôle dédié ne garantit la séparation des contributions entre les
deux boucles. Une contribution de développement pourrait modifier les vérificateurs
qu’elle doit respecter ; une consolidation pourrait corriger le code sans relier
ces corrections à des conventions et à leurs contrôles. Aucun incident concret
de ce type n’a été établi pendant l’interview.

## Proposition et périmètre confirmés

- Refuser toute PR de développement comportant un ajout, une modification,
  une suppression ou un déplacement touchant `codebase-integrity/`.
- Exiger que toute PR de consolidation relie ses corrections aux conventions
  techniques concernées, nouvelles ou existantes, avec ajout ou renforcement
  de leurs contrôles.
- Lorsqu’une convention existe déjà, la référencer sans en créer une copie.
- Rattacher ces vérifications au contrôle des contributions et des PR,
  distinct des sept tests actuels d’isolation des processus.

L’exception confirmée pour les consolidations sans correction de code figure
dans les décisions complémentaires. Aucune implémentation n’est validée ici.

## Critères observables à analyser

- Une PR de développement touchant le dossier protégé est bloquée,
  y compris par suppression ou déplacement entrant ou sortant.
- Une PR de consolidation sans association entre corrections, conventions
  et contrôles est bloquée.
- Les contributions conformes sont acceptées ; les tests des vérificateurs
  couvrent les cas conformes, les écarts et les contournements retenus à l’analyse.

## Questions pour l’analyse

- Déterminer le type de la contribution depuis les demandes et cartes liées ;
  définir le refus des références absentes, contradictoires ou mixtes.
- Définir les preuves vérifiables du lien entre correction, convention et contrôle,
  en distinguant leur présence de leur adéquation, soumise à revue humaine.
- Définir la comparaison Git utilisée avant PR et en CI, ainsi que la résistance
  à une modification du contrôle par la contribution examinée.
- Examiner le cas des consolidations sans correction de code et celui d’un contrôle
  existant déjà suffisant ; soumettre toute exception nécessaire à arbitrage.

## État de travail à l’interview

Rédaction dans `worktree/devops`, branche `layers/devops`, propre et index vide
avant création. Base locale commune à develop :
`531f4db38c93f4fab61bc190ec4d26c46062e57b`.
Aucune mission d’implémentation active identifiée ; les anciennes mentions de
livraison restent conservées. Aucun changement de code, de contrôle ou de convention,
aucune carte ni opération Git de livraison à cette étape.

## Analyse — 2026-11-01

### Couverture et constats

Inventaire des 277 fichiers suivis hors copies de worktrees ; recherches ciblées
sur contributions, types, conventions et points de contrôle. Lecture des scripts
de commits, typage et qualité, de leurs tests associés, du workflow unique,
des règles Git, du classement des conventions, des étapes concernées des boucles
et du routage des couches. Les 24 demandes suivies portent un type :
16 consolidations et 8 développements. La présente demande reste non suivie.

- `check_commits.py` vérifie chaque commit et ses références dans l’arbre final,
  mais ne lit pas le type et ne limite pas les chemins selon la boucle.
- `check_demands.py` contrôle le type dans la copie de travail, sans l’associer
  à une plage Git ni aux fichiers modifiés.
- Les README définissent les conventions locales ; aucun registre structuré
  de liens correction–convention–contrôle n’est présent.
- `quality.py` contrôle les commits avant les autres vérifications lorsqu’une
  base est fournie. Sans base, il poursuit avec un avertissement.
- La CI transmet base et tête, mais exécute les outils de la contribution.
  Elle ne garantit donc pas une vérification par une version déjà intégrée.
- DEM-027 illustre une consolidation de retrait de test sans nouvelle convention
  générale ; elle révèle un cas à arbitrer, sans réécrire cette décision passée.

Cette analyse porte sur les sources et configurations locales, sans exécution
des tests, audit des dépendances installées, données, `.env` ni fichiers ignorés.
Les protections GitHub et l’exigence distante du statut CI ne sont pas vérifiées.
Aucun écart historique n’est à corriger rétroactivement.

### Options et proposition de contrôle

Une simple exigence de fichiers README et tests modifiés serait peu coûteuse,
mais ne prouverait aucune association avec les corrections. Une déclaration
structurée propre à la demande, référençant les règles sans les recopier,
permettrait un contrôle précis de présence et de couverture ; coût supérieur
de validation et de maintenance. Cette seconde option est proposée.

Le contrôle bloquant proposé utilise une base et une tête explicites, lit leurs
objets Git sans dépendre de fichiers locaux modifiés et vérifie tous les commits
nouveaux, ainsi que le diff final. Un changement protégé ensuite annulé reste
détectable. Suppressions et déplacements sont examinés des deux côtés.

Le type est déduit des demandes uniques référencées par les commits et leurs
cartes ; références manquantes, ambiguës, contradictoires ou mélange des deux
types sont refusés. Pour une demande existante, un changement opportuniste de
type depuis la base est refusé. La pertinence du type déclaré reste humaine.

Pour une consolidation, la déclaration proposée associe les chemins corrigés,
la convention dans son README source et les fichiers de contrôle ajoutés ou
renforcés. Chemins, ancres, unicité, couverture déclarée et modifications effectives
sont vérifiables. La pertinence de la règle et la suffisance du test restent
soumis à revue humaine ; modifier un fichier de test ne prouve pas son renforcement.
Le format peut être porté par un bloc JSON unique dans la demande, sans recopier
les conventions ni ajouter un registre parallèle. Les fichiers d’accompagnement
sont déclarés séparément avec leur motif ; leur qualification reste humaine.

Le vérificateur de contribution serait chargé depuis la base d’intégration,
avant installation ou exécution du code candidat ; les tests de la nouvelle
version seraient exécutés séparément. Le premier déploiement de ce vérificateur
nécessite une amorce explicite, car il n’existe pas dans la base actuelle.
La protection contre la suppression de son workflow exige un statut obligatoire
et une protection distante ; une modification du seul dépôt ne suffit pas.

### Décisions complémentaires confirmées — 2026-11-01

Réponses humaines exactes à l’interview interactive :

- « Exiger un motif explicite “sans correction de code”, soumis à revue humaine,
  sans nouveau contrôle obligatoire (recommandé). »
- « Oui, maintenir l’exigence confirmée d’ajout ou de renforcement du contrôle
  (recommandé). » Même un contrôle existant jugé suffisant ne dispense donc pas
  une consolidation corrective de cette exigence.
- « Retenir cette approche avec contrôle bloquant avant PR et en CI
  (recommandé). » L’approche présentée associe déclaration structurée,
  vérificateur exécuté depuis la base d’intégration, revue humaine de l’adéquation
  et refus des PR mélangeant développement et consolidation.

### Découpage retenu

| Carte | Couche | Mission | Dépendance | État |
| --- | --- | --- | --- | --- |
| [OPS-079](../tasks/OPS-079-controler-contributions.md) | devops | Conventions, déclaration, vérificateur, tests et CI | Aucune dépendance amont | Correction validée ; commit local autorisé |

Une seule mission évite des dépendances artificielles entre documentation,
outillage et CI de la même couche. Applications, design, environnements et skills
personnels restent hors périmètre. OPS-079 est libre après vérification des noms
dans toutes les références Git locales et des identifiants dans les documents
des worktrees ; maximum antérieur OPS-078. Même session que l’interview.

Prévoir `demands/DEM-028` depuis develop dans le dossier principal libre et propre,
après validation et commits des cartes. Aucune branche créée à cette étape.

### Limite de mise en service

L’implémentation et ses tests peuvent être préparés sans protection distante.
Avant de déclarer le blocage effectif en livraison, il faudra établir comment
amorcer le contrôle absent de la base actuelle et vérifier le statut obligatoire
sur GitHub. Aucun repli silencieux vers le code candidat ni contournement de
protection n’est autorisé ; une autorisation manquante restera à obtenir à cette étape.

## Déclaration de contribution

```contribution-json
{
  "version": 1,
  "corrections": [
    {
      "chemins": [
        ".github/workflows/quality.yml",
        "codebase-integrity/scripts/check_contributions.py",
        "codebase-integrity/scripts/contribution.py",
        "codebase-integrity/scripts/quality.py",
        "codebase-integrity/tests/test_contributions.py",
        "codebase-integrity/tests/test_commits.py"
      ],
      "convention": "docs/git-workflow/README.md#vérification",
      "controles": ["codebase-integrity/tests/test_contributions.py", "codebase-integrity/tests/test_commits.py"]
    }
  ],
  "accompagnements": [
    {
      "chemins": [
        "codebase-integrity/README.md",
        "codebase-integrity/tests/README.md",
        "dev-book/README.md",
        "docs/git-workflow/README.md",
        "docs/git-workflow/convention-de-commits.md",
        "docs/git-workflow/regles-de-pr.md",
        "docs/architecture/03-developpement-loop/06-livraison.md",
        "docs/architecture/04-consolidation-loop/06-livraison.md"
      ],
      "motif": "Définir les règles et le format, documenter les commandes et relier les procédures sans recopier les conventions."
    }
  ],
  "sans_correction": ""
}
```

## Suivi d’implémentation

Résultat, contrôles et limites consignés dans OPS-079. Aucun commit ni verdict
humain du résultat ; la validation du cadrage ne vaut pas validation de la réalisation.

## Verdict du résultat

OPS-079 validée explicitement le 2026-11-01 : « validé ».
Preuves et identité du contenu conservées dans la carte. Reconstitution et livraison
restent à effectuer ; aucune protection distante ni amorçage déclaré acquis.

## Commit local validé

OPS-079 : `0cb25aaa55149b533be1bbc7919986834421f668`.
Contenu vérifié : 15 fichiers autorisés, preuves et verdict compris ; arbre propre
après commit. Contrôle des commits et vérificateur candidat de contribution
sur la plage depuis la base d’OPS-079 : conformes (un commit).
Ce dernier vérifie la déclaration sur les objets commités, sans constituer
une exécution par le vérificateur de la base, encore absent ; amorçage non résolu.
La présente consignation est une trace documentaire complémentaire.

## Reconstitution — 2026-11-01

Principal libre et propre sur develop avant création de `demands/DEM-028` ;
base locale vérifiée `531f4db38c93f4fab61bc190ec4d26c46062e57b`.
Cherry-picks `-x` sans conflit, dans l’ordre :

| Source validée | Commit obtenu | Rôle |
| --- | --- | --- |
| `0cb25aaa55149b533be1bbc7919986834421f668` | `d0912d7c62913d750e51376904d7e4319d7ea746` | OPS-079 |
| `feaa599ed3698809bbd31558adddbc3fb141dfdc` | `06d75f4b90b01c35d3d2b0a364ab40b61afe4b83` | Trace du commit validé |

Arbre reconstitué identique à `layers/devops` avant la présente trace ; provenance
des deux commits vérifiée. Contrôle des commits, vérificateur candidat de
contribution, documentation, types des demandes et espaces : conformes.
Les 102 tests déjà réussis portent sur le même contenu ; pas de nouvelle exécution.
Le contrôle depuis la base reste indisponible jusqu’à résolution de l’amorçage ;
la conformité du vérificateur candidat ne remplace pas cette précondition.

Les couches conservent leurs branches ; aucun fetch, push, PR ou fusion effectué.
La présente trace reste non commitée pour la livraison. Aucun résultat applicatif
complet ou contrôle distant supplémentaire revendiqué à cette étape.

## Contrôles de livraison — 2026-11-01

Remote et authentification vérifiés ; fetch d’origin/develop sur
`531f4db38c93f4fab61bc190ec4d26c46062e57b`, identique à la base locale.
Branche reconstituée sur `06d75f4`, aucun autre commit à livrer avant les traces.
Aucune PR existante pour `demands/DEM-028` ; Rebase and merge autorisé.

- `python3 codebase-integrity/scripts/quality.py --commit-base develop --commit-head HEAD` :
  échec, code 1. Le vérificateur de base est absent d’origin/develop, confirmé par
  lecture Git ; l’amorçage ne peut pas être remplacé par l’exécution du candidat.
- Contrôles indépendants : `python3 codebase-integrity/scripts/quality.py`, sortie 0,
  hors bac à sable pour le serveur HTTP local. Types, documentation, 102 tests,
  contrôles API, contrat OpenAPI, typage et builds applicatifs réussis.
  Journal : `/tmp/dem028-quality-independent.log`. L’avertissement sans base est
  attendu ; cette réussite ne vaut pas réussite du contrôle de contribution.
- GitHub : pas de protection de branche classique, mais ruleset actif
  `Protection develop` (25975725), imposant PR, résolution des discussions,
  interdiction de suppression et de push non linéaire. Aucun statut obligatoire
  ni protection dédiée du workflow dans les règles effectives consultées.
  Aucune protection modifiée ; aucun contournement employé.
- Inventaire : API, backoffice, web et devops propres ; design porte trois fichiers
  non suivis dans `design/drafts/`, préservés sans intervention. Son alignement
  reste bloqué tant que ce travail étranger n’est pas coordonné.

La mise en service exige un arbitrage explicite d’amorçage et une protection
distante adaptée. Aucun changement fonctionnel, push, PR ou fusion effectué.
Le contrôle requis échoué interdit l’ouverture de PR à cette étape ; aucune
livraison ni clôture annoncée. Les seules écritures sont les traces documentaires.

## Évolution du mécanisme d’amorçage — 2026-11-01

Après blocage de la livraison reconstituée sur `demands/DEM-028`, l’humain refuse
une dispense ponctuelle de contrôle et choisit de revoir le mécanisme.
La proposition d’une première installation limitée au contenu d’un commit
explicitement approuvé est expliquée, puis sa préparation est autorisée : « go ».
Cette autorisation ne vaut pas approbation du contenu corrigé ni de son futur SHA.

Le fonctionnement normal reste inchangé. Pour DEM-028 seule, depuis la base
initiale sans vérificateur, la commande charge le vérificateur d’un commit approuvé
fourni hors des fichiers candidats. Elle vérifie l’identité du contenu Git complet
avec ce commit, puis applique tous les contrôles à la contribution, restreinte
à cette consolidation. Les SHA peuvent différer après réécriture si le contenu
est identique. Toute différence, autre base, autre demande ou absence d’approbation
est refusée. Dès que la base possède le contrôleur, l’approbation d’amorçage ne
sert plus et aucun remplacement du contrôleur intégré n’est permis.

La documentation d’exécution et la variable externe sont définies dans le README
de Codebase Integrity. Leur activation attend validation humaine et commit identifié ;
aucune variable ni protection distante n’est modifiée pendant cette préparation.
Les anciennes validations couvrent l’état précédent ; une nouvelle vérification
de la correction est requise avant nouveau commit, reconstitution et livraison.

Coordination confirmée : devops réservé à DEM-028 pendant la correction, écritures
de l’autre mission suspendues ; conserver sa carte OPS-080 sans modification.

## Retour documentaire — 2026-11-02

Instruction humaine : aucune référence à une demande dans les README ; le chapitre
des conventions ne contient que des règles courtes destinées aux tests.
README concernés corrigés sans ajout ni réordonnancement de rubriques.
Commandes, préconditions et explications déplacées vers les guides Git existants,
sans changement du comportement des contrôles. Autres retours humains attendus.

## Validation de la correction — 2026-11-02

Correction d’OPS-079 validée explicitement : « ok go c’est validé ».
Périmètre, identité et preuves dans la carte. Le contrôle par commit, la déclaration
structurée et le mécanisme d’amorçage présentés sont conservés.
La correction doit encore être commitée puis réunie sur la branche reconstituée.
L’approbation du contenu final d’amorçage et son activation distante restent à faire.
