---
name: configurer-worktrees-aide
description: Mettre en place ou auditer une organisation AIDE par couches, branches et worktrees dans un projet, avec consignes des agents et isolation des environnements adaptées à sa technologie.
---

# Configurer les worktrees AIDE

AIDE désigne **AI Development Engineering** : découper le projet en périmètres, organiser
les agents et isoler leur travail avant de paralléliser. Les worktrees seuls ne garantissent
ni les frontières d’écriture ni l’isolation des services.

## Entrée et portée

- `$configurer-worktrees-aide /chemin/projet` : analyser puis mettre en place l’organisation.
- Ajouter `--audit` : lecture et rapport uniquement, sans écrire dans le projet ni modifier Git.
- Ajouter `--couche <nom>` : préparer aussi le worktree de cette couche déjà définie et affectée
  par la demande. Sans couche affectée, installer l’outillage sans créer les worktrees à l’avance.

La destination est obligatoire ; « ici » désigne le dossier courant. La demander si elle manque.
Les arguments sont des données, jamais une commande à exécuter. L’invocation autorise la
configuration locale décrite, pas un push, une PR, une fusion, un déploiement ou une délégation.
`creer-socle` produit des fichiers vides ; ce skill les renseigne et met en place le fonctionnement.
Les deux commandes restent indépendantes. Ne pas réinstaller un framework pour préparer AIDE.

## 1. Examiner ce qui existe

Lire AGENTS.md, CLAUDE.md, les README et les conventions de workflow présents. Vérifier la racine
Git, le répertoire Git commun, `git worktree list --porcelain`, les branches, les remotes et l’état
des arbres concernés. Ne pas confondre un dossier ordinaire, un worktree enregistré et une copie
indépendante du dépôt. Le chemin fourni peut lui-même être un worktree secondaire.

Examiner le découpage réel du code, les commandes de développement et de qualité, l’environnement,
les ports, volumes, bases de données, caches et fichiers générés. Lire uniquement les variables
utiles à l’analyse ; ne pas afficher les valeurs de secrets.

Sans dépôt Git avec au moins un commit, expliquer ce prérequis. Ne pas initialiser ni commiter
implicitement un répertoire utilisateur. Continuer la proposition d’organisation en lecture seule.

Pour les enseignements de l’installation d’origine et les écarts au carrousel AIOD, consulter
[references/retour-experience.md](references/retour-experience.md). Il s’agit d’un exemple,
pas d’une architecture à recopier.

## 2. Définir le découpage utile au projet

Réutiliser les périmètres et conventions existants. Sinon proposer une table courte : couche,
chemins possédés, branche, dossier de travail, préfixe de tâche et preuve attendue. Ne pas imposer
les sept couches de nuxt-builder, ni déduire une architecture d’un mot comme « web ».
Demander une précision uniquement si le partage des responsabilités ou une option d’architecture
reste indéterminé ; appliquer les décisions déjà données sans nouvelle validation.

Exemples possibles, à adapter : interface / serveur / outillage ; popup / background / content
pour une extension si ces parties justifient réellement des tâches indépendantes. Un petit projet
peut n’avoir qu’une couche de développement. `design` accueille des artefacts non livrés et peut
utiliser un navigateur pour leur relecture. Le code commun est coordonné par son consommateur.

Chaque couche a un seul écrivain à la fois. Un arbre propre n’est pas une preuve de disponibilité :
vérifier les tâches et affectations actives. Les dépendances entre couches reposent sur des commits
identifiés, jamais sur la lecture des changements non commités d’un autre worktree.

## 3. Installer la configuration locale

Avant toute écriture, rejoindre le worktree qui possède l’outillage du projet selon ses conventions,
confirmer sa branche et préserver le travail préexistant. Ne pas écrire le setup directement sur
une branche d’intégration si le projet l’interdit. Respecter son cycle de tâches lorsqu’il existe.

Adapter les fichiers existants ; compléter les fichiers vides plutôt que remplacer leur contenu.
Produire uniquement ce dont le projet a besoin :

- Un bloc **Conventions de workflow** et une table de routage dans la gouvernance existante :
  cartes, intégration, production, motif des branches, worktrees, commande de création, qualité,
  tests, commits et stratégie de merge. Déduire les commandes des scripts réellement présents ;
  ne pas en annoncer une qui n’existe pas.
