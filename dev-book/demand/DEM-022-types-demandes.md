# DEM-022 — Définir les types de demandes

- Type : consolidation
- Date : 2026-10-30.
- Session de création : `01a18b94-1588-7021-869d-d11d9ff6ba72`.
- État : OPS-072 validée et commitée localement le 2026-10-30 ; à livrer.
- Couche : devops ; worktree `worktree/devops` ; branche `layers/devops`.
- Continuité documentaire de la même session : seule DEM-021 préexistait non commitée, identifiée et préservée ; index vide. Aucune mission d’implémentation ouverte.

## Constat et besoin

DEM-021 porte un champ « Type : consolidation »
alors que le [README du dev-book](../README.md) ne définit ni ce champ ni ses valeurs.
Les interviews de [développement](../../docs/architecture/03-developpement-loop/01-interview.md)
et de [consolidation](../../docs/architecture/04-consolidation-loop/01-interview.md)
ont des sorties distinctes sans format commun explicite pour identifier leur boucle.
Formaliser cette distinction évitera une interprétation au cas par cas.

## Convention technique

La définition en vigueur figure dans le [README du dev-book](../README.md#types-de-demandes).

## Arbitrage humain — 2026-10-30

Confirmation : « Oui, tous les autres points », après exclusion des rapports
d’analyse séparés : « on ne conserve pas les analyses pour le moment ».
Leur contenu peut éventuellement figurer dans le corps d’un futur commit ou dans
la PR ; cette possibilité n’autorise pas leur création à cette étape.

- Définition unique dans le README du dev-book ; liens depuis AGENTS.md, guides
  et les deux skills personnels d’interview, adaptés séparément hors dépôt.
- Un seul champ en métadonnées : `- Type : développement` ou
  `- Type : consolidation`, sans point final ; normaliser les demandes récentes.
- Champ obligatoire pour les nouvelles demandes et toute demande modifiée ou
  renommée, correction mineure comprise. Les 18 historiques inchangées restent
  exemptées, sans classification rétrospective ni réécriture de leurs décisions.
- Besoin mixte : deux demandes liées avec dépendance explicite.
- Changement de type : confirmation humaine, ancien et nouveau type, motif,
  session intervenante et état de reprise ; aucun transfert automatique de verdict.
- Contrôle bloquant sur le format, intégré à quality.py : inventaire figé des
  chemins et empreintes historiques, sans dépendance à Git distant. Aucune
  extension automatique des exemptions pour masquer un écart.
- Revue humaine du choix du type et de la cohérence de la boucle suivie.
- Périmètre : documentation et outillage devops, adaptations des deux skills
  personnels ; aucune autorisation Git modifiée, aucun changement applicatif.

Preuves requises : tests des deux valeurs, champ absent hors exemption, valeur
inconnue, doublons, exemptions inchangées/modifiées/renommées et erreurs de lecture
ou d’inventaire ; distinguer métadonnées et exemples. Exécuter le vérificateur sur
le corpus, les tests d’outillage et la qualité complète avant PR.

### Révision prioritaire — 2026-10-30, même session

Décision humaine : « inutile de se préoccuper des demandes legacy, on corrige
c’est tout, ensuite on vérifie avec les tests que tout soit conforme ».

Remplace les décisions de migration progressive et d’inventaire ci-dessus : typer
immédiatement toutes les demandes, sans exemption ni fichier d’empreintes ; appliquer
le même contrôle bloquant à chacune. Conserver leurs décisions, verdicts et sessions
d’origine : le typage ajouté ne prouve pas la boucle historiquement suivie.
Vérifier ensuite le corpus complet et les cas d’erreur par les tests. Les autres
points adoptés restent applicables.

Correction humaine supplémentaire : dans AGENTS.md, écrire l’instruction de typage
et de routage directement, sans renvoi documentaire pour cette consigne.
SETUP.md est exclu du changement ; son ajout est retiré à la demande humaine.
Dernière révision : convention réduite à l’indication du type ; ponctuation finale
facultative, acceptée par le contrôle. Les explications supplémentaires du README
sont retirées à la demande humaine.

Le rapport d’analyse séparé est supprimé conformément à la réserve humaine.
Aucun autre point de la proposition présentée ne reste non tranché.

## Limites et suite

Cette demande concerne le format et le routage des demandes, distincts des conventions
documentaires de DEM-021. Carte : [OPS-072](../tasks/OPS-072-types-demandes.md),
qui conserve les preuves, limites, verdict humain et SHA du commit.

Révision humaine : la validation en consolidation déclenche les commits locaux,
comme en développement. Skills, AGENTS.md et guide de vérification alignés ;
nouvelle présentation validée par « validé » ; commits locaux autorisés.

## Livraison — 2026-10-30, même session

Commits validés réunis par avance rapide sur `demands/DEM-022` depuis develop
`b40faca917b01074d078e49ad1cad6f7fb2ff7b6`, dans le principal initialement propre.
L’humain confirme que l’invocation autorise la livraison complète et demande
l’alignement du skill : `livrer-consolidation`, AGENTS.md et guide corrigés.
DEM-021 reste hors livraison ; son lien local est remplacé par son identifiant.

Qualité de livraison réussie sur `3fe38fca51bab7a2ea972e688601240344985f5a` dans devops :
39 tests d’outillage, contrôles API, types et builds web/backoffice ; journal
`/tmp/dem022-delivery-quality.log`. Corpus commité vérifié séparément : 19 demandes
conformes, sans DEM-021. Changements suivants limités aux consignes et traces.

Couches propres et sans autre mission active identifiée : API, web, backoffice.
Design contient trois `.gitkeep` non suivis ; devops contient DEM-021 non suivie.
Ces deux couches restent intactes et bloqueront la clôture de leur alignement.
