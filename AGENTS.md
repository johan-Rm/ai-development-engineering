# Consignes des agents

Lire [les couches](docs/02-cadre/couches.md), la carte demandée et les README applicables avant d’écrire.
Les instructions explicites de l’utilisateur priment. Une mission précise son worktree absolu,
sa branche, ses chemins autorisés, ses dépendances par commit et sa preuve attendue.
Ne déléguer que sur demande explicite.

## Conventions de workflow

- **Cartes de tâches** : `dev-book/tasks/`, préfixes et routage dans [les couches](docs/02-cadre/couches.md).
- **Branche d’intégration** : `develop` ; **production** : `master` ; `main` reste historique.
- **Branches de travail** : `layers/<couche>` ; **arbres de travail** : `worktree/<couche>`.
- **Maintenance du cadre** : devops, `layers/devops`, préfixe `OPS`.
- **Créer un arbre** : `python3 codebase-integrity/scripts/worktrees.py add --layer <couche> --branch layers/<couche> --base develop` (base locale explicite, sans fetch).
- **Qualité avant PR** : `python3 codebase-integrity/scripts/quality.py` ; **tests de l’outillage** : `python3 codebase-integrity/scripts/check.py`.
- **Stratégie de merge proposée** : merge commit, sous réserve de la politique GitHub configurée.

Les skills portent les procédures des étapes ; les règles suivantes précisent leurs limites ici :
commit, push, PR, merge et opérations distantes seulement sur demande, aucun changement de tâche
sur l’intégration ou la production. Préserver le travail existant et les `.env` ; pas de stash,
reset --hard, force-push ou suppression de worktree pour résoudre une situation.
Vérifier la branche et l’état Git dans le worktree absolu affecté ; un arbre propre ne prouve pas
qu’une couche est libre. Les dépendances et la reconstitution reposent sur des commits identifiés,
jamais sur la copie du travail non commité d’une autre mission. Ne pas rebaser une branche
partagée ou occupée sans coordination. Après merge, réaligner seulement les branches libres,
sans perte de données ; signaler les divergences.

Un worktree n’isole pas les services : ports, volumes, bases, caches et destinations d’écriture
restent à isoler et à vérifier avant d’en annoncer l’isolation. Les outils excluent `worktree/`.
La [documentation d’infrastructure](infra/README.md) décrit les témoins Docker ; aucun déploiement
applicatif n’est configuré. Les changements de conventions techniques et contrôles passent par la
consolidation selon [Codebase Integrity](codebase-integrity/README.md).

## Documentation et README

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
Ils restent personnels, hors du dépôt. Si un skill manque, suivre la carte, les instructions
ci-dessus et les [commandes de qualité](docs/01-codebase-integrity/points-de-controle.md) ; signaler toute procédure manquante
plutôt que supposer le skill installé ou inventer ses étapes.

### Boucle de développement

| Brique AIDE | Skill ou intervention à privilégier |
| --- | --- |
| Avant le cadrage, sujet à discuter | `evoquer-un-sujet` : discuter sans écrire ni ouvrir une tâche |
| 01 Interview | `creer-tache` : clarifier le besoin |
| 02 Découpage | `creer-tache` : écrire les cartes par couche et préparer la branche |
| 03 Implémentation | `demarrer-tache` : réaliser la carte, produire la preuve, les tests pertinents et la documentation |
| 04 Vérification | Verdict humain sur le résultat ; aucun skill ne le remplace |
| 05 Reconstitution | Aucun skill dédié : rassembler uniquement les commits autorisés après identification des dépendances et de la branche de réunion |
| 06 Livraison | `commit-tache` pour clôturer la carte et committer ; `creer-pr` pour les contrôles de livraison et la PR |
| Après fusion | `apres-pr-mergee` pour vérifier le merge et réaligner les branches libres |

### Boucle de consolidation

| Brique AIDE | Skill ou intervention à privilégier |
| --- | --- |
| 01 Interview | `evoquer-un-sujet` si la règle est encore à discuter, puis `creer-tache` pour formaliser la décision |
| 02 Analyse globale | Aucun skill dédié : examiner toute la base concernée par la convention technique pour relever ses applications et écarts ; ne pas confondre avec le simple état Git |
| 03 Arbitrage | Décision humaine sur la règle et les corrections à retenir |
| 04 Implémentation | `demarrer-tache` sur les cartes cadrées : corriger les écarts et automatiser les contrôles adaptés |
| 05 Vérification | Vérification humaine de l’application de la règle, appuyée par les preuves et contrôles exécutés |
| 06 Livraison | `commit-tache`, puis `creer-pr` ; `apres-pr-mergee` après fusion demandée |

`etat-des-lanes` sert à lire l’état des branches sans choisir ni démarrer une tâche.
Les tests et la documentation pertinents accompagnent l’implémentation avant sa présentation.
Commit, push, PR et merge restent soumis aux demandes explicites prévues ci-dessus.

## Référence graphique à conserver

Pour tout travail graphique, lire la charte officielle du dépôt :
[Brand Guidelines — Graines Digitales](<design/Brand Guidelines - Graines Digitales (standalone).html>).
Ne pas lui substituer une copie externe. La [synthèse opérationnelle](design/charte-graphique.md)
rappelle ses règles et les adaptations explicitement demandées pour AIDE : humain/cadre en olive,
IA en terre cuite `#C07040`, couleurs dans les fonds/textes/bordures, sans traits décoratifs de rôle.