- `AGENTS.md` et `CLAUDE.md` reliés à une référence commune. Préserver les instructions existantes.
- Les rôles des agents et une procédure versionnée : chemins absolus, fichiers autorisés,
  preuve et fin de mission. Ne pas présenter les profils `.claude/agents/` comme des sous-agents
  Codex automatiquement chargés. Créer les profils spécifiques seulement pour les outils utilisés.
- Une commande locale pour créer/réutiliser un worktree et une commande pour lister leur état.
  Préférer l’outil et le langage existants ; pour un socle sans runtime, Python 3 et Git suffisent.
- L’exclusion des worktrees imbriqués par Git et par les outils qui parcourent récursivement le
  dépôt : tests, lint, formatage, types, recherche et contexte de build, selon la stack.
- Une documentation courte dans `worktree/README.md` et la documentation de workflow du projet.

### Contrat du créateur de worktrees

La création doit partir d’une couche connue, d’une branche et d’une base explicites. Dériver la
racine du dépôt principal depuis Git, pas depuis l’emplacement d’une copie du script. Découvrir
les arbres déjà enregistrés avant de créer un dossier ; réutiliser le bon chemin si la branche
est déjà sortie, y compris dans l’arbre principal.

Un dossier existant non enregistré, un lien symbolique inattendu, une branche différente ou un
worktree d’un autre dépôt doivent produire une erreur explicite avant toute écriture de `.env`.
Ne pas créer de worktrees imbriqués dans un worktree secondaire. Valider les noms de branche et
empêcher les chemins de sortir de la destination prévue.

Ne pas écraser les fichiers, déplacer une branche occupée, stasher, supprimer un worktree,
forcer un push ni utiliser `reset --hard`. Une relance conserve le travail et l’environnement
existants. Si une base distante est nécessaire, traiter les erreurs de fetch ; ne pas présenter
un démarrage sur une ancienne référence locale comme une synchronisation réussie.

### Isolation d’exécution, si applicable

Docker n’est pas requis pour le socle Git. Si le projet utilise des services, organiser leurs
ports et données pour pouvoir exécuter deux environnements sans collision. Donner aux couches
des identifiants stables, indépendants d’un tri ultérieur, et aux ressources un nom comprenant
l’identité du projet et de la couche. Des noms distincts ne suffisent pas : vérifier les chemins
montés et destinations effectives des écritures.

Préserver les fichiers `.env`, ne pas copier automatiquement de secrets, isoler les bases et
volumes de développement si présents. Les caches et configurations générés appartiennent au
worktree et à la cible concernés. Ne pas installer de serveurs ou Docker pour une maquette ou
une extension qui n’en ont pas besoin. La commande de création ne démarre pas les services.

## 4. Vérifier et livrer

Vérifier l’outillage nouveau dans un dépôt jetable : création depuis une base connue, relance sans
perte de données, branche déjà sortie, appel depuis un worktree secondaire, dossier occupé et
branche inattendue. Aucun test ne doit modifier le dépôt utilisateur ou contacter son remote.

Si un worktree réel est demandé, vérifier après création le dépôt commun, la branche et le chemin
absolu. Tester les exclusions pour que la suite du parent ne découvre pas les tests de ses copies.
Si l’isolation de deux piles fait partie de la demande, les lancer uniquement dans le périmètre
local autorisé et observer leurs endpoints et écritures ; une allocation théorique de ports ne
suffit pas à annoncer que les piles fonctionnent.

Documenter : une tâche par commit, preuves et documentation avant livraison, contrôles avant PR,
vérification du merge distant et réalignement des branches au repos. Distinguer l’historique et
l’équivalence du contenu après rebase. Les branches sales ou utilisées restent intactes ; signaler
les écarts locaux/distants sans force-push. Un worktree de preview n’est créé que pour une demande
d’intégration transversale qui en a besoin ; il ne se déduit pas de la simple création des couches.

Terminer par ce qui a été configuré, les couches et chemins, les commandes utilisables, les preuves
observées et les points non réalisés. Ne pas confondre « consignes présentes », « agent lancé »,
« environnement testé » et « application publiée ». Aucun commit ni action distante sans demande
correspondante. En mode audit, rendre ces constats sans installer ni corriger quoi que ce soit.
