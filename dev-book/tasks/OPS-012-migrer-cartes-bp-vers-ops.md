# OPS-012 — Migrer les cartes BP vers OPS

- **Date** : 2026-10-23.
- **Session** : non disponible (Codex).
- **Statut** : ✅ fait le 2026-10-23.
- **Type** : docs.
- **Demande** : « bp doit etre migrer dans ops » ; cette instruction remplace la conservation antérieure des identifiants BP.
- **Mission** : devops, `layers/devops`, worktree `/home/johan/www/lab/ai-orchestrated-development/worktree/devops`.
- **Dépendance** : `e624ad92e8d5268e7cba65f0c881a73082da7578`.
- **Chemins autorisés** : cartes `dev-book/tasks/`, `dev-book/README.md`, `docs/couches.md`, `docs/adoption.md`, `ia-engineering/gouvernance.md`, README entrants concernés.
- **Tests** : inventaire des 21 migrations, absence de collision, comparaison du contenu avec substitution des identifiants, liens locaux et `git diff --check`. Aucun nouveau test exécutable : renommage documentaire uniquement.

## Périmètre et décisions

Réserver OPS-012 à cette migration ; attribuer OPS-013 à OPS-033 aux 21 cartes
anciennement BP-001 à BP-021, dans cet ordre. Adapter les références des fichiers Markdown,
les liens et les conventions. Conserver une table des anciens identifiants dans le dev-book.
Préserver les statuts, preuves, affectations et SHA historiques ; seule leur référence de carte change.
Les commits existants et les ressources originales restent inchangés.

## Hors périmètre

Applications, ressources graphiques et réécriture de l’historique Git. Aucun push ni PR.

## Définition de terminé

- [x] Les 21 cartes sont renommées sans collision ni perte de contenu.
- [x] Les références documentaires et conventions utilisent OPS ; les anciens identifiants sont traçables.
- [x] Les liens locaux et le diff sont vérifiés.

## Vérification — 2026-10-23

21 cartes migrées vers OPS-013 à OPS-033 ; comparaison au contenu initial réussie
après substitution des références uniquement. Aucun doublon d’identifiant.
99 liens Markdown locaux vérifiés, aucune cible absente (fragments non contrôlés).
Table de correspondance ajoutée au dev-book ; gouvernance et guides actualisés.
`git diff --check` réussi. Aucun changement de statut ou d’affectation des anciennes cartes,
aucune réécriture de commit ni publication.

## Livré et clôture

Migration des 21 cartes, références entrantes, conventions et table de correspondance
réunies dans le commit OPS-012 demandé par l’utilisateur. Comparaison au contenu
versionné répétée avant indexation : seules les références de cartes changent.
Aucun travail hors périmètre restant ; aucune publication.
