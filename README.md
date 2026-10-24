# AIDE — AI Development Engineering

**Des conventions techniques humaines, des contributions isolées et des résultats vérifiables.**

AIDE organise le développement logiciel assisté par IA autour de conventions techniques humaines,
de contributions isolées et de résultats vérifiables.

Sa brique centrale est le **Codebase Integrity** : les contrôles déterministes qui
vérifient l’application des conventions techniques du projet. L’IA peut aider à écrire ces
contrôles ; leur exécution ne dépend pas de son jugement.

Deux boucles font vivre le système :

- La boucle de développement transforme les demandes en changements implémentés, vérifiés et livrés.
- La boucle de consolidation examine les pratiques dans toute la base, corrige les écarts et enrichit les conventions techniques et leurs contrôles.

Quatre piliers soutiennent ces boucles : la consolidation, les couches, l’IA Engineering
et la documentation. L’humain définit les règles, arbitre les choix et valide les résultats.

[Codebase Integrity](#codebase-integrity) · [Les quatre piliers](#les-quatre-piliers) · [Les deux boucles](#les-deux-boucles) · [Se repérer](#se-repérer)

## Codebase Integrity

Le Codebase Integrity est la brique la plus importante d’AIDE. Il rend les exigences
du projet vérifiables par des tests et des vérificateurs exécutables sans IA, en CI/CD ou
à la demande.

Les humains définissent les conventions techniques et leurs exceptions. Les conventions techniques
sont documentées au plus près du code, dans les README des dossiers concernés ; les
contrôles vérifient leur application. Une convention technique encore dépourvue de contrôle doit
rester identifiable comme telle.

> [!IMPORTANT]
> La boucle de développement applique les conventions techniques et exécute les contrôles.
> Leur évolution passe par la consolidation, après arbitrage humain. Un échec de contrôle
> n’autorise pas l’IA à affaiblir la règle pour faire passer son changement.

Les contrôles bloquants doivent réussir avant l’ouverture d’une PR. Les résultats qui
nécessitent une interprétation restent soumis au jugement humain.

[Explorer le Codebase Integrity](codebase-integrity/README.md)

## Les quatre piliers

| Pilier | Rôle dans AIDE |
| --- | --- |
| **Consolidation** | Transformer les constats en corrections globales, conventions techniques validées et contrôles durables. |
| **Couches** | Définir les responsabilités, isoler les contributions et expliciter les contrats et dépendances. |
| **IA Engineering** | Donner aux agents les instructions, le contexte et les skills adaptés à chaque étape. |
| **Documentation** | Expliquer le projet, conserver les décisions et définir les responsabilités et conventions techniques locales. |

Une couche dispose de sa branche, de son worktree et de son environnement. Un seul agent
y écrit à la fois. L’isolation des fichiers doit être complétée par celle des ports, des
bases et des autres ressources utilisées.

## Les deux boucles

### Développement

**Demande → Interview → Découpage → Implémentation → Vérification → Reconstitution → Livraison → PR**

L’IA clarifie la demande avec l’humain, la découpe en tâches par couche et réalise chaque
contribution. L’humain vérifie le résultat et les preuves, puis valide ou demande des
corrections. Chaque tâche validée produit un commit distinct. La reconstitution réunit
les commits de la demande avant les contrôles de livraison et la préparation de sa PR.

### Consolidation

**Constat → Interview → Analyse globale → Arbitrage → Implémentation → Vérification → Livraison**

Un constat local peut révéler un problème présent dans toute la base. L’IA analyse les
occurrences et propose une règle et ses corrections. L’humain arbitre ; l’implémentation
corrige le code concerné et ajoute les vérifications retenues. Après vérification humaine
et contrôles réussis, la livraison produit les PRs de consolidation et les règles et
contrôles qui renforcent les cycles suivants.

[Consulter le schéma interactif AIDE](dev-book/resources/vue-d-ensemble-ai-development-engineering.html)

## Se repérer

| Emplacement | Contenu |
| --- | --- |
| [codebase-integrity/](codebase-integrity/README.md) | Outillage commun et tests de ses vérificateurs ; les tests applicatifs restent dans les applications. |
| [docs/](docs/index.md) | Explications du système AIDE et de ses boucles. |
| [AGENTS.md](AGENTS.md) et [.codex/config.toml](.codex/config.toml) | Instructions du projet, skills recommandés et configuration Codex. |
| [dev-book/](dev-book/README.md) | Demandes, tâches, procédures, ressources et preuves. |
| `**/README.md` | Responsabilités et conventions techniques des dossiers concernés. |
| [app/](app/README.md) | Applications de démonstration : API Symfony/API Platform, web et backoffice Nuxt. |
| [design/](design/README.md) et [infra/](infra/README.md) | Références graphiques et infrastructure de recette. |

AIDE est indépendant des langages et frameworks du projet. Les applications de ce dépôt
illustrent son utilisation et peuvent être remplacées par une autre stack.

Installation et adaptation au projet : [SETUP.md](SETUP.md).
