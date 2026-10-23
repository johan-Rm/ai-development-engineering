# Adoption

## Dans un projet existant

1. Lire ses consignes, ses scripts et son workflow Git. Préserver les fichiers existants.
2. Copier la documentation `docs/aiod/` et adapter ses liens. Copier aussi `ia-engineering/`. Compléter les entrées `AGENTS.md`
   et `CLAUDE.md` au lieu de remplacer des consignes existantes.
3. Adapter les cinq couches proposées avec les responsables, puis renseigner la table de routage
   et `codebase-quality-control/scripts/aiod.json`. Les deux doivent décrire les mêmes couches.
4. Installer les scripts et leurs tests ensemble (ou seulement `worktrees.py`, `aiod.json` et `test_worktrees.py` pour le seul outillage Git), puis les exclusions `worktree/` dans les outils
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

## Adopter les applications fournies

1. Partir d’un clone contenant les trois applications, puis suivre [le démarrage](../demarrage.md).
2. Choisir le nom du projet, ses couches utiles et sa stratégie Git. Adapter `codebase-quality-control/scripts/aiod.json`, les responsabilités et les consignes dans `ia-engineering/`.
3. Lire l’inventaire des exemples ci-dessous et [la convention des cartes](../../dev-book/README.md). Les cartes de construction et de maintenance restent dans `dev-book/tasks/`, avec leur statut et leurs preuves historiques.
4. Dans une copie destinée à un nouveau projet, choisir explicitement de conserver ces cartes pour la traçabilité ou de les retirer de cette copie. Conserver les README et créer la première demande propre au projet. Ne pas déplacer les cartes dans `docs/` ni vider automatiquement les cartes d’un projet existant.
5. Remplacer ou conserver explicitement l’exemple Article et la marque Graines Digitales. Adapter ensemble code, tests, OpenAPI, liens et consignes graphiques. Le schéma AIOD reste une illustration de méthode.
6. Exécuter `python3 codebase-quality-control/scripts/quality.py`, puis les parcours navigateur selon [la qualité](../qualite.md). Vérifier la CI avant de commencer les tâches du produit.

Le nettoyage concerne les fichiers de la copie adoptée, pas l’historique Git ni les worktrees du dépôt d’origine. Aucun script ne supprime les données, les `.env` ou les tâches.

## Exemples remplaçables

- L’entité Article, sa migration et les parcours associés dans les trois applications sont une démonstration CRUD.
- Les tests HTTP, le contrat OpenAPI et les parcours Playwright correspondent à cette démonstration : les adapter ensemble lorsqu’elle est remplacée.
- La [charte Graines Digitales](<../../design/Brand Guidelines - Graines Digitales (standalone).html>), le [schéma du cadre](cadre-aiod.html), la [synthèse graphique](charte-graphique.md) et les [sources](sources/README.md) sont les références fournies. Dans le projet adopté, les remplacer ou retirer si elles ne sont pas utilisées, puis adapter les liens et la consigne graphique dans `AGENTS.md`.
- `infra/compose.process.yaml` et le [runbook de recette](../../dev-book/runbooks/recette-aiod.md) vérifient le processus indépendamment de l’application.

La maintenance du cadre relève de devops. Les identifiants BP et les affectations historiques
sont conservés pour la traçabilité ; ils ne définissent aucune couche supplémentaire.
