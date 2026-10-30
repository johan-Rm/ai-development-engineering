# Points de contrôle

> Relier les conventions techniques du projet à des vérifications reproductibles.

## De la convention au contrôle

Une convention technique est une règle écrite dans un README, destinée à devenir
un contrôle automatique. Le point de contrôle traduit cette règle en vérification
exécutable sans jugement d’IA. Il relie la convention, le périmètre examiné et le
résultat attendu.

Une règle encore dépourvue de contrôle reste identifiable comme telle. L’existence
d’une documentation ou d’un outil ne suffit pas à démontrer qu’elle est vérifiée.

## Interpréter les résultats

Un contrôle bloquant établit un écart sans ambiguïté et empêche la validation tant
que cet écart subsiste. Un contrôle informatif apporte un constat qui nécessite
une interprétation humaine.

La réussite ne vaut que pour le périmètre effectivement examiné. Un contrôle non
exécuté, une erreur d’exécution ou un résultat inconnu ne constituent pas une
conformité. Les préconditions et les limites permettent de comprendre la portée
du résultat.

## Vérifier les vérificateurs

Les contrôles possèdent eux-mêmes des tests : ils doivent accepter les cas
conformes, détecter les écarts et respecter les exceptions autorisées. Ces tests
protègent la fiabilité du système quand ses règles et son outillage évoluent.

La réussite technique ne remplace pas la vérification humaine de l’adéquation
d’une règle au besoin ou du résultat à la demande.

## Faire évoluer le système

La boucle de développement applique les conventions et exécute les contrôles.
La consolidation examine les écarts, fait confirmer les évolutions de règles,
puis adapte les vérificateurs et leurs tests. Un échec n’autorise pas à affaiblir
une règle pour faire passer une contribution.

Le système s’enrichit avec le projet. Les modalités d’exécution, configurations
et détails propres aux contrôles vivent dans Codebase Integrity ; ce guide
explique leur rôle commun sans en dresser le catalogue.
