# Skills AIDE

Sources versionnées des procédures AIDE. Douze skills correspondent aux douze étapes,
six pour chaque boucle indépendante. Les outils transversaux restent hors de ces étapes.

## Rôle et responsabilités

Chaque dossier contient un SKILL.md autonome, utilisable après installation personnelle.
Les procédures lisent les conventions du projet d’accueil. Les décisions d’arbitrage et les
verdicts de vérification restent humains. Une invocation ne déclenche pas l’étape suivante.
Aucune boucle ne requiert un skill ni un livrable de l’autre ; elles partagent seulement les
conventions du projet et, si nécessaire, les outils transversaux.

| Étape | Développement | Consolidation |
| --- | --- | --- |
| 01 | Interview : [`interviewer-demande`](interviewer-demande/SKILL.md) | Interview : [`interviewer-constat`](interviewer-constat/SKILL.md) |
| 02 | Découpage : [`decouper-demande`](decouper-demande/SKILL.md) | Analyse globale : [`analyser-convention`](analyser-convention/SKILL.md) |
| 03 | Implémentation : [`implementer-tache`](implementer-tache/SKILL.md) | Arbitrage : [`arbitrer-convention`](arbitrer-convention/SKILL.md) |
| 04 | Vérification : [`verifier-tache`](verifier-tache/SKILL.md) | Implémentation : [`implementer-consolidation`](implementer-consolidation/SKILL.md) |
| 05 | Reconstitution : [`reconstituer-demande`](reconstituer-demande/SKILL.md) | Vérification : [`verifier-consolidation`](verifier-consolidation/SKILL.md) |
| 06 | Livraison : [`livrer-demande`](livrer-demande/SKILL.md) | Livraison : [`livrer-consolidation`](livrer-consolidation/SKILL.md) |

## Outils transversaux et migration

| Ancien skill | Destination |
| --- | --- |
| `evoquer-un-sujet` | [Conservé](evoquer-un-sujet/SKILL.md), discussion avant les boucles |
| `creer-tache` | Remplacé par interview et découpage du développement ; la consolidation possède son interview et prépare ses cartes après arbitrage, dans son implémentation |
| `demarrer-tache` | Remplacé par les deux implémentations distinctes |
| `commit-tache` | [Conservé](commit-tache/SKILL.md), après verdict humain, sur demande explicite |
| `creer-pr` | [Conservé](creer-pr/SKILL.md), outil commun aux livraisons autorisées |
| `apres-pr-mergee` | [Conservé](apres-pr-mergee/SKILL.md), après fusion prouvée |
| `etat-des-lanes` | [Conservé](etat-des-lanes/SKILL.md), inventaire en lecture seule |
| `configurer-worktrees-aiod` | Renommé [configurer-worktrees-aide](configurer-worktrees-aide/SKILL.md), préparation ou audit du cadre |

Le développement prépare ses cartes et branches au découpage ; sa vérification recueille
le verdict avant le commit demandé ; sa reconstitution réunit les SHA autorisés.
La consolidation prépare ses cartes et branches dans son implémentation, à partir de
l’arbitrage ; sa vérification recueille le verdict avant les commits demandés ; sa livraison
réunit elle-même les contributions autorisées. Aucun passage par la reconstitution du développement.

## Conventions techniques

Un dossier par skill, nommé comme le champ `name` de son frontmatter YAML. La description
précise quand l’invoquer. Les ressources nécessaires restent dans ce dossier pour que
l’installation d’un seul skill fonctionne sans copier un autre skill de boucle.
Les outils transversaux restent optionnels : leur absence renvoie à la procédure du projet,
sans inventer leur contenu ni sauter les vérifications nécessaires.
Les références historiques de configuration sont des exemples datés, jamais des valeurs par défaut.

## Installation personnelle ultérieure

La présence de ces sources ne vaut pas installation ni activation dans une session.
Pour une installation demandée ultérieurement, copier les dossiers choisis dans le répertoire
personnel de skills configuré pour l’outil. Examiner d’abord les destinations existantes et
préserver leurs adaptations ; ne pas écraser une ancienne installation automatiquement.
Chaque dossier se copie avec ses ressources. Vérifier ensuite les skills exposés par la session.
Les noms `creer-tache`, `demarrer-tache` et `configurer-worktrees-aiod` sont remplacés dans
ce catalogue ; leur retrait personnel est une opération distincte et explicitement demandée.
La présente refonte ne modifie aucun fichier personnel.
