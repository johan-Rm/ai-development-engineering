# Règles de PR

> Présenter et vérifier une demande complète avant son intégration.

La PR présente une demande reconstituée vers develop. Son titre exprime le résultat
global, par exemple `Clarifier les conventions des commits (DEM-024)` ; il ne
reprend pas le titre de la première carte. Le corps explique le problème résolu,
le comportement obtenu, les vérifications et leurs limites.

Avant ouverture, les cartes attendues ont leurs verdicts et leurs commits, et
les contrôles qualité portent sur l'ensemble à livrer. Le vérificateur des messages
examine toute la plage : un commit invalide au milieu de la série bloque la PR.
Les références sont confrontées aux documents présents dans l'arbre reconstitué.

La relecture humaine porte aussi sur ce que les contrôles ne peuvent pas établir :
la précision du titre, la pertinence du type et l'adéquation du résultat au besoin.
Une correction fonctionnelle nécessite une nouvelle validation. La réussite
technique ne vaut pas verdict humain, et un contrôle inconnu ne vaut pas réussite.

La préparation de la PR, son intégration et le suivi sont distincts. Une instruction
limitée à la PR n'autorise pas sa fusion. Les conditions et commandes d'exécution
sont conservées dans les procédures de livraison et de Codebase Integrity.
