# Consignes des agents

Lire [les couches](docs/02-cadre/couches/index.md), la carte demandée et les README applicables avant d’écrire.
Les instructions explicites de l’utilisateur priment. Une mission précise son worktree relatif à la racine du dépôt principal,
sa branche, ses chemins autorisés, ses dépendances par commit et sa preuve attendue.
Ne déléguer que sur demande explicite.

## Réponses et documents

Rédiger des réponses et documents strictement concis et précis, sans répétitions ni
détails superflus. Conserver les informations, preuves et décisions nécessaires.
Si davantage de détails ou une présentation exhaustive paraît nécessaire, fournir
d’abord une synthèse concise, demander l’accord de l’humain et attendre sa validation
explicite avant de développer la réponse ou le document. Le silence ne vaut pas accord.

## Conventions de workflow

- **Cartes de tâches** : `dev-book/tasks/`, préfixes et routage dans [les couches](docs/02-cadre/couches/index.md).
- **Branche d’intégration** : `develop` ; **production** : `master` ; `main` reste historique.
- **Branches de travail** : `layers/<couche>` ; **arbres de travail** : `worktree/<couche>`.
- **Maintenance du cadre** : devops, `layers/devops`, préfixe `OPS`.
- **Créer un arbre** : `python3 codebase-integrity/scripts/worktrees.py add --layer <couche> --branch layers/<couche> --base develop` (base locale explicite, sans fetch).
- **Qualité avant PR** : `python3 codebase-integrity/scripts/quality.py` ; **tests de l’outillage** : `python3 codebase-integrity/scripts/check.py`.
- **Stratégie de merge proposée** : merge commit, sous réserve de la politique GitHub configurée.

Les skills portent les procédures des étapes ; les règles suivantes précisent leurs limites ici :
dans la boucle de développement, `implementer-demande` réalise les cartes sans commit,
y compris leurs corrections. `verifier-demande` autorise les commits locaux distincts des
cartes explicitement validées par l’humain, avec leur code, tests, documentation, preuves
et verdict, puis les traces documentaires nécessaires. Aucun verdict ne peut être inventé. Le découpage est autonome
et prévoit la branche dédiée `demands/<identifiant>`, créée à la reconstitution, même pour
une seule couche ; ne pas utiliser une branche de couche pour porter une demande reconstituée.
Invoquer `livrer-demande` autorise la livraison complète en autonomie : commits documentaires
nécessaires, vérification distante et fetch, push sans forcer, création ou mise à jour de la PR
vers `develop`, fusion après contrôles et protections satisfaits, retour du worktree à sa branche
de couche, réalignement des couches libres et suppression des seules branches
temporaires livrées. Conserver les worktrees, .env et données. Ne pas redemander une autorisation pour chacune de ces
opérations. Une demande limitée explicitement à une PR reste limitée à cette PR.
Hors de ce périmètre, les autres opérations Git nécessitent une demande explicite. Aucun changement de tâche
sur l’intégration ou la production. Préserver le travail existant et les `.env` ; pas de stash,
reset --hard, force-push ou suppression de worktree pour résoudre une situation.
Vérifier la branche, l’index et l’état Git dans le worktree absolu affecté. Ne pas commencer
une nouvelle mission si des modifications suivies, indexées ou des fichiers non suivis sont
présents ; préserver cet état et signaler le blocage. Une reprise de la même mission peut
conserver ses modifications non commitées identifiées, sans changement étranger ; un arbre propre ne prouve pas
qu’une couche est libre. Les dépendances et la reconstitution reposent sur des commits identifiés,
jamais sur la copie du travail non commité d’une autre mission. Ne pas rebaser une branche
partagée ou occupée sans coordination. La livraison complète inclut le réalignement
de toutes les couches configurées sur le même SHA que develop après fusion vérifiée.
Avant la PR, examiner les divergences : les copies de contributions déjà validées peuvent
être rattachées par merges ciblés à la branche de livraison, après vérification de leur
équivalence et sans changement du résultat validé, pour permettre les avances rapides finales.
Après fusion, avancer develop et toutes les couches confirmées libres et propres par
avance rapide, préserver les worktrees et les .env, puis vérifier les SHA et états Git.
Une couche occupée, sale ou contenant du travail inédit reste intacte : signaler le blocage
et ne pas annoncer le suivi de livraison terminé tant que toutes les couches ne sont pas alignées.

Un worktree n’isole pas les services : ports, volumes, bases, caches et destinations d’écriture
restent à isoler et à vérifier avant d’en annoncer l’isolation. Les outils excluent `worktree/`.
La [documentation d’infrastructure](infra/README.md) décrit les témoins Docker ; aucun déploiement
applicatif n’est configuré. Les changements de conventions techniques et contrôles passent par la
consolidation selon [Codebase Integrity](codebase-integrity/README.md).

## Rangement des demandes

Les noms de fichiers et dossiers `DEM-*` sont réservés aux documents de demande
situés dans `dev-book/demand/`. Les rapports éventuels ont un nom décrivant leur rôle.

La reconstitution consiste à créer `demands/<identifiant>` depuis le develop local
vérifié, dans un worktree existant libre et propre, puis à y cherry-pick les commits
validés avec `git cherry-pick -x`, dans l’ordre des dépendances. Aucune copie ou
dossier de réunion supplémentaire. Noter la branche de couche à retrouver après
livraison ; conserver le worktree et ses fichiers locaux. Consigner les SHA sources
et obtenus dans la demande ou les cartes, sans nouveau rapport séparé.

