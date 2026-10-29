# OPS-070 — Préparer le dépôt par les commandes du SETUP

- Date : 2026-10-29 ; état : validée avec réserve Ubuntu neuf ; commit local à effectuer.
- Session de création : `01a18808-fc0b-7aa0-b084-441015c3c7ad`.
- Demande : DEM-018 ; référence actuelle `tmp/demande-setup-commandes.md`, relative
  au dépôt principal (hors du worktree). Contenu et décisions à cet emplacement.
- Référence future : `dev-book/demand/DEM-018-setup-commandes.md`, à créer dans
  le principal uniquement à la reconstitution ; ce fichier n’existe pas encore.
- Mission : devops ; worktree `worktree/devops` ; branche `layers/devops`.
- Base locale : `57ae8c5623a9610e70a40f5589bcdaac977e1b21`, commune avec develop.
- Dépendances : aucune contribution amont ; aucune importation de travail non commité.

## Objectif et périmètre

Réaliser les critères de DEM-018 dans une contribution cohérente : commande Make
pour préparer les worktrees, génération du workspace, installation et activation
de l’alias, SETUP validé en sept chapitres et recette complète sur Ubuntu neuf.
Le contenu approuvé reste dans la demande ; ne pas le recopier ici.

Chemins autorisés : `Makefile`, `codebase-integrity/scripts/` pour le lanceur et
la réutilisation de `worktrees.py`, `codebase-integrity/tests/` pour les tests
fonctionnels adaptés, `*.code-workspace`, `SETUP.md` ; README de ces dossiers
et références entrantes sous `docs/architecture/`, `README.md`, `worktree/README.md`
pour les seules corrections nécessaires ; cette carte pour preuves et verdict.
`infra/config/layers.json` est la source de routage à lire, sans redéfinir les couches.
Lire les README applicables avant chaque intervention.

L’outil livré pourra modifier le fichier personnel d’alias Bash de l’utilisateur,
en préservant son contenu ; ne pas modifier directement le shell personnel de
l’environnement de développement pour réaliser la carte. Utiliser un HOME isolé
pour les tests et l’environnement Ubuntu neuf pour la recette effective.

Exclusions : onboarding personnalisable, autres OS/outils IA, publication des
skills, applications, données et `.env`, conventions techniques et affaiblissement
des contrôles. Aucun commit pendant l’implémentation.

## Critères, contrôles et preuves

- Couvrir tous les critères de la demande, y compris l’alias utilisable au chapitre 5,
  l’installation des skills via Codex et l’accès aux trois applications de devops.
- Tester dans un dépôt temporaire avec HOME isolé : première préparation, relance
  sans altération, chemins avec espaces, préservation des configurations/alias et
  refus explicite d’une incompatibilité sans écrasement. Vérifier les cinq branches,
  les dossiers et la configuration du workspace, ainsi que la commande de l’alias.
- Vérifier syntaxe des scripts, JSON du workspace, liens et ancres documentaires.
  Adapter le lien final au déplacement déjà livré sous `docs/architecture/`.
- Exécuter `python3 codebase-integrity/scripts/check.py` ; qualité complète avant PR
  selon les points de contrôle du dépôt. Ne modifier aucun contrôle de convention
  pour faire passer la contribution.
- Préparer puis suivre le parcours complet sur Ubuntu neuf avec interface graphique ;
  relever version, commandes/résultats, ouverture réelle du workspace, disponibilité
  des skills, trois adresses et lancement de l’interview. Sans environnement neuf,
  accès au dépôt privé ou authentification Codex, consigner le blocage : recette non réussie.
- Conserver les preuves dans cette carte ou par liens vers des artefacts distincts ;
  ne pas recopier les guides. Aucun résultat ni verdict humain présumé.

## État et suite

Au découpage : branche existante conservée, index vide et arbre propre avant
création de cette carte. Dernière livraison DEM-017 clôturée dans son brouillon ;
DEM-016 est seulement cadrée, sans mission devops affectée observée.
Maximum OPS local observé : 069, toutes références et fichiers concernés examinés,
sans fetch. Aucun contrôle d’implémentation ni recette exécuté à cette étape.

Après implémentation : vérification humaine, puis commit local de cette seule carte
explicitement validée avec sa contribution et ses preuves. Reconstitution prévue
sur `demands/DEM-018` depuis develop local vérifié dans le principal (`.`), libre
et propre, par cherry-pick du commit validé. Retour du principal sur develop après
fusion ; couches conservées sur `layers/*`. Ne pas créer cette branche au découpage.

