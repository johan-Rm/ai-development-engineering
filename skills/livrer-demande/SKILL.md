---
name: livrer-demande
description: "Contrôler une demande de développement reconstituée et préparer sa PR avec les preuves finales."
---

# Développement · 06 Livraison

## Entrée

Branche réunissant tous les commits de tâches validées et documentation à jour.

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

Vérifier la complétude face à la demande, les cartes clôturées, les commits et le diff cumulé.
Exécuter les commandes de qualité requises sur l’ensemble à livrer et attendre leurs sorties finales.
Un résultat inconnu ou un échec bloque l’ouverture de PR. Corriger dans le périmètre autorisé ; ne modifier
aucune règle ni aucun contrôle du Codebase Integrity. Si une correction change le résultat validé,
la présenter de nouveau à l’humain avant livraison.
Préparer un titre et un corps de PR décrivant le besoin, le comportement final, les vérifications et limites.
Utiliser l’outil transversal `creer-pr` s’il est disponible et l’ouverture demandée ; sinon fournir le
contenu prêt à relire. Une preuve actuelle couvrant exactement le même HEAD et les mêmes commandes
peut être réutilisée pour éviter un second passage identique. Push et PR suivent les autorisations explicites.
Ne pas merger. Le suivi après fusion appartient à l’outil transversal dédié.

## Sortie et preuve

Dossier de livraison contrôlé ; URL uniquement si la PR a été autorisée et créée, sinon titre et corps prêts.

## Arrêt

Contrôle requis absent, inconnu ou échoué, arbre incomplet ou verdict manquant : exposer ce qui empêche la livraison.
