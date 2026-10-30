# Corps du message et références

> Expliquer les motivations du changement et conserver son rattachement à la demande.

Le titre donne le changement ; le corps apporte ce que le diff explique mal :
une motivation, une contrainte ou la raison d'un choix. Un changement simple
peut se passer de paragraphe explicatif, tout en conservant son rattachement à
la demande.

```text
ci(OPS-075): vérifier les messages de chaque commit de la PR

Détecter aussi les titres invalides au milieu d'une série.

Demande : DEM-024
```

La carte conserve les preuves et le verdict ; le message n'en fait pas une copie.
Git fournit déjà les fichiers modifiés : un inventaire dans le corps ajouterait
une information redondante. La trace de cherry-pick remplit un autre rôle : elle
relie le commit reconstitué à sa source.

Pour une trace portant sur l'ensemble de la demande, le scope peut désigner
celle-ci, par exemple `docs(DEM-024): consigner les contrôles de livraison`.
Ce cas ne sert pas à regrouper du code de plusieurs cartes sous une seule référence.
