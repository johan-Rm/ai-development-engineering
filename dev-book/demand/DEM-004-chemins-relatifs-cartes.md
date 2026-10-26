# DEM-004 — Utiliser des chemins relatifs dans les cartes

- Date : 2026-10-26.
- État : validée.
- Confirmation humaine : « oui, go », après restitution du cadrage dans le chat.
- Session : référence de session indisponible.
- Carte externe : aucune.

## Contexte et problème observé

Le renommage du dossier du projet révèle des chemins personnels absolus dans les
cartes de tâches. Ces chemins dépendent de la machine et deviennent obsolètes après
un déplacement du dépôt. Les consignes d’affectation demandent actuellement un
worktree absolu, tandis que le README du dev-book prévoit déjà la neutralisation
des chemins personnels historiques.

Les personnes et agents qui lisent les cartes ou exécutent les missions ont besoin
de références portables, tout en vérifiant précisément leur dossier de travail.

## Résultat attendu

Les cartes versionnées utilisent des chemins relatifs à la racine du dépôt principal,
par exemple `worktree/devops`. Cette origine reste explicite même lorsqu’une carte
est consultée depuis un worktree de couche. Le chemin absolu est résolu et vérifié
uniquement lors de l’exécution, avec la branche et l’état Git.

## Périmètre et contraintes

- Corriger les cartes ouvertes et clôturées, y compris leurs chemins personnels historiques.
- Harmoniser les consignes et guides concernés pour empêcher la réapparition de ces chemins.
- Conserver le sens des preuves historiques, leurs dates, SHA et statuts ; les originaux
  restent consultables dans l’historique Git.
- Préserver le travail existant et les fichiers `.env`.
- Lors de l’interview : aucun commit, push, PR ou merge. L’invocation ultérieure
  d’`implementer-demande` autorise le commit local d’implémentation, sans réécriture
  d’historique ni opération distante.

## Critères d’acceptation

1. Les affectations des cartes désignent leurs worktrees relativement au dépôt principal.
2. Les documents concernés ne contiennent plus de chemins personnels absolus vers ce dépôt.
3. Les consignes et guides distinguent la référence relative versionnée du chemin absolu
   résolu et vérifié à l’exécution ; aucune règle concernée n’impose sa persistance dans une carte.
4. Les cartes clôturées restent des traces historiques et ne sont pas rouvertes par la correction.
5. Une recherche des chemins personnels et une relecture des références corrigées apportent
   la preuve du nettoyage ; les contrôles pertinents du projet réussissent.

## Exclusions

- Réparation des liens Git des worktrees après déplacement du dépôt.
- Modification ou redémarrage des environnements Docker.
- Modification des skills personnels hors du dépôt : aucun changement de ces fichiers
  n’a été demandé dans ce cadrage.

## Décisions humaines

- Choix explicite : chemins relatifs au dépôt principal, par exemple `worktree/devops` ;
  chemin absolu résolu seulement lors de l’exécution.
- Cadrage confirmé : correction des cartes, y compris clôturées, et des consignes et guides ;
  vérification de l’absence de chemins personnels et contrôles pertinents.
- La confirmation du besoin ne constitue pas une validation d’un résultat implémenté.

## Questions ouvertes

Aucune question de besoin bloquante. Le découpage devra préciser les documents et
contrôles concernés à partir de l’inventaire des occurrences.

## Tâches issues du découpage

| Carte | Couche | Couverture | Ordre et dépendances |
| --- | --- | --- | --- |
| [OPS-049 — Rendre les chemins documentaires portables](../tasks/OPS-049-chemins-relatifs-cartes.md) | devops | Critères 1 à 5 : cartes ouvertes et historiques, demandes liées, consignes, guides et preuves | Carte unique ; aucune tâche amont à produire |

## Réunion prévue

- Branche dédiée : `demands/DEM-004`.
- Worktree prévu : `worktree/DEM-004`, relativement au dépôt principal.
- Création à la reconstitution seulement, après identification du commit validé d’OPS-049.
- Ne pas réunir la demande sur `develop`, `master` ou une branche de couche.

