# Conventions techniques et domaines

> Une convention technique formule une exigence du projet avant qu’un point de contrôle vérifie son application.

## Définir une convention technique

Chaque convention technique précise la règle attendue, son périmètre et ses exceptions justifiées. Elle est arbitrée par l’humain et documentée dans le chapitre `Conventions techniques` du README concerné.

L’état de vérification est explicite : **point de contrôle implémenté** ou **à implémenter**. Une convention technique écrite n’est pas encore un contrôle automatisé.

## Classer par domaine

Chaque convention technique appartient à un seul domaine. Le classement proposé couvre :

| Domaine | Domaine | Domaine |
| --- | --- | --- |
| Règles métier | Données | Authentification et autorisations |
| Intégrations et échanges | Contrats et compatibilité | Parcours utilisateur |
| Interface et internationalisation | Accessibilité | Rendu visuel |
| Architecture et dépendances | Qualité du code | Sécurité |
| Performance et robustesse | Construction et livraison | Fiabilité des vérifications |

## Référencer sans dupliquer

Une vue centrale propre au projet relie chaque convention technique à son README source, à son domaine et à ses points de contrôle. Elle rend visibles les contrôles manquants sans recopier les règles locales.

L’ajout ou la modification d’une convention technique passe par la [consolidation](../04-consolidation-loop/index.md).
