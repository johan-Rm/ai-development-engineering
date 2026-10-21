# Vérification de la vue AIOD

`vue-aiod.cjs` vérifie le panneau de détails de la vue HTML : souris, clic, clavier,
focus, tactile et absence de débordement horizontal. Il ouvre le fichier local sans serveur.

Après installation des dépendances de la webapp et de Chromium :

```sh
node codebase-quality-control/tests/browser/vue-aiod.cjs web/targets/app
```

Le second argument désigne l’application Nuxt fournissant Playwright. Les captures sont écrites
dans le dossier temporaire du système. Ce test se lance séparément des tests unitaires Python.
