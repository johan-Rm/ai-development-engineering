# DEM-012 — Alléger les consignes des agents

- Date : 2026-10-28.
- État : reconstituée sur `demands/DEM-012` ; à livrer.
- Session de création : `01a1820d-ecd1-7600-8d49-1422ef8b8f1b`.
- Couche concernée : devops.

## Besoin et utilisateurs

L’humain et les agents doivent repérer rapidement les consignes décisives.
AGENTS.md mélange actuellement règles permanentes, procédures et documentation,
avec des répétitions qui réduisent son efficacité.

## Décisions confirmées

- Viser environ 60 lignes dans AGENTS.md ; chaque règle doit éviter une mauvaise décision.
- Conserver les références à consulter, le routage des missions, les limites
  d’intervention, les autorisations, les contrôles essentiels et les critères de fin.
- Ajuster les guides concernés pour conserver les règles déplacées ; renvoyer
  aux skills pour leurs procédures et supprimer les doublons.
- Employer des consignes concrètes, des chemins précis et des liens ciblés.
- Préserver les autorisations existantes, les validations humaines et le travail local.

L’exigence prioritaire demandée par l’humain est intégrée dans
[AGENTS.md](../../AGENTS.md#réponses-et-documents), qui en est la référence.

L’humain a choisi l’ajustement des guides puis confirmé le cadrage par « oui »
dans le chat. Cette confirmation ne valide aucune implémentation.

## Critères d’acceptation et preuves

1. AGENTS.md est ramené à environ 60 lignes utiles, sans répétition inutile.
2. Chaque règle retirée est conservée dans une référence adaptée ou identifiée
   comme un doublon ; aucune autorisation ni protection n’est perdue.
3. Les références sont valides et les documents concernés ne se contredisent pas.
4. Les contrôles essentiels et les conditions de fin sont directement repérables.
5. AGENTS.md contient l’exigence prioritaire référencée ci-dessus ; toute duplication
   nécessaire dans le correctif est justifiée et explicitement approuvée par l’humain.

Preuves attendues : diff, relecture de conservation des règles et autorisations,
vérification des liens et contrôles documentaires pertinents du projet.

## Contraintes et exclusions

Aucun changement du workflow, des autorisations ou du code applicatif.
La cible de longueur reste indicative : la précision des garde-fous prime.
Les skills personnels ne sont pas modifiés dans ce périmètre.

## Questions ouvertes

Aucune décision de besoin en attente. Destinations et preuves dans la carte.

## Tâches issues du découpage

| Carte | Affectation | Dépendance | Couverture |
| --- | --- | --- | --- |
| [OPS-065](../tasks/OPS-065-alleger-agents.md) | `worktree/devops`, `layers/devops` | Aucune | Critères 1 à 5 |

Une carte atomique évite une dépendance artificielle entre le retrait des règles
et leur centralisation. Base locale propre et alignée sur develop :
`2bd2a014dbfb41643a2ad8bc42c1cebb12fd5f74`. Aucun fetch ni commit au découpage.

Reconstitution prévue après validation et commit d’OPS-065 : branche
`demands/DEM-012` depuis develop local vérifié, dans le dépôt principal
(worktree relatif `.`), libre et propre ; retour sur develop après fusion distante.
Prévision exécutée lors de la reconstitution ci-dessous.


## Suivi d’implémentation

Résultat et preuves dans OPS-065. Carte unique réalisée ; aucune autre carte bloquée.
Correction humaine appliquée et validée : README dev-book inchangé ; aucune
intervention sur les conventions techniques.


## Verdict et commit

Validation humaine explicite du 2026-10-28 : « validé ».
OPS-065 : `b502f0d00e05b9f1f5e1ea1bb37a0239052ce785` ; réserve préexistante acceptée dans la présentation.


## Reconstitution

Dépôt principal, worktree relatif `.` ; branche `demands/DEM-012` créée depuis
le develop local propre `2bd2a014dbfb41643a2ad8bc42c1cebb12fd5f74`, sans fetch.
Branche à retrouver après fusion distante : `develop`. Worktrees de couche conservés.

| Commit source validé | Commit obtenu avec `cherry-pick -x` |
| --- | --- |
| `b502f0d00e05b9f1f5e1ea1bb37a0239052ce785` | `5d22e906c65b6fa4ec3b6bee347a4671bd2027a8` |
| `74219d6588d55636fa60dda0917953b518fb31f6` | `2804141f05fb5cbf691c531bc89aca14dda41120` |

Aucun conflit ; arbre des deux commits reconstitués identique à celui de la source
validée. Preuves qualité et réserve préexistante conservées dans OPS-065.
La demande définitive et les liens de sa carte sont intégrés au dossier de livraison.

Vérifications de reconstitution : `git diff --check` réussi ; 53 liens et ancres
locaux valides ; `python3 codebase-integrity/scripts/check.py` réussi (23 tests,
relance hors sandbox pour le serveur HTTP local). Qualité applicative déjà réussie
sur le contenu source identique ; non répétée à cette étape documentaire.


## Préparation de livraison

Historique source `layers/devops` rattaché par merge ciblé après vérification
de l’égalité des arbres avec les cherry-picks ; aucun changement de contenu.
Les cinq couches sont propres ; seules les contributions validées de DEM-012
divergeaient sur devops. Leur rattachement permet les avances rapides finales.


## Livraison

PR : https://github.com/johan-Rm/ai-development-engineering/pull/12
Source : `demands/DEM-012` ; cible : `develop` ; stratégie : merge commit.
Qualité complète de livraison réussie sur `f3dffef` (journal local
`/tmp/dem012-delivery-quality.log`) ; aucune modification applicative depuis.
Carte OPS-065 validée et commitée ; contrôles distants à vérifier avant fusion.
Suivi réel après fusion consigné dans le brouillon conservé sous tmp/.
