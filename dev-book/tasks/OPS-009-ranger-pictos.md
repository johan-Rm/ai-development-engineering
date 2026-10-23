# OPS-009 — Ranger les pictos dans les ressources

- Statut : clôturée le 2026-10-23.
- Date : 2026-10-23.
- Mission : devops, branche `layers/devops`, worktree `worktree/devops` (chemin absolu résolu par Git).
- Périmètre : deux pictos à la racine, `dev-book/resources/` et cette carte ; préserver les travaux précédents.
- Demande : nettoyer les fichiers isolés à la racine et ranger les deux pictos dans les ressources.
- Preuves : déplacement sans modification des octets, recherche des références, diff sans erreurs.

## Preuves

Les deux pictos sont déplacés dans `dev-book/resources/` avec empreintes SHA-256 identiques avant/après. Aucune référence active à leurs anciens chemins trouvée. README de ressources ajouté. Les autres fichiers racine sont des fichiers de configuration ou points d’entrée du dépôt. `git diff --check` réussi. Travaux OPS-007 et OPS-008 préservés. Comparaison aux originaux versionnés répétée avant commit : contenu identique.
