# OPS-071 — Définir le README de la documentation

- Date : 2026-10-30 ; état : validée et commitée localement (périmètre réduit), à reconstituer.
- Session de création : `01a18b7d-7bf6-7582-921d-c2f516c32379`.
- Demande : DEM-020 ; source actuelle : `tmp/demande-readme-documentation.md`
  relativement au dépôt principal, sans copie dans la couche.
- Fichier futur : `dev-book/demand/DEM-020-readme-documentation.md`, à matérialiser
  seulement à la reconstitution ; absent au découpage.
- Mission : devops ; worktree `worktree/devops` ; branche `layers/devops`.
- Base locale vérifiée : `907ffee98240ddefb6ada9fd0cba47d07d27d641`, commune avec develop.
- Dépendances par commits : aucune contribution amont identifiée. Aucun fetch réalisé.

## Objectif et chemins autorisés

Décision humaine du 2026-10-30, session identique : aucune exception à la
consolidation. Le périmètre ci-dessous est remplacé par la seule création de
`docs/README.md`, avec les responsabilités retenues et le chapitre « Conventions
techniques » vide. AGENTS.md, le guide, les noms et les index restent inchangés.
Les critères antérieurs portant sur ces changements sont reportés à la consolidation.
Le brief de déclenchement est fourni dans le chat ; aucune consolidation démarrée.
La condition de préparation ci-dessous est donc levée pour ce seul périmètre réduit.

Créer `docs/README.md` selon le contenu retenu dans la demande, ajouter la consigne
convenue dans `AGENTS.md` et ajuster `docs/architecture/02-cadre/documentation.md`
pour supprimer les doublons et contradictions. La demande est la référence du
contenu ; ne pas le recopier dans cette carte.

Chemins autorisés : ces trois fichiers et cette carte pour les preuves et le verdict.
Lire leurs README parents avant intervention. Aucun changement applicatif, de skill,
de contrôle, d’autorisation Git ou de donnée ; aucun renommage global sous couvert
de cette carte. Préserver les historiques, worktrees et `.env`.

## Critères et preuves attendus

- Couvrir les critères de DEM-020 : structure officielle, rédaction et organisation
  retenues, conventions définies dans le README, consigne des agents, guide cohérent.
- Vérifier que les index restent des tables des matières et que les citations
  concernent les chapitres explicatifs. Relever les écarts existants sans les masquer.
- Relire le diff, contrôler les liens et ancres des fichiers modifiés ; exécuter
  `git diff --check` et `python3 codebase-integrity/scripts/check.py` depuis la couche.
  Qualité complète avant PR : `python3 codebase-integrity/scripts/quality.py`.
- Consigner ici commandes, résultats, limites et fichiers présentés. Pas de tests
  applicatifs spécifiques ajoutés pour ces seuls changements documentaires.
- Aucun commit pendant l’implémentation ; validation humaine du résultat distincte
  du cadrage. Aucun contrôle exécuté à ce stade.

## Condition de préparation

AGENTS.md impose la consolidation pour faire évoluer les conventions techniques
et leurs contrôles. DEM-020 définit notamment l’absence de numérotation et des index
limités aux tables des matières, alors que `docs/architecture/` contient des noms
numérotés et des index explicatifs (par exemple celui des couches).

La migration de ces contenus et l’éventuelle adaptation des contrôles ne sont pas
cadrées. Résoudre leur traitement par la boucle de consolidation avant de déclarer
la mission prête ; ne pas déduire une exception de la demande de découpage.
Si des commits amont sont nécessaires, inscrire leurs SHA avant consommation.

## Disponibilité et suite

### Verdict humain — 2026-10-30

« validé » pour OPS-071 sur le périmètre réduit présenté : README avec responsabilités
et conventions techniques vides. Qualité complète restante avant PR.
Branche, HEAD et index revérifiés ; seuls les deux fichiers attendus sont non suivis.
Empreintes SHA-256 identiques à la présentation, avant ajout du verdict :

- `docs/README.md` : `f4f15ab6880af70603a58dd565325104a72f0b28492ed36b18f5b3c002c0298f`.
- Cette carte : `235dcc986bf91fd0deef14c83edea42a550deb6415cc9cb87194603e864ed172`.

Aucune modification fonctionnelle après présentation ; aucune livraison autorisée ici.

Commit local de la contribution validée : `eee753443ea29b80dd691fdca48a4338dc247fb6`.
Le commit documentaire suivant consigne uniquement cette trace ; aucun push ni PR.

### Preuves d’implémentation — 2026-10-30

HEAD inchangé : `907ffee98240ddefb6ada9fd0cba47d07d27d641`. Deux fichiers non
suivis présentés : `docs/README.md` et cette carte ; aucun fichier suivi modifié.
README relu : responsabilités conformes à la demande, section des conventions
vide, aucun lien à vérifier dans ce nouveau fichier. AGENTS.md et guide inchangés.
`git diff --check` réussi (ne couvre pas les nouveaux fichiers non suivis).
`python3 codebase-integrity/scripts/check.py` : 30 tests réussis hors sandbox,
après un premier échec dû à l’interdiction d’ouvrir le socket HTTP temporaire.
Qualité complète non exécutée à cette étape, obligatoire avant PR.
Aucun commit ni verdict humain sur le résultat.

Branche existante conservée, index vide et arbre propre avant création de cette carte.
Aucune mission concurrente active identifiée : DEM-016 et DEM-019 seulement cadrées ;
dernière contribution devops OPS-070 intégrée à la livraison DEM-018 clôturée.
Maximum OPS observé : 070, historique de toutes les références locales et fichiers
des worktrees examinés sans fetch ; identifiant OPS-071 réservé ici.

Après résolution de la condition, implémentation puis vérification humaine.
Reconstitution prévue dans le principal (`.`), libre et propre, sur
`demands/DEM-020` créée depuis develop local vérifié, par cherry-pick des seuls
commits validés. Retour du principal sur develop après fusion distante ; les
couches conservent `layers/*`. Aucune branche créée ni implémentation au découpage.
