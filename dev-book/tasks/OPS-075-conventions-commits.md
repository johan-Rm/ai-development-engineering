# OPS-075 — Documenter et contrôler les conventions des commits

- Demande : [DEM-024](../demand/DEM-024-conventions-commits.md#décisions-complémentaires-confirmées).
- Session de création : `01a18cd5-5286-75e0-bd7f-b86c292bcf63`.
- Couche : devops ; worktree `worktree/devops` ; branche `layers/devops`.
- Base : `6aee39172aebb0539c0972ef98a59e3e0ec15dca` ; aucune dépendance de code.
- Statut : validée humainement et commitée localement le 2026-10-30.

## Mission et périmètre

Appliquer les décisions de la demande : source unique dans le guide dédié des commits,
renvois depuis AGENTS et les procédures, contrôle Python des messages et plages
Git, tests et intégration aux contrôles qualité/CI.

Chemins autorisés : `README.md`, `AGENTS.md`, `docs/`,
`codebase-integrity/`, `.github/workflows/quality.yml`, cette carte et sa demande.
Exclure code applicatif, autres cartes hors correction de liens validée ci-dessous, ressources graphiques, données, `.env`,
skills personnels et autres worktrees. Aucun commit pendant l'implémentation.

## Critères et preuves attendues

- Respecter les décisions liées sans modifier architecture, autorisations ou historique.
- Vérifier tous les commits de la plage explicite, y compris un écart intermédiaire ;
  distinguer format du message et vérification des documents de référence.
- Tester conformités, écarts, traces de provenance, merges, références
  absentes ou ambiguës, historique superficiel et erreurs Git.
- Préserver les traces de cherry-pick ; laisser langue, infinitif et pertinence
  à la relecture humaine. Ne pas annoncer ces critères comme contrôlés automatiquement.
- Exécuter tests ciblés, `check.py`, `check_docs.py`, `check_demands.py` et contrôle
  des espaces ; qualité complète avant PR. Consigner résultats et limites ici.

Reconstitution : `demands/DEM-024` depuis develop dans le dossier principal libre
et propre, après verdict et commits de l'étape 04. Aucune branche créée ici.

## Résultat et preuves — 2026-10-30

Documentation Git organisée en sept chapitres ; conventions techniques dans son
README local. README principal inchangé. Pages d’interview des deux boucles
complétées pour éviter les références documentaires fragiles dans les demandes.
Guide des points de contrôle recentré sur le système. Les trois pages d’étape
revertées par l’humain ne sont pas reprises.

Contrôle Python du format avant commit et de chaque commit de la plage à livrer,
avec vérification des références dans l’arbre HEAD. Intégration à la qualité et
à la CI avec historique complet. Aucun mécanisme d’exceptions historiques.
Aucune documentation ajoutée dans Codebase Integrity.

Vérifications finales :

- `python3 codebase-integrity/scripts/check.py` : 81 tests réussis, dont 15 propres
  aux commits ; serveur HTTP local du test existant autorisé hors bac à sable.
- Contrôles documentaires et typage des demandes : conformes.
- Diff suivi et indexé : aucun défaut d’espaces.

Limites : CI distante et qualité applicative complète non exécutées ; elles
restent requises avant livraison. La plage finale sera vérifiée après reconstitution.

## Verdict humain

Verdict exact : « validé », après présentation des résultats et écarts de la revue.
Session intervenante : `01a18cd5-5286-75e0-bd7f-b86c292bcf63`.
Base : SHA indiqué en tête ; 23 chemins présentés, index déjà partiellement préparé.
Empreinte SHA-256 noms et contenus avant consignation du verdict :
`9567770ab70852af2f95a09bb498231982ed4e5d22e457e071cce1eeadf4f11b`.
Identité revérifiée avant ajout de ces seules traces documentaires.

Le périmètre validé inclut la suppression des renvois devenus caducs dans DEM-013,
DEM-018 et OPS-066, nécessaire après retrait de la section d’exécution.
Aucun changement fonctionnel depuis la présentation. Aucun push, PR ou merge.

## Commit local

Commit validé : `29f6a8dcd677e803cdcf808375f83a2cafda729d`. Périmètre vérifié : 23 fichiers,
preuves et verdict compris. Contrôle de la plage base → commit : conforme (un commit).
La présente consignation constitue une trace documentaire complémentaire.
