# BP-011 — Préparer l’adoption du boilerplate

> Note historique ajoutée lors d’OPS-010 : les mentions de fusion préparée, de fichiers non commités ou d’anciens chemins décrivent l’état lors de cette tâche. Elles ne décrivent pas l’état Git actuel ni un travail restant. Les cartes sont désormais réunies dans `dev-book/tasks/`.

- Statut : réalisée le 2026-10-20.
- Date : 2026-10-20.
- Demande : corriger les cinq points de l’audit après commit de BP-010.
- Mission historique : maintenance du cadre, sur la branche historique de maintenance, worktree principal (chemin obtenu avec `git rev-parse --show-toplevel`).
- Périmètre : documentation, consignes, archivage documentaire, scripts communs, tests de ces scripts et CI. Aucun changement fonctionnel des applications.
- Preuves attendues : tests Python, exécution des contrôles applicatifs disponibles, validation des liens et absence de chemins personnels actifs.

## Critères

- [x] Démarrage commun et chemins portables.
- [x] Consignes opérationnelles dans IA Engineering.
- [x] Historique séparé des tâches du projet et procédure de nettoyage.
- [x] Commandes stables et contrôles automatisés en CI.
- [x] Documentation et preuves mises à jour.

## Livré

- Consignes déplacées vers `ia-engineering/` ; entrées des assistants et liens adaptés.
- Cartes de construction déplacées vers `docs/boilerplate/tasks/`, exemples identifiés et nettoyage d’adoption documenté sans suppression automatique.
- Chemins locaux remplacés par des chemins relatifs dans les guides et par des placeholders dans les archives.
- Commandes communes `apps.py` (installation, lancement, contrôle) et `quality.py` (ensemble des contrôles), avec comparaison du contrat OpenAPI sans écrasement.
- Workflow CI : outillage, contrôles des applications et parcours Chromium. Aucun déploiement ajouté.
- README d’accueil et guides de démarrage/qualité actualisés ; responsabilités des nouveaux dossiers documentées.

## Vérification — 2026-10-20

- BP-010 commité avant les corrections : `995cbcf`.
- `python3 codebase-quality-control/scripts/apps.py install all` : réussi avec accès réseau autorisé, caches temporaires. Aucun verrou de dépendances modifié. Premier essai interrompu par l’absence de résolution réseau du bac à sable ; nouvelle exécution réussie.
- `python3 codebase-quality-control/scripts/quality.py` : code de sortie 0 ; tests outillage, contrat HTTP CRUD avec SQLite temporaire, conteneur Symfony, mapping Doctrine, comparaison OpenAPI, types et builds des deux applications Nuxt.
- `python3 codebase-quality-control/scripts/check.py` après ajout du contrôle de régression OpenAPI : 15 tests réussis. Couvre notamment conservation du `.env`, chemin avec espaces, arrêt après échec et rejet du contrat obsolète sans modification du fichier.
- `npm run test:e2e` dans chaque application Nuxt : 1 test réussi par application, contre l’API locale de développement déjà démarrée ; Chromium et bibliothèques temporaires disponibles dans l’environnement de vérification. Les serveurs locaux existants ont été réutilisés par Playwright.
- Workflow YAML analysé avec succès ; script Bash du parcours validé avec `bash -n`.
- Liens locaux Markdown : aucune cible absente ; aucun chemin personnel absolu ni dépendance aux skills du poste dans les documents Markdown.
- `git diff --check` : réussi.

## Limites

La CI est configurée mais n’a pas été exécutée sur GitHub ; aucun push demandé. La recette Docker existante n’a pas été relancée. Les 11 alertes npm de sévérité élevée déjà documentées restent présentes. Les applications restent exécutées sur l’hôte ; cette tâche n’ajoute pas leur conteneurisation. Les corrections BP-011 sont incluses dans le commit de cette carte.

## Mise en commit — 2026-10-21

Trois tests ciblés de `tests/test_apps.py` réussis ; `git diff --check` réussi. Les preuves applicatives du 2026-10-20 ci-dessus sont conservées comme preuves datées ; aucun nouveau passage complet avant PR.