## Preuve du découpage — 2026-10-26

Historique de toutes les références Git locales et fichiers des worktrees examinés sans
fetch : maximum OPS-048, d’où OPS-049. Aucun doublon correspondant au besoin trouvé.
Branche locale `layers/devops` conservée au commit
`ce9fca295d748188c03f65e0d056011a036a621b`, sans rebase ni synchronisation distante.
Avant écriture, seul ce document DEM-004 était non suivi ; aucune mission en cours
n’a été identifiée dans les cartes devops consultées. Cette lecture ne garantit pas
l’absence d’une session concurrente : revérifier la disponibilité avant implémentation.

Les commandes Git ordinaires du worktree échouent, car son fichier `.git` pointe encore
vers l’ancien emplacement. L’état a été lu en passant explicitement à Git les chemins
locaux actuels des métadonnées et du worktree, sans modifier ces liens.
La branche existe, mais l’environnement n’est pas annoncé prêt. Réparation à traiter
séparément, puis revérification de la branche, de l’état et de la disponibilité.
Aucun commit, création de branche, fetch ou opération distante pendant le découpage.

## Implémentation — 2026-10-26

OPS-049 couvre les cinq critères ; résultats et limites détaillés dans sa carte.
Les 36 références personnelles au dépôt sont remplacées par des chemins relatifs,
ainsi que les références génériques de mission encore préfixées par le placeholder
historique du dépôt. Les consignes précisent l’origine commune et la résolution locale.
Les références aux skills externes sont neutralisées par un placeholder documenté.
Dates, SHA, statuts et verdicts des documents historiques sont préservés.

Le lien Git n’a pas été réparé. Le démarrage a été rendu possible en désignant
explicitement les métadonnées et le worktree actuels pour les commandes Git, sans
modification de ces fichiers. Le blocage signalé au découpage reste une limite des
commandes Git ordinaires, mais ne bloque plus cette implémentation documentaire.
Qualité complète réussie hors sandbox, après un refus de socket local dans le sandbox.
Commit local d’OPS-049 créé avec cette demande ; SHA communiqué dans le chat.
Aucun verdict humain, aucune reconstitution ni opération distante à cette étape.

## Verdict humain — 2026-10-26

Verdict explicite dans le chat : « validé », après présentation des cinq critères,
des preuves et de la limite du lien Git cassé, hors périmètre.
La validation globale couvre DEM-004 et sa seule carte OPS-049, sur le commit
d’implémentation `60ccb2acdc9436eefc709845b49a6174c96ac181`.
Les cinq critères sont acceptés ; aucune correction demandée.

Branche `layers/devops` et arbre propre vérifiés avant consignation, en désignant
explicitement les métadonnées Git actuelles. Seules DEM-004 et OPS-049 sont modifiées
pour ce verdict et son commit documentaire. Aucun code modifié, aucune réparation Git,
aucun push, PR ou merge. Reconstitution et livraison restent à lancer séparément.

## Preuve de reconstitution — 2026-10-26

Branche dédiée `demands/DEM-004`, worktree `worktree/DEM-004`, créés à la tête
`083dcbee81570fd8770bb211cee2dfb46a881284`, après vérification de leur absence.
Base locale de la carte : `ce9fca295d748188c03f65e0d056011a036a621b`.
Les seuls commits de contribution au-dessus de cette base sont, dans cet ordre :

1. `60ccb2acdc9436eefc709845b49a6174c96ac181` : implémentation validée d’OPS-049.
2. `083dcbee81570fd8770bb211cee2dfb46a881284` : trace du verdict humain.

Leur ascendance dans la branche dédiée est vérifiée par `git merge-base --is-ancestor`.
Les commits étaient déjà réunis : aucun rejeu, cherry-pick, conflit ni copie de fichiers
non commités. Aucune branche existante déplacée ; intégration et production inchangées.
La base locale et son historique sont conservés, sans fetch ni affirmation de synchronisation
distante. La référence locale `origin/develop` est absente au moment de cette étape ;
la comparaison avec la cible distante restera à faire lors de la livraison autorisée.

