# Lancer et vérifier les interfaces Nuxt

> Les deux interfaces utilisent la même procédure locale, chacune dans son propre dossier.

## Préparer l’interface

Prévoir Node 22.12 ou plus et npm. Les applications utilisent Nuxt 4, Vue 3 et
TypeScript, avec rendu côté serveur. Nuxt est fixé à 4.6.2 dans les manifestes ;
les versions installées sont verrouillées dans les fichiers `package-lock.json`.

Depuis la racine de la copie de travail, entrer dans le dossier de l’interface :

| Interface | Dossier | Adresse locale |
| --- | --- | --- |
| [Web](web.md) | `app/web/targets/app/` | http://127.0.0.1:3000 |
| Backoffice | `app/backoffice/` | http://127.0.0.1:3001 |

```sh
npm ci
npm run dev
```

Démarrer séparément l’[API](api.md#démarrer-sur-lhôte). Pour utiliser une stack Docker
isolée, suivre le [guide des couches](../architecture/02-cadre/couches/dockerisation.md).
Les serveurs sur l’hôte écoutent seulement sur `127.0.0.1` ; DevTools est désactivé.
Le témoin de vérification du cadre reste indépendant des applications.

## Configurer la connexion

Copier `.env.example` vers `.env` seulement si nécessaire, sans remplacer un fichier
existant. `NUXT_API_BASE` désigne la racine de l’API ; sa valeur par défaut est
`http://127.0.0.1:8000/api`. Elle reste côté serveur : le navigateur passe par les
routes de son interface. Le [contrat API](api.md#consulter-le-contrat) fait référence.

Aucune donnée de démonstration n’est injectée. Ce socle local n’apporte ni
identification des utilisateurs ni contrôle de permissions.

## Vérifier et construire

Depuis le dossier de l’interface choisie :

```sh
npm run typecheck
npm run build
npm run preview
# Pour les tests navigateur, avec une API locale de développement :
npx playwright install chromium
npm run test:e2e
```

Les tests démarrent Nuxt si nécessaire et créent puis suppriment leurs articles.
Ils vérifient aussi les états d’erreur et l’absence de débordement sur mobile.
Les parcours propres à chaque interface sont décrits dans leurs guides.

Pour servir directement le build, fournir `NUXT_API_BASE` si nécessaire, puis
lancer `.output/server/index.mjs` avec Node en définissant `NITRO_HOST=127.0.0.1`
et `NITRO_PORT=3000` pour le web ou `3001` pour le backoffice.

Documentation officielle : [Nuxt](https://nuxt.com/docs/4.x/getting-started/introduction).
