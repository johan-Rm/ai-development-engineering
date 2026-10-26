# OPS-002 — Définir le Codebase Quality Control

> Note historique ajoutée lors d’OPS-010 : les mentions de fusion préparée, de fichiers non commités ou d’anciens chemins décrivent l’état lors de cette tâche. Elles ne décrivent pas l’état Git actuel ni un travail restant. Les cartes sont désormais réunies dans `dev-book/tasks/`.

- Statut : réalisée, non commitée.
- Date : 2026-10-21.
- Mission : devops, branche `layers/devops`, worktree `/home/johan/www/lab/ai-orchestrated-development/worktree/devops`.
- Demande : intégrer le texte validé et remplacer le nom de la brique dans le schéma interactif AIDE.
- Périmètre : page de référence, liens documentaires, contenu de la brique dans la vue interactive et vérification navigateur.
- Dépendance : OPS-001, préparée dans ce même worktree sans commit.
- Critères : 15 domaines ; conventions propres à chaque projet et vivantes ; règle, périmètre, exceptions, points de contrôle et niveau ; documentation répartie sans duplication ; conventions sans contrôle visibles ; vérificateurs testés ; consolidation après arbitrage humain.
- Preuve attendue : panneau accessible au clic et au clavier, contenu complet, géométrie préservée et tests de l’outillage réussis.

## Livré et vérifié

- Page `docs/aiod/codebase-quality-control.md` : texte validé et 15 domaines.
- Liens depuis les index documentaires et la page des commandes qualité.
- Vue interactive : libellé Codebase Quality Control et panneau complet ; géométrie conservée.
- Nom du cadre AIDE (AI Development Engineering), sans renommage du dépôt ni des dossiers.
- `python3 -B codebase-quality-control/scripts/check.py` : 15 tests réussis.
- Test Chromium `codebase-quality-control/tests/browser/vue-aiod.cjs` : réussi avec les dépendances Playwright de
  la webapp du worktree principal, `PLAYWRIGHT_BROWSERS_PATH=/tmp/aiod-playwright` et les
  bibliothèques de `/tmp/aiod-browser-libs/root/usr/lib/x86_64-linux-gnu`.
- Capture `/tmp/aide-codebase-quality-control.png` relue : nouveau nom visible et panneau
  détaillé lisible ; interactions, clavier, tactile et dimensions ordinateur/mobile vérifiés.
- `git diff --check` : réussi sur les changements de la tâche.
- Aucun contrôle applicatif complet, déploiement, commit ou push exécuté.
