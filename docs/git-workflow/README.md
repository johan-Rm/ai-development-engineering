# Workflow Git

Documentation du travail avec Git, des contributions isolées à leur intégration.

## Rôle et responsabilités

- Expliquer le modèle de branches et le parcours des contributions.
- Définir les conventions techniques des messages et titres de PR.
- Distinguer les pratiques établies des choix de publication restant à définir.

## Conventions techniques

### Messages de commit

- Format du titre : `type(CARTE): changement`, en français, verbe à l'infinitif,
  description précise et sans point final. Aucun titre provisoire `wip`, `fixup`
  ou « corrections diverses ».
- Types autorisés : `feat` (fonctionnalité), `fix` (correction), `docs` (documentation),
  `refactor` (réorganisation sans changement de comportement), `test` (tests),
  `perf` (performance), `build` (construction ou dépendances), `ci` (intégration continue),
  `style` (formatage sans changement de comportement), `chore` (autre maintenance).
  Choisir le type selon le changement principal.
- Scope de carte : préfixe `API`, `WEB`, `BO`, `UX` ou `OPS`, tiret et au moins
  trois chiffres. Ligne `Demande : DEM-NNN` obligatoire dans le corps.
- Réserver `docs(DEM-NNN)` aux traces documentaires de la demande entière,
  dans les fichiers Markdown de `dev-book/demand/` et `dev-book/tasks/`.
  La ligne de demande est alors facultative ; si présente, elle concorde avec le scope.
- Séparer titre et corps par une ligne vide. Le paragraphe explicatif est facultatif :
  décrire une motivation ou une contrainte sans recopier les preuves ni l'inventaire
  des fichiers. Expliquer les incompatibilités sans imposer de syntaxe `!`.
- Les documents référencés sont uniques et la carte est rattachée à la demande annoncée.
  Préserver les traces de cherry-pick. Aucune convention d'attribution supplémentaire.

### Titres de PR

- Exprimer le résultat global en français et terminer par `(DEM-NNN)`.
  Aucun préfixe Conventional Commit imposé.

### Vérification

- Contrôler chaque nouveau commit de la plage à livrer : format, références,
  périmètre documentaire des scopes DEM et absence de merges. Les erreurs sont bloquantes.
- Appliquer le contrôle aux nouveaux commits à livrer ; ne pas reprendre ni réécrire
  les commits passés. Aucun mécanisme d’exception historique.
