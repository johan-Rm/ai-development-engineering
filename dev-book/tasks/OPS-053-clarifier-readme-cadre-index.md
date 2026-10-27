# OPS-053 — Clarifier les README du cadre et la hiérarchie documentaire

- État : validée ; non livrée.
- Date : 2026-10-27.
- Demande : [DEM-006](../demand/DEM-006-clarifier-responsabilites-dossiers-cadre.md).
- Couche : devops.
- Worktree : `worktree/devops`, relatif à la racine du dépôt principal.
- Branche : `layers/devops` ; branche existante conservée.
- Session : référence de session indisponible ; mission définie dans ce chat.
- Base locale vérifiée : `779ce88da0a8e1945061cd2805bd0005ce01c13b` ; aucun fetch.

Le chemin absolu du worktree est résolu localement et sa branche, son état et sa
 disponibilité sont revérifiés avant exécution. Aucune délégation n’est autorisée.

## Objectif et chemins autorisés

Réécrire `codebase-integrity/README.md`, `dev-book/README.md` et `infra/README.md`
selon les responsabilités et la structure confirmées dans DEM-006. Dans `docs/index.md`,
renommer le chapitre 02 « Les quatre piliers » et imbriquer les environnements locaux
sous Couches, sans changer les cibles des liens.
La présente carte et DEM-006 peuvent recevoir leurs preuves et liens de suivi.

## Exclusions

README design confié à UX-001 ; README des sous-dossiers de dev-book ; procédures
existantes ; déplacement de configuration confié à OPS-054 ; migration générale des README.
Les détails retirés des README ne doivent pas être déplacés vers de nouveaux documents
ou réintroduits sous forme de conventions sans demande humaine.

## Dépendances et ordre

Base locale ci-dessus déjà présente. Aucun commit d’implémentation amont nécessaire.
Le cadrage et les cartes existent dans ce worktree ; les conserver dans les commits
locaux de l’étape d’implémentation si celle-ci est explicitement invoquée.
Exécuter avant OPS-054, séquentiellement dans la même couche.

## Critères et preuve

Les trois README sont courts, non exhaustifs, avec uniquement les deux rubriques
attendues et aucune convention renseignée. Dev-book définit les quatre sous-dossiers ;
les runbooks sont ponctuels, exceptionnels, liés à une livraison et conservés avec
état d’exécution et preuve, sans modèle imposé. La limite avec docs est explicite.
Infra conserve la mention d’absence de déploiement applicatif configuré.
L’index présente quatre piliers, avec les environnements locaux sous Couches.

Relire le diff et les liens relatifs modifiés, exécuter `git diff --check`.
Consigner les résultats dans la carte. Pas de tests applicatifs pour ce changement documentaire.

## Contraintes communes

Lire AGENTS.md, les couches, la demande et les README applicables avant écriture.
Préserver le travail existant et les `.env`. Aucun changement sur develop ou master,
aucun rebase implicite, aucun déploiement. Ne pas affaiblir les conventions ou contrôles.
Les README simplifiés ont une description courte, puis uniquement
« Rôle et responsabilités » et « Conventions techniques », cette dernière rubrique vide.
Ne pas ajouter de tests qui reproduisent seulement le texte documentaire.
La validation humaine et la livraison restent des étapes distinctes.

## Réalisation et verdict

Réalisée le 2026-10-27. Les trois README et la hiérarchie du chapitre 02 suivent
le cadrage. Relecture du diff, vérification des cibles locales de docs/index.md et
`git diff --check` : réussis. Aucun test applicatif requis pour ces textes.
Le cadrage et les trois cartes sont enregistrés avec ce commit pour permettre leur
transmission par commit identifié. Aucun verdict humain à ce stade.

## Verdict humain — 2026-10-27

Validation globale explicite dans le chat : « validé », après présentation des trois
cartes de DEM-006. Commit accepté pour cette carte : `56c8a954cc5ad2073b336e7d73b6622ebfcdb87f`.
Aucune correction demandée. La livraison reste à effectuer.
