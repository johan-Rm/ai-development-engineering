# API-001 — Socle API Platform

- **Créée le** : 2026-10-18.
- **Session** : non disponible (Codex).
- **Statut** : ✅ fait le 2026-10-18.
- **Type** : feat.
- **Tests** : CRUD HTTP, validation 422, persistance SQLite, documentation OpenAPI.
- **Réf** : demande utilisateur, docs/aiod/couches.md.
- **Mission** : couche `api`, branche `layers/api`, worktree `worktree/api`.
- **Chemins autorisés** : `app/api/`, cette carte.
- **Base vérifiée** : `f19ba58b78eff96d0ea618e03b44343f64812a66` ; aucune réécriture de branche.

## Contexte

Installer une application minimale réelle dans le worktree existant, pour servir de point de départ.
L'utilisateur a autorisé les trois cartes puis leur réalisation dans cette session.

## Périmètre

Socle API Platform. Ressource Article : id entier, title obligatoire (1 à 160 caractères),
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
Ce commit constitue la livraison du contrat API ; les interfaces le référencent par SHA
avant la réunion locale des trois branches sur develop.

## Hors périmètre

Authentification, permissions métier, données sensibles, déploiement, DNS, push et PR.
Commit et intégration locale sur develop autorisés par l’utilisateur le 2026-10-18. Ne pas modifier les .env existants. Pas de sous-agent.

## Règles et cas limites

Valider les titres vides et trop longs, conserver les saisies en cas d'erreur.
Ne pas insérer automatiquement de données dans la base de développement.
La pagination doit permettre d'atteindre les articles au-delà de la première page.
Ce socle ouvert sert au développement local et ne constitue pas une administration sécurisée.

## Documentation impactée

`api/README.md`, exemples de configuration et commandes de lancement propres à l'application.

## Définition de terminé

- [x] Application installée avec dépendances verrouillées.
- [x] CRUD HTTP, validation 422, persistance SQLite, documentation OpenAPI.
- [x] Commandes de démarrage, contrat et limites documentés.
- [x] Preuves consignées et travail préexistant préservé.

## Vérification

- `python3 tests/smoke.py` : OK, CRUD HTTP, 3 titres invalides rejetés en 422,
  validation PATCH sans écriture, pagination 21 articles sur deux pages, suppression puis 404, OpenAPI.
- `doctrine:schema:validate`, `lint:container`, `lint:yaml config` : OK.
- Isolation HTTP renforcée par `variables_order=EGPCS` et assertion du nombre de lignes dans la base temporaire.
- `composer validate --strict --no-check-publish` : OK.
- Migration exécutée sur la base locale vide ; aucune donnée de démonstration ajoutée.
- API Platform 4.4.5, Symfony 7.4.21, fichiers lock conservés.
- Serveur de développement vérifié sur 127.0.0.1:8000.
- Contrôle du dépôt `python3 codebase-quality-control/scripts/check.py` : 12 tests OK.

- PHP minimum corrigé à 8.4, conformément aux dépendances Doctrine verrouillées.
- `openapi.json` régénéré avec `api:openapi:export` ; validation Composer stricte réussie.

- Vérification avant commit : test HTTP rejoué, 1 test réussi en 2,1 secondes.

## Livré

API Platform, entité Article, migration SQLite, contrat OpenAPI, test HTTP et README.

## Reste à faire (hors périmètre)

Dockerisation applicative, authentification et déploiement. Aucun push demandé.
