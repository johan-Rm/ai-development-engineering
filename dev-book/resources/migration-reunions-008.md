# Migration des copies de réunion — demande 008

Date : 2026-10-27. Carte : [OPS-060](../tasks/OPS-060-deplacer-copies-reunion.md).

## Dépendances et périmètre

OPS-058 : `caf3ad1`, correction `073ada7` ; OPS-059 : `619a84d`.
Les six copies DEM-002 à DEM-007 sont détachées, sans changement Git local au
contrôle préalable. Les deux premiers enregistrements pointaient vers l’ancien
nom du dépôt ; `git worktree repair` a corrigé leurs chemins sans supprimer de
métadonnées. Aucune branche de couche ou intégration déplacée.

## Incident de conservation de la copie 002

Le premier déplacement visait /tmp/aide-reunions. Pendant l’interruption de la
session, /tmp a été purgé, y compris le script et sa preuve non finalisée.
La copie 002 avait déjà été déplacée ; les cinq autres étaient encore en place.
Le HEAD et l’index de 002 restent dans Git, mais son répertoire physique a disparu.

Les fichiers suivis ont été rétablis depuis l’index propre du commit
`fadf907cb9102fdf021a8217cc05002922d229fe`, dans une destination neuve avec
`git checkout-index --all --prefix=<destination>/`, puis son fichier .git et
l’enregistrement ont été réparés. Son état Git est propre et son HEAD inchangé.
Aucun écrasement de fichier existant, reset ou suppression de worktree.

**Limite non résolue : la conservation des fichiers ignorés ou non suivis de la
copie 002 ne peut pas être prouvée.** Elle occupait environ 555 Mio avant incident,
ce qui dépassait son contenu suivi. Les dépendances générées peuvent être
réinstallées depuis leurs fichiers de verrouillage, mais aucune réinstallation
ne permet d’affirmer la récupération de données ou .env inconnus. Aucun contenu
d’une autre mission n’a été copié pour masquer cette limite. L’incident empêche
de déclarer satisfait le critère de conservation intégrale de DEM-008.

## Destination corrigée et méthode de préservation

Le temporaire de mission utilisé est désormais un dossier persistant extérieur,
frère du dépôt : `<parent-du-depot>/ai-development-engineering-reunions/`.
Les copies portent le nom `ai-development-engineering-reunion-<numero>`.
Aucune destination existante n’est écrasée. Le caractère temporaire désigne ici
la durée de la mission ; l’emplacement doit résister aux interruptions et ne pas
être purgé automatiquement. Instructions et guide corrigés par `073ada7`.

Pour chacune des cinq copies encore présentes : inventaire de chaque entrée,
empreinte SHA-256 et mode de tous les fichiers réguliers (suivis, ignorés et non
suivis), cible des liens et présence des dossiers. Métadonnées internes .git
exclues du contenu, car Git doit en actualiser les chemins. Inventaire enregistré
avant déplacement, puis comparaison après `git worktree move`. Vérifier également
l’identité du HEAD et l’accès à git status. Aucun lien traversé pour le calcul.

Les preuves détaillées sont conservées à côté des copies dans `.migration-008/` :
`avant-003.json` à `avant-007.json` et `reunion-003.json` à `reunion-007.json`.
Ces noms n’utilisent pas DEM-. Les changements de noms/liens nécessaires dans la
copie 007 sont séparés de la preuve d’identité du déplacement.

## Résultats des cinq déplacements vérifiés

| Copie | Fichiers dont le contenu est vérifié | Entrées comparées | Contenu identique au déplacement |
| --- | ---: | ---: | --- |
| ai-development-engineering-reunion-003 | 34822 | 41135 | oui |
| ai-development-engineering-reunion-004 | 34824 | 41137 | oui |
| ai-development-engineering-reunion-005 | 34845 | 41160 | oui |
| ai-development-engineering-reunion-006 | 34847 | 41162 | oui |
| ai-development-engineering-reunion-007 | 216 | 274 | oui |

La copie 007 porte ensuite un diff local attendu : rapport renommé, DEM-007 et
OPS-055 avec liens corrigés. Aucun commit n’a été créé dans cette ancienne copie
et son HEAD livré reste inchangé. Les cinq autres copies sont propres, y compris
002 restaurée pour ses seuls fichiers suivis. Aucune copie n’a été supprimée.

## Inventaire final des noms

Parcours du principal, des cinq couches et des six copies extérieures, fichiers
ignorés et dépendances compris, sans suivre les liens. Métadonnées Git internes
exclues : leurs identifiants de références/enregistrements ne sont pas des
artefacts de demande. Aucune erreur de lecture. Les documents légitimes de chaque
`dev-book/demand/` sont conservés.

- `.` : `dev-book/resources/DEM-007-audit-contenu-local.md`.
- `worktree/api` : `dev-book/resources/DEM-007-audit-contenu-local.md`.
- `worktree/backoffice` : `dev-book/resources/DEM-007-audit-contenu-local.md`.
- `worktree/web` : `dev-book/resources/DEM-007-audit-contenu-local.md`.
- `worktree/design` : `dev-book/resources/DEM-007-audit-contenu-local.md`.
- `worktree/devops` : aucun nom DEM-* hors demand/.
- `reunion-002` : aucun nom DEM-* hors demand/.
- `reunion-003` : aucun nom DEM-* hors demand/.
- `reunion-004` : aucun nom DEM-* hors demand/.
- `reunion-005` : aucun nom DEM-* hors demand/.
- `reunion-006` : aucun nom DEM-* hors demand/.
- `reunion-007` : aucun nom DEM-* hors demand/.

Les rapports encore présents sur le principal et les quatre autres couches sont
suivis par Git et attendent la livraison et leur alignement, conformément au
périmètre OPS-060. Aucun changement de tâche sur develop ni copie de travail non
commité vers une autre couche. Le renommage commité OPS-059 les corrigera.
Les anciennes copies ont toutes un nom extérieur conforme ; leurs fichiers .git
et les chemins enregistrés pointent vers leurs destinations persistantes.

## Contrôles et limites

- Git status consultable pour chacune des six copies ; HEAD inchangés.
- Inventaires SHA-256 de 003 à 007 identiques après déplacement, modes et liens compris.
- Le rapport renommé de 007 conserve son contenu ; seuls deux documents de liens
  sont modifiés en plus de ce renommage.
- Liens des documents modifiés et `git diff --check` vérifiés dans devops.
- Aucun contrôle permanent, code applicatif ou test de vérificateur modifié.
- Qualité globale et conformité des couches après propagation restent à vérifier
  à la livraison ; aucune livraison ni verdict humain annoncés ici.
- Le critère de conservation complète de 002 reste non prouvé ; aucune affirmation
  de conformité intégrale de la demande n’est faite.
