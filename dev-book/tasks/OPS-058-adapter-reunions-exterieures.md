# OPS-058 — Adapter les procédures aux réunions extérieures

- État : validée ; non livrée.
- Date : 2026-10-27.
- Demande : [DEM-008](../demand/DEM-008-reserver-noms-demandes.md).
- Couche : devops.
- Worktree : `worktree/devops`, relatif à la racine du dépôt principal.
- Branche : `layers/devops`, existante conservée.
- Session : référence de session indisponible ; mission définie dans ce chat.

Chemin absolu résolu localement ; vérifier branche, index, missions actives et
état Git avant chaque écriture. Un arbre propre ne prouve pas sa disponibilité.
Aucune délégation. Préserver .env, données, travaux en cours et historiques.

## Objectif, périmètre et chemins autorisés

Documenter la règle humaine confirmée : seuls les documents de demande dans
`dev-book/demand/` portent un nom DEM-*. Prévoir les réunions hors du projet dès
leur création, sans préfixe DEM-, avec branche dédiée conservée. Définir une base
temporaire extérieure, configurable, sans chemin personnel codé en dur, et traiter
collisions, reprise, conservation des contributions actives et accès. Corriger le
lien mort du README worktree vers ia-engineering dans ce périmètre.

Chemins autorisés : `AGENTS.md`, `worktree/README.md`, `dev-book/README.md`,
`docs/03-developpement-loop/02-decoupage.md`, `05-reconstitution.md`,
`06-livraison.md`, `docs/02-cadre/couches/index.md`, `SETUP.md`, et seulement les
références actives directement concernées identifiées avant écriture.
Examiner les skills personnels decouper-demande, reconstituer-demande et
livrer-demande ; s’ils nécessitent une adaptation, la limiter au rangement et à
la cohérence avec les guides, sans modifier leurs autorisations. Ils restent hors
Git : preuve de diff et vérification de disponibilité distinctes, accès en écriture
à résoudre selon l’environnement. Utiliser skill-creator si une édition est nécessaire.
Ne modifier ni Codebase Integrity ni ses seuils ou tests : aucun nouveau contrôle demandé.

## Dépendances par commit

Aucune dépendance amont d’implémentation. DEM-008 et les cartes ne sont pas encore
commitées : enregistrement préalable à l’implémentation, puis réalisation et commit
propre de cette carte. Base locale `cff25a1ac80533e634be9df3ebba725cb8950128`.

## Critères, contrôles et preuves

Relire la cohérence des instructions et skills ; vérifier les liens concernés.
Exercer création et reprise d’une réunion dans un dépôt jetable et un temporaire
extérieur avec un nom sans DEM-, sans déplacer de copie réelle. Prouver qu’aucun
changement des autorisations Git ou des couches n’a été introduit.

## Documentation et réalisation

Mettre à jour cette carte et DEM-008 avec les preuves et SHA avant vérification.
Lire les README applicables avant écriture. Aucun stash, reset destructif,
force-push ni rebase implicite. Aucun changement direct de tâche sur develop.
Réalisation décrite dans les preuves ci-dessous ; verdict humain consigné en fin de carte.

## Preuve OPS-058 — 2026-10-27

Cadrage commité : `75b126e`. Instructions et guides adaptés, couches conservées,
branches de réunion inchangées ; lien mort du README worktree corrigé. Trois skills
personnels lus : ils prescrivent déjà de résoudre les chemins selon le projet,
sans chemin de réunion interne imposé. Aucune édition de skill nécessaire et
aucune autorisation Git changée. Aucun vérificateur modifié.

Création d’un dépôt jetable develop et d’un worktree extérieur sur branche dédiée,
puis reprise par consultation de son enregistrement et état Git : réussies.
Aucun dossier de réunion interne créé. `git diff --check` réussi.

## Correction de conservation — 2026-10-27

L’interruption pendant OPS-060 a révélé la purge de /tmp, après déplacement de
la copie 002. Les instructions précisent désormais que le temporaire de mission
est un emplacement extérieur persistant, conservé à travers les interruptions,
et non /tmp. Aucun skill ou contrôle modifié. L’incident et ses limites de
récupération sont détaillés dans la preuve OPS-060, sans masquer la perte possible
de contenus ignorés de la copie 002.

## Verdict humain — 2026-10-27

L’humain répond « oui validé » après présentation des trois cartes et demande
explicite d’acceptation de la réserve OPS-060. Commits présentés et acceptés : `caf3ad1` et sa correction `073ada7`.
Validation des procédures de rangement et du stockage de mission extérieur persistant.
Aucune correction fonctionnelle demandée. Ancienne mention « Non commencée »
rectifiée dans cette trace documentaire. Livraison non effectuée.
