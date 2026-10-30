# Stratégie de merge

> Intégrer les contributions validées en conservant leurs commits et leur traçabilité.

Utiliser **Rebase and merge** pour intégrer les PR vers develop. Chaque commit est
conservé avec un nouvel identifiant ; aucun commit de fusion ni squash n’est créé.
Vérifier la méthode permise par GitHub ; si elle est interdite, signaler le blocage
sans substituer une autre stratégie ni modifier les protections. Les branches de
PR doivent être linéaires : ne pas créer de merges pour rattacher les couches.
Une modification nécessaire du contenu validé demande une nouvelle vérification.

Avant intégration, consigner la PR, son HEAD, les SHA sources et reconstitués,
les contrôles et les verdicts. Après intégration, vérifier l’état intégré de la PR,
le SHA résultant et sa présence dans develop distant ; tracer les correspondances
avec les commits réécrits. Une équivalence de patch seule ne prouve pas l’intégration.
Ne pas réécrire les anciens commits de fusion.
