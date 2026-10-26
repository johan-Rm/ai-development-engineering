# OPS-015 — Préparer la branche develop

- **Créée le** : 2026-10-05.
- **Session** : non disponible (Codex).
- **Statut** : clôturée le 2026-10-06.
- **Type** : outillage.
- **Tests** : contrôles Git locaux et relance sans perte ; les tests de l’outil sont exécutés
  si celui-ci change. Aucun test applicatif : aucun code applicatif produit.
- **Réf** : OPS-014 ; OPS-013 validée et commitée avant intégration du blueprint ; `docs/aiod/couches.md`, `docs/aiod/gouvernance.md`.
- **Rattachement** : maintenance du cadre, sur la branche historique de maintenance, préfixe BP.
- **Dossier de coordination** : `.`.
- **Affectation d’exécution** : non attribuée ; à vérifier au démarrage.

## Contexte

Les cinq couches sont définies mais leurs worktrees n’existent pas. Le dépôt ne possède pour
l’instant que `main` et la branche historique de maintenance. L’utilisateur demande une tâche d’initialisation
pour chaque couche, ainsi que les branches `master` et `develop`.

## Périmètre

Créer ou réutiliser `develop` depuis `master`, puis intégrer le commit validé de OPS-013
par SHA identifié. Rendre disponibles sur develop les scripts, la configuration des cinq couches
et les consignes nécessaires aux futurs worktrees.

## Décisions de cadrage

`develop` devient la base explicite des cinq couches. La réunion se fait avec le commit
validé de OPS-013, jamais par copie du travail non commité. Maintenir l’arbre principal sur
la branche historique de maintenance. Si un checkout est nécessaire, utiliser un worktree d’intégration temporaire
vérifié plutôt que basculer un arbre modifié. Un arbre temporaire reste inventorié jusqu’à
une décision explicite de retrait.

## Règles et cas limites

Préserver tous les fichiers et missions actifs. Réutiliser les références et worktrees compatibles ;
refuser un dossier occupé, un lien symbolique ou une branche inattendue. Ne pas stasher, supprimer,
réinitialiser ou forcer un push. Un arbre propre ne prouve pas une couche libre.

## Hors périmètre

Installation de framework, services, secrets, DNS réel, déploiement, push et PR.
La stack et l’exemple applicatif seront définis séparément ; ils ne bloquent pas le socle Git.

## Documentation impactée

`docs/aiod/gouvernance.md`, `docs/aiod/git-workflow.md`, `docs/aiod/premiere-tache.md`, `worktree/README.md` : remplacement opérationnel de main par develop.

## Définition de terminé

- [x] `refs/heads/develop` existe et contient le commit validé du blueprint.
- [x] Les scripts et la configuration nécessaires sont présents dans l’arbre develop.
- [x] Les consignes donnent develop comme intégration/base, master comme référence publique.
- [x] Les exemples de recette, commandes de création et worktree/README.md utilisent develop.
- [x] Les contrôles du blueprint passent sur le contenu intégré.
- [x] Les cinq tâches aval disposent d’une base contenant réellement l’outillage.
- [x] Les commandes, chemins absolus et SHA observés sont consignés dans la carte.
- [x] Le travail préexistant reste intact ; aucun accès distant ou déploiement n’a lieu.

## Première étape d’implémentation

Vérifier master et le SHA commité de OPS-013 ; arrêter si OPS-013 est encore non commitée.

## Preuves et livraison

Preuve du 2026-10-06 : develop a été créée depuis master puis avancée sans force par fetch local vers `0a11fa5`, contenant OPS-013 (`8dc7c36`). Les exemples et la gouvernance utilisent désormais develop. Les tests Git du blueprint passent. Le commit de documentation de cette tâche sera également intégré par avance rapide locale. Une tâche, un commit demandé explicitement, avec sa carte
clôturée et sa documentation. Les opérations Git locales sont prouvées par les références,
branches et chemins observés ; leur simple présence dans la carte n’est pas une exécution.
