# DEM-021 — Consolider les conventions documentaires

- Type : consolidation
- Date : 2026-10-30.
- Session de création : `01a18b94-1588-7021-869d-d11d9ff6ba72`.
- Session intervenante : `01a18c38-1b13-7953-9118-aadc8cde8794` ; ajout demandé des suppressions ci-dessous.
- Étape : livraison en cours ; contrôles réussis.
- Statut : prête pour PR vers develop par Rebase and merge ; suivi des couches à terminer.
- Enregistrement demandé par l’humain dans la même session ; origine : interview conservée, sans nouvelle adoption de règle.
- Couche : devops ; worktree `worktree/devops` ; branche `layers/devops`.
- Base : `b40faca917b01074d078e49ad1cad6f7fb2ff7b6`, arbre et index propres avant création ; livraison DEM-020 clôturée, aucune autre mission active identifiée.
- Prochaine étape : `livrer-consolidation` pour DEM-021.

## Besoin et périmètre

Définir dans `docs/README.md` les conventions proposées :

- Nommer sans numérotation les seuls dossiers de thématiques directement sous `docs/` ; voir l’ajustement de portée dans l’arbitrage.
- Réserver les `index.md` aux tables des matières.
- Commencer chaque chapitre explicatif par une courte citation résumant son idée principale.
- Utiliser des titres précis et des paragraphes courts ; éviter répétitions, détails inutiles et formulations superflues.
- Employer « convention technique » pour désigner une règle technique du projet.

Ajouter dans `AGENTS.md` que les conventions techniques sont définies dans le
README concerné et que la documentation apporte des explications complémentaires.
Éliminer les doublons avec le guide documentaire en conservant une source de référence.
Cette proposition reprend le périmètre reporté par [DEM-020](DEM-020-readme-documentation.md).

Inclure la suppression des fichiers suivants :

- `infra/config/README.md`
- `dev-book/resources/README.md`
- `app/web/README.md`
- `app/api/README.md`
- `app/backoffice/README.md`
- `codebase-integrity/scripts/README.md` (ajout demandé dans la session intervenante).

L’analyse précisera le devenir de leur contenu utile et les références à adapter.

L’absence de numérotation vise uniquement les dossiers de thématiques directement
sous `docs/`. La numérotation des niveaux inférieurs, des piliers et des étapes
est conservée ; les identifiants des demandes et cartes le sont aussi. Les index doivent servir de tables des
matières ; les citations concernent les chapitres explicatifs. La portée de ces
règles hors de `docs/` reste à examiner, sans extension implicite.

## Constats vérifiés

- Lors de l’interview, le README était en cours dans OPS-071. À l’enregistrement,
  [le README](../../docs/README.md) est livré avec ses conventions vides ;
  les preuves restent dans [OPS-071](../tasks/OPS-071-readme-documentation.md).
- `docs/architecture/01-codebase-integrity/` à `04-consolidation-loop/` et les
  fichiers d’étapes portent des préfixes numériques.
- L’[index des couches](../../docs/architecture/02-cadre/couches/index.md) contient
  des explications, commandes et règles de coordination, au-delà d’un sommaire.
