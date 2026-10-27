# OPS-064 — Cadrer la concision dans les skills personnels

- Date : 2026-10-27 ; état : validée par l’humain ; commit local à réaliser.
- Session de création : `01a17e56-dc43-76f2-83fb-d8006838ac17`.
- Demande : [DEM-011](../demand/DEM-011-concision-reponses-documents.md).
- Couche de suivi : devops ; worktree : `worktree/devops` ; branche : `layers/devops`.
- Base locale : `884b0f53a005080bca2c1241122b4f2972e6cedb` ; aucun fetch.
- Dépendances : aucune carte amont. OPS-063 est complémentaire et indépendante.

## Objectif et chemins autorisés

Appliquer la règle confirmée aux `SKILL.md` personnels sous le répertoire de
skills de l’utilisateur, hors dépôt, pour les skills suivants :

- Développement : interviewer-demande, decouper-demande, implementer-demande,
  verifier-demande, reconstituer-demande, livrer-demande.
- Consolidation : interviewer-constat, analyser-convention, arbitrer-convention,
  implementer-consolidation, verifier-consolidation, livrer-consolidation.
- Appui : configurer-worktrees-aide, etat-des-lanes, creer-socle, create-readme,
  documentation-writer, vulgariser.

Dans le dépôt, seules cette carte et DEM-011 sont autorisées pour le suivi.
Lire les skills complets et leurs instructions locales avant modification ;
résoudre les chemins personnels à l’exécution. Ne pas copier les skills dans le dépôt.

## Critères et exclusions

1. Réponses et documents strictement concis et précis, sans répétition ni détail superflu.
2. Si davantage de détails paraît nécessaire : synthèse concise, demande d’accord,
   attente d’une validation humaine explicite avant développement.
3. Préserver les étapes, autorisations, informations et preuves obligatoires.
4. Vérifier la cohérence avec la règle de DEM-011 et les consignes du dépôt.

Exclure les skills système et de plugins, les autres réglages personnels et
les corrections de workflow étrangères à la concision.

## Vérification et preuve

Conserver les différences avant/après pour relecture humaine ; consigner ici les
skills modifiés, les résultats et deux exemples courts (réponse courante et demande
d’accord). Vérifier la syntaxe et les métadonnées des skills modifiés avec leur
validateur disponible, sans inventer de réussite si indisponible.
Pas de test automatisé de jugement rédactionnel.

Les chemins externes ne sont pas inscriptibles dans le sandbox actuel : utiliser
le mécanisme d’autorisation de l’environnement à l’implémentation. Aucun changement
externe n’a été réalisé au découpage. Les modifications des skills ne peuvent pas
être livrées par le Git du projet ; leur preuve et leur validation sont suivies ici.

## Preuves d’implémentation

- Les 18 `SKILL.md` listés dans le périmètre ont reçu la même règle de concision
  que le dépôt, après autorisation d’écriture hors sandbox.
- `create-readme` demande désormais un README concis au lieu de « comprehensive » ;
  `documentation-writer` propose un plan concis au lieu d’un plan détaillé.
- Métadonnées et procédures conservées : comparaison de chaque fichier à son état
  initial après retrait des seuls changements rédactionnels prévus, 18 réussites.
- Validateur `skill-creator/scripts/quick_validate.py <dossier-du-skill>` : code 0
  et « Skill is valid! » pour chacun des 18 skills. Ce contrôle vérifie la structure,
  pas le jugement rédactionnel.
- Diff local avant/après : `/tmp/dem011-skills.diff`, SHA-256
  `399e35526f3ae30592e0f42117610c1ca2f2cc46c2ac82a71e08650a9cfc4368`.
  États avant/après : `/tmp/dem011-skills-plan.json` ; fichiers temporaires à préserver
  jusqu’à la vérification, hors du contenu Git livré.
- Exemple courant : « README créé : installation et commandes utiles. »
- Exemple avant développement : « Le guide tient en trois étapes. Souhaites-tu
  une version détaillée avec les cas particuliers ? » Attendre un accord explicite.
- Base du suivi Git : `884b0f53a005080bca2c1241122b4f2972e6cedb` ; seuls cette
  carte et DEM-011 portent les traces, les skills restent hors dépôt.
- Verdict humain en attente ; aucun commit ni livraison des skills par Git.

## Suite

Attendre le verdict humain avant le commit local des traces de cette carte.
La reconstitution de DEM-011 attend ce SHA et celui d’OPS-063 ; les fichiers
personnels restent hors dépôt et font l’objet d’une vérification locale séparée.

## Verdict humain

Le 2026-10-27, validation globale explicite dans le chat : « validé », couvrant
OPS-063 et OPS-064 présentées ensemble. Contenu vérifié inchangé avant commit.
