# OPS-063 — Cadrer la concision dans le dépôt

- Date : 2026-10-27 ; état : validée par l’humain ; commit local à réaliser.
- Session de création : `01a17e56-dc43-76f2-83fb-d8006838ac17`.
- Demande : [DEM-011](../demand/DEM-011-concision-reponses-documents.md).
- Couche : devops ; worktree : `worktree/devops` ; branche : `layers/devops`.
- Base locale : `884b0f53a005080bca2c1241122b4f2972e6cedb` ; aucun fetch.
- Dépendances : aucune carte amont. OPS-064 est complémentaire et indépendante.

## Objectif et chemins autorisés

Inscrire la règle confirmée dans `AGENTS.md` et l’expliquer brièvement dans
`docs/02-cadre/ia-engineering.md`. Autoriser aussi cette carte et DEM-011 pour
les preuves et le suivi. Lire les README applicables avant écriture.

## Critères et exclusions

1. Réponses et documents : concision stricte, précision, aucune répétition ni détail superflu.
2. Avant un développement jugé nécessaire : synthèse concise, demande d’accord,
   puis attente d’une validation humaine explicite ; le silence ne vaut pas accord.
3. Les consignes sont cohérentes et préservent les informations nécessaires,
   les preuves et les validations déjà exigées par le projet.

Exclure les applications, la configuration du modèle, les contrôles techniques,
la réécriture des documents historiques et toute autre modification de workflow.
Les skills personnels relèvent d’OPS-064.

## Vérification et preuve

Relire le diff et fournir deux exemples courts dans cette carte : réponse courante
concise et synthèse demandant l’accord avant développement. Vérifier les liens et
`git diff --check` ; exécuter `python3 codebase-integrity/scripts/quality.py` avant PR.
Pas de test automatisé de jugement rédactionnel. Consigner les résultats réels ;
laisser le verdict humain en attente et les modifications non commitées.

## Preuves d’implémentation

- Base présentée : `884b0f53a005080bca2c1241122b4f2972e6cedb`, branche `layers/devops`, index vide.
- Diff : ajout de la règle dans `AGENTS.md` et renvoi dans le guide IA Engineering ;
  aucune modification des autorisations ou contrôles techniques.
- `git diff --check` et vérification des liens locaux : réussis.
- `python3 codebase-integrity/scripts/quality.py` : premier essai bloqué par le
  sandbox sur un socket local ; relance autorisée hors sandbox réussie (code 0),
  dont 23 tests d’outillage, contrat API, types et builds applicatifs.
- Exemple courant : « Les deux liens sont corrigés. Vérification réussie. »
- Exemple avant développement : « Trois options répondent au besoin. Je recommande
  la deuxième pour sa simplicité. Souhaites-tu le comparatif détaillé ? »
  Attendre un accord explicite avant de produire ce comparatif.
- Limite : les exemples illustrent le comportement ; la conformité rédactionnelle
  reste soumise à la relecture humaine. Verdict en attente, aucun commit.

## Suite

Après validation humaine, commit distinct par carte via la vérification.
La reconstitution de DEM-011 attend les SHA validés et crée `demands/DEM-011`
depuis develop local vérifié dans un worktree existant libre et propre, conformément
à AGENTS.md. Conserver les worktrees et noter la branche de couche à retrouver.

## Verdict humain

Le 2026-10-27, validation globale explicite dans le chat : « validé », couvrant
OPS-063 et OPS-064 présentées ensemble. Contenu vérifié inchangé avant commit.
