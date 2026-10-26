# TASK API-002 — Renommer le préfixe temporaire du test API

- **Créée le** : 2026-10-24.
- **Session** : non disponible (Codex).
- **Statut** : ✅ fait le 2026-10-24.
- **Livraison** : préfixe temporaire du test API harmonisé en `aide-api-`.
- **Type** : refactor.
- **Tests** : Vérification ponctuelle du préfixe effectif par création du dossier temporaire puis de sa suppression en sortie du contexte ; vérifier la syntaxe Python et le diff limité au littéral, sans lancer de serveur ni modifier de base. Contrôle `git diff --check`. Aucun nouveau test permanent pour ce renommage réversible à faible impact.
- **Réf** : OPS-040 ; `app/api/README.md` ; `docs/02-cadre/couches.md`.
- **Demande d’origine** : harmonisation des identifiants AIOD restants dans `app/`, découpage et vérifications validés par l’utilisateur le 2026-10-24.
- **Couche et branche** : `api`, `layers/api`.
- **Worktree** : `worktree/api`.
- **Chemins autorisés** : `app/api/app/tests/smoke.py`, présente carte.
- **Dépendances par commit** : base `ed715efb57b780305138ee814891bcb1e0334077` incluant OPS-040 ; aucune dépendance entre BO-002, WEB-002 et API-002, aucun aval requis.

## Contexte

L’écosystème s’appelle AIDE. Des identifiants applicatifs emploient encore AIOD ;
OPS-040 ne concernait que les textes documentaires et excluait ces identifiants.

## Périmètre

Remplacer uniquement le préfixe `aiod-api-` par `aide-api-` dans `TemporaryDirectory`.

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

Implémentation le 2026-10-24 sur `layers/api`, base inchangée
`ed715efb57b780305138ee814891bcb1e0334077`. Seule la présente carte non suivie
était présente au démarrage ; aucun autre travail touché, aucun réalignement requis.

- `app/api/app/tests/smoke.py` : préfixe `aide-api-` dans `TemporaryDirectory`.
- Compilation Python en mémoire : réussie, sans fichier généré.
- Extraction AST du préfixe réellement déclaré dans l’unique appel à
  `tempfile.TemporaryDirectory` : `aide-api-` ; création effective d’un dossier
  portant ce préfixe, existence vérifiée dans le contexte et absence confirmée
  après sa fermeture.
- Comparaison textuelle avec `git show HEAD:app/api/app/tests/smoke.py` :
  strictement identique après la seule substitution du préfixe.
- Aucune occurrence AIOD restante dans ce fichier ; `git diff --check` réussi.

Aucun nouveau test permanent ajouté conformément au cadrage. Aucun serveur démarré,
aucune base ni aucun `.env` modifié ; suite HTTP non exécutée pour ce seul littéral.
Aucune documentation durable à modifier : responsabilités, conventions et commandes
inchangées. Aucun autre worktree modifié. Mise en commit demandée explicitement
par l’utilisateur le 2026-10-24 après présentation du résultat ; aucun push.

## Livré

- `app/api/app/tests/smoke.py` : seul préfixe temporaire renommé.
- Présente carte : cadrage, preuves et clôture.

## Reste à faire (hors périmètre)

Aucun reliquat pour API-002. Les travaux BO-002 et WEB-002 sont indépendants
et restent hors de ce commit.
