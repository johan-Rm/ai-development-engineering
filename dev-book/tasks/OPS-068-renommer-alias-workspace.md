# OPS-068 — Renommer l’alias du workspace

- Date : 2026-10-29 ; état : validée par l’humain, commit local à créer.
- Session de création : `01a1869b-17bd-7292-a890-d6785556af2c`.
- Demande : DEM-015 ; besoin de référence : `tmp/demande-renommer-alias-workspace.md`, relatif au dépôt principal, hors de ce worktree.
- Future demande : `dev-book/demand/DEM-015-renommer-alias-workspace.md` ; à créer à la reconstitution, absente à ce stade.
- Mission : devops ; worktree `worktree/devops` ; branche `layers/devops`.
- Base locale vérifiée : `69a709acb15f10a5390867380a88b9cd11fade75`, commune avec develop.
- Dépendances : aucune carte amont ni commit à importer.

## Objectif et périmètre

Réaliser tous les critères de DEM-015 ; le brouillon fait référence pour les noms,
la commande attendue et les exclusions.

Chemins autorisés : `/home/johan/.bash_aliases` pour le seul renommage confirmé,
et cette carte pour les preuves, l’état et le verdict humain.
Préserver les autres définitions ; ne modifier ni le workspace ni les autres réglages.
Le changement personnel reste hors Git ; seules ses traces seront versionnées.
Demander l’autorisation d’écriture via le mécanisme de l’environnement à l’implémentation.

## Vérifications et documentation

- Relever la définition avant modification ; vérifier que le nouveau nom n’existe pas déjà.
- Vérifier le diff limité au nom et la commande inchangée ; ne pas copier les autres alias dans les preuves.
- Exécuter `bash -n /home/johan/.bash_aliases`.
- Dans un Bash neuf sans profils, charger ce fichier et vérifier la définition exacte du nouvel alias et l’absence de l’ancien.
- Faire vérifier humainement l’ouverture du workspace dans VS Code, sans inventer de verdict.

Consigner ici résultats, limites et verdict. Aucun test ajouté au dépôt ni documentation
durable à modifier pour cet alias personnel. Aucun contrôle applicatif nécessaire au renommage.

## Suite et preuves

Le 2026-10-29, renommage effectué dans `/home/johan/.bash_aliases` après
autorisation de l’environnement. Comparaison en mémoire avant/après : seul le nom
de l’alias a changé ; tous les autres octets sont identiques.

- `bash -n /home/johan/.bash_aliases` : code 0.
- `bash --noprofile --norc -c 'source /home/johan/.bash_aliases; alias vscode-worktree-ai-powered-development-engineering; if alias aide-code-workspace >/dev/null 2>&1; then exit 1; fi'` : code 0 ; définition conforme au besoin et ancien alias absent.
- Aucun lancement de VS Code effectué : ouverture du workspace à vérifier humainement.
- État soumis : HEAD de base ci-dessus inchangé ; seul fichier Git non suivi :
  cette carte, index vide. Modification externe limitée au renommage ; brouillon ignoré actualisé.

Les shells déjà ouverts peuvent conserver l’ancienne définition en mémoire ; la preuve
porte sur un shell neuf. Aucun verdict humain ni commit à cette étape.

Après validation humaine à l’étape 04, le commit local portera les traces de cette carte,
sans inclure le fichier personnel. La reconstitution attendra ce commit validé.

## Verdict humain

Le 2026-10-29, réponse explicite « validé » à la présentation d’OPS-068 et à
la vérification demandée de l’ouverture du workspace. Aucun lancement graphique
observé par l’agent ; verdict humain consigné tel quel.

Avant commit, HEAD et index inchangés ; empreintes SHA-256 identiques à la présentation :

- `/home/johan/.bash_aliases` : `67dbda9050b57327052a15343c4bdc142c700d8a46bfcfeeb109c0331a988768`.
- Carte avant ajout du verdict : `d297b66d6d2417426bd27858206d7cc434682cd0afaab86e1f9adf395d000740`.

Syntaxe, définition exacte, absence de l’ancien alias et présence du workspace :
contrôles réussis à la vérification. Seules les traces documentaires du verdict
sont ajoutées au contenu présenté.
