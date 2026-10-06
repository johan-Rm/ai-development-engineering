# Travail parallèle

Un worktree isole les fichiers et la branche. Il ne verrouille pas une mission et n’isole pas
les ports, bases ou services extérieurs. Un arbre propre n’est pas une couche disponible.

`python3 scripts/worktrees.py list` affiche les branches et l’état Git, pas les affectations.
Le coordinateur vérifie qui travaille avant d’attribuer la couche.

Le créateur découvre les arbres enregistrés par Git, réutilise une branche déjà sortie,
et place les nouveaux arbres sous `worktree/` du dépôt principal, même s’il est appelé depuis
un arbre secondaire. Il ne copie aucun `.env`, ne démarre aucun service et ne synchronise pas le remote.

Si des services sont ajoutés, définir des identifiants stables par couche et une identité de projet,
puis isoler ports, volumes, bases, caches et destinations d’écriture. Vérifier deux environnements
réels avant d’annoncer leur isolation. Aucun service n’existe dans ce blueprint.

Les exclusions Git et de recherche sont fournies. Le contrôle Python cible explicitement `tests/`
et les sources de l’arbre courant ; il ne descend pas dans `worktree/`.
Chaque outil ajouté ensuite doit appliquer cette même exclusion.

## Préparer l’exemple concret

Pour chacune des cinq couches, définir ensuite le runtime, les commandes de démarrage,
les dépendances, les ports et les données. Pour web, préciser aussi le choix de cible et la
destination des builds. Devops documentera les domaines et l’infrastructure sans intégrer
de credentials. Le créateur actuel prépare uniquement les worktrees Git.
