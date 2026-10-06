# Principes

AIOD signifie **AI-Orchestrated Development**. L’humain cadre et valide ; les assistants
travaillent dans des responsabilités explicites, produisent des preuves et livrent des changements relisibles.

## Quatre piliers

- **Architecture** : une couche rassemble un périmètre, une branche et un préfixe de tâches.
  Le nombre de couches suit le projet ; une seule peut suffire.
- **Isolation** : chaque écrivain actif a son dossier Git. Si des services existent, leurs ports,
  données et fichiers générés doivent aussi être isolés. Docker est une option selon la stack.
- **Cycle IA** : cadrer la demande, affecter les tâches, réaliser, prouver, valider et intégrer.
  Une tâche produit un commit avec ses tests pertinents, sa documentation et sa carte.
- **Consolidation** : une session explicitement demandée transforme les répétitions et défauts
  observés en conventions, améliorations et contrôles.

## Adaptations aux documents d’origine

Le carrousel illustre une installation avec Docker, des vhosts et plusieurs sous-agents.
Ce blueprint fonctionne aussi sans services et avec un seul assistant.

Un worktree propre peut être occupé par une mission : sa disponibilité se vérifie auprès du
coordinateur et des affectations, pas seulement avec `git status`. Les frontières d’écriture
restent des consignes ; Git ne les impose pas mécaniquement et aucun verrou distribué n’est fourni.

Les tests pertinents et la documentation voyagent avec chaque tâche. La passe de contrôles
avant PR vérifie ensuite l’ensemble. Une preuve visible complète les tests selon le besoin.

Une demande transversale peut réunir des commits identifiés sur une branche de preview, créée
pour cette demande. Le rebase d’une branche seule ne rassemble pas plusieurs branches.
La stratégie de réunion doit être choisie explicitement, puis testée.

La relecture humaine couvre le comportement, les changements et leurs risques ; la consolidation
ultérieure ne remplace pas cette relecture.
