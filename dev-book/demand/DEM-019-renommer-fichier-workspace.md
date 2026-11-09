# DEM-019 — Renommer le fichier workspace

- Date : 2026-10-29.
- Type : consolidation
- Session de création : `01a18820-739b-71f2-8c66-bdf77fe2dd9e`.
- Session intervenante : `01a19ce5-e7cc-7623-88ec-2098a3afb7b0` (2026-11-02).
- Session intervenante : `01a1c0bc-2805-70e1-a520-6daa5dd4d039` (2026-11-09).
- État : Reconstituée sur `demands/DEM-019`, à livrer ; réserves conservées. Réserves levées lors de la recette finale, voir OPS-083.
- Couche concernée : devops ; mission OPS-083 en cours.

## Besoin et utilisateurs

Pour les utilisateurs du workspace VS Code, remplacer le nom technique
`aide.code-workspace` par `ai-powered-development-engineering.vscode-worktree`.
Ce choix confirmé le 2026-11-09 remplace les noms précédemment envisagés.
Convention proposée à examiner : employer le nom du projet suivi de
`.vscode-worktree` pour le workspace et ses références actives.

## Périmètre et critères observables

- Renommer le fichier à la racine sans modifier son contenu ; l’ancien fichier disparaît.
- Adapter les références actives de la documentation, du script de préparation
  et de ses tests, notamment dans `codebase-integrity/`.
- Adapter la cible de l’alias personnel dans `~/.bash_aliases`, en conservant
  son nom et les autres alias ; vérifier la syntaxe Bash et la cible chargée.
- Vérifier l’identité du contenu, l’absence de références actives à l’ancien nom,
  le fonctionnement de la préparation et la réussite des tests adaptés.
- Vérifier humainement l’ouverture effective du même workspace dans VS Code
  avec le nom final exact ; une ouverture non vérifiée reste à signaler.
- En cas d’incompatibilité du nom final, arrêter et soumettre le blocage à
  l’humain avant toute adaptation de la commande d’ouverture.

## Contraintes et exclusions

Préserver les traces historiques, les réglages du workspace, les worktrees,
les `.env` et les données. Aucun changement applicatif ni nouveau comportement
du workspace. Le point antérieur relatif à un commit de concision dans
`AGENTS.md` reste hors de cette reprise du cadrage. Le fichier personnel extérieur au dépôt reste soumis aux permissions
de l’environnement à l’implémentation.

## Coordination et questions ouvertes

Le [DEM-018](DEM-018-setup-commandes.md) prévoit de générer le workspace
et d’installer le même alias : coordonner ces travaux avec le nom décidé ici.
La [demande historique DEM-015](DEM-015-renommer-alias-workspace.md)
décrit l’alias existant et reste inchangée.
Test exploratoire du 2026-11-09 : une copie temporaire identique nommée
`vscode-worktree.ai-powered-development-engineering` a été ouverte par
`code --new-window` (code 0 après autorisation de la socket locale).
L’humain confirme avoir observé le workspace avec ses dossiers. Cette preuve
ne porte pas sur le nom final retenu, qui reste à tester.

Aucune question de besoin ouverte. La confirmation porte sur le cadrage,
pas sur un résultat implémenté.

## Tâches issues du découpage

| Carte | Couche / branche | Couverture | Dépendances |
| --- | --- | --- | --- |
| [OPS-083](../tasks/OPS-083-renommer-fichier-workspace.md) | devops / `layers/devops` | Tous les critères | Aucune dépendance de réalisation |

Reconstitution prévue sur `demands/DEM-019` depuis develop local vérifié dans le
principal (`.`), libre et propre. Branche créée uniquement à l’étape 05 ; retour
sur develop après fusion. Les couches conservent leurs branches.

## Analyse — 2026-11-09

