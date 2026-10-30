# Codebase Integrity

Les outils qui vérifient les conventions techniques du projet de manière déterministe, sans jugement d’IA à l’exécution.

## Rôle et responsabilités

- Fournir les contrôles des conventions techniques et leurs configurations.
- Tester les vérificateurs pour détecter les écarts et accepter les cas conformes.
- Rendre visibles les conventions techniques encore dépourvues de contrôle.
- Préparer et vérifier les environnements de travail isolés.
- Piloter l’installation, le lancement et la vérification des applications.

## Conventions techniques

Les outils utilisent la configuration de leur copie de travail.

- Utiliser le dépôt du script comme référence, sans parcourir les worktrees imbriqués.
- `worktrees.py` lit `infra/config/layers.json` ; `process.py` lit aussi `infra/process-check.json`.
  Appliquer les [conventions d’infrastructure](../infra/README.md#configuration-des-couches).
