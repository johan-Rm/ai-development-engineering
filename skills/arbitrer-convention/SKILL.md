---
name: arbitrer-convention
description: "Présenter une analyse de consolidation à l’humain et consigner sa décision sur la règle, les exceptions et les contrôles."
---

# Consolidation · 03 Arbitrage

## Entrée

Constat, analyse globale, options et limites documentés.

## Conventions du projet

Lire les instructions du projet, la demande ou carte fournie et les README applicables.
Résoudre les chemins, couches, branches, commandes de tests et qualité depuis le projet ;
annoncer les valeurs utilisées et les inconnues, sans imposer de valeurs personnelles.
Avant une écriture, confirmer le worktree absolu, la branche autorisée et la disponibilité de la couche.
Préserver les modifications préexistantes et les `.env`. Ne pas utiliser stash, reset --hard,
force-push ou suppression de worktree pour résoudre une situation. Ne pas rebaser une branche occupée.
Commit, push, PR et merge nécessitent l’autorisation prévue par le projet ; une invocation d’étape
ne les autorise pas implicitement. Les autorisations explicites déjà données restent valables.
Ne pas déléguer sans autorisation. Ne pas enchaîner automatiquement une autre étape.

## Procédure

Présenter les options avec leurs conséquences : corrections, exceptions, coût, faux positifs possibles,
contrôle proposé et niveau bloquant ou informatif. L’humain adopte, ajuste, diffère ou rejette.
Consigner exactement sa décision et les motifs exprimés. Pour une adoption, fixer le périmètre,
les critères, exceptions, contrôles attendus et preuves requises. Une adoption partielle doit nommer
ce qui reste exclu ou non tranché. Une règle sans automatisation retenue reste identifiée comme telle.
Ne pas déduire l’accord d’un silence ni d’une validation ancienne portant sur une autre proposition.
Ne pas modifier le code ni les contrôles et ne pas démarrer l’implémentation dans cette invocation.

## Sortie et preuve

Décision humaine traçable, périmètre approuvé et critères de conformité, ou motif de report/rejet.

## Arrêt

Verdict absent ou ambigu : conserver la proposition en attente ; un report ou rejet interdit son implémentation.