## Documentation et README

Toute nouvelle demande et toute nouvelle carte doivent renseigner l’identifiant réel de la
session qui les crée. Le relever depuis le contexte de session ou une source locale fiable
(par exemple `CODEX_THREAD_ID` ou `CODEX_SESSION_ID`), jamais le déduire du numéro DEM/OPS.
Si l’identifiant est absent ou contradictoire, signaler le blocage avant création au lieu
d’écrire « référence de session indisponible ». À la reprise dans une autre session,
conserver l’identifiant d’origine et ajouter celui de la session intervenante.


- [docs/index.md](docs/index.md) est l’index des guides et références durables du projet.
- [dev-book/README.md](dev-book/README.md) décrit les demandes, cartes de tâches, procédures et preuves.
- Les `**/README.md`, y compris `**/**/README.md`, portent les règles locales de leurs dossiers.
  Avant toute écriture, lire les README existants sur le chemin concerné, de la racine au dossier
  modifié. Le plus proche précise les responsabilités et conventions techniques du parent, dans le respect
  des présentes consignes. Ne pas parcourir tous les README pour une mission locale.
- Si une règle locale change, mettre à jour le README concerné avec le changement.

Un README de sous-dossier d’un projet applicatif contient uniquement cette structure :

```markdown
# Nom du dossier

Description courte.

## Rôle et responsabilités

## Conventions techniques
```

Aucun autre chapitre. Cette structure ne s’impose pas au README racine du dépôt, aux index
documentaires ni aux README du cadre AIDE. Les README applicatifs existants ne sont pas
migrés automatiquement.

## Code Review Rules

Les conventions techniques sont définies dans le chapitre `## Conventions techniques` des
README de chaque dossier concerné. La revue de code vérifie leur application, ainsi que le
respect du chapitre `## Rôle et responsabilités`. Lire les README applicables avant la revue ;
ils constituent la référence locale, sans recopier leurs conventions techniques dans AGENTS.md.
Signaler les contradictions avec ces consignes et les écarts observés avec leurs fichiers
concernés. Une convention technique modifiée doit être documentée dans son README et vérifiée par les
contrôles pertinents.

## Skills à privilégier pour les boucles AIDE

La [vue AIDE](dev-book/resources/vue-d-ensemble-ai-development-engineering.html) définit les
briques des deux boucles. Les skills ci-dessous sont des procédures recommandées lorsqu’ils
sont disponibles ; leur mention ne les installe pas et ne déclenche aucune étape automatiquement.
Les skills sont personnels, hors du dépôt. Si un skill manque dans la session, suivre la carte
et les instructions du projet ; signaler la procédure manquante sans inventer son contenu.

Les deux boucles ont chacune six skills indépendants. Les skills de vérification et d’arbitrage
accompagnent et consignent les décisions humaines sans les remplacer.

### Boucle de développement

| Étape | Skill |
| --- | --- |
| 01 Interview | `interviewer-demande` |
| 02 Découpage | `decouper-demande` |
| 03 Implémentation | `implementer-demande` |
| 04 Vérification | `verifier-demande` |
| 05 Reconstitution | `reconstituer-demande` |
| 06 Livraison | `livrer-demande` |

### Boucle de consolidation

| Étape | Skill |
| --- | --- |
| 01 Interview | `interviewer-constat` |
| 02 Analyse globale | `analyser-convention` |
| 03 Arbitrage | `arbitrer-convention` |
| 04 Implémentation | `implementer-consolidation` |
| 05 Vérification | `verifier-consolidation` |
| 06 Livraison | `livrer-consolidation` |

`etat-des-lanes` et `configurer-worktrees-aide` sont les deux outils hors des boucles.
En développement, l’implémentation prépare des changements non commités avec leurs preuves.
La vérification recueille le verdict dans le chat puis crée un commit distinct par carte validée,
avec l’implémentation et sa trace de verdict. Les corrections restent non commitées jusqu’à leur
nouvelle validation à cette étape, puis produisent de nouveaux commits sans réécriture.
Une dépendance amont attend son commit après validation avant que son consommateur démarre.
Une carte validée et commitée reste à livrer. La reconstitution réunit ces SHA et leurs verdicts.
En consolidation, les autorisations propres aux skills et au projet continuent à s’appliquer.
En développement, invoquer la livraison autorise push, PR, fusion et suivi sans confirmation
intermédiaire, dans le périmètre validé et sous réserve des contrôles et protections.
Les skills doivent être disponibles et vérifiés dans la session avant la livraison.
Les tests et la documentation pertinents accompagnent l’implémentation avant présentation.
Les autorisations accordées par les invocations des étapes sont définies ci-dessus.
Toute évolution d’un skill qui modifie ces autorisations doit mettre à jour les présentes
consignes et les guides concernés dans le même changement ; vérifier leur cohérence avant présentation.

## Référence graphique à conserver

Pour tout travail graphique, lire la charte officielle du dépôt :
[Brand Guidelines — Graines Digitales](<design/Brand Guidelines - Graines Digitales (standalone).html>).
Ne pas lui substituer une copie externe. La [synthèse opérationnelle](design/charte-graphique.md)
rappelle ses règles et les adaptations explicitement demandées pour AIDE : humain/cadre en olive,
IA en bleu `#1B6EAE`, couleurs dans les fonds/textes/bordures, sans traits décoratifs de rôle.