Contrôles dans le worktree de réunion :

- branche `demands/DEM-004`, index et arbre propres avant la preuve ;
- `git diff ce9fca295d748188c03f65e0d056011a036a621b HEAD --check` réussi ;
- recherches des anciens chemins personnels dans cartes et demandes : aucune occurrence ;
- liens réciproques de DEM-004 et OPS-049 valides ;
- `python3 codebase-integrity/scripts/check.py` : 23 tests réussis hors sandbox,
  nécessaire pour le test HTTP local.

La qualité complète a réussi sur le même contenu d’implémentation dans le worktree
source ; elle n’est pas relancée dans ce nouvel arbre sans dépendances applicatives
installées. Aucun changement applicatif ou de contrat n’est ajouté par la reconstitution.
Aucune preview, aucun service applicatif démarré ni environnement Docker modifié.
Les anciens liens Git cassés des autres worktrees restent hors périmètre ; le nouveau
worktree de réunion fonctionne avec les commandes Git ordinaires.

Demande reconstituée et prête pour l’étape de livraison ; aucun push, PR ou merge effectué.
La présente preuve est conservée dans un commit documentaire sur la branche dédiée.

## Ajustement de livraison confirmé — 2026-10-26

Décision humaine explicite : livrer uniquement les chemins relatifs et conserver les
règles de workflow actuelles de `develop`. Les effets des commits antérieurs hors demande
`2c9aeb3` et `ce9fca2` sont donc exclus du diff final, sans réécrire l’historique.

La cible distante observée est `63313b9cda819f1d6b7d672925537f58b4dec4d1`.
Intégration de cette cible dans la branche dédiée par merge commit. Les conflits add/add
sur DEM-003 et OPS-048 sont résolus en conservant intégralement leurs documents distants,
avec uniquement les substitutions de chemins de DEM-004. Les dates, SHA et statuts
historiques distants sont comparés et préservés. Les guides de livraison restent identiques
à la cible ; aucun changement graphique, applicatif ou du Codebase Integrity.
Les quatre documents partagés reçoivent seulement le patch de chemins d’OPS-049,
appliqué aux versions distantes. Le résultat demandé et validé est conservé.

## Préparation de livraison — 2026-10-26

Qualité complète réussie (code de sortie 0) sur
`c227f0140aeb429dae7be88e5c7ae64395a3c9e0`, après installation verrouillée par
`python3 codebase-integrity/scripts/apps.py install all` dans le worktree de réunion.
Commande : `python3 codebase-integrity/scripts/quality.py`, hors sandbox pour les
sockets localhost des tests. Journaux locaux : `/tmp/DEM-004-install.log` et
`/tmp/DEM-004-quality.log`. Les 23 tests d’outillage, le contrat API, le lint Symfony,
le mapping Doctrine, la comparaison OpenAPI, les types et builds web/backoffice passent.
La synchronisation du schéma est exclue par le contrôle existant `--skip-sync`.
Aucune modification de dépendance versionnée ou de fichier `.env` existant.

Le diff final depuis `origin/develop` porte sur les 48 fichiers autorisés : consignes,
README, guides des missions, cartes et demandes. Comparaison exhaustive des documents
historiques avec la cible : uniquement les substitutions de chemins attendues.
Recherche de chemins personnels et liens DEM-004/OPS-049 réussis ; `git diff --check`
réussi. Aucun changement de workflow, de graphique, d’application ou de contrôle.
Seule la présente preuve documentaire est ajoutée après les contrôles.

Distant vérifié : dépôt `johan-Rm/ai-development-engineering`, branche par défaut
`develop`, merge commit permis ; cible non protégée et aucun ruleset observé.
Aucune PR existante pour la branche DEM-004 lors de la recherche préalable.
Les commits originaux validés restent ancêtres de la branche ; leurs effets hors périmètre
hérités ont été exclus du résultat final selon la décision humaine.
Livraison prévue uniquement vers `develop`, sans promotion vers `master`.
