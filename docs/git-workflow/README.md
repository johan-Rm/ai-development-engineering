# Workflow Git

Documentation du travail avec Git, des contributions isolées à leur intégration.

## Rôle et responsabilités

- Expliquer le modèle de branches et le parcours des contributions.
- Définir les conventions techniques des messages et titres de PR.
- Distinguer les pratiques établies des choix de publication restant à définir.

## Conventions techniques

### Messages de commit

- Utiliser le titre `type(CARTE): changement`.
- Rédiger en français, avec un verbe à l’infinitif et sans point final.
- Décrire précisément le changement.
- Refuser `wip`, `fixup`, `squash` et « corrections diverses » comme titres provisoires.
- Limiter les types à `feat`, `fix`, `docs`, `refactor`, `test`, `perf`, `build`, `ci`, `style` et `chore`.
- Choisir le type selon le changement principal.
- Former le scope avec `API`, `WEB`, `BO`, `UX` ou `OPS`, un tiret et au moins trois chiffres.
- Ajouter une ligne `Demande : DEM-NNN` unique pour chaque commit de carte.
- Réserver `docs(DEM-NNN)` aux traces Markdown de `dev-book/demand/` et `dev-book/tasks/`.
- Faire concorder toute ligne de demande présente avec le scope documentaire.
- Séparer le titre et le corps par une ligne vide.
- Limiter le corps facultatif aux motivations et contraintes utiles.
- Ne pas imposer la syntaxe `!` pour signaler une incompatibilité.
- Exiger des documents référencés uniques et un rattachement cohérent de la carte.
- Préserver les traces de cherry-pick, sans attribution supplémentaire obligatoire.

### Titres de PR

- Exprimer le résultat global en français et terminer par `(DEM-NNN)`.
  Aucun préfixe Conventional Commit imposé.

### Vérification

- Contrôler chaque nouveau commit de la plage à livrer.
- Refuser les messages invalides, références incohérentes et commits de fusion.
- Limiter les scopes documentaires aux chemins autorisés.
- Ne pas appliquer les contrôles rétroactivement aux commits hors plage.
- Interdire tout changement dans `codebase-integrity/` par une contribution de développement.
- Détecter aussi les suppressions, déplacements et changements annulés ensuite.
- Associer chaque correction de consolidation à une convention et à un contrôle ajouté ou renforcé.
- Référencer les conventions existantes sans les recopier.
- Exiger un motif explicite pour une consolidation sans correction de code.
- Ne pas exiger de nouveau contrôle en l’absence de correction de code.
- Refuser les références ambiguës, types contradictoires et changements de type.
- Refuser les contributions mélangeant développement et consolidation.
- Contrôler la contribution avant PR et avant l’applicatif en CI.
- Bloquer la contribution si un contrôle obligatoire échoue.
