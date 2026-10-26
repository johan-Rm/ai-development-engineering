---
name: commit-tache
description: "Clôturer une carte validée et créer son commit distinct, sur demande, dans l’une ou l’autre boucle AIDE."
---

# commit-tache

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

Entrée : carte implémentée, verdict humain explicite et demande de commit.
Vérifier branche et worktree ; refuser l’intégration et la production. Lire le diff réel, l’index
et les fichiers non suivis ; distinguer les tâches et préserver les changements étrangers.
Vérifier les critères, preuves, tests pertinents et documentation déjà réalisés avant revue humaine.
Ne pas imposer de nouveau test qui répète l’implémentation ; toute exemption doit être motivée.
Clôturer la carte avec date réelle, livraison et preuves, dans le même commit que ses changements.
Indexer les fichiers explicites de cette seule tâche puis relire intégralement le diff indexé.
Un index contenant un travail étranger bloque le commit ; ne pas modifier cet index sans coordination.
Créer un commit selon la convention du projet et vérifier son contenu et le travail restant.
Sortie et preuve : SHA, carte clôturée, résumé du contenu et état Git observé.
Arrêt : verdict, preuve ou critère manquant ; ne pas committer une tâche incomplète.
Aucun push ni PR ; aucun lien obligatoire vers une boucle particulière.
