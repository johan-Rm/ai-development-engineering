# Documentation

> La documentation rend le projet compréhensible, conserve les décisions et donne à chaque dossier des responsabilités explicites.

## Ranger selon l’usage

| Emplacement | Contenu |
| --- | --- |
| [README racine](../../README.md) | Présentation et vue d’ensemble d’AIDE. |
| [SETUP.md](../../SETUP.md) | Installation et adaptation au projet. |
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

## Écrire pour une lecture rapide

Commencer chaque chapitre explicatif par une courte citation qui en donne l’idée principale. Utiliser des titres précis, des paragraphes courts et des liens vers les détails. Toujours employer « convention technique » pour désigner une règle technique du projet.

La [charte officielle](<../../design/Brand Guidelines - Graines Digitales (standalone).html>) gouverne les travaux graphiques. Pour le schéma AIDE : humain en olive, IA en terre cuite `#C07040`, sans traits décoratifs de rôle.
