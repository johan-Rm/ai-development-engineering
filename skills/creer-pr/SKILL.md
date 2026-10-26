---
name: creer-pr
description: "Préparer et ouvrir une PR explicitement demandée à partir de commits validés, après les contrôles requis."
---

# creer-pr

## Conventions du projet

Lire les instructions du projet, la demande ou carte fournie et les README applicables.
Résoudre les chemins, couches, branches, commandes de tests et qualité depuis le projet ;
annoncer les valeurs utilisées et les inconnues, sans imposer de valeurs personnelles.
Avant une écriture, confirmer le worktree absolu, la branche autorisée et la disponibilité de la couche.
Préserver les modifications préexistantes et les `.env`. Ne pas utiliser stash, reset --hard,
force-push ou suppression de worktree pour résoudre une situation. Ne pas rebaser une branche occupée.
Commit, push, PR et merge nécessitent l’autorisation prévue par le projet ; une invocation d’étape
ne les autorise pas implicitement. Les autorisations explicites déjà données restent valables.
Ne pas déléguer sans autorisation. Ne pas enchaîner automatiquement une autre étape.

## Procédure

Entrée : branche source, cible et commits de tâches validées ; demande d’ouverture pour agir à distance.
Vérifier le worktree, l’état Git, les cartes et le diff cumulé par rapport à la cible réellement retenue.
Refuser de livrer des fichiers non commités ; distinguer les contributions multi-couches autorisées
sans exiger artificiellement une seule couche. Vérifier les contrats générés et la documentation.
Exécuter tous les contrôles requis ou lire leurs preuves actuelles pour le même HEAD et environnement.
Attendre les résultats ; ne jamais ouvrir avec un contrôle requis échoué ou inconnu.
Présenter titre et corps conformes au template du projet : besoin, comportement, preuves et limites.
Si push et ouverture sont autorisés, utiliser le connecteur disponible ou gh authentifié avec le corps
dans un fichier passé par --body-file. Ne pas exposer de secrets ni forcer un push.
Sans accès ou autorisation, fournir le contenu prêt à relire et signaler que la PR n’a pas été créée.
Sortie et preuve : cible, source, contrôles, SHA livré et URL réellement obtenue, ou contenu préparé.
Arrêt : arbre incomplet, carte non validée ou contrôle requis non réussi.
La stratégie de fusion vient du projet et de sa politique distante ; ne pas supposer un squash ou rebase.
Ne pas merger ni supprimer les branches. Ce skill ne déclenche aucune boucle.
