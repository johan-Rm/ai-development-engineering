# DEM-008 — Réserver les noms DEM-* aux documents de demande

- Date : 2026-10-27.
- État : cadrage confirmé et découpé ; non implémentée.
- Référence de session : référence de session indisponible.
- Carte externe : aucune fournie.

## Besoin, contexte et utilisateurs

L’humain souhaite un rangement strict et lisible : les noms `DEM-*` doivent
apparaître uniquement dans `dev-book/demand/`. Les copies de réunion présentes
sous `worktree/DEM-*` et les rapports nommés `DEM-*` ailleurs créent une confusion.
Les contributeurs humains et agents doivent retrouver les demandes à un seul
emplacement logique et utiliser des noms adaptés pour les autres artefacts.

Les dossiers de réunion sont des copies Git complètes, pas des documents de besoin.
La procédure actuelle les crée dans le projet puis les conserve après livraison.
Les dossiers `worktree/DEM-002` à `worktree/DEM-007` ont été observés ; les
métadonnées des deux premiers pointent encore vers l’ancien emplacement du dépôt.
Ces observations sont à revérifier avant déplacement. Un rapport tel que
`dev-book/resources/DEM-007-audit-contenu-local.md` est également concerné.

## Résultat attendu et périmètre

Réserver strictement les noms de fichiers et dossiers commençant par `DEM-` aux
seuls documents de demande dans `dev-book/demand/`, dans chaque copie du dépôt.
Cette décision porte sur les noms et emplacements physiques ; les identifiants
DEM dans le texte et les références aux demandes restent utiles et conservés.

Déplacer les copies de réunion existantes à l’extérieur du projet, sans perte de
contenu, et les renommer sans préfixe `DEM-*`. Créer les futures copies de réunion
dans un emplacement temporaire extérieur dès leur création, avec un nom sans
préfixe `DEM-*`. Conserver la branche de réunion dédiée à chaque demande et
l’isolation des contributions ; le nom d’une référence Git n’est pas un nom de
fichier ou dossier à ranger dans `dev-book/demand/`.

Renommer les rapports et autres artefacts concernés en gardant leur emplacement
adapté à leur rôle ; ne pas déplacer les preuves dans demand/ pour conserver un
préfixe. Mettre à jour leurs liens et les instructions et procédures qui prescrivent
les anciens noms ou emplacements. Examiner le principal, les couches et les copies
de réunion existantes, avec une preuve explicite de couverture.

## Critères observables et preuves attendues

1. L’inventaire identifie tous les fichiers et dossiers `DEM-*` du périmètre,
   distingue les documents autorisés dans demand/ des éléments à corriger et
   explicite les limites de lecture ou d’accès.
2. Aucun fichier ni dossier `DEM-*` ne subsiste hors du dossier logique
   `dev-book/demand/` de chaque copie du dépôt après correction.
3. Les copies de réunion existantes sont déplacées à l’extérieur, sous des noms
   sans préfixe `DEM-*`, sans perte de fichiers suivis, ignorés ou non suivis,
   environnements et données compris. Les worktrees restent utilisables et leurs
   enregistrements Git pointent sur les chemins réels.
4. Les rapports renommés conservent leur contenu et leur rôle. Les liens actifs
   sont corrigés ; les traces historiques restent compréhensibles sans prétendre
   décrire les nouveaux chemins. Aucune réécriture de l’historique Git.
5. Les instructions et procédures de reconstitution et livraison concernées
   utilisent un emplacement temporaire extérieur et des noms conformes ; aucune
   copie de réunion n’est créée dans le projet, même pendant une demande.
6. Les preuves comprennent les inventaires avant/après, la préservation des
   contenus déplacés, les contrôles des liens et des métadonnées des worktrees.
   Vérifier le parcours de préparation d’une réunion avec le nouvel emplacement
   dans un environnement jetable, sans migration destructive du travail en cours.
7. Les tests de l’outillage sont exécutés si son comportement change ; les
   contrôles de qualité applicables sont précisés au découpage et à la livraison.
   Aucun contrôle nouveau non demandé n’est ajouté pour étendre le périmètre.

## Contraintes et exclusions

- Préserver les .env, données, changements locaux, historiques, branches de couche
  et copies de travail. Pas de suppression d’une copie pour éviter de la déplacer.
- Respecter les missions en cours ; une cible occupée nécessite coordination.
  Ne pas déduire sa disponibilité de son seul état Git propre.
- Aucun stash, reset destructif, force-push ou rebase implicite.
- Résoudre les chemins extérieurs selon l’environnement, avec contrôle d’accès et
  gestion des collisions ; ne pas imposer de chemin personnel dans la documentation.
  L’usage de temporaire ne doit pas provoquer la perte d’une contribution active.
