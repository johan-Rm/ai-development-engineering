# TASK OPS-040 — Harmoniser les mentions actuelles de l’écosystème AIDE

- **Créée le** : 2026-10-24.
- **Session** : non disponible (Codex).
- **Statut** : ✅ fait le 2026-10-24.
- **Livraison** : mentions actuelles harmonisées avec AIDE dans sept documents ; noms techniques et traces historiques préservés.
- **Type** : docs.
- **Tests** : sans objet pour de nouveaux tests — correction éditoriale sans code exécutable ; vérifier les occurrences restantes, les liens concernés et `git diff --check`.
- **Réf** : `README.md`, `AGENTS.md`, `docs/02-cadre/couches.md`, `dev-book/README.md`.
- **Demande d’origine** : échange utilisateur du 2026-10-24 ; l’écosystème s’appelle désormais AIDE, périmètre éditorial validé.
- **Couche et branche** : devops, `layers/devops`.
- **Worktree** : `worktree/devops`.
- **Dépendances par commit** : base locale `e89440ea47112ad6e4ce7316afed6cd6a1287814`, commune à `develop` et `layers/devops` au cadrage ; aucun autre commit amont requis, aucune tâche aval imposée.

## Contexte

Le README racine présente déjà AIDE — AI Development Engineering. Des textes actuels
emploient encore AIOD pour désigner cet écosystème, ce qui rend son identité incohérente
pour les lecteurs et les agents.

## Périmètre

Rechercher et corriger les mentions éditoriales actuelles d’AIOD dans la documentation
et les instructions du cadre. Chemins autorisés : `AGENTS.md`, `README.md`, `SETUP.md`,
les documents textuels sous `docs/`, `dev-book/` (hors cartes historiques), `design/`,
`infra/`, `codebase-integrity/` et `ia-engineering/`, ainsi que la présente carte.
Seuls leurs textes documentaires et instructions sont concernés, aucun code exécutable.
Lire les README applicables avant chaque modification.

## Hors périmètre

- Renommage des fichiers, dossiers, chemins, liens cibles, clés de configuration et identifiants techniques, notamment `aiod.json`, `recette-aiod.md` et les identifiants Docker.
- Réécriture des cartes historiques, preuves datées, archives et références explicites à un ancien nom ou emplacement.
- Applications, comportements, environnements, `.env`, services, ressources Docker et éléments graphiques.
- Push, PR, merge et opérations distantes ; commit uniquement sur demande explicite.

## Décisions de cadrage

Le 2026-10-24, l’utilisateur valide le remplacement dans les textes actuels uniquement.
Conserver les noms techniques et les traces historiques évite de transformer cette
correction éditoriale en migration. Aucun remplacement global automatique.
La tâche ne change aucune convention technique et ne crée aucun contrôle permanent.

## Règles et cas limites

Examiner chaque occurrence selon son sens : remplacer AIOD lorsqu’il désigne
l’écosystème actuel ; conserver une mention historique explicite ou un identifiant
technique, même dans une phrase corrigée. Préserver les destinations des liens.
Tout besoin hors des chemins et exclusions ci-dessus doit être signalé avant extension.
API, données, permissions, états de chargement, concurrence et contraintes de rendu
sont sans objet pour cette correction documentaire.

## Documentation impactée

Occurrences déjà observées : `AGENTS.md`, `design/README.md`, `infra/README.md`.
Vérifier les autres textes actuels des chemins autorisés, notamment la synthèse
graphique et les procédures de recette, sans changer leur présentation graphique.
Les références techniques présentes dans `SETUP.md` et `docs/02-cadre/couches.md`
restent valides et ne justifient pas à elles seules une modification.

## Définition de terminé

- [x] Les mentions éditoriales actuelles identifiées dans le périmètre désignent AIDE.
- [x] Les occurrences AIOD restantes sont expliquées comme techniques, historiques ou hors périmètre dans la preuve de réalisation.
- [x] Aucun nom technique, contenu historique, comportement ou élément graphique n’est modifié.
- [x] Les liens concernés sont vérifiés et `git diff --check` réussit.
- [x] La carte contient les fichiers corrigés, les vérifications exécutées et les éventuelles limites pour la relecture humaine.

## Vérification

Réalisation le 2026-10-24 dans le worktree affecté, sur `layers/devops`.
Seule la carte non suivie était présente au démarrage ; aucun autre travail modifié.
Branche alignée sur le commit de base, aucun fetch ni réalignement nécessaire.

Sept fichiers documentaires corrigés : `AGENTS.md`, `design/README.md`,
`design/charte-graphique.md`, `infra/README.md`, `dev-book/runbooks/recette-aiod.md`,
`codebase-integrity/tests/browser/README.md` et `dev-book/resources/README.md`.
L’index des ressources précise que la vue synthétique conserve l’ancien nom ;
le document graphique lui-même reste intact.

Preuves et contrôles :

- Recherche `rg -n -i 'aiod'` dans les Markdown du périmètre, hors cartes :
  les occurrences restantes sont des chemins, commandes et noms de fichiers
  (`aiod.json`, `vue-aiod.cjs`, `recette-aiod.md`, anciennes cartes et ressources),
  ou des mentions historiques explicites (`.aiod/`, vue synthétique historique).
- Comparaison des destinations des liens Markdown de chaque fichier corrigé avec
  `HEAD` : toutes inchangées ; les 23 liens locaux de ces fichiers existent.
- Relecture du diff : uniquement les sept documents listés, sans code exécutable,
  changement graphique, ressource originale, environnement ni carte historique.
- `git diff --check` : réussi. Aucun nouveau test ajouté ni suite applicative
  exécutée : aucune modification de comportement.

Limites : les ressources graphiques originales (carrousel, PDF, image et
`cadre-aiod.html`) conservent AIOD ; les identifiants techniques et traces
historiques sont volontairement préservés. Le chemin `ia-engineering/` indiqué
au cadrage n’existe pas dans cette base ; aucun fichier à y corriger.
Aucun push ni autre opération distante. Mise en commit demandée explicitement par
l’utilisateur le 2026-10-24 après présentation du résultat.


## Livré

- `AGENTS.md` : nom actuel dans les consignes graphiques.
- `design/README.md` et `infra/README.md` : nom actuel dans les textes de recette.
- `design/charte-graphique.md` : nom actuel dans la synthèse documentaire.
- `dev-book/runbooks/recette-aiod.md` : titre harmonisé, chemin conservé.
- `codebase-integrity/tests/browser/README.md` : titre harmonisé, commande conservée.
- `dev-book/resources/README.md` : distinction explicite entre vue actuelle et historique.
- Présente carte : cadrage, preuves et clôture dans le même commit.

## Reste à faire (hors périmètre)

Aucun reliquat d’implémentation. Les noms techniques et les ressources historiques
restent volontairement inchangés conformément au cadrage validé.