Recherche globale des noms dans les fichiers actifs du principal, hors worktrees,
Git, tmp, dépendances et .env : le workspace racine, la constante de
`setup_worktrees.py`, trois attentes dans `test_setup_worktrees.py` et le guide
`docs/architecture/02-cadre/couches/organisation.md` sont concernés. Les autres
occurrences relevées dans DEM-014, DEM-015, OPS-044, OPS-070 et OPS-081 sont des
traces historiques à conserver. SETUP invoque seulement le nom inchangé de
l’alias ; Makefile ne contient pas le nom du fichier. Aucune application concernée.

Lecture ciblée de l’alias personnel : sa cible désigne toujours l’ancien fichier.
Le script refuse cette cible après changement de sa constante : adapter la cible
personnelle avant sa recette. Son comportement de refus reste conservé ; pas de
migration automatique des alias arbitraires. DEM-018 est livrée, son script est
présent dans la base : coordination satisfaite sans dépendance non commitée.

Option retenue par le cadrage confirmé : nom exact sans extension .code-workspace,
contenu et commande d’ouverture inchangés. Garder l’extension native aurait limité
le risque de reconnaissance, mais contredirait ce choix ; aucune solution de
contournement n’est autorisée sans retour humain en cas d’incompatibilité.

La convention sera placée dans la rubrique existante du README de Codebase
Integrity, responsable de la génération. Les tests de setup existants vérifient
la génération et l’alias dans des dépôts jetables ; leurs attentes indépendantes
seront adaptées, avec absence de recréation de l’ancien fichier. Réutiliser ces
contrôles bloquants plutôt qu’ajouter un vérificateur global limite le coût et
couvre le comportement demandé. Les contrôles documentaires couvrent les liens,
pas tous les noms écrits en texte : recherche ciblée complémentaire obligatoire.
Les historiques sont exclus de cette recherche de conformité active.

Décisions de nom, portée, exceptions, préservation, tests adaptés et arrêt sur
incompatibilité : cadrage confirmé dans cette session ; aucune nouvelle décision
de besoin. L’ouverture réelle reste hors des tests automatisés (binaire VS Code
simulé) : preuve humaine avec le nom final et résolution réelle des dossiers
requise, éventuellement après réunion des commits. Aucun résultat présumé.

Base commune principal/devops : `b93a9897c0a120e3f773308e7d356c2e993448fd`.
Les traces de clôture DEM-030/DEM-031 établissent la disponibilité devops ; index
et arbre propres avant création. Carte préparée sans changement de branche,
fetch, commit ni implémentation. La déclaration contribution-json sera renseignée
sur les chemins et contrôles effectivement livrés, avant livraison.

## Suivi d’implémentation — 2026-11-09

Contribution non commitée dans devops ; preuves et limites dans OPS-083.
La bascule de l’alias personnel dépend de la présence du fichier dans le principal
après reconstitution, afin de préserver son ouverture actuelle. L’ouverture réelle
avec le nom final reste à observer à ce moment. Aucun commit ni passage automatique
à l’étape suivante ; aucune validation du résultat.

## Vérification — 2026-11-09

Verdict humain « validé » sur OPS-083 avec les réserves présentées, consignées
uniquement dans la carte. Identité du contenu revérifiée avant commit.
Commit local : `929e959afee67d8bb3e143c6d5ab0e0864221c3b` sur `layers/devops`.
Déplacement reconnu à 100 %, six fichiers dans le commit ; index et arbre propres
après création. Aucun push, PR ni reconstitution effectués. Le brouillon reste
hors Git ; conserver l’identité et les réserves à la reconstitution.

## Reconstitution — 2026-11-09

Principal libre et propre sur develop avant création de `demands/DEM-019` ;
base locale vérifiée : `b93a9897c0a120e3f773308e7d356c2e993448fd`.
Reprise après interruption : provenance du cherry-pick et identité des arbres
source/cible vérifiées, sans second passage ni conflit. Aucun fetch ni merge.

| Source validée | Commit obtenu |
| --- | --- |
| `929e959afee67d8bb3e143c6d5ab0e0864221c3b` | `ad52038d3453851de6dcea113ca0938eef9a62da` |

