# BO-001 — Socle dashboard Nuxt

- **Créée le** : 2026-10-18.
- **Session** : non disponible (Codex).
- **Statut** : ✅ fait le 2026-10-18.
- **Type** : feat.
- **Tests** : typecheck, build, rendu SSR et parcours de création, modification, suppression.
- **Réf** : demande utilisateur, docs/aiod/couches.md.
- **Mission** : couche `backoffice`, branche `layers/backoffice`, worktree `worktree/backoffice`.
- **Chemins autorisés** : `app/backoffice/`, cette carte.
- **Base vérifiée** : `921a7bf15d7e44ef88d89a1ee47d764e9904d261` ; aucune réécriture de branche.

## Contexte

Installer une application minimale réelle dans le worktree existant, pour servir de point de départ.
L'utilisateur a autorisé les trois cartes puis leur réalisation dans cette session.

## Périmètre

Socle dashboard Nuxt. Ressource Article : id entier, title obligatoire (1 à 160 caractères),
content facultatif (texte), published booléen. Collection JSON-LD `/api/articles`
avec `member` et `totalItems`, détail `/api/articles/{id}` ; POST JSON-LD,
PATCH merge-patch JSON et DELETE. Pagination serveur, 20 éléments par page.
API sur 127.0.0.1:8000, webapp sur 127.0.0.1:3000, dashboard sur 127.0.0.1:3001.

## Décisions de cadrage

Hypothèses assumées pour ce mini boilerplate : interface en français, SQLite local,
Nuxt avec TypeScript et SSR, styles CSS simples et responsive, aucun service Docker requis.
Web en lecture ; dashboard CRUD. États chargement, vide et erreur visibles.
Les clients utilisent un proxy Nuxt de même origine vers une URL API configurable côté serveur.
Contrat décrit ici avant réalisation ; aucune copie de fichiers non commités entre couches.
Contrat API livré par le commit `bc9ea8fb2f80160c02c8dd3f91f38b877fdf1474` (API-001),
référence utilisée pour l’intégration locale sur develop.

## Hors périmètre

Authentification, permissions métier, données sensibles, déploiement, DNS, push et PR.
Commit et intégration locale sur develop autorisés par l’utilisateur le 2026-10-18. Ne pas modifier les .env existants. Pas de sous-agent.

## Règles et cas limites

Valider les titres vides et trop longs, conserver les saisies en cas d'erreur.
Ne pas insérer automatiquement de données dans la base de développement.
La pagination doit permettre d'atteindre les articles au-delà de la première page.
Ce socle ouvert sert au développement local et ne constitue pas une administration sécurisée.

## Documentation impactée

`app/backoffice/README.md`, exemples de configuration et commandes de lancement propres à l'application.

## Définition de terminé

- [x] Application installée avec dépendances verrouillées.
- [x] typecheck, build, rendu SSR et parcours de création, modification, suppression.
- [x] Commandes de démarrage, contrat et limites documentés.
- [x] Preuves consignées et travail préexistant préservé.

## Vérification

- Nuxt 4.6.2, versions verrouillées dans package-lock.json.
- `npm run typecheck` : OK ; `npm run build` : OK, build SSR de production.
- `npm run test:e2e` : 1 test Chromium réussi : création 201 via formulaire, édition,
  publication, échec PATCH simulé avec saisies conservées, suppression confirmée et retrait de la liste.
- Captures ordinateur et mobile relues ; absence de débordement à 390px vérifiée dans le navigateur.
- Les articles créés pendant les tests ont été supprimés.
- Audit npm : 11 alertes high transitives, aucune critique ; limite documentée dans le README.
- Vérification du build servi : SSR et proxy 200, page invalide 400 ; méthodes interdites refusées en 405.
- Services locaux : API 8000, webapp 3000, dashboard 3001 ; base de développement vide après tests.

- Vérification avant commit : test navigateur rejoué et réussi.

## Livré

Dashboard Nuxt SSR, proxy CRUD, formulaire, styles, test navigateur et README.

## Reste à faire (hors périmètre)

Dockerisation applicative, authentification et déploiement. Aucun push demandé.
Les alertes npm transitives restent documentées dans le README.