## Implémentation et preuves — 2026-10-29

Reprise de la seule carte non suivie créée au découpage ; aucune modification
étrangère. Base et branche inchangées : `57ae8c5623a9610e70a40f5589bcdaac977e1b21`,
`layers/devops` ; index vide. Session identique à la création.

- `make setup-worktrees` appelle le nouveau `setup_worktrees.py` : précontrôle des
  destinations, workspace et alias avant création, réutilisation de `worktrees.py`,
  conservation des fichiers compatibles et refus des conflits. Aucun fetch.
- Workspace technique existant `aide.code-workspace` conservé, ou généré s’il manque ;
  ses réglages personnalisés ne sont pas réécrits. Alias installé dans `.bash_aliases` ;
  activation explicite dans SETUP. Aucun fichier personnel de l’hôte modifié.
- SETUP en sept chapitres selon le contenu confirmé, sans commentaire « à créer »
  devenu obsolète. Ubuntu 24.04 LTS retenu comme cible technique : paquets
  [docker-compose-v2](https://packages.ubuntu.com/noble/docker-compose-v2) et
  [docker.io](https://packages.ubuntu.com/uk/noble/docker.io) répertoriés dans Universe.
  Disponibilité documentaire vérifiée ; installation non exécutée sur Ubuntu neuf.
- Responsabilité du lanceur ajoutée au README des scripts ; deux ancres entrantes
  corrigées, lien final vers la boucle déplacée sous `docs/architecture/`.

Commandes depuis le worktree de mission :

| Contrôle | Résultat |
| --- | --- |
| `python3 -B -m unittest discover -s codebase-integrity/tests -p test_setup_worktrees.py -v` | 7 tests réussis ; Git et HOME jetables, espaces/apostrophe/dollar dans le chemin, alias exécuté avec un faux VS Code, configurations et travaux locaux préservés |
| `python3 codebase-integrity/scripts/check.py` | 30 tests réussis hors sandbox ; premier passage bloqué par le socket HTTP temporaire, sans modification de contrôle |
| `make test` | Réussi hors sandbox : cinq identités, quinze configurations, raccourcis et collisions de ports ; premier passage limité par le socket temporaire |
| `git diff --check` | Réussi |
| Analyse Python, `bash -n` sur les blocs du SETUP, JSON workspace | Réussies |
| Liens et ancres concernés | 3 cibles locales valides |

Périmètre présenté : cinq fichiers suivis modifiés (`Makefile`, `SETUP.md`, README
des scripts, deux index documentaires) ; trois fichiers non suivis :
`codebase-integrity/scripts/setup_worktrees.py`,
`codebase-integrity/tests/test_setup_worktrees.py` et cette carte.
Aucun commit, aucune branche de demande, aucun changement applicatif.

### Limite de recette

Parcours complet sur Ubuntu neuf **non exécuté** : ni `/dev/kvm`, ni QEMU,
Multipass ou virt-install disponibles ; accès Docker courant refusé au socket.
Un conteneur seul ne prouverait pas l’installation de Docker et du bureau VS Code.
Accès effectif au dépôt privé des skills et connexion Codex non vérifiés ; aucun
compte personnel utilisé pour simuler ce parcours. Qualité complète avant PR non
exécutée à cette étape, applications inchangées.

Recette restante : sur une installation neuve Ubuntu Desktop 24.04 LTS avec accès
GitHub/Codex, suivre SETUP de bout en bout, relever les versions installées, vérifier
les cinq worktrees et l’ouverture réelle du workspace par l’alias, installer et
retrouver les skills dans Codex, ouvrir les trois adresses du chapitre 6 et lancer
l’interview du chapitre 7. Consigner les résultats ici sans répéter les commandes.
La carte ne satisfait pas encore ce critère ; aucun verdict humain obtenu.

## Verdict humain — 2026-10-29

« validé », après présentation explicite de la réserve : parcours complet sur
Ubuntu neuf non exécuté. Validation avec cette réserve, sans déclarer la recette
réussie. Huit empreintes identiques à l’état soumis, HEAD de base inchangé et
index vide avant ajout de cette seule trace ; aucun changement fonctionnel.
