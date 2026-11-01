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

Le contrôle des [contributions](../docs/git-workflow/README.md#vérification)
se lance avant PR depuis la copie contenant le candidat commité :

```sh
python3 codebase-integrity/scripts/contribution.py --repo . --base develop --head HEAD
```

La base doit être le SHA d’intégration vérifié ; le nom `develop` ci-dessus est
un exemple local. Historique complet et Git/Python sont requis, sans Docker ni
remote pendant le contrôle. Le lanceur extrait uniquement le vérificateur et
ses dépendances depuis cette base, puis lit le dépôt candidat comme données.
Une base absente, un vérificateur absent/non régulier ou une plage vide échouent,
sans repli sur la version candidate. La commande ne contrôle pas les fichiers
non commités. `quality.py --commit-base <base> --commit-head <tête>` l’exécute
avant les autres contrôles ; sans base, la qualité locale n’est pas une preuve
de conformité de contribution.

La CI sépare ce contrôle de l’exécution applicative par deux jobs dépendants.
Les tests de la version candidate restent exécutés par `check.py`.
Le statut `Contribution de confiance` et le workflow doivent être protégés
sur GitHub : le chargement depuis la base ne protège pas un workflow supprimé
ou neutralisé. Aucune configuration distante n’est prouvée par les tests locaux.
Lors de la première installation, l’absence du vérificateur dans la base est
un blocage d’amorçage à traiter explicitement à la livraison, sans exception
automatique ni faux succès.
