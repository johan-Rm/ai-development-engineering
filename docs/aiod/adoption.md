# Adoption

## Dans un projet existant

1. Lire ses consignes, ses scripts et son workflow Git. Préserver les fichiers existants.
2. Copier la documentation `docs/aiod/` et adapter ses liens. Compléter les entrées `AGENTS.md`
   et `CLAUDE.md` au lieu de remplacer des consignes existantes.
3. Adapter les cinq couches proposées avec les responsables, puis renseigner la table de routage
   et `scripts/aiod.json`. Les deux doivent décrire les mêmes couches.
4. Installer `scripts/worktrees.py`, ses tests et les exclusions `worktree/` dans les outils
   réellement présents : recherche, tests, lint, types, formatage et build.
5. Adapter les commandes de qualité et la stratégie Git aux scripts et branches du projet.
6. Affecter une première tâche avant de créer son worktree et vérifier son résultat.

Le dépôt doit déjà avoir un premier commit pour créer des worktrees. Le blueprint ne remplace
ni l’architecture du produit ni sa configuration de développement.

## Dans un projet nouveau

Créer le socle documentaire, définir le besoin et l’architecture minimale, puis initialiser Git
et créer le premier commit avec une autorisation explicite. Définir ensuite les couches.
Les dossiers vides ne sont pas suivis par Git : les créer au moment de leur premier usage.

## Indépendance des outils

Les procédures sont lisibles sans commande slash ou skill installé sur le poste de l’auteur.
Le lecteur peut les suivre manuellement avec Git et Python 3. Adapter les profils au client IA
utilisé ; un profil Claude ne constitue pas une configuration Codex.

Les sources sont conservées pour comprendre la démarche ; elles ne sont pas nécessaires
à l’exécution des scripts. Aucune licence de redistribution n’a encore été choisie.
