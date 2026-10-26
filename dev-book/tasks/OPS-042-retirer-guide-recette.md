# TASK OPS-042 — Retirer le guide de recette demandé

- **Créée le** : 2026-10-24.
- **Session** : non disponible (Codex).
- **Statut** : ✅ fait le 2026-10-24.
- **Type** : docs.
- **Tests** : sans objet — suppression documentaire sans code exécutable ; contrôle des liens remplacés et `git diff --check`.
- **Mission** : devops, `layers/devops`, `/home/johan/www/lab/ai-orchestrated-development/worktree/devops`.
- **Dépendances par commit** : base `bd95c1c` ; aucune autre dépendance.
- **Demande** : suppression explicite du guide, puis commit distinct autorisé par l’utilisateur.

## Contexte et périmètre

Retirer `dev-book/runbooks/recette-aiod.md` et remplacer ses trois liens actifs
par la documentation d’infrastructure dans `AGENTS.md`, `SETUP.md` et
`docs/02-cadre/couches.md`.

## Hors périmètre

Outillage, configuration, applications, cartes historiques et ressources Docker.

## Décisions de cadrage

Carte rédigée après réalisation, à la mise en commit : la suppression avait été
demandée directement, sans passage préalable par `creer-tache`. Écart de processus
explicite, sans reconstitution fictive d’un cadrage antérieur.

## Vérification

- Guide absent ; trois liens actifs remplacés par des chemins existants vers `infra/README.md`.
- Aucune référence au guide dans `AGENTS.md`, `SETUP.md` et `docs/`.
- `git diff --check` réussi ; aucun code exécutable modifié.

## Documentation impactée et livré

Suppression du guide ; consignes, installation et documentation des couches
actualisées ; présente carte clôturée dans le même commit.

## Définition de terminé

- [x] Guide supprimé et liens actifs corrigés.
- [x] Diff documentaire relu et contrôle des espaces réussi.

## Reste à faire (hors périmètre)

Séparation des configurations à cadrer dans une carte distincte.
