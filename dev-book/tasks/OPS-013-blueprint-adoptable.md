# OPS-013 — Un blueprint AIOD adoptable

- État : clôturée le 2026-10-06
- Date : 2026-10-05
- Demande : rendre les documents AIOD plus faciles à intégrer depuis un dépôt GitHub public.
- Rattachement historique : maintenance du cadre
- Affectation : session Codex, sur la branche historique de maintenance, dossier
  `.`.
- Dépendance : socle initial `9a60e1c`.

## Périmètre

Documentation `docs/aiod/`, entrées des assistants, dev-book, scripts et tests Git.
Aucun dossier templates. Aucun framework, service, publication, push ou profil personnel requis.

## Critères d’acceptation

- Un lecteur peut comprendre, adopter et essayer le workflow avec Git et Python 3.
- Les consignes sont communes et les responsabilités explicites.
- Le créateur conserve les données et refuse les destinations incompatibles.
- Les tests ne modifient pas le dépôt utilisateur et ne contactent pas son remote.
- Le parcours manuel est prêt à être essayé avec l’utilisateur.

## Preuves

- `python3 -B codebase-quality-control/scripts/check.py` : neuf scénarios Git validés dans des dépôts jetables.
- Les cinq couches (backoffice, API, web, devops et design) sont documentées et déclarées dans `codebase-quality-control/scripts/aiod.json`.
- Les documents originaux ont été déplacés sans modification dans `docs/aiod/sources/`.
- La recette humaine est décrite dans `docs/aiod/premiere-tache.md`, à effectuer ensemble.
- Aucun service n’est configuré ; la stack de l’exemple concret reste à définir.

Verdict humain : blueprint accepté dans l’échange. Les essais Git automatisés valident les invariants ; le parcours manuel reste disponible pour une recette accompagnée. Aucun service applicatif demandé.
