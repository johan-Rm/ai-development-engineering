# Réparer les liens des worktrees déplacés

## Objectif et préconditions

Rétablir les liens d’un dépôt déplacé et de ses worktrees existants sans changer
leurs branches ou leurs fichiers. Coordonner les couches avant intervention.
Depuis la racine du dépôt principal, résoudre les chemins absolus des cinq arbres.
Vérifier leur existence et les fichiers `.git`, ainsi que les backlinks `gitdir`
sous le répertoire Git commun. Ne pas recréer un worktree par-dessus un dossier existant.

## Étapes

1. Conserver localement les liens avant intervention. Relever HEAD, branche, état,
   diff et empreintes des fichiers locaux à préserver, sans publier les secrets.
   Si le lien `.git` est cassé, utiliser temporairement `git --git-dir=<gitdir-réel>
   --work-tree=<worktree-absolu> status --short --branch` pour l’inventaire.
2. Depuis le dépôt principal, exécuter `git worktree repair <chemin-absolu-api>
   <chemin-absolu-web> <chemin-absolu-backoffice> <chemin-absolu-design>
   <chemin-absolu-devops>`. Fournir uniquement les arbres existants et identifiés.
3. Vérifier `git worktree list --porcelain` puis, dans chacun des cinq arbres,
   `git status --short --branch` et `git rev-parse HEAD` avec les commandes ordinaires.
4. Comparer l’inventaire avant/après : aucune branche, HEAD, modification ou donnée
   locale ne doit avoir changé. Consigner la preuve dans la carte de l’intervention.

## Arrêt et retour arrière

Arrêter si un dossier manque, si un arbre est occupé ou si une branche diffère de
l’inventaire. Ne pas utiliser prune, reset, stash, remove ou rebase pour réparer les liens.
En cas d’erreur de liaison identifiée, restaurer seulement les fichiers de métadonnées
sauvegardés, après vérification qu’aucune autre opération Git n’a eu lieu. Ne restaurer
ni index, ni source, ni données applicatives pour résoudre une erreur de chemin.
