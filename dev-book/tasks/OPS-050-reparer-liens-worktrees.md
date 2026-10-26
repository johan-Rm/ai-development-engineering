# OPS-050 — Réparer les liens Git des cinq worktrees

- État : implémentée et commitée, à vérifier.
- Date : 2026-10-26.
- Demande d’origine : [DEM-005](../demand/DEM-005-dockeriser-applications-worktrees.md).
- Couche : devops.
- Session : référence de session indisponible ; mission confiée dans ce chat.
- Worktree : `worktree/devops`, relatif à la racine du dépôt principal.
- Branche : `layers/devops` ; conserver la branche existante, sans rebase.

Le chemin absolu du worktree sera résolu et vérifié avant exécution. Les liens Git
obsolètes empêchent actuellement les commandes ordinaires ; le découpage a vérifié
la branche et l’état via le gitdir réel. Lire les README applicables avant toute écriture.

## Objectif et chemins autorisés

Rendre les cinq worktrees API, web, backoffice, design et devops utilisables à leur
emplacement actuel, sans déplacer les branches ni modifier leur contenu.
Périmètre : métadonnées Git locales de liaison des cinq worktrees ; cette carte et
`dev-book/runbooks/reparer-liens-worktrees.md` dans le worktree devops.
Les chemins absolus sont à résoudre depuis le dépôt principal au moment de l’intervention.

## Dépendances par commit

Base locale observée de `layers/devops` : `ffd216fb6997f8e8e78a4e89b153c8b02653a780`.
Aucune dépendance amont d’implémentation. La demande confirmée existe sans commit dans
ce worktree ; son éventuel commit relève d’une autorisation distincte.

## Critères d’acceptation

- Inventorier avant intervention branches, HEAD, modifications, liens et fichiers locaux
  à préserver, dont les `.env`, sans publier leurs secrets.
- Réparer uniquement les liens cassés ; `git -C <worktree> status --short --branch`
  et `git worktree list --porcelain` reconnaissent les cinq emplacements actuels.
- Les HEAD, branches, modifications et fichiers locaux préexistants sont conservés.
- Toute occupation ou incohérence nouvelle arrête l’intervention concernée et est signalée.

## Tests, documentation et preuve

Comparer les états avant/après et les destinations réelles des liens ; exécuter les
commandes Git ordinaires dans les cinq arbres. Documenter préconditions, méthode,
vérifications et retour arrière des seules métadonnées modifiées dans le runbook.
Ne pas écrire un test qui exigerait de casser les vrais worktrees.

## Exclusions

Aucune synchronisation, suppression, création ou rebase de branche/worktree ; aucun
changement de code, démarrage Docker, copie de secrets ou nettoyage des données.

## Réalisation et preuves

2026-10-26 : inventaire local avant intervention, puis `git worktree repair` avec
les cinq chemins absolus actuels. Les cinq fichiers `.git` et leurs backlinks ont été
réparés. Les commandes Git ordinaires fonctionnent dans chacun des arbres.
Comparaison automatisée avant/après : HEAD, branche, état porcelain, diff HEAD et
empreintes des `.env` présents inchangés pour les cinq couches. Les deux `.env`
observés (API et devops) sont préservés, sans publier leurs valeurs.
Les quatre documents non suivis DEM-005/OPS-050/051/052 de devops sont conservés.
Aucune branche déplacée, aucun service démarré ni fichier applicatif modifié.
Le runbook `dev-book/runbooks/reparer-liens-worktrees.md` conserve la procédure.
La réparation locale n’est pas transmissible par commit : ce commit conserve uniquement
la demande, la procédure et la preuve. Le SHA se lit dans l’historique de cette carte.
