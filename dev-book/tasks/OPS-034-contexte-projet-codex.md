# TASK OPS-034 — Préparer le contexte Codex du projet AIDE

- **Créée le** : 2026-10-23.
- **Session** : non disponible (Codex).
- **Statut** : ✅ fait le 2026-10-24.
- **Type** : outillage et documentation.
- **Tests** : lecture du TOML avec un parseur ; vérification des liens et des références actives ; `python3 codebase-quality-control/scripts/check.py` ; `git diff --check`. Pas de nouveau test applicatif : aucun comportement applicatif modifié.
- **Réf** : `AGENTS.md`, `ia-engineering/gouvernance.md`, `docs/couches.md`, `docs/README.md`, `dev-book/README.md`, `dev-book/resources/vue-d-ensemble-ai-development-engineering.html` ; OPS-033 pour les étapes de consolidation.

## Contexte

Le projet doit fournir à Codex un contexte explicite pour trouver ses règles, sa documentation et les procédures correspondant aux boucles AIDE. L'entrée AGENTS.md existe, mais les références actives présentent encore un support Claude que l'utilisateur a décidé de retirer.

## Mission et affectation

- Couche : devops ; branche : `layers/devops`.
- Worktree : `/home/johan/www/lab/ai-orchestrated-development/worktree/devops`.
- Base observée : `72588b43f6aae4abbada33640c978894c7162f0c` ; aucune dépendance non commitée.
- Chemins autorisés pour l'implémentation : `.codex/config.toml`, `AGENTS.md`, `CLAUDE.md`, `.claude/`, `README.md`, `ia-engineering/`, documentation active concernée sous `docs/`, cette carte et contrôles sous `codebase-quality-control/` uniquement si le retrait de Claude impose leur adaptation.
- Preuve attendue : configuration lisible, navigation documentaire cohérente, correspondance explicite entre boucles AIDE et skills disponibles, contrôles du dépôt réussis.

## Périmètre

- Créer `.codex/config.toml` comme socle minimal commenté propre au projet.
- Enrichir AGENTS.md existant en conservant la gouvernance, les règles des worktrees, la non-délégation par défaut et la référence graphique officielle.
- Indiquer le rôle de `docs/` et de son index, de `dev-book/` et des `README.md` à tous les niveaux (`**/README.md`, y compris les dossiers imbriqués).
- Expliquer la lecture des README du chemin concerné avant écriture, du général au particulier, et la mise à jour de la documentation locale quand ses règles changent.
- Ajouter dans AGENTS.md une section `## Code Review Rules` : les conventions techniques sont définies dans la section `## Conventions techniques` de chaque README concerné et servent de référence à la revue de code.
- Définir le format des README des sous-dossiers d'un projet applicatif : un titre H1, une description courte, puis uniquement `## Rôle et responsabilités` et `## Conventions techniques`. Aucun autre chapitre.
- Associer les briques des boucles de développement et de consolidation AIDE aux skills à privilégier, selon leur portée réelle.
- Retirer CLAUDE.md, le support propre à Claude sous `.claude/` et les références actives devenues obsolètes ; adapter les contrôles concernés si nécessaire.

## Hors périmètre

- Installation, déplacement, copie ou modification des skills personnels hors dépôt.
- Création de nouveaux skills ou remplacement des décisions humaines par un skill.
- Réécriture des cartes historiques, des ressources sources ou de l'historique Git.
- Modification des applications, du schéma visuel AIDE, des modèles, des permissions, des secrets ou de la configuration personnelle Codex.
- Réécriture systématique des README applicatifs existants : cette tâche définit leur convention dans AGENTS.md ; elle ne lance pas une migration de tous les fichiers.
- Commit, push, PR, merge et opérations distantes.

## Décisions de cadrage

L'utilisateur a validé le périmètre et le socle minimal commenté. Aucun modèle ni réglage de permissions n'est imposé. Vérifier les clés éventuelles dans la documentation officielle de Codex ; ne pas inventer de configuration. Les commentaires peuvent suffire à ce socle.

Les skills personnels restent externes au dépôt : recommander leurs noms sans chemin personnel obligatoire. Leur absence ne doit pas empêcher de suivre les procédures documentées du projet. Ne pas prétendre qu'une mention dans AGENTS.md installe ou configure un skill.

Pour le développement, examiner notamment `evoquer-un-sujet`, `creer-tache`, `demarrer-tache`, `commit-tache`, `creer-pr` et `apres-pr-mergee` ; `etat-des-lanes` sert à se situer. Pour la consolidation, utiliser les étapes de la vue AIDE comme référence, indiquer les correspondances réellement applicables et signaler les étapes sans skill dédié. Les arbitrages et vérifications humains restent humains.

