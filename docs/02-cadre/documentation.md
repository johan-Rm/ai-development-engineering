# Documentation

> La documentation rend le projet compréhensible, conserve les décisions et donne à chaque dossier des responsabilités explicites.

## Ranger selon l’usage

| Emplacement | Contenu |
| --- | --- |
| [README racine](../../README.md) | Présentation et vue d’ensemble du cadre. |
| [SETUP.md](../../SETUP.md) | Préparation du dépôt et démarrage du travail. |
| [docs/index.md](../index.md) | Explications et références, organisées par thème. |
| [dev-book/](../../dev-book/README.md) | Demandes, cartes, procédures, ressources et preuves. |
| `**/README.md` | Responsabilités et conventions techniques locales. |
| [AGENTS.md](../../AGENTS.md) | Instructions de travail des agents. |

Les index de `docs/` s’appellent `index.md`. Les cartes ne remplacent pas la documentation durable ; elles pointent vers les documents concernés.

## Garder les README applicatifs courts

Un README de sous-dossier applicatif contient seulement :

```markdown
# Nom du dossier

Description courte.

## Rôle et responsabilités

## Conventions techniques
```

Lire les README du chemin concerné avant d’écrire ou de relire le code. Le README le plus proche précise les règles du parent. Toute évolution d’une règle locale est documentée à cet endroit, sans duplication dans les guides centraux.

Cette structure ne s’impose ni au README racine, ni aux index documentaires,
ni aux README du cadre. Ne pas migrer automatiquement les README existants.

## Relire le code

Vérifier les chapitres « Rôle et responsabilités » et « Conventions techniques »
des README applicables. Signaler les écarts avec leurs fichiers et les contradictions
avec AGENTS.md. Toute convention technique modifiée est documentée dans son README
et vérifiée par les contrôles pertinents, selon la boucle de consolidation.

## Écrire pour une lecture rapide

Commencer chaque chapitre explicatif par une courte citation qui en donne l’idée principale. Utiliser des titres précis, des paragraphes courts et des liens vers les détails. Toujours employer « convention technique » pour désigner une règle technique du projet.

Pour les travaux graphiques, suivre la [référence graphique du projet](../../AGENTS.md#références-à-consulter-selon-la-tâche).
