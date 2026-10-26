# Retour d’expérience : nuxt-builder

Observation locale du 2026-09-22. Cette référence décrit un cas concret et ses limites ; les noms,
ports et chemins ci-dessous ne sont pas des valeurs par défaut pour d’autres projets.

## Sources examinées

Document utilisateur `dev-book/resources/AIOD-carrousel.pdf` (11 pages), `CLAUDE.md`, `AGENTS.md`,
`docs/1.getting-started/agents-codex.md`, `worktree/README.md`, `.claude/agents/`, cartes OPS-006 à
OPS-012, scripts de worktrees et configurations de développement/qualité.

Le carrousel présente quatre piliers : architecture par couches, isolation des piles, cycle IA,
consolidation. Pour une demande traversant plusieurs couches, il décrit une réunion des commits
sur une branche et un worktree de preview, puis une PR. La version du projet est une adaptation :
les instructions actuelles et les choix de l’utilisateur priment sur ce document de référence.

## Mise en place observée

| Étape | Mise en place |
| --- | --- |
| Architecture | Sept couches et responsabilités dans CLAUDE.md ; README de périmètre |
| OPS-006 | Worktrees, allocation des ports, Docker/Bun/Nuxt, proxy Caddy, commandes Make |
| OPS-007 | Sept profils Claude et table de routage ; frontières déclaratives |
| OPS-008 | Identité UID/GID pour les écritures des conteneurs |
| OPS-009 | tsconfig généré selon la cible ; exclusion des worktrees voisins des types |
| OPS-010 | Exclusion `worktree/**` dans Vitest, sans exclure `scripts/worktree/` |
| OPS-011 | Préparation Nuxt au démarrage, quand les sources sont montées |
| OPS-012 | Entrée AGENTS.md et procédure de coordination/intégration pour Codex |

Sept branches `layers/<couche>` : domaine, bff, socle-webapp, design, sites, dashboard, dev-ops.
Elles ne signifient pas sept agents en cours d’exécution. Trois arbres existent à la date de lecture :
arbre principal sur dev-ops, `worktree/bff`, `worktree/design`. Les autres worktrees attendent une
tâche affectée. La lane de rendu possède aussi `sites/demo`, bien que ce dossier soit sous `sites`.

La commande `make worktree-add COUCHE=bff` appelle `scripts/worktree/init.ts`, qui crée le worktree
et un `.env` d’allocation. Elle ne démarre pas de conteneur. `make dev-up` lance ensuite la pile du
dossier courant. Les paramètres proviennent de `scripts/worktree/ranks.ts` : rang principal 0,
port 8080, décalage 100 par rang, noms Docker `gd-<couche>` et domaines `wt-<couche>.localhost`.
Chaque pile démarre une seule cible Nuxt, avec un réseau Compose et un volume de dépendances.
Le projet ne contient pas de base applicative locale ; l’API SaaS est extérieure.

La preuve varie : tests pour le métier, appel HTTP pour le BFF, rendu pour l’interface, regard pour
le design et contrôles pour l’outillage. Le cycle fournit les cartes, commits, PR et réalignements.
Les vérifications historiques de deux piles sont consignées dans OPS-011 ; elles n’ont pas été
rejouées pendant cet audit documentaire.

## Limites observées à ne pas reproduire

1. **Un dossier n’est pas un worktree.** `init.ts` vérifie uniquement son existence et peut ensuite
   y écrire un `.env`. Reproduction dans un dossier temporaire contenant un simple `worktree/bff`,
   sans dépôt Git : sortie 0, `.env` créé, message « pile prête ». Aucun vrai arbre n’était présent.
2. **Racine liée au script.** `ROOT` est déduit de `import.meta.url`. Une invocation depuis une copie
   dans un worktree secondaire peut viser un sous-dossier `worktree/` de cette copie. Les consignes
   imposent aujourd’hui de lancer la création depuis le principal ; l’outil pourrait le garantir.
3. **Rangs positionnels.** Les rangs sont calculés par index dans un tableau. L’ordre est déclaré
   immuable, mais les tests d’unicité et de continuité ne figent pas l’association historique entre
   une couche et son rang. Réordonner le tableau peut changer les ports en gardant ces tests verts.
4. **Identité spécifique au projet.** Les noms `gd-<couche>` isolent les couches de ce dépôt, mais
   deux clones/configurations utilisant les mêmes noms sur le même moteur Docker peuvent entrer
   en collision. Une généralisation demande une identité de projet explicite.
5. **Lint lié à une cible.** `eslint.config.mjs` importe `.nuxt-graines-digitales/eslint.config.mjs`.
   Pour la PR design, préparer uniquement `demo` ne suffisait pas. La génération des types par
   cible ne résout pas à elle seule ce couplage de la configuration ESLint.
6. **Consignes design contradictoires.** Le profil Claude historique interdit presque tout usage
   du terminal, alors que le README de design intégré autorise les maquettes HTML/CSS et leur
   consultation. L’autorisation utilisateur avait permis DS-001 ; les documents restent à harmoniser.
7. **Pas d’application mécanique des frontières.** Aucune CI versionnée dans `.github` sur develop
   lors de l’audit ; pas de contrôle empêchant un agent d’écrire hors de son périmètre, ni de verrou
   d’affectation automatique. Les consignes et la coordination assurent cette discipline.
8. **Intégration transversale partielle.** Aucun worktree de preview commun ni chaîne automatisée
   regroupant plusieurs couches en une PR n’est installé. Les PR observées concernent une couche.

## État Git observé

Sans nouveau fetch pendant l’audit : develop et six branches de couche locales sont à `10a30c9`.
L’arbre principal dev-ops reste à `b68be0f`, avec le backlog modifié et la charte non suivie ; ces
fichiers ont été préservés. Les références distantes des autres couches n’ont pas toutes été
réalignées après la fusion. Pour design, `origin/layers/design` et la branche locale ont des SHA
différents, mais `git cherry` reconnaît le patch intégré et le diff des arbres est vide. Une
création de branche/reprise ne doit donc ni confondre cette divergence avec du travail inédit,
ni tenter un force-push implicite.

## Ce qui est réutilisable

Conserver la carte des responsabilités, les chemins absolus, les worktrees à la demande, les preuves
adaptées, l’isolation des données et outils, et le cycle par tâche. Adapter le nombre de couches,
le runtime, les services et le mode d’intégration au projet réel. Pour un socle vide, on peut
installer la gouvernance et la mécanique Git ; on ne peut pas affirmer qu’une application encore
inexistante ou ses piles ont été testées. Les tests et la documentation accompagnent chaque tâche
avant sa livraison selon les règles actuelles, plutôt que d’attendre leur réunion finale telle que
la décrivait le carrousel initial.
