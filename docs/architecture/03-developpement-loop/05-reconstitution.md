# Reconstitution

> Réunir les commits validés sur une branche de demande depuis develop.

Créer une branche depuis develop et y cherry-pick les commits validés de la demande.

## Entrée

Demande, cartes validées et SHA de leurs commits, verdicts compris.

## Déroulement

1. Vérifier les commits attendus et l’ordre de leurs dépendances.
2. Choisir le worktree existant prévu pour la demande, libre et propre ; noter sa branche de couche.
3. Y créer `demands/<identifiant>` depuis le develop local vérifié avec `git switch -c demands/<identifiant> develop`.
4. Appliquer les commits avec `git cherry-pick -x <sha>`, dans l’ordre.
5. Vérifier le diff et les contrôles pertinents ; noter les SHA sources et obtenus dans la demande ou les cartes.

Aucune copie ou dossier de réunion à créer. Une reprise vérifie les cherry-picks
déjà présents pour ne pas les rejouer ; une branche existante n’est pas déplacée.
Ne copier aucun travail non commité. Un conflit qui change le résultat validé
nécessite une décision humaine. Ne pas modifier develop ou une branche de couche
pour porter directement la reconstitution.

## Sortie

Branche de demande prête pour livraison. Le worktree sera rendu à sa branche de
couche après la fusion distante et conservé avec ses fichiers locaux.

## Procédure associée

`reconstituer-demande`.