- Le [guide documentaire](../../docs/README.md#rédaction-et-source-de-référence)
  définit déjà citation introductive, rédaction et terminologie. Les recopier
  dans le README laisserait deux sources normatives.

Ces écarts appellent une migration globale, plutôt qu’un ajout isolé au README.

## Migration et conformité proposées

- Partir du README livré par DEM-020, déjà inclus dans la base identifiée ci-dessus.
- Définir les conventions dans le README et remplacer leurs formulations normatives
  dans le guide par des liens ; conserver seulement les explications complémentaires utiles.
- Ajouter la consigne AGENTS.md prévue, sans y recopier les conventions documentaires.
- Appliquer la portée des noms ajustée dans l’arbitrage, extraire les explications des index
  vers des documents nommés par sujet, puis adapter les références actives et ancres.
- Revoir les chapitres explicatifs, titres, paragraphes et occurrences de terminologie ;
  supprimer les répétitions en conservant une source par information.

## Analyse globale — 2026-10-30

Analyse dans la session intervenante ci-dessus, sur
`3fe38fca51bab7a2ea972e688601240344985f5a`, branche `layers/devops`.
Reprise de DEM-021 : seule cette demande était non suivie, index vide ;
aucun travail étranger identifié. Aucun code, contrôle ou règle modifié.

### Couverture et limites

Lecture des 25 fichiers Markdown suivis de `docs/`, des cinq README à supprimer,
de leurs README parents, des instructions et de l’outillage documentaire concerné.
Recherche des chemins concernés dans tous les fichiers texte suivis, fichiers
cachés inclus : 52 fichiers, 126 lignes correspondantes avant cette mise à jour.
Les correspondances incluent des chemins historiques, pas seulement des liens.
Les ressources HTML, la CI et la configuration Codex ont été recherchées ; aucune
dépendance directe supplémentaire aux chemins renommés n’y a été relevée.

Exclusions : copies de worktrees, dépendances et fichiers ignorés, `.env`, binaires
et sources graphiques originales. Les skills personnels hors dépôt ne sont pas
audités globalement ; leurs liens éventuels restent à vérifier avant livraison.
Pas de vérification réseau ni de recette applicative : aucun comportement modifié.

### Écarts et corrections proposées

| Sujet | État et périmètre de correction |
| --- | --- |
| Noms | 4 dossiers sous `docs/architecture/` et 12 fichiers d’étapes sont préfixés. Ces numéros sont conservés après l’ajustement humain ci-dessous. Le seul dossier thématique de premier niveau, `architecture/`, est déjà conforme ; aucun renommage requis. |
| Index | Sur 5 index, seul `docs/index.md` est déjà un sommaire sans développement. Extraire les explications de l’index des couches et des deux boucles ; retirer ou déplacer le texte explicatif de l’index d’architecture. Conserver titres, liens, libellés brefs et tableaux de navigation. |
| Citations | 22 documents sur 25 commencent par une citation après le titre principal. Exceptions actuelles : README de docs, dockerisation et reconstitution. Les 86 sections H2 montrent que « chapitre » doit être défini avant toute migration. |
| Source normative | Le guide documentaire prescrit rédaction, terminologie et structure des README ; les principes du Codebase Integrity rappellent aussi l’emplacement des règles. Centraliser les règles documentaires dans `docs/README.md`, celles des README applicatifs dans `app/README.md`, et remplacer les prescriptions répétées par des liens. |
| Rédaction | La terminologie « convention technique » est déjà largement employée. Revoir les doublons sur les autorisations et verdicts dans les guides d’étapes, et la mention dépassée « Avant intégration de DEM-005 » dans la dockerisation. La précision et la concision exigent une revue humaine, sans remplacement lexical aveugle. |

La migration des références actives touche `AGENTS.md`, `SETUP.md`, les index et
liens internes de `docs/`, le README de l’outillage et `worktree/README.md`.
Ce dernier contient déjà deux liens absents vers `docs/02-cadre/couches/index.md`
et `docs/03-developpement-loop/05-reconstitution.md` : les corriger vers les
nouvelles destinations. Les ancres des explications extraites changent aussi de
fichier ; maintenir une correspondance ancien chemin/ancre → nouvelle cible.

Les demandes et cartes contiennent les autres références relevées, notamment
DEM-005, DEM-017, OPS-043, OPS-044, OPS-051 et OPS-069. Proposition : migrer les
liens de navigation, conserver les chemins littéraux décrivant une preuve passée.
Ne pas réécrire les résultats, SHA ou verdicts historiques.

### Suppressions : devenir des informations

Les cinq suppressions demandées sont recensées dans le périmètre, sans nouvelle liste.
Avant suppression, proposer les destinations suivantes, sans recopier les contenus :

| Contenu actuel | Destination proposée |
| --- | --- |
| Configuration des couches | Conventions dans `infra/README.md` ; usage dans le document des couches extrait de son index. Le README de l’outillage renvoie à cette source. |
| Ressources et originaux | Consigne de conservation et liens utiles dans `dev-book/README.md` ; règle graphique déjà présente dans `design/charte-graphique.md`. |
| Contrat et démarrage des applications | Règles communes dans `app/README.md` ; contrat détaillé référencé via `app/api/app/openapi.json` ; explications distinctes par application sous un thème applicatif de `docs/`. Vérifier chaque commande lors de cette migration. |

Adapter les trois liens de `app/README.md` vers les README supprimés et les renvois
API des deux interfaces. Éviter de transférer les constats d’audit npm datés comme
s’ils décrivaient l’état actuel ; conserver leur preuve historique dans les cartes.

### Options d’arbitrage

| Choix | Option recommandée | Alternative et coût |
| --- | --- | --- |
| Portée | Noms et index limités à `docs/`, identifiants DEM/OPS conservés ; suppressions explicitement demandées hors docs. | Étendre à tout le dépôt nécessiterait un nouvel inventaire des noms et exceptions. |
| Citation | Une citation après le H1 de chaque document explicatif ; README et sommaires exemptés. Ajouter celle de dockerisation et reconstitution. | Une citation par section explicative H2/H3 : revue beaucoup plus large, risque de répétition ; qualification préalable de chaque section. |
| Historique | Liens navigables migrés, littéraux probatoires conservés. | Réécriture exhaustive : coût élevé et altération possible des traces ; conservation de tous les anciens liens : navigation dégradée. |
| Contrôle | Règles structurelles et liens locaux bloquants ; qualité rédactionnelle en revue humaine. | Structure seulement : coût moindre, références cassées non détectées. Tout automatiser : faux verdicts sur la qualité sémantique. |

### Contrôles à créer après arbitrage

`quality.py` exécute le typage des demandes, les tests de l’outillage et les contrôles
applicatifs ; la CI appelle cette commande. Aucun vérificateur documentaire dédié
n’a été trouvé dans les scripts et tests examinés. Les conventions de rédaction
existantes sont donc documentées, sans contrôle automatisé spécifique.

Proposer un vérificateur intégré à `quality.py`, avec tests dans l’outillage :

- Noms : accepter `docs/architecture/03-developpement-loop/01-interview.md`,
  rejeter `docs/01-architecture/` ; ne pas appliquer cette règle aux fichiers
  ni aux niveaux inférieurs ou aux identifiants du dev-book.
- Index : accepter listes/tableaux de liens et titres ; rejeter paragraphes
  explicatifs et blocs de commandes. Définir précisément les libellés autorisés ;
  leur pertinence reste humaine.
- Citations : vérifier la présence après H1 selon l’option arbitrée ; ignorer les
  blocs de code, exempter README et index. La justesse du résumé reste humaine.
- Liens : vérifier les destinations locales Markdown et les ancres des contenus
  actifs, y compris hors `docs/`. Tester accents, titres identiques, espaces,
  parenthèses et liens entre chevrons ; accepter liens externes sans requête réseau.
  Ajouter les liens par référence et HTML ou les signaler comme non couverts,
  jamais comme vérifiés. Les chemins dynamiques nécessitent une revue.
- Historique : inventorier les liens déjà cassés et autoriser uniquement des
  exceptions explicites par fichier/cible ; aucune exclusion globale du dev-book.
  Les chemins littéraux d’anciennes preuves ne sont pas des liens à résoudre.

Un sondage exploratoire par expression régulière a reconnu 183 liens locaux dans
145 Markdown suivis : deux cibles actives réellement absentes (ci-dessus), cinq
occurrences historiques à qualifier et deux faux positifs dus aux parenthèses de
la charte graphique. Ce sondage ne valide ni les ancres ni tous les liens ; il
justifie un analyseur adapté plutôt qu’une simple expression régulière bloquante.

### Impacts et vérification attendue

Devops porte migration des guides, instructions et vérificateur. Les suppressions
applicatives nécessitent des contributions API, web et backoffice coordonnées ;
aucun transfert de fichiers non commités entre couches. Aucun changement graphique
proposé. Coût principal : extraction des index et migration des liens/ancres ;
les renommages seuls sont mécaniques. Aucune carte avant arbitrage.

L’analyse est prête pour arbitrage avec les limites de couverture ci-dessus.
Les vérifications futures restent celles de la section suivante ; aucun succès
d’implémentation ou verdict humain n’est déduit de cet inventaire.

## Arbitrage humain — 2026-10-30

Session : session intervenante indiquée en tête. Verdict exact : « validé »,
en réponse aux six points présentés avec `arbitrer-convention`.
Adoption de l’ensemble, sans ajustement ni motif supplémentaire exprimé :

- Noms et index : périmètre et corrections de l’analyse adoptés, limités à `docs/`.
- Citations : option recommandée adoptée ; une après H1 par document explicatif,
  README et sommaires exemptés, sans obligation par section H2/H3.
- Conventions : centralisation dans les README concernés et remplacement des
  doublons par des liens, selon les destinations proposées dans l’analyse.
- Suppressions : les cinq README du périmètre seront supprimés après transfert
  des informations utiles et adaptation de leurs références.
- Historique : migration des liens navigables, conservation des chemins littéraux
  probatoires, SHA, résultats et verdicts passés.
- Contrôles : noms, structure des index, présence des citations et liens locaux
  bloquants ; qualité rédactionnelle soumise à revue humaine, sans automatisation
  sémantique retenue. Cas, exceptions et limites définis dans l’analyse ci-dessus.

### Ajustement humain de la portée des noms

Même session intervenante, 2026-10-30 : « la suppression des numéros ne s'appliquer
que pour le premier niveau, le niveau des thématique documentaire », puis
« par contre ce qui parle des 4 piliers ou des steps de loop, les numéros sont les bienvenue ».
Cette précision remplace la portée générale des noms adoptée précédemment :
seuls les dossiers directement sous `docs/` sont sans préfixe numérique.
Les niveaux inférieurs et fichiers conservent leur numérotation, notamment les
quatre rubriques sous `docs/architecture/` et les douze étapes. Le contrôle et
ses tests appliquent cette limite ; les autres points de l’arbitrage restent acquis.

Preuves requises : tests du vérificateur sur cas conformes, écarts et exceptions,
contrôle des références migrées et commandes de la section suivante, avec résultats
réels et limites explicites. Les exceptions historiques restent à inventorier par
fichier/cible ; aucune dispense générale n’est adoptée. L’extension des règles de
noms et d’index hors `docs/` reste exclue. Cet arbitrage ne valide aucun résultat
d’implémentation et ne déclenche ni implémentation ni opération Git.

## Vérification envisagée

Après arbitrage et implémentation : contrôle des liens et références migrés,
`git diff --check`, tests des vérificateurs via
`python3 codebase-integrity/scripts/check.py` si adaptés, puis
`python3 codebase-integrity/scripts/quality.py` avant PR. Aucun résultat futur
n’est acquis ; aucun contrôle ni convention en vigueur n’est modifié à l’interview.

## Cartes d’implémentation

- [OPS-073](../tasks/OPS-073-conventions-documentaires.md)
- [API-003](../tasks/API-003-migrer-documentation.md)
- [WEB-003](../tasks/WEB-003-migrer-documentation.md)
- [BO-003](../tasks/BO-003-migrer-documentation.md)

### Prise en charge globale des cartes restantes

Instruction humaine du 2026-10-30, session intervenante : « implémente une demande,
à toi de creer toutes les modifications des taches concernés », avec invocation
d’`implementer-demande`. Le type consolidation reste inchangé ; aucun contrôle ni
convention n’est modifié dans cette reprise.

Cette instruction remplace le découpage séquentiel initial pour les seules cartes
API-003, WEB-003 et BO-003 : mission documentaire unique dans `worktree/devops`,
branche `layers/devops`, dépendant du commit validé d’OPS-073 déjà présent.
Les autres worktrees restent intacts. Les anciennes dépendances entre interfaces
organisaient l’édition des liens partagés ; elles ne décrivaient pas des dépendances
de code et sont retirées. Les trois cartes seront présentées ensemble, sans commit
intermédiaire ni présomption de validation humaine.

Les informations communes aux interfaces sont centralisées dans un guide partagé,
avec renvois depuis leurs guides respectifs. Après cette reprise, l’humain demande de mettre aussi `app/README.md` à la
structure attendue : description, liste de responsabilités sans renvois, puis
conventions techniques. Cette correction remplace le rétablissement antérieur ;
la navigation vers les guides reste dans le sommaire des applications.
Sur précision humaine, la section des conventions techniques reste vide pour le moment.

### Preuves de la reprise documentaire

Base de cette reprise : `cb3336b1389d32c0a3118c7870393a3d3f5349bc`.
Contrôles exécutés le 2026-10-30 depuis `worktree/devops` :

- `python3 codebase-integrity/scripts/check_docs.py` : conforme, aucun avis dynamique.
- `python3 codebase-integrity/scripts/check_demands.py` : conforme.
- `git diff --check` et vérification de forme des nouveaux guides : réussis.
- Vérification des sources locales : trois suppressions confirmées ; scripts npm,
  ports et prérequis cohérents avec les deux manifestes ; chemins des commandes API,
  configuration de connexion et contrat OpenAPI présents et relus.

Aucun lancement applicatif, installation ou test navigateur effectué pour cette
migration documentaire. Aucune donnée ni configuration d’environnement modifiée.
La qualité complète reste à exécuter avant PR ; aucune validation humaine des trois
cartes restantes n’est déduite de ces contrôles. Aucun commit créé pendant l’implémentation ; les commits issus de la validation
sont référencés dans les cartes.

Contenu présenté : 14 chemins, dont quatre guides et un sommaire nouveaux sous
`docs/applications/`, trois README supprimés et les adaptations de structure,
de navigation et de suivi. Empreinte SHA-256 des chemins triés et contenus,
suppressions marquées, hors demande et cartes de suivi :
`88a945f26d0d0caba488fe3a02443361dc93603589f353b1f1feb994b694a5d5`. Index Git vide.

### Verdict sur les trois cartes restantes

Le 2026-10-30, même session intervenante : verdict humain exact « validé » en
réponse à la présentation de vérification d’API-003, WEB-003 et BO-003.
L’empreinte du contenu présenté ci-dessus a été revérifiée identique avant
consignation. L’adoption couvre les trois suppressions, les guides, la navigation
et la structure d’`app/README.md` avec conventions techniques vides.

Répartition des fichiers partagés pour les commits distincts : API-003 porte la
structure du README commun et l’entrée documentaire des applications ; WEB-003
introduit la procédure commune des interfaces ; BO-003 complète sa navigation.
Les fichiers de travail restent ceux validés ; seules les références disponibles
à chaque commit sont indexées dans les sommaires intermédiaires.
Aucun changement applicatif, contrôle, environnement ni travail étranger ajouté.

### Fin de vérification

Les trois commits distincts sont consignés dans les sections « Commit local »
des cartes ci-dessus. Leur résultat cumulé sur les 14 chemins est identique à
l’empreinte validée, hors traces documentaires. Le worktree et l’index étaient
propres après le troisième commit ; ce complément consigne uniquement les SHA
et l’état de vérification. Contrôles documentaire, typage et diff conformes.
La livraison et sa qualité complète restent à effectuer ; aucun push, PR ou merge.

## Reconstitution — 2026-10-30

Même session intervenante. Dossier principal libre et propre avant création,
sur develop local `eac1b98072f82de8be79e1ffb9ce9d7c2493a5b3`.
Branche créée : `demands/DEM-021` ; retour prévu sur develop après livraison.
Les branches de couche, leurs environnements et les données sont conservés.

| Commit source validé | Commit obtenu par cherry-pick -x |
| --- | --- |
| `a2c52a8d8f1b3850b30bae6c1f51f706ed148562` | `ab5a3f60753f142d64b61174e6492ef0e95cdefe` |
| `cb3336b1389d32c0a3118c7870393a3d3f5349bc` | `478f64623a419702e3b2d3e281e02934812fe5c2` |
| `6eaa52ac1e2d61bd5d73b18715440ec5ef407fc7` | `ee1f7c9b6e52408a924f80b4a80b8c10e9658dcd` |
| `91e090d090eaaa9d5b9c3c76abd016b8048cb864` | `7a77e0f941a8d94c44fa9a22e934021b101b92f4` |
| `cbf2f368654c31370af9975ec1b696750861c78c` | `806561a212d6bb2a6c60c6c37d63ded82bc1b51e` |
| `6a527151f01c097ed39b5f67791a7d6d52f8440c` | `bc7095103e95320b7440cbedf31f1b48864401d3` |

Les six commits se sont appliqués sans conflit. Leurs patch-id sont identiques ;
`git range-diff` relève seulement la provenance ajoutée aux messages. Les écarts
avec la branche source correspondent aux changements de develop déjà intégrés
par DEM-022 ; aucun changement fonctionnel validé n’a été réinterprété.
DEM-023 et le brief non suivi DEM-024 sont exclus de cette reconstitution.

Contrôles depuis le dossier principal reconstitué :

- `python3 codebase-integrity/scripts/check.py` : 66 tests réussis, socket locale autorisée.
- `python3 codebase-integrity/scripts/check_docs.py` : conforme.
- `python3 codebase-integrity/scripts/check_demands.py` : conforme.
- `git diff --check develop..HEAD` : réussi.

La qualité complète reste à exécuter avant PR. La présente trace documentaire
reste non commitée pour le commit documentaire de livraison ; aucun push, PR ou
fusion réalisé à cette étape. develop reste au SHA de base indiqué ci-dessus.

## Livraison — 2026-10-30

Même session intervenante ; dépôt principal sur `demands/DEM-021`, index vide
avant les seules traces documentaires. Six contributions validées réunies au HEAD
`bc7095103e95320b7440cbedf31f1b48864401d3` ; correspondances ci-dessus.

`python3 codebase-integrity/scripts/quality.py` : réussi avec autorisation des
sockets locales ; 66 tests d’outillage, contrat API, lint du conteneur, mapping
Doctrine, export OpenAPI, typage et builds web/backoffice. Le premier passage
restreint échouait uniquement à créer la socket du test d’identité.
Synchronisation de base exclue par `--skip-sync` ; aucun test navigateur demandé.
Contrôles documentaires, typage des demandes et `git diff --check` réussis.

Distant vérifié : `johan-Rm/ai-development-engineering`, develop
`eac1b98072f82de8be79e1ffb9ce9d7c2493a5b3`. Rebase and merge autorisé,
protections lues et conservées ; aucune approbation requise par la règle active.
Aucune PR préexistante pour cette branche. DEM-023/DEM-024 restent exclues.

Inventaire : API, web et backoffice propres, sans mission active identifiée
depuis le suivi DEM-022, à `eac1b98` ; avance rapide possible après intégration.
Design à `b40faca`, trois `.gitkeep` non suivis : couche préservée. Devops à
`6aee391`, contributions DEM-023 et brief non suivi DEM-024 : couche préservée.
Ces deux couches empêchent la clôture du suivi, sans bloquer la PR de DEM-021.
URL, SHA intégré et correspondances réécrites seront consignés après vérification
distante dans le brouillon local de cette demande, sans écriture sur develop.
