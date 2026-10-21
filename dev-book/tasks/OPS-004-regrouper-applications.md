# OPS-004 — Regrouper les applications

- Statut : réalisée.
- Date : 2026-10-21.
- Mission : devops, branche `layers/devops`, worktree `/home/johan/www/lab/ai-orchestrated-development/worktree/devops`.
- Demande : rassembler `api/`, `backoffice/` et `web/` sous `app/`.
- Périmètre : déplacement des dossiers, commandes applicatives, CI, documentation, liens et tests concernés.
- Dépendance : OPS-003, commit `16856b9`.
- Critères : applications sous `app/`, commandes adaptées, cinq couches conservées et liens cohérents ; aucun changement métier.
- Preuves attendues : tests de l’outillage, résolution des cibles et du contrat API, test du schéma et contrôle du diff.

## Livré et vérifié

- Applications déplacées sous `app/api/`, `app/backoffice/` et `app/web/`.
- README commun ajouté ; commandes, CI, documentation et liens relatifs adaptés.
- Tests applicatifs conservés dans leurs applications ; noms des couches inchangés.
- Suite Python : 17 tests réussis, dont installation backoffice depuis le nouvel emplacement.
- Résolution des trois cibles et lecture de leurs manifestes : réussies ; contrat OpenAPI présent.
- Commandes `process.py info` et `worktrees.py list` : réussies.
- Test Chromium du schéma : réussi après déplacement.
- `git diff --check` : réussi.
- Builds complets et tests applicatifs réels non relancés : les dépendances ne sont pas
  installées dans ce worktree. Aucun comportement métier ni dépendance modifiés.
