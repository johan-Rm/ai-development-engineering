# DEM-030 — Renommer app en apps

- Type : développement
- Date : 2026-11-06
- État : séparation de Codebase Integrity vers DEM-031 effectuée ; contrôles à reprendre, aucune livraison.
- Session de création : `01a1b040-6627-7b60-a2ec-ab2f985bf83d`

## Besoin et périmètre

Renommer le dossier racine `app/` en `apps/` pour organiser les applications
sous ce nom pluriel. Les utilisateurs concernés sont les contributeurs du dépôt.
Adapter toutes les références actives nécessaires : code, configuration, outillage,
CI, documentation et liens utiles, y compris dans les documents historiques.
Conserver les anciens chemins lorsqu’ils constituent des preuves historiques.

## Critères d’acceptation

- Les applications sont regroupées sous `apps/`, sans alias `app/`.
- Les applications, commandes locales et CI restent fonctionnelles.
- Les liens actifs vers les applications sont valides ; aucune référence active
  ne dépend de l’ancien emplacement.
- Les fichiers locaux, `.env` et données sont conservés.
- Aucun comportement fonctionnel applicatif ne change.

## Contraintes et exclusions

Appliquer les [conventions de typage](../README.md#types-de-demandes)
et le [routage des couches](../../docs/architecture/02-cadre/couches/organisation.md).
Le découpage déterminera les missions et contrôles adaptés aux chemins touchés.
Préserver les preuves historiques et le travail préexistant.
Cette interview ne réalise ni renommage, ni carte, ni opération Git de livraison.

## Vérifications attendues

Recherche des références résiduelles avec distinction entre usages actifs et preuves
historiques ; contrôle des liens, contrôles qualité du dépôt et vérifications
applicatives et locales proportionnées. Commandes exactes à résoudre au découpage.

## Décisions humaines et questions ouvertes

L’humain a retenu la conservation des chemins dans les preuves historiques,
puis les critères ci-dessus et confirmé le cadrage. Aucune question ouverte.

## Tâches issues du découpage

| Carte | Couche et branche | Dépendance |
| --- | --- | --- |
| [API-004](../tasks/API-004-deplacer-api-vers-apps.md) | api / `layers/api` | Aucune |
| [WEB-004](../tasks/WEB-004-deplacer-web-vers-apps.md) | web / `layers/web` | Aucune |
| [BO-004](../tasks/BO-004-deplacer-backoffice-vers-apps.md) | backoffice / `layers/backoffice` | Aucune |
| [OPS-081](../tasks/OPS-081-adapter-references-apps.md) | devops / `layers/devops` | Indépendante pour les références ; trois commits requis pour la preuve globale |

Analyse du 2026-11-06, même session : quatre branches existantes conservées,
propres et alignées sur `d42251e1dca1c4efd700a6a453f4bec80a2634c3` avant cartes ;
aucune mission concurrente identifiée. Aucun fetch, alignement ou commit effectué.
Le déplacement par couche respecte le routage ; une carte globale déplacerait
des contenus hors du périmètre Devops. Les trois premières cartes couvrent
le déplacement et la conservation ; OPS-081 couvre les références et la preuve globale.

OPS-081 adapte les références indépendamment ; ses contrôles globaux consommeront
les trois déplacements après validation et commits, sans copie non commitée. Les contrôles communs peuvent échouer
avant cette réunion : les références partagées sont volontairement traitées ensuite.
Reconstitution prévue dans le principal (`.`), branche `demands/DEM-030` depuis
le develop local vérifié ; demande définitive créée alors seulement. Le principal
porte actuellement une modification préexistante d’AGENTS.md : sa disponibilité
et sa propreté devront être résolues avant reconstitution, sans effacer ce travail.
Après fusion distante, retour prévu sur develop selon la procédure de livraison.

## Suivi d’implémentation

Le 2026-11-06, les trois cartes amont sont présentées à la vérification humaine ;
leurs preuves et limites figurent dans chacune des cartes liées dans la matrice.
Dépendance corrigée sur instruction humaine : OPS-081 peut être implémentée ;
seule sa vérification globale attend les trois commits amont.
La demande reste partielle ; aucune branche de réunion ni aucun commit créé.

OPS-081 implémentée sur instruction humaine : références et dépendance corrigées,
skills personnels et guides ajustés. Preuves, contrôles différés et incompatibilité
avec la règle de contribution de développement touchant Codebase Integrity : voir
la carte OPS-081. Les quatre cartes restent non commitées et à vérifier.

## Vérification humaine et commits

Verdict du 2026-11-06 : « validé » pour les quatre cartes avec les réserves
présentées. Empreintes vérifiées avant chaque commit ; aucune modification fonctionnelle.

| Carte | Commit validé | Trace documentaire |
| --- | --- | --- |
| API-004 | `0a68888028ac81d266c226af85fb796078bc2560` | `d346dcb3e9d407dcda7701e3fb140b4392f5583c` |
| WEB-004 | `633bb0bbbf4c127108b6c93c5505de2bd5834b03` | `1dc2c24b191285837534e093ba9f092d5ac22ed5` |
| BO-004 | `f68df8ed4dad8545d556c95f7394755892a1d7bb` | `0d8fe64c83a18a9f848f8435fc3eb22c8f5471a7` |
| OPS-081 | `48eab41ca24a990957f4e178135ea220378ee80e` | `e62d7f92f3333d3e071ef67ae031264717f9fb9d` |

Les quatre couches sont propres ; aucun push, reconstitution ou livraison effectué.
Les skills personnels validés restent hors dépôt. Les contrôles globaux et
l’incompatibilité avec la règle de contribution restent à résoudre avant livraison.

## Reconstitution

Le 2026-11-06, même session ; principal (`.`), branche `demands/DEM-030`
créée depuis develop local vérifié : `d42251e1dca1c4efd700a6a453f4bec80a2634c3`.
Aucun fetch, copie de travail non commité, push ou fusion. Retour prévu sur develop
après fusion distante. Modification étrangère d’AGENTS.md mise en stash sur
instruction humaine explicite « stash » ; stash conservé : `54cab4b443f54eb8f8e220997771c506e184cdf3`.

| Carte | Nature | Source | Obtenu |
| --- | --- | --- | --- |
| API-004 | implementation | `0a68888028ac81d266c226af85fb796078bc2560` | `ffb79dee5c611118b185ad9f24f988f664dd9e9b` |
| API-004 | trace | `d346dcb3e9d407dcda7701e3fb140b4392f5583c` | `6d1f442cb8929d7d534db8df32c6eef3b56c49c9` |
| WEB-004 | implementation | `633bb0bbbf4c127108b6c93c5505de2bd5834b03` | `f53225b192a168d1351d840efbce30ef433e7c15` |
| WEB-004 | trace | `1dc2c24b191285837534e093ba9f092d5ac22ed5` | `bbecfae11afb8ef96790306fb8d5f15f6c80d706` |
| BO-004 | implementation | `f68df8ed4dad8545d556c95f7394755892a1d7bb` | `403a75043c846a879e28616539b7ca8ea561670a` |
| BO-004 | trace | `0d8fe64c83a18a9f848f8435fc3eb22c8f5471a7` | `a8db31745acec5764772e1f035d8df05efeb5e8d` |
| OPS-081 | implementation | `48eab41ca24a990957f4e178135ea220378ee80e` | `a536906b8baa2e9911b0d6cd785c66750a0273eb` |
| OPS-081 | trace | `e62d7f92f3333d3e071ef67ae031264717f9fb9d` | `893d95257fc53f322f8f7fede1818934b2350ccc` |

### Contrôles de reconstitution

Huit cherry-picks sans conflit ; provenances et patch-id source/obtenu identiques.
HEAD reconstitué : `893d95257fc53f322f8f7fede1818934b2350ccc`.
Les 42 246 entrées locales résiduelles de l’ancien `app/` du principal ont été
réunies avec `apps/`, sans copie intermission ni écrasement. Inodes, modes, tailles
et dates des fichiers conservés ; dépendances, `.env` et données préservés.
L’ancien chemin `app/` est absent. Ces ressources locales restent ignorées.

`check_docs.py`, `check_demands.py`, `git diff --check` et la plage develop/HEAD :
réussis. Après déplacement des ressources locales, `quality.py` réussit :
documentation, types, 111 tests d’outillage, test API, vérifications Symfony,
contrat OpenAPI, typechecks et builds des deux interfaces.
L’échec initial des liens venait des dépendances locales restées sous `app/` ;
il est résolu sans exception ni changement de contrôle.

Limites : `quality.py` sans base ne vérifie ni contribution ni messages des commits.
Le document définitif reste non commité pour la trace de livraison ; la règle
interdisant une demande de développement touchant Codebase Integrity reste
incompatible avec OPS-081. Tests runtime et navigateur non exécutés sur une stack
réunie : aucune stack applicative ne doit être lancée dans le principal.
Les quatre worktrees de couche restent sur leurs branches `layers/*` ; stash
étranger conservé. Aucun push, PR, fusion ou passage automatique à la livraison.

## Tentative de livraison

Le 2026-11-06 : fetch autorisé effectué ; `origin/develop` vérifié à
`d42251e1dca1c4efd700a6a453f4bec80a2634c3`.
Candidat contrôlé : `04b7a20739c6eee2a88612e8793977c29698e79f`.
`check_commits.py --base origin/develop --head HEAD` : neuf commits conformes ;
`check_docs.py` réussi. Preuve applicative de reconstitution conservée ci-dessus.

`contribution.py --repo . --base origin/develop --head HEAD` : refus du commit
OPS-081 reconstitué `a536906b8baa2e9911b0d6cd785c66750a0273eb`, motif
« développement touchant codebase-integrity/ ». Vérificateur chargé depuis
la base distante vérifiée ; aucune règle ni exception modifiée.
La levée du blocage nécessite un arbitrage de convention à l’étape Analyse,
selon les [règles de contribution](../../docs/git-workflow/README.md#vérification).
Aucun push, PR, fusion ou alignement effectué ; branches, fichiers locaux et stash conservés.

## Séparation vers DEM-031

Instruction humaine du 2026-11-09 : transférer uniquement les deux fichiers
Codebase Integrity vers une consolidation distincte, sans déplacer les autres
changements d’OPS-081. Session intervenante identique à la session de création.
Anciennes tentatives ci-dessus conservées comme preuves historiques.
Historique antérieur préservé dans `archive/DEM-030-avant-separation` ; aucun
force-push, reset destructif ou rebase. Les ressources locales restent intactes.

| Carte | Nature | Source | Nouveau commit |
| --- | --- | --- | --- |
| API-004 | implementation | `0a68888028ac81d266c226af85fb796078bc2560` | `af541f8c183a0bcfb89561da004f982d6320baa8` |
| API-004 | trace | `d346dcb3e9d407dcda7701e3fb140b4392f5583c` | `28cd1dbc9f507782e85ead745f917eebadc9ef9f` |
| WEB-004 | implementation | `633bb0bbbf4c127108b6c93c5505de2bd5834b03` | `289edcf087948ef66929b2f4be1f7fc24dd9bebc` |
| WEB-004 | trace | `1dc2c24b191285837534e093ba9f092d5ac22ed5` | `aaf781c7574dc78e76908b278cb906cdb8dbe24d` |
| BO-004 | implementation | `f68df8ed4dad8545d556c95f7394755892a1d7bb` | `a1225cce19f207dd8c342a8ff822b238f1495da8` |
| BO-004 | trace | `0d8fe64c83a18a9f848f8435fc3eb22c8f5471a7` | `c646e9195c5698ddff3bef3e0c2254231507b17d` |
| OPS-081 | périmètre restant | `48eab41ca24a990957f4e178135ea220378ee80e` | `f37c01973e1fb4f2fd9a5fe941257621ad42536b` |

Les deux fichiers sont absents de tous les commits de la nouvelle plage DEM-030.
Le périmètre transféré est réservé dans `tmp/demande-adapter-lanceur-apps.md`
du principal ; demande définitive DEM-031 à matérialiser à sa reconstitution.
L’ordre de livraison reste à résoudre : le lanceur ancien utilise `app/`,
le nouveau utilise `apps/`. Aucune compatibilité ni règle de contrôle ajoutée.
