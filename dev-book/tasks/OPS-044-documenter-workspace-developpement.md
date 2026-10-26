# TASK OPS-044 — Documenter le workspace de développement

- **Créée le** : 2026-10-26.
- **Statut** : clôturée — ✅ fait le 2026-10-26.
- **Type** : docs.
- **Couche** : devops.
- **Session** : non disponible (Codex).
- **Mission** : `layers/devops`, `worktree/devops`.
- **Demande d’origine** : échange du 2026-10-26 ; intégrer le workspace au projet, documenter son rôle dans la boucle de développement et son installation, puis créer la carte et committer.
- **Dépendances par commit** : base locale `a100043dcc7bc0ebca7c44296b4c3b7b46c8ea34` ; aucune dépendance au travail non commité d’une autre mission.
- **Tests** : sans objet — documentation et configuration déclarative VS Code, aucun code exécutable ajouté. Vérifications ponctuelles du JSON, des chemins et des liens documentaires.

## Contexte et décisions

Le workspace était conservé hors du dépôt avec des chemins relatifs à son ancien
emplacement. Le placer à la racine du dépôt principal permet de partager la vue des
couches et de préparer l’environnement de la boucle de développement.
La carte est formalisée après réalisation, à la demande explicite de l’utilisateur ;
elle ne constitue pas un cadrage préalable. L’utilisateur a validé le résultat
présenté avant de demander ce commit.

## Périmètre et exclusions

Chemins autorisés : `aide.code-workspace`, `SETUP.md`,
`docs/02-cadre/couches.md`, `docs/03-developpement-loop/index.md` et présente carte.
Aucun changement des scripts, services, applications ou règles du Codebase Integrity.
La carte OPS-043 préexistante reste intacte et hors commit.
L’alias personnel et le workspace local du dépôt principal ne sont pas inclus dans
les opérations Git de cette mission. Aucun push, PR ou merge demandé.

## Livré

- `aide.code-workspace` : dépôt principal et cinq couches, chemins relatifs,
  exclusions de recherche, détection Git et confirmation sur branches protégées.
- `SETUP.md` : prérequis, création des worktrees manquants, ouverture et alias personnel.
- `docs/02-cadre/couches.md` : utilisation du workspace aux étapes de la boucle,
  vérification du répertoire et de la branche avant écriture, limites de l’isolation.
- `docs/03-developpement-loop/index.md` : accès aux guides de préparation et d’utilisation.

## Vérification

Preuves du 2026-10-26 :

- `git branch --show-current` : `layers/devops`.
- Numérotation vérifiée sur les cartes des branches locales et références distantes
  disponibles, ainsi que les cartes locales non suivies : OPS-044 disponible.
- Lecture par `json.loads` : JSON valide ; les six dossiers existent lorsque les
  chemins sont résolus depuis le dépôt principal, emplacement prévu du workspace.
- Résolution des liens Markdown locaux des trois guides : cibles présentes.
- `git diff --check` et `git diff --cached --check` : aucune erreur.
- Aucun lancement de VS Code ni validation visuelle de son interface ; les contrôles
  portent sur la configuration et les chemins. Les gates complètes restent pour la PR.

## Définition de terminé

- [x] Workspace partageable sans chemin personnel absolu.
- [x] Installation et rôle dans la boucle documentés.
- [x] Configuration, dossiers et liens locaux vérifiés.
- [x] Carte, configuration et documentation réunies dans un commit unique.

## Reste à faire (hors périmètre)

La carte OPS-043 reste prête à implémenter. Livraison distante et intégration non demandées.
