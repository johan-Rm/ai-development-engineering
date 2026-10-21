# BP-019 — Intégrer les textes validés du développement

- Statut : réalisée le 2026-10-20.
- Date : 2026-10-20.
- Mission historique : maintenance du cadre, sur la branche historique de maintenance, worktree principal (chemin absolu obtenu par `git rev-parse --show-toplevel`).
- Périmètre : détails des six étapes dans `docs/aiod/vue-d-ensemble-aiod.html`, adaptation des assertions navigateur concernées et cette carte. Préserver les autres travaux et les pictos ajoutés par l’utilisateur.
- Demande : intégrer les six textes validés un à un dans le chat, sans modification de la présentation.
- Critères : demande pouvant contenir plusieurs tâches par couche, une tâche/un commit, une PR par demande ; isolation et disponibilité des couches ; vérification humaine ; reconstitution ; contrôles réussis avant écriture des tests et de la documentation en finalisation.
- Preuve : lecture des six panneaux dans Chromium, ordre de finalisation, interactions et géométrie du schéma conservées.

## Livré

Les six panneaux reprennent les textes validés : objectif, actions et sortie attendue. L’étape 02 autorise plusieurs tâches dans une couche et rattache leurs commits à une PR de demande. L’étape 03 précise l’attente d’une couche occupée et la conservation de la couche pendant les corrections. L’étape 04 formalise le verdict humain et les demandes de consolidation. L’étape 05 réunit l’ensemble. L’étape 06 impose l’ordre validé : contrôles réussis, écriture des tests et de la documentation, exécution des tests ajoutés, préparation de la PR.

## Preuves

- `node tests/browser/vue-aiod.cjs web/targets/app` : réussi. Les six panneaux ont été ouverts ; présence de la sortie attendue et ordre de finalisation vérifiés. Géométrie, liens, rôles, interactions et absence de défilement vertical toujours validés sur ordinateur et mobile.
- Capture du panneau Finalisation relue : les quatre rubriques sont visibles et l’ordre est correct.
- `git diff --check` : réussi.
- Aucun changement de présentation ni des pictos fournis ; aucun commit, push ou contrôle applicatif demandé pour cette modification documentaire.

Ajustement de vocabulaire validé : étape 03 renommée « Implémentation », avec actualisation des renvois et des assertions concernées. Les identifiants techniques internes sont conservés pour préserver les liaisons.

Étape 06 renommée « Livraison » à la demande de l’utilisateur ; intitulé et renvois actualisés dans la vue et son test. Identifiant technique interne conservé.

## Mise en commit — 2026-10-21

`node tests/browser/vue-aiod.cjs web/targets/app` réussi dans Chromium, avec `PLAYWRIGHT_BROWSERS_PATH=/tmp/aiod-playwright` et les bibliothèques de `/tmp/aiod-browser-libs/root/usr/lib/x86_64-linux-gnu`. `git diff --check` réussi. Les cartes BP-013 à BP-021 sont livrées ensemble avec la version finale de la vue et de son test : leurs états intermédiaires non commités ne sont pas reconstruits. Écart à la convention un commit par tâche pour cette reprise du travail accumulé.
