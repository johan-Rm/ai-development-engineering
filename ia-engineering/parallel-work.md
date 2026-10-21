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
réels avant d’annoncer leur isolation. Le blueprint propose uniquement des conteneurs témoins pour sa recette de processus.

Les exclusions Git et de recherche sont fournies. Le contrôle Python cible explicitement `tests/`
et les sources de l’arbre courant ; il ne descend pas dans `worktree/`.
Chaque outil ajouté ensuite doit appliquer cette même exclusion.

## Préparer l’exemple concret

L’arbitrage est de tester le processus AIOD sans stack produit. Chaque couche reçoit un
conteneur témoin BusyBox, son port, son réseau et son volume. Les identifiants stables sont
1 backoffice, 2 API, 3 web, 4 devops et 5 design ; les ports partent de la base 18100.
Les noms incluent l’identité du dépôt et la couche. Les ports de deux clones doivent être
configurés sur des bases différentes pour exécuter les mêmes couches sur le même hôte.

Le créateur prépare uniquement Git. Depuis une couche, `python3 scripts/process.py up`
lance la recette ; `down` arrête les conteneurs en conservant les volumes.
Les artefacts locaux sont exclus de Git, de la recherche et du contexte de build.
La [procédure de recette](../dev-book/runbooks/recette-aiod.md) détaille les preuves.
