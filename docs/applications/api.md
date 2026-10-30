# Utiliser l’API des articles

> L’API fournit les articles aux deux interfaces et conserve leurs données localement.

## Démarrer sur l’hôte

Prévoir PHP 8.4 ou plus, les extensions SQLite/PDO et Composer. L’application utilise
Symfony 7.4 et API Platform 4 ; les versions sont verrouillées par Composer.
Depuis la racine de la copie de travail :

```sh
cd app/api/app
composer install
# Seulement si .env n’existe pas :
cp -n .env.example .env
php bin/console doctrine:migrations:migrate --no-interaction
php -d variables_order=EGPCS -S 127.0.0.1:8000 -t public public/router.php
```

La base locale `app/api/app/var/app.db` est ignorée par Git. Aucune donnée de
démonstration n’est ajoutée au démarrage. Les recettes Symfony sont verrouillées
dans `symfony.lock`. Ce serveur est indépendant du témoin de vérification du cadre.
Pour un lancement Docker, suivre le
[guide des couches](../architecture/02-cadre/couches/dockerisation.md).

## Consulter le contrat

Le [contrat OpenAPI versionné](../../app/api/app/openapi.json) décrit les opérations,
les champs et la validation des articles. La documentation interactive est servie
sur http://127.0.0.1:8000/api/docs ; le contrat généré est disponible sur
http://127.0.0.1:8000/api/docs.jsonopenapi.

Depuis `app/api/app/`, régénérer le contrat après un changement approuvé :

```sh
php bin/console api:openapi:export --output=openapi.json
```

Ce socle local expose aussi les brouillons et ne fournit aucune authentification.
Les interfaces passent par leur serveur Nuxt ; aucune configuration CORS n’est
nécessaire pour ce fonctionnement. La liste contient 20 articles par page, classés
par identifiant décroissant.

## Vérifier l’API

Prévoir aussi Python 3. Depuis `app/api/app/` :

```sh
python3 tests/smoke.py
php bin/console doctrine:schema:validate
php bin/console lint:container
```

Le test utilise une base temporaire et un serveur sur un port libre. Il couvre
création, lecture, modification, suppression, validation, pagination et OpenAPI,
sans modifier la base de développement.
