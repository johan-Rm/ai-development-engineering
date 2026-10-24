# TASK BO-002 — Renommer le paquet du backoffice en aide-dashboard

- **Créée le** : 2026-10-24.
- **Session** : non disponible (Codex).
- **Statut** : ✅ fait le 2026-10-24.
- **Livraison** : nom du paquet harmonisé en `aide-dashboard`, manifeste et lockfile synchronisés.
- **Type** : refactor.
- **Tests** : Charger les deux JSON, vérifier les trois noms et comparer les structures avant/après en excluant ces seuls champs ; aucune dépendance ni intégrité ne doit changer. Contrôle `git diff --check`. Aucun nouveau test permanent pour ce renommage réversible à faible impact.
- **Réf** : OPS-040 ; `app/backoffice/README.md` ; `docs/02-cadre/couches.md`.
- **Demande d’origine** : harmonisation des identifiants AIOD restants dans `app/`, découpage et vérifications validés par l’utilisateur le 2026-10-24.
- **Couche et branche** : `backoffice`, `layers/backoffice`.
- **Worktree absolu** : `/home/johan/www/lab/ai-orchestrated-development/worktree/backoffice`.
- **Chemins autorisés** : `app/backoffice/package.json`, `app/backoffice/package-lock.json`, présente carte.
- **Dépendances par commit** : base `ed715efb57b780305138ee814891bcb1e0334077` incluant OPS-040 ; aucune dépendance entre BO-002, WEB-002 et API-002, aucun aval requis.

## Contexte

L’écosystème s’appelle AIDE. Des identifiants applicatifs emploient encore AIOD ;
OPS-040 ne concernait que les textes documentaires et excluait ces identifiants.

## Périmètre

Remplacer `aiod-dashboard` par `aide-dashboard` dans le manifeste et les deux mentions du lockfile.

## Hors périmètre

Changement de dépendances, de contrat, de comportement ou de convention technique.
Autres couches, identifiants du cadre, ressources historiques, documentation déjà
harmonisée, fichiers générés et `.env`. Aucun service démarré, aucune migration,
aucun commit, push, PR ou merge sans demande explicite.

## Décisions de cadrage

L’utilisateur a validé trois cartes indépendantes, une par couche. La présente carte
ne traite que sa couche ; aucun travail d’une autre mission n’est copié.
Les contrôles ponctuels vérifient le renommage et la préservation du reste, sans
ajout de test permanent qui reproduirait le changement de nom.

## Règles et cas limites

Lire les README applicables avant toute écriture. Préserver le reste des fichiers.
API, permissions, états d’interface, concurrence, accessibilité et performance
ne changent pas ; ces dimensions sont sans objet pour ce renommage.
Toute référence supplémentaire découverte impose d’en examiner l’usage avant
extension du périmètre ; ne pas remplacer globalement AIOD dans le dépôt.

## Documentation impactée

Aucune documentation durable à modifier pour ce seul identifiant interne.
Les responsabilités et commandes des README restent valides. La présente carte
portera les vérifications et les éventuelles limites.

## Définition de terminé

- [x] Le renommage décrit est effectué dans les seuls fichiers autorisés.
- [x] Aucune occurrence AIOD ne reste dans ces fichiers.
- [x] Les contrôles ponctuels annoncés réussissent et leurs résultats sont consignés.
- [x] Le diff ne comporte aucun autre changement fonctionnel et `git diff --check` réussit.
- [x] La preuve de réalisation permet la relecture humaine ; aucun test permanent superflu n’est ajouté.

## Vérification

Implémentation le 2026-10-24 sur `layers/backoffice`, base inchangée
`ed715efb57b780305138ee814891bcb1e0334077`. Seule la présente carte non suivie
était présente au démarrage ; aucun autre travail touché.

- `app/backoffice/package.json` : `name` vaut désormais `aide-dashboard`.
- `app/backoffice/package-lock.json` : `name` racine et `packages[""].name`
  valent désormais `aide-dashboard`.
- Contrôle Python ponctuel : chargement JSON des deux fichiers réussi ; comparaison
  avec `git show HEAD:<chemin>` après neutralisation des trois champs de nom :
  structures strictement identiques, dépendances et intégrités préservées.
- Recherche insensible à la casse dans les deux fichiers : aucune occurrence AIOD.
- `git diff --check` : réussi ; diff limité à trois substitutions de nom.

Aucun test permanent ajouté conformément au cadrage. Aucun build ou test applicatif
exécuté pour ce seul renommage de métadonnées. Aucune documentation durable à
modifier : responsabilités, conventions et commandes inchangées.
Aucun service, environnement ou autre couche modifié. Mise en commit explicitement
demandée par l’utilisateur le 2026-10-24 après présentation du résultat ; aucun push.

## Livré

- `app/backoffice/package.json` : nouveau nom du paquet.
- `app/backoffice/package-lock.json` : deux champs de nom synchronisés.
- Présente carte : cadrage, preuves et clôture.

## Reste à faire (hors périmètre)

Aucun reliquat pour BO-002. Les cartes WEB-002 et API-002 restent indépendantes,
sans modification dans ce commit.
