# Reconstitution

> Réunir les commits des cartes validées sur une branche de consolidation dédiée.

## Entrée

Toutes les cartes attendues validées et commitées, avec leurs verdicts et SHA.

## Déroulement

Appliquer la [procédure commune de reconstitution](../03-developpement-loop/05-reconstitution.md).
Créer `demands/<identifiant>` depuis develop dans le dossier principal libre et
propre, puis cherry-pick les commits validés dans l’ordre. Tracer les correspondances
source → obtenu et vérifier l’ensemble, sans copier de travail non commité.

## Sortie

Branche de consolidation reconstituée et contrôlée, prête pour la livraison.
Un conflit modifiant le résultat validé retourne à la décision humaine.

## Procédure associée

`reconstituer-consolidation`.