Brouillon matérialisé avec identité, sessions et décisions conservées ; liens
adaptés à son emplacement définitif. Carte actualisée pour référencer cette
demande. Ces seules traces documentaires restent non commitées pour la livraison.
Les couches restent sur layers/* ; retour du principal sur develop après fusion.
Aucune bascule d’alias ni recette graphique effectuée pendant cette étape :
réserves d’OPS-083 à traiter avant clôture. Aucun push, PR ou fusion de livraison.

Contrôles de reconstitution : sept tests de setup réussis ; liens et structure
documentaires conformes ; `git diff --check` réussi. Contenu fonctionnel identique
au commit validé, seul le lien de la carte est adapté. Qualité complète et
contrôle de contribution de la plage finale à exécuter avant PR.

## Déclaration de contribution

```contribution-json
{
  "version": 1,
  "corrections": [
    {
      "chemins": [
        "aide.code-workspace",
        "ai-powered-development-engineering.vscode-worktree",
        "codebase-integrity/scripts/setup_worktrees.py",
        "codebase-integrity/tests/test_setup_worktrees.py",
        "codebase-integrity/README.md",
        "ai-powered-development-engineering.code-workspace"
      ],
      "convention": "codebase-integrity/README.md#conventions-techniques",
      "controles": [
        "codebase-integrity/tests/test_setup_worktrees.py"
      ]
    }
  ],
  "accompagnements": [
    {
      "chemins": [
        "docs/architecture/02-cadre/couches/organisation.md",
        "SETUP.md"
      ],
      "motif": "Actualiser la référence active au workspace renommé."
    }
  ],
  "sans_correction": ""
}
```

## Préparation de livraison — 2026-11-09

Recette finale et bascule de l’alias : preuves uniques dans OPS-083, réserves
levées par observation humaine explicite. Qualité complète sur l’arbre reconstitué :
`python3 codebase-integrity/scripts/quality.py`, sortie 0, journal
`/tmp/dem019-quality.log` : 117 tests d’outillage, contrôles API, contrat, types et
builds web/backoffice. Contrôle de contribution et messages sur les commits finaux
à vérifier avant push. Aucun contrôle affaibli.

Après fetch autorisé, origin/develop et develop local partagent la base
`b93a9897c0a120e3f773308e7d356c2e993448fd`. GitHub autorise Rebase and merge ;
aucune PR ouverte pour cette source avant création. Principal réservé à DEM-019 ;
les cinq couches sont propres, dernières missions clôturées sauf OPS-083 livrée
ici. Devops ne porte que le commit source validé ; aucune contribution inédite
sur les autres couches. Aucun layer publié. Retour prévu sur develop après fusion.

## Correction du besoin et reprise — 2026-11-09

L’humain corrige son observation précédente : VS Code s’ouvrait sans dossiers.
La preuve graphique annoncée réussie est donc retirée ; livraison suspendue.
Il confirme ensuite le nom `ai-powered-development-engineering.code-workspace`,
puis demande ce même nom pour l’alias personnel. Ces décisions remplacent le
nom sans extension native et la conservation du nom d’alias du cadrage antérieur.
Le fichier et son contenu restent identiques ; adapter aussi SETUP à la commande.

Correction effectuée dans le principal déjà reconstitué sur `demands/DEM-019`,
sans copier de travail entre couches et sans nouveau commit. Préparation, tests,
convention, guide et SETUP adaptés. Alias personnel renommé et cible corrigée,
autres octets préservés ; syntaxe Bash et définition en shell neuf conformes.
Lancement réel via le nouvel alias : code 0 ; observation des six dossiers et
nouvelle validation du résultat encore attendues. L’ancien verdict ne couvre
pas cette correction. La réécriture documentaire précédemment proposée reste
non autorisée ; le contrôle historique demeure à résoudre avant publication.

## Validation de la correction — 2026-11-09

Après lancement du nouvel alias et demande de vérification des dossiers,
l’humain répond « parfait ça roule », puis demande à nouveau la livraison.
La correction du nom et de l’alias est validée ; preuve dans OPS-083.
Le blocage historique documentaire reste distinct de cette validation.
