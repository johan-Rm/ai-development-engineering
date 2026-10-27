# OPS-014 — Préparer la branche master

- **Créée le** : 2026-10-05.
- **Session** : non disponible (Codex).
- **Statut** : clôturée le 2026-10-06.
- **Type** : outillage.
- **Tests** : contrôles Git locaux et relance sans perte ; les tests de l’outil sont exécutés
  si celui-ci change. Aucun test applicatif : aucun code applicatif produit.
- **Réf** : OPS-013 : cadrage de la gouvernance validé ; `docs/aiod/couches.md`, `docs/aiod/gouvernance.md`.
- **Rattachement** : maintenance du cadre, sur la branche historique de maintenance, préfixe BP.
- **Dossier de coordination** : `.`.
- **Affectation d’exécution** : non attribuée ; à vérifier au démarrage.

## Contexte

Les cinq couches sont définies mais leurs worktrees n’existent pas. Le dépôt ne possède pour
l’instant que `main` et la branche historique de maintenance. L’utilisateur demande une tâche d’initialisation
pour chaque couche, ainsi que les branches `master` et `develop`.

## Périmètre

Créer ou réutiliser `master` comme branche de référence publique à partir du commit local
actuellement porté par `main` (`9a60e1c5b6908f1c87fa3c2264fad778ba5f583a` à ce cadrage).
Vérifier le SHA au démarrage et consigner toute évolution avant de choisir la base.

## Décisions de cadrage

`master` porte la référence publique ; `develop` portera l’intégration. Conserver `main`
comme référence historique pendant la transition, sans suppression ni changement de branche
du worktree principal. Aucun worktree permanent master n’est nécessaire. La branche par défaut
GitHub n’est pas modifiée dans cette tâche.

## Règles et cas limites

Préserver tous les fichiers et missions actifs. Réutiliser les références et worktrees compatibles ;
refuser un dossier occupé, un lien symbolique ou une branche inattendue. Ne pas stasher, supprimer,
réinitialiser ou forcer un push. Un arbre propre ne prouve pas une couche libre.

## Hors périmètre

Installation de framework, services, secrets, DNS réel, déploiement, push et PR.
La stack et l’exemple applicatif seront définis séparément ; ils ne bloquent pas le socle Git.

## Documentation impactée

`docs/aiod/gouvernance.md`, `docs/aiod/git-workflow.md` : rôle de master et transition depuis main.

## Définition de terminé

- [x] `refs/heads/master` existe sur la base explicitement choisie.
- [x] Une référence master préexistante divergente est signalée, sans déplacement forcé.
- [x] La branche courante et les modifications ouvertes restent intactes.
- [x] La documentation distingue master, develop et main conservée temporairement.
- [x] Les commandes, chemins absolus et SHA observés sont consignés dans la carte.
- [x] Le travail préexistant reste intact ; aucun accès distant ou déploiement n’a lieu.

## Première étape d’implémentation

Lire les références Git, l’état des arbres et les missions ; vérifier la base prévue avant création.

## Preuves et livraison

Observation du 2026-10-06 : `refs/heads/master` créée sur
`9a60e1c5b6908f1c87fa3c2264fad778ba5f583a`. La branche courante reste la branche historique de maintenance ;
aucun fichier ouvert n’a été déplacé ou écrasé. `main` est conservée.
La documentation durable indique master comme référence publique et la transition depuis main.

 Une tâche, un commit demandé explicitement, avec sa carte
clôturée et sa documentation. Les opérations Git locales sont prouvées par les références,
branches et chemins observés ; leur simple présence dans la carte n’est pas une exécution.
