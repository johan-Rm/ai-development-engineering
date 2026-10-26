---
name: implementer-tache
description: "Implémenter une carte de développement prête avec ses tests, sa documentation et ses preuves avant revue humaine."
---

# Développement · 03 Implémentation

## Entrée

Carte prête, branche et worktree affectés, dépendances présentes par commits, couche disponible.

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

Vérifier Git dans le worktree affecté et lire la carte et les README. Réaliser uniquement le périmètre
confié. Appliquer les conventions existantes ; ne modifier ni conventions techniques ni Codebase Integrity,
configurations, seuils, exceptions ou tests des vérificateurs pour faire passer le changement.
Écrire les tests pertinents et la documentation avant de présenter le résultat. Exécuter les tests et
contrôles concernés jusqu’à obtenir leur état réel. Produire une preuve du comportement correspondant
aux critères, avec commandes, observations et limites. Mettre la carte à jour sans la déclarer validée.
Une correction demandée reprend cette même carte et nécessite de nouvelles preuves.
Ne pas committer ni substituer une suite verte au verdict humain.

## Sortie et preuve

Changement, tests, documentation et preuves reproductibles prêts pour vérification humaine.

## Arrêt

Échec de contrôle, besoin de changement du cadre ou dépassement de périmètre : exposer le constat et attendre la décision nécessaire sans affaiblir le contrôle.
