# Consignes des agents

## Réponses et documents

Rédiger des réponses et documents strictement concis et précis ; conserver les preuves et décisions nécessaires.
Si davantage de détails paraît nécessaire, donner une synthèse puis attendre l’accord humain explicite avant de développer. Le silence ne vaut pas accord.

**Réduire le bruit et la redondance est une exigence prioritaire.** Chaque information doit avoir un emplacement de référence unique. Avant d’écrire, vérifier si elle existe déjà ; privilégier un lien plutôt qu’une copie. Ne créer ou répéter du contenu que s’il apporte une information utile et distincte. Toute duplication jugée nécessaire doit être justifiée et soumise à l’accord explicite de l’humain.

## Avant d’intervenir

- Les instructions explicites de l’utilisateur priment. Ne déléguer que sur demande explicite.
- Lire la demande, la carte et les [couches](docs/architecture/02-cadre/couches/organisation.md) ; respecter worktree, branche, chemins autorisés et dépendances par commits.
- Lire les README existants de la racine au dossier concerné, sans parcourir les autres dossiers. Ils définissent les responsabilités et conventions techniques locales ; la documentation apporte les explications complémentaires. Voir [documentation et revue](docs/architecture/02-cadre/documentation.md).
- Avant toute écriture, vérifier le chemin absolu, la branche, l’index et `git status --porcelain=v1 --untracked-files=all` dans le worktree affecté.
- Une couche sale ou occupée bloque une nouvelle mission ; une reprise conserve seulement ses changements identifiés, sans travail étranger. Un arbre propre ne prouve pas la disponibilité.
- Préserver travail existant, worktrees, `.env` et données. Pas de stash, reset --hard, force-push ni suppression de worktree pour résoudre une situation ; pas de rebase d’une branche partagée ou occupée sans coordination.

## Workflow et autorisations

- Intégration : `develop` ; production : `master` ; `main` reste historique. Aucune contribution de tâche sur intégration ou production.
- Missions : `layers/<couche>` dans `worktree/<couche>` ; cadre : devops, préfixe OPS. [Routage et création des worktrees](docs/architecture/02-cadre/couches/organisation.md).
- Suivre l’étape demandée de la [boucle de développement](docs/architecture/03-developpement-loop/index.md) ou de [consolidation](docs/architecture/04-consolidation-loop/index.md), avec son skill disponible ; [disponibilité et limites des skills](docs/architecture/02-cadre/ia-engineering.md#utiliser-les-skills).
- `implementer-demande` ne crée aucun commit, corrections comprises. `verifier-demande` et `verifier-consolidation` créent les commits locaux distincts des cartes explicitement validées, avec code, tests, documentation, preuves et verdict, puis leurs traces documentaires. La validation autorise ces commits sans confirmation supplémentaire. Ne jamais inventer de verdict.
- Le découpage est autonome. La reconstitution réunit les commits validés sur `demands/<identifiant>` ; jamais de copie de travail non commité. [Procédure de reconstitution](docs/architecture/03-developpement-loop/05-reconstitution.md).
- Invoquer `livrer-demande` ou `livrer-consolidation` autorise commits documentaires nécessaires, vérification distante et fetch, push sans forcer, PR vers develop, fusion après contrôles et protections satisfaits, retour du worktree, alignement des couches libres et suppression des seules branches temporaires livrées. Pas de confirmation intermédiaire ; une instruction limitée à la PR garde cette limite. [Procédure et conditions de fin](docs/architecture/03-developpement-loop/06-livraison.md).
- Hors de ces autorisations, les autres opérations Git nécessitent une demande explicite. En consolidation, appliquer les autorisations propres aux skills et au projet.
- Toute évolution d’un skill modifiant ces autorisations met à jour ce fichier et les guides concernés dans le même changement ; vérifier leur cohérence avant présentation.

## Contrôles et fin du travail

- Appliquer les conventions techniques ; leur évolution et celle des contrôles passent par la consolidation selon [Codebase Integrity](codebase-integrity/README.md).
- Exécuter les contrôles proportionnés au changement depuis le worktree affecté : [commandes par périmètre](docs/architecture/01-codebase-integrity/points-de-controle.md#exécuter-dans-ce-dépôt).
- Avant PR : `python3 codebase-integrity/scripts/quality.py`. Tests de l’outillage : `python3 codebase-integrity/scripts/check.py`.
- Présenter le comportement obtenu, les vérifications et leurs limites, avec documentation à jour et preuves dans la carte. Un résultat inconnu ne vaut pas réussite ; une implémentation ne vaut pas validation humaine.
- Après livraison complète, develop et toutes les couches configurées doivent partager le même SHA vérifié. Une couche occupée, sale ou portant du travail inédit reste intacte et bloque la clôture du suivi.

## Demandes et cartes

- Indiquer le type de chaque demande (`développement` ou `consolidation`).
- Réserver les noms de fichiers et dossiers `DEM-*` aux demandes dans `dev-book/demand/` ; nommer les rapports selon leur rôle.
- Toute demande ou carte indique sa session réelle de création, issue du contexte ou de `CODEX_THREAD_ID` / `CODEX_SESSION_ID`, jamais déduite du numéro DEM/OPS. Une source absente ou contradictoire bloque la création ; ne pas écrire de référence d’indisponibilité. Une reprise conserve la session d’origine et ajoute la session intervenante.

## Références à consulter selon la tâche

- Journal des demandes, cartes et preuves : [dev-book](dev-book/README.md).
- Skills et définition des missions : [IA Engineering](docs/architecture/02-cadre/ia-engineering.md).
- Isolation des services : [couches](docs/architecture/02-cadre/couches/organisation.md) ; un worktree seul n’isole pas ports, bases, volumes, caches et écritures.
- Travail graphique : lire la [charte officielle du dépôt](<design/Brand Guidelines - Graines Digitales (standalone).html>) et ses [adaptations au schéma](design/charte-graphique.md), sans substituer de copie externe.
- Autres guides durables : [index documentaire](docs/index.md).
