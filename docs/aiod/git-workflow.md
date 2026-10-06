# Workflow Git

## Une tâche

Cadrer le besoin, écrire sa carte et affecter une couche. Vérifier le worktree et sa disponibilité,
réaliser le changement puis produire une preuve. Tests pertinents, documentation et carte clôturée
accompagnent le commit lorsque celui-ci est demandé.

Avant staging, lire `git status` et `git diff`. Ajouter les fichiers par chemins explicites,
puis relire `git diff --cached` pour ne pas embarquer le travail d’une autre session.

## Avant la PR

Exécuter `python3 scripts/check.py` et les contrôles propres au projet adopté. Le titre et la
description expliquent le problème, le comportement obtenu, les preuves et les limites.
Aucun remote n’est contacté par le contrôle du blueprint.

## Demande transversale

Attendre les commits de chaque couche. Choisir explicitement la branche de réunion et les commits
à intégrer, puis vérifier l’ensemble. Un worktree de preview ne se crée que si cette intégration
en a besoin. Ne pas rebasing une branche partagée ou occupée sans coordination.

## Après le merge

Sur demande, actualiser les références distantes et vérifier que la PR est réellement fusionnée.
Pour une branche propre et explicitement libre, tenter un réalignement sans perte de données
(par exemple `git merge --ff-only origin/develop` lorsque l’historique le permet).
Si la commande ne peut pas avancer simplement, signaler la divergence et choisir la stratégie
avec le coordinateur. Ne pas modifier une branche sale ou occupée.

Un SHA différent ne prouve pas un changement inédit : après rebase ou squash, comparer également
les arbres et l’équivalence des patches. Aucun force-push ni réécriture automatique.

## Référence publique

`master` porte la référence publique. `main` est conservée durant la transition ;
aucune branche par défaut GitHub n’est modifiée automatiquement.

Les couches partent de `develop`. Les changements validés y sont intégrés avant publication
sur `master`. Les branches d’intégration ne reçoivent aucun commit direct.
