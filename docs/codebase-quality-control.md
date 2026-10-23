# Codebase Quality Control

Le **Codebase Quality Control** rassemble les conventions techniques d’un projet et les
points de contrôle qui vérifient leur application.

Chaque projet possède son propre Codebase Quality Control. Son contenu est vivant : comme
la documentation, il est enrichi, réécrit et ajusté en permanence. Les conventions peuvent
être génériques, reprises d’autres projets ou propres au projet.

AIDE (AI Development Engineering) fournit une structure agnostique, utilisable quels que
soient les langages et les technologies. Les applications Symfony et Nuxt de ce dépôt
sont des exemples. Les noms du dépôt et des dossiers restent inchangés.

## Organisation

**Domaine → Conventions techniques (règles) → Points de contrôle**

Chaque convention appartient à un seul domaine et précise :

- **La règle** : ce qui doit être respecté.
- **Le périmètre** : où elle s’applique.
- **Les exceptions** : les dérogations explicites et justifiées.
- **Les points de contrôle** : comment vérifier son application.
- **Le niveau de chaque contrôle** : bloquant ou informatif.

Un contrôle peut être **bloquant** lorsque le résultat permet de constater un écart sans
ambiguïté. Il reste **informatif** lorsque son résultat nécessite une interprétation humaine.

Une convention peut être documentée sans point de contrôle implémenté. Cet état doit être visible.

## Domaines

1. Règles métier
2. Données
3. Authentification et autorisations
4. Intégrations et échanges
5. Contrats et compatibilité
6. Parcours utilisateur
7. Interface et internationalisation
8. Accessibilité
9. Rendu visuel
10. Architecture et dépendances
11. Qualité du code
12. Sécurité
13. Performance et robustesse
14. Construction et livraison
15. Fiabilité des vérifications

## Documentation et contrôles

Les conventions sont documentées au plus près du code concerné, notamment dans les README.
La documentation centrale apporte les explications et les exemples.

Une **vue centrale organisée par domaine** référence les conventions et leurs points de
contrôle, sans recopier leur contenu. Elle indique les conventions dont le contrôle reste
à implémenter.

Les points de contrôle sont exécutables sans jugement d’IA. Les vérificateurs spécifiques
au projet sont eux-mêmes testés pour vérifier qu’ils détectent les écarts et acceptent les
cas conformes.

## Évolution

La consolidation fait évoluer le Codebase Quality Control à partir des constats du projet.
Après arbitrage humain, elle ajoute, modifie ou retire des conventions et adapte les points
de contrôle associés.

Les moments d’exécution et les étapes bloquées par ces contrôles sont définis par les autres
briques du cadre AIDE.

Les [commandes de contrôle fournies dans ce dépôt](qualite.md) décrivent l’existant
du socle ; cette page définit la structure à faire vivre dans chaque projet.