## Règles et cas limites

- Les instructions explicites de l'utilisateur et la gouvernance du dépôt priment ; les recommandations de skills ne déclenchent pas une étape automatiquement.
- Ne pas lire tous les README du dépôt à chaque mission : lire ceux du chemin concerné et les références utiles.
- Le format minimal demandé s'applique aux README des sous-dossiers applicatifs. Il n'est pas imposé aux index documentaires, au README racine du dépôt ou aux README du cadre AIDE. Les conventions techniques restent définies localement dans les README concernés ; AGENTS.md explique leur rôle sans les recopier.
- Conserver les traces historiques mentionnant Claude ; distinguer ces traces du support actif à retirer.
- Ne pas inscrire de chemins personnels, de secrets ou de confiance globale dans la configuration versionnée.
- L'identifiant fiable de session n'est pas fourni ; aucune propriété de mission ne doit être déduite de cette absence.

## Documentation impactée

AGENTS.md, README.md racine, `ia-engineering/README.md` et les guides actifs évoquant le support Claude ou la configuration Codex, notamment `docs/adoption.md`. Actualiser les autres README concernés par une convention changée sans dupliquer la gouvernance.

## Définition de terminé

- [x] `.codex/config.toml` existe, est commenté et se parse sans erreur, sans modèle ni permissions imposés.
- [x] AGENTS.md expose les points d'entrée documentaires et les règles de lecture des README imbriqués.
- [x] La section `## Code Review Rules` d'AGENTS.md désigne les README concernés comme référence des conventions techniques à vérifier en revue.
- [x] AGENTS.md prescrit pour les README des sous-dossiers applicatifs exactement un H1, une description courte et les deux H2 `## Rôle et responsabilités` et `## Conventions techniques`, sans autre chapitre.
- [x] Les skills recommandés sont associés aux briques des deux boucles AIDE sans inventer de capacités ou automatiser les décisions humaines.
- [x] Le support Claude est retiré et les références actives sont cohérentes ; l'historique des cartes est conservé.
- [x] Les skills personnels restent hors dépôt et leur absence possède un repli documentaire explicite.
- [x] Les liens touchés sont vérifiés ; le contrôle du dépôt et `git diff --check` réussissent.
- [x] La réalisation et les preuves sont consignées dans cette carte avant sa clôture.

## Réalisation et preuves

Implémentation réalisée le 2026-10-23 dans le worktree affecté.

- `.codex/config.toml` créé avec uniquement des commentaires : parsing Python `tomllib` réussi, résultat `{}` ; aucun réglage effectif ajouté.
- AGENTS.md enrichi : navigation documentaire, README imbriqués, format applicatif, `Code Review Rules` et correspondance des deux boucles avec les skills. Les étapes humaines et les étapes sans skill dédié sont explicites.
- CLAUDE.md et `.claude/README.md` supprimés ; README racine, index documentaire, adoption et entrée IA Engineering actualisés. Les cartes historiques et les ressources sources sont conservées.
- `python3 codebase-quality-control/scripts/check.py` : 17 tests réussis.
- Vérification des liens locaux des cinq documents modifiés : réussie (y compris la charte au nom contenant des parenthèses).
- Recherche des références Claude dans AGENTS.md, README.md, ia-engineering/, docs/ et codebase-quality-control/ : aucune référence active restante.
- `git diff --check` : réussi.

La configuration étant vide de clés, aucune option Codex non vérifiée n'est introduite. Aucun test applicatif ajouté pour ce changement documentaire. Aucun fetch, rebase, commit, push ou PR effectué : la gouvernance du dépôt prévaut sur les opérations automatiques de la procédure importée. La suppression et les ajouts restent locaux à `layers/devops`, en attente de revue et de commit demandé.

## Mise en commit — 2026-10-24

Autorisation explicite de l’utilisateur de committer le travail accumulé. Socle TOML vérifié et support Claude supprimé. Les compléments AGENTS.md et les liens ont été retravaillés par OPS-036 puis intégrés dans la réécriture documentaire OPS-037 ; ils voyagent dans ce dernier commit pour ne pas reconstruire des versions intermédiaires artificielles. Les anciennes références de périmètre de cette carte décrivent son cadrage initial.
`git diff --check` réussi. La relecture finale par l’utilisateur reste à venir ; la réalisation technique ne vaut pas son verdict éditorial.
**Tests** : sans objet pour de nouveaux tests exécutables — instructions et documentation uniquement ; liens actifs et TOML vérifiés dans le lot final.
