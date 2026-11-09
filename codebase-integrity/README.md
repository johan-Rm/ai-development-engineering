# Codebase Integrity

Les outils qui vérifient les conventions techniques du projet de manière déterministe, sans jugement d’IA à l’exécution.

[Commandes et préconditions](../docs/git-workflow/regles-de-pr.md#exécuter-les-contrôles).

## Rôle et responsabilités

- Fournir les contrôles des conventions techniques et leurs configurations.
- Tester les vérificateurs pour détecter les écarts et accepter les cas conformes.
- Rendre visibles les conventions techniques encore dépourvues de contrôle.
- Préparer et vérifier les environnements de travail isolés.
- Piloter l’installation, le lancement et la vérification des applications.

## Conventions techniques

- Utiliser le dépôt du script comme référence, sans parcourir les worktrees imbriqués.
- Lire les configurations depuis la copie de travail appelante.
- Résoudre les applications sous `apps/` si cet emplacement existe dans la racine
  sélectionnée, sinon sous `app/` ; ne pas revenir à `app/` si `apps/` est incomplet.
- Lire les couches dans `infra/config/layers.json` et les témoins dans `infra/process-check.json`.
- Contrôler les objets Git de la base et de la tête explicitement désignées.
- Charger le vérificateur et ses dépendances depuis la base d’intégration.
- Refuser une base invalide, un historique incomplet ou une plage vide.
- Limiter l’amorçage au périmètre configuré et au contenu d’un commit explicitement approuvé.
- Refuser les branches et SHA abrégés comme approbation d’amorçage.
- Utiliser exclusivement le vérificateur intégré dès qu’il existe dans la base.
- Exécuter le contrôle de contribution avant le code applicatif en CI.
- Bloquer le job applicatif si le contrôle de contribution échoue.
