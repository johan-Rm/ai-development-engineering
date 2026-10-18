# API — API Platform

Mini API Symfony 7.4 / API Platform 4, PHP >= 8.4, extensions SQLite/PDO,
Composer et Python 3 pour le test du contrat. Branche `layers/api`, tâche API-001.

Depuis `/home/johan/www/lab/ai-orchestrated-development/worktree/api/api/app` :

```sh
composer install
# Seulement lors d'une nouvelle installation, si .env n'existe pas :
cp -n .env.example .env
php bin/console doctrine:migrations:migrate --no-interaction
php -d variables_order=EGPCS -S 127.0.0.1:8000 -t public public/router.php
```

Documentation interactive : http://127.0.0.1:8000/api/docs ; OpenAPI :
http://127.0.0.1:8000/api/docs.jsonopenapi.
Le contrat généré est versionné dans `app/openapi.json`. Pour le régénérer :
`php bin/console api:openapi:export --output=openapi.json`.
La base `app/var/app.db` est locale et ignorée. Aucune donnée n'est injectée au lancement.
Les dépendances sont verrouillées dans `composer.lock` et les recettes dans `symfony.lock`.
Le témoin `scripts/process.py` reste indépendant de cette application.

## Contrat Article

- GET `/api/articles?page=1` : collection JSON-LD `member`, `totalItems`, `view`, 20 par page, id décroissant.
- GET `/api/articles/{id}` : détail, 404 si absent.
- POST `/api/articles` : `Content-Type: application/ld+json`, renvoie 201.
- PATCH `/api/articles/{id}` : `Content-Type: application/merge-patch+json`, renvoie 200.
- DELETE `/api/articles/{id}` : renvoie 204.

Chaque article expose `id`, `title` (obligatoire, non blanc, maximum 160 caractères),
`content` (texte, vide par défaut) et `published` (booléen, false par défaut).
Les requêtes utilisent `Accept: application/ld+json`. Une validation invalide renvoie 422.

```sh
curl -X POST http://127.0.0.1:8000/api/articles \
  -H 'Content-Type: application/ld+json' -H 'Accept: application/ld+json' \
  -d '{"title":"Bonjour","content":"Premier article","published":true}'
```

Les interfaces Nuxt passent par leur propre proxy serveur ; aucun CORS n'est nécessaire.
Ce socle local ne filtre pas les brouillons et ne fournit aucune authentification.

## Vérifier

```sh
python3 tests/smoke.py
php bin/console doctrine:schema:validate
php bin/console lint:container
```

Le test lance un serveur sur un port libre et migre une base temporaire. Il couvre CRUD,
validation, pagination et OpenAPI sans modifier la base de développement.
