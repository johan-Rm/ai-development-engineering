# DEM-020 — Définir le README de la documentation

- Date : 2026-10-30.
- Session de création et d’intervention : `01a18b7d-7bf6-7582-921d-c2f516c32379`.
- État : validée et reconstituée sur `demands/DEM-020`, à livrer.

## Besoin et décisions humaines

Donner aux contributeurs humains et agents un README pour organiser et rédiger
la documentation au fil des développements. Cadrage confirmé par « super le cadrage
est good », complément AGENTS.md initialement accepté par « go ».

L’humain a ensuite refusé toute exception au passage par consolidation : « ensuite
tu pourra creer le README avec le chapitre convention technqiues vide ».
Le périmètre définitif se limite donc au [README documentaire](../../docs/README.md),
avec les responsabilités validées et le chapitre « Conventions techniques » vide.
Le contenu livré fait référence ; aucune copie conservée ici.

## Critères et exclusions

- Structure : titre, description, « Rôle et responsabilités », « Conventions techniques ».
- Responsabilités : documentation au fil du développement, thématiques principales
  directement sous docs/, niveaux supplémentaires selon le besoin, sujet expliqué
  dans un document unique et liens depuis les autres, détails complémentaires.
- Chapitre des conventions vide ; aucun changement d’AGENTS.md, du guide, des noms,
  des index, des contrôles ou des applications.
- Conventions proposées et consigne des agents reportées à une consolidation distincte,
  non démarrée. Brief fourni dans le chat : noms sans numérotation, index limités
  aux tables des matières, citation introductive des chapitres explicatifs,
  rédaction concise, terme « convention technique » et définition des règles dans
  les README. Examiner les migrations et contrôles dans cette autre boucle.

## Carte et vérification humaine

| Carte | Mission | Dépendances | État |
| --- | --- | --- | --- |
| [OPS-071](../tasks/OPS-071-readme-documentation.md) | devops, `worktree/devops`, `layers/devops` | Aucune sur le périmètre réduit | Validée et commitée |

Verdict humain : « validé » après présentation du périmètre réduit et des limites.
Les preuves, empreintes et résultats des tests sont conservés dans la carte.

## Reconstitution — 2026-10-30

Principal (`.`) libre, propre et sur develop avant création de la branche ; dernière
livraison DEM-018 clôturée, autres demandes identifiées seulement cadrées.
Base locale : `907ffee98240ddefb6ada9fd0cba47d07d27d641`. Aucun fetch.

| Commit source validé | Commit obtenu avec provenance `-x` |
| --- | --- |
| `eee753443ea29b80dd691fdca48a4338dc247fb6` | `3e4491b0cb9befca65a9b15e4bf41e6cdb2a2a9c` |
| `35ea9949bc0276ff633655e6dca50ac6c6f36cb8` | `6fe121d761294b11dd16e9eeb6cfe04067da99dd` |

Cherry-picks sans conflit ; `git diff --exit-code layers/devops HEAD` réussi avant
matérialisation. Brouillon d’origine conservé dans tmp/, sans copie de travail
non commité d’une couche. Carte reliée à cette demande ; seules les traces
documentaires de reconstitution restent non commitées pour la livraison.
Principal conservé sur `demands/DEM-020`, retour prévu sur develop après fusion
distante ; couches conservées sur `layers/*`. Aucun push, PR ou fusion ici.

Contrôles : 30 tests d’outillage réussis, 3 liens locaux valides, empreinte du
README identique au résultat validé et `git diff --check` réussi. Qualité complète
restante avant PR.

## Préparation de livraison — 2026-10-30

Après fetch autorisé, origin/develop confirme la base locale
`907ffee98240ddefb6ada9fd0cba47d07d27d641`. Cible et branche par défaut : develop ;
merge commit permis, branche non protégée selon GitHub. Aucune PR existante pour
demands/DEM-020. Les cinq couches sont propres et aucune autre mission active
identifiée ; DEM-016 et DEM-019 seulement cadrées.

Les deux seuls commits divergents de devops sont les sources validées d’OPS-071.
Leur rattachement ciblé dans la branche de livraison permet les avances rapides
finales ; aucun changement du contenu validé n’est permis.

Rattachement effectué : `e6eb0d2`. Conflit limité à la carte documentaire résolu
avec sa version reconstituée ; arbre strictement identique au premier parent.
Qualité complète locale réussie : `python3 codebase-integrity/scripts/quality.py`,
code 0 ; journal `/tmp/dem020-quality.log` (tests d’outillage, API, types et builds
web/backoffice). Seules des traces documentaires ont changé depuis le lancement.
