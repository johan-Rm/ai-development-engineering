# Principes fondamentaux

> Le **Codebase Integrity est la pierre angulaire de l’écosystème AIDE — AI Development Engineering**, un cadre d’ingénierie pour concevoir, développer et faire évoluer des logiciels avec l’assistance de l’IA. Les conventions techniques humaines guident la conception ; les contrôles vérifient leur application.

## Préambule

Le **Codebase Integrity cadre et contrôle la boucle de développement** en vérifiant l’application des conventions techniques du projet.

**La validation de toute PR de développement exige la réussite des tests du Codebase Integrity.** Un résultat absent ou inconnu ne vaut pas réussite.

**La boucle de développement ne peut modifier aucun élément du dossier `codebase-integrity/`** : scripts, tests, configurations ou autres fichiers. Toute modification de ce dossier relève de la boucle de consolidation, après arbitrage humain.

## L’humain décide, l’IA assiste

L’humain définit et valide les conventions techniques, leurs exceptions et les contrôles attendus. L’IA peut analyser, proposer et implémenter ces décisions.

Un échec n’autorise pas l’IA à affaiblir une règle ou à désactiver son contrôle.

## Les conventions techniques guident, les contrôles vérifient

Les conventions techniques précisent les exigences, leur périmètre et leurs exceptions. Elles vivent dans la section `Conventions techniques` des README concernés, sans duplication dans la documentation centrale.

Les tests et vérificateurs s’exécutent **sans jugement d’IA**, en CI/CD ou à la demande. Les vérificateurs spécifiques sont eux-mêmes testés. Une convention technique sans contrôle automatisé doit être signalée.

Les tests et les autres contrôles bloquants doivent réussir sur la version soumise à validation. Les constats informatifs demandent une interprétation humaine. Des contrôles réussis ne remplacent pas la vérification humaine du résultat.

## Une brique vivante, deux boucles

Le Codebase Integrity se construit **surtout pendant la construction du projet** : les réalisations et les revues révèlent les règles à préciser et les contrôles à enrichir.

| Boucle | Rôle |
| --- | --- |
| **Développement** | Appliquer les conventions techniques, exécuter les contrôles et présenter les preuves. |
| **Consolidation** | Après arbitrage humain, corriger les écarts dans toute la base concernée et faire évoluer les conventions techniques et contrôles. |

Ce cadre reste propre aux besoins du projet et indépendant de sa stack. Toute évolution des règles et contrôles passe par la consolidation et la validation humaine.
