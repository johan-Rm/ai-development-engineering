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
Leurs sources sont versionnées dans [skills/](skills/README.md) ; l’installation personnelle
reste une opération distincte. Si un skill manque dans la session, consulter sa source versionnée
et la carte ; signaler ce qui n’est pas disponible sans supposer son installation.

Les deux boucles ont chacune six skills indépendants. Les skills de vérification et d’arbitrage
accompagnent et consignent les décisions humaines sans les remplacer.

### Boucle de développement

| Étape | Skill |
| --- | --- |
| 01 Interview | [`interviewer-demande`](skills/interviewer-demande/SKILL.md) |
| 02 Découpage | [`decouper-demande`](skills/decouper-demande/SKILL.md) |
| 03 Implémentation | [`implementer-tache`](skills/implementer-tache/SKILL.md) |
| 04 Vérification | [`verifier-tache`](skills/verifier-tache/SKILL.md) |
| 05 Reconstitution | [`reconstituer-demande`](skills/reconstituer-demande/SKILL.md) |
| 06 Livraison | [`livrer-demande`](skills/livrer-demande/SKILL.md) |

### Boucle de consolidation

| Étape | Skill |
| --- | --- |
| 01 Interview | [`interviewer-constat`](skills/interviewer-constat/SKILL.md) |
| 02 Analyse globale | [`analyser-convention`](skills/analyser-convention/SKILL.md) |
| 03 Arbitrage | [`arbitrer-convention`](skills/arbitrer-convention/SKILL.md) |
| 04 Implémentation | [`implementer-consolidation`](skills/implementer-consolidation/SKILL.md) |
| 05 Vérification | [`verifier-consolidation`](skills/verifier-consolidation/SKILL.md) |
| 06 Livraison | [`livrer-consolidation`](skills/livrer-consolidation/SKILL.md) |

`evoquer-un-sujet`, `etat-des-lanes` et `configurer-worktrees-aide` servent avant ou autour
des boucles. `commit-tache` clôture et committe une tâche validée sur demande ; `creer-pr`
sert aux livraisons autorisées ; `apres-pr-mergee` intervient après fusion prouvée.
Le [catalogue](skills/README.md) décrit la migration des anciens noms et l’installation ultérieure.
Les tests et la documentation pertinents accompagnent l’implémentation avant présentation.
Commit, push, PR et merge restent soumis aux demandes explicites prévues ci-dessus.

## Référence graphique à conserver

Pour tout travail graphique, lire la charte officielle du dépôt :
[Brand Guidelines — Graines Digitales](<design/Brand Guidelines - Graines Digitales (standalone).html>).
Ne pas lui substituer une copie externe. La [synthèse opérationnelle](design/charte-graphique.md)
rappelle ses règles et les adaptations explicitement demandées pour AIDE : humain/cadre en olive,
IA en terre cuite `#C07040`, couleurs dans les fonds/textes/bordures, sans traits décoratifs de rôle.
