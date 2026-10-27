# UX-001 — Clarifier les responsabilités du dossier design

- État : implémentée et commitée, à vérifier.
- Date : 2026-10-27.
- Demande : [DEM-006](../demand/DEM-006-clarifier-responsabilites-dossiers-cadre.md).
- Couche : design.
- Worktree : `worktree/design`, relatif à la racine du dépôt principal.
- Branche : `layers/design` ; branche existante conservée.
- Session : référence de session indisponible ; mission définie dans ce chat.
- Base locale vérifiée : `779ce88da0a8e1945061cd2805bd0005ce01c13b` ; aucun fetch.

Le chemin absolu du worktree est résolu localement et sa branche, son état et sa
 disponibilité sont revérifiés avant exécution. Aucune délégation n’est autorisée.

## Objectif et chemins autorisés

Réécrire uniquement `design/README.md` : références visuelles, maquettes, prototypes,
références graphiques et vérification visuelle des parcours ; préciser que les composants
applicatifs sont implémentés dans les couches web et backoffice.
La présente carte peut recevoir les preuves et le verdict à l’étape correspondante.

## Exclusions

Aucun changement graphique, maquette, charte, composant, application ou autre README.
Aucune nouvelle convention technique.

## Dépendances et transmission

Base locale commune déjà présente dans layers/design. Aucun commit technique amont.
DEM-006 et cette carte sont actuellement rédigés seulement dans worktree/devops.
Un commit documentaire contenant le cadrage et la carte doit être identifié puis
transmis par une opération Git autorisée avant démarrage dans design ; SHA absent,
mission non prête. Ne pas copier les fichiers non commités depuis devops.
La branche design est préparée mais aucune implémentation ni transmission n’est faite ici.
La carte n’a pas de dépendance fonctionnelle avec OPS-054.

## Critères et preuve

Description courte et non exhaustive ; seules rubriques « Rôle et responsabilités »
et « Conventions techniques », cette dernière vide. Responsabilités et limite avec
les couches consommatrices conformes à DEM-006.
Relire le diff, vérifier les éventuels liens et exécuter `git diff --check` depuis
design ; consigner le SHA de transmission et le résultat dans cette carte.
Aucun rendu graphique ni test applicatif requis pour ce texte seul.

## Contraintes communes

Lire AGENTS.md, les couches, la demande et les README applicables avant écriture.
Préserver le travail existant et les `.env`. Aucun changement sur develop ou master,
aucun rebase implicite, aucun déploiement. Ne pas affaiblir les conventions ou contrôles.
Les README simplifiés ont une description courte, puis uniquement
« Rôle et responsabilités » et « Conventions techniques », cette dernière rubrique vide.
Ne pas ajouter de tests qui reproduisent seulement le texte documentaire.
La validation humaine et la livraison restent des étapes distinctes.

## Réalisation et verdict

Réalisée le 2026-10-27 dans worktree/design après vérification de layers/design propre.
Cadrage transmis depuis OPS-053 `56c8a954cc5ad2073b336e7d73b6622ebfcdb87f`
par cherry-pick local `8dafce6`. Aucune copie de fichiers non commités.
README conforme à la proposition retenue : texte non exhaustif, deux rubriques,
conventions vides et limite avec les couches web/backoffice. Aucun lien à vérifier.
Relecture du diff et `git diff --check` : réussis. Aucun test applicatif requis.
Aucun verdict humain à ce stade.