- Ne pas renommer les demandes ni leurs identifiants pour contourner leur rangement.
- Ne pas reprendre les fonctionnalités de nettoyage automatique abandonnées dans
  DEM-007. Cette demande traite le rangement explicitement confirmé ici.
- Cette interview ne déplace ni ne renomme rien et ne lance aucune étape suivante.

## Décisions humaines et confirmation

L’humain demande « je ne veux pas voir de fichier de ce genre hors du dossier
 dev-book/demand/ », puis choisit de ne plus créer de copies de réunion dans le
projet, même pendant une demande, et d’utiliser un temporaire extérieur.
Il étend explicitement le rangement aux rapports : réserver les noms DEM-* à
`dev-book/demand/`, rapports compris. Il insiste ensuite : « les fichiers DEM-*
doivent etre dans dev-book/demand/ unqieument et strictement ».

Le cadrage final prévoit le déplacement sans perte des anciennes copies vers
l’extérieur avec renommage, le même emplacement extérieur pour les futures copies,
le renommage des rapports, la correction des liens, la vérification du projet et
des couches et l’adaptation des instructions et procédures. L’humain le confirme
par « oui », le 2026-10-27. Cette confirmation valide le besoin, pas son implémentation.

## Questions ouvertes

Aucune décision de besoin nécessaire ne reste ouverte. Le choix technique du
répertoire extérieur, les noms sans préfixe réservé, la réparation des anciennes
métadonnées et les fichiers exacts à adapter restent à déterminer au découpage.
Les skills personnels concernés seront à identifier : leur évolution doit rester
cohérente avec AGENTS.md et les guides, sans inventer une autorisation de livraison.

## Tâches issues du découpage

| Critères couverts | Carte | Couche | Ordre |
| --- | --- | --- | --- |
| Règle et procédures, préparation extérieure (5, 6) | [OPS-058](../tasks/OPS-058-adapter-reunions-exterieures.md) | devops | 1 |
| Rapports, contenus et liens (1, 2, 4) | [OPS-059](../tasks/OPS-059-renommer-rapports-demandes.md) | devops | 2, commit OPS-058 requis |
| Migration, métadonnées, conservation et recette (1 à 3, 6, 7) | [OPS-060](../tasks/OPS-060-deplacer-copies-reunion.md) | devops | 3, commits OPS-058 et OPS-059 requis |

Exécution séquentielle sans délégation. Les dépendances sans SHA restent à
résoudre avant leurs consommateurs ; aucune copie de travail non commité.

## Réunion prévue

Branche dédiée `demands/DEM-008`, créée uniquement à la reconstitution.
Worktree extérieur : `<temp>/aide-reunions/<projet>-reunion-008`. Résoudre le
répertoire temporaire et l’identité de projet localement, vérifier qu’il est hors
dépôt, accessible, sans collision et conservable pendant la mission. Aucun
`worktree/DEM-008` à créer ; aucune branche de couche utilisée pour la réunion.

## Preuve du découpage — 2026-10-27

Instructions, demande et README applicables consultés. Historique des cartes de
toutes les références Git locales et fichiers des worktrees examinés sans fetch :
plus grand OPS observé OPS-057 ; attribution OPS-058 à OPS-060.
Worktree absolu utilisé : dossier `worktree/devops` du dépôt principal, branche
`layers/devops` à `cff25a1ac80533e634be9df3ebba725cb8950128`. Seule DEM-008 était
non suivie avant cette écriture. Les contributions de DEM-007 sont livrées ; aucune
mission concurrente identifiée. Disponibilité à revérifier avant implémentation.
Branche existante conservée ; aucune synchronisation distante ni rebase.
Aucune branche créée, migration, modification de procédure ou implémentation.
L’accès en écriture aux destinations extérieures et skills personnels reste à
vérifier lors de leur utilisation, pas supposé acquis par le découpage.

## Preuve d’enregistrement

Historique de toutes les références Git locales et demandes présentes dans les
worktrees examinés, sans fetch : plus grand numéro observé DEM-007. Aucun doublon
correspondant au besoin identifié. Attribution DEM-008.

Enregistrement limité à ce document dans `worktree/devops`, branche
`layers/devops`, HEAD `cff25a1ac80533e634be9df3ebba725cb8950128`, état Git propre
avant écriture. Instructions, couches et README applicables consultés.
Aucun déplacement, renommage, nettoyage, commit, push, PR, merge ou découpage.

## Implémentation OPS-058 — 2026-10-27

Cadrage et cartes : `75b126e`. Règle de rangement et temporaire extérieur documentés
dans les instructions et guides. Essai de création/reprise réussi dans un dépôt
jetable ; aucun skill personnel ni contrôle modifié. Carte à vérifier humainement.
