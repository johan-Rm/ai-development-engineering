# OPS-047 — Passer les éléments IA du schéma AIDE en bleu

- État : validée par l’humain ; commit d’implémentation identifié, livraison non effectuée.
- Date : 2026-10-26.
- Demande d’origine : [DEM-002](../demand/DEM-002-couleur-ia-schema-aide.md).
- Couche : devops, maintenance du schéma du cadre et de ses références partagées.
- Session : identifiant fiable indisponible.
- Worktree : `/home/johan/www/lab/ai-orchestrated-development/worktree/devops`.
- Branche : `layers/devops`, existante et conservée sans rebase.
- Base locale observée : `6477c51f6428bccdd81c08be20edf644e94fee31`.
- Dépendances par commit : aucune tâche amont distincte ; les décisions graphiques sont
  confirmées dans DEM-002. Demande et carte sont enregistrées dans ce même worktree.

## Objectif

Remplacer la couleur IA par `#1B6EAE` dans toute la vue interactive et aligner ses consignes.

## Chemins autorisés

- `dev-book/resources/vue-d-ensemble-ai-development-engineering.html` : couleur des éléments IA.
- `design/charte-graphique.md` : adaptation explicitement demandée pour l’IA.
- `AGENTS.md` : référence graphique à la couleur IA.
- `dev-book/resources/README.md` et `design/README.md` : uniquement si une règle locale change.
- `dev-book/demand/DEM-002-couleur-ia-schema-aide.md` et la présente carte : suivi et preuves.

Lire les README applicables et la charte officielle locale avant écriture graphique.
La référence partagée de design appartient au périmètre de cette mission consommatrice ;
vérifier l’absence d’autre écrivain sur ces chemins avant de commencer.

## Exclusions

Charte officielle HTML, ressources historiques, textes et structure du schéma, comportements,
couleurs humaines, applications, infrastructure, skills personnels, modifications d’anciennes cartes.
Ne pas créer de nouvelle convention ou de contrôle bloquant dans cette carte.

## Critères d’acceptation

1. Les actions IA des deux boucles et la légende utilisent toutes `#1B6EAE`.
2. Aucun usage actif de la terre cuite pour le rôle IA ne subsiste dans les chemins concernés.
3. La synthèse graphique et AGENTS.md décrivent la même adaptation demandée.
4. Les couleurs humaines, la typographie, les textes, la disposition et les interactions sont préservés.
5. Le texte blanc cassé sur bleu reste lisible, avec mesure du contraste et relecture visuelle.

## Tests, documentation et preuves attendues

- Relire le diff et rechercher les anciennes et nouvelles couleurs ainsi que les mentions de terre cuite.
- Mesurer le contraste du texte `#FAFAF6` sur `#1B6EAE` ; viser au moins 4,5:1 pour le texte courant.
- Produire des captures des deux boucles et de la légende, à une taille ordinateur et une taille mobile ;
  vérifier les interactions existantes et le plein écran.
- Consigner les commandes, résultats et chemins des captures dans cette carte.
- Exécuter `git diff --check`. Pas de test applicatif ni de déploiement requis pour ce changement.
- Avant PR : `python3 codebase-integrity/scripts/quality.py`, selon les consignes du projet.
  `python3 codebase-integrity/scripts/check.py` si l’outillage est touché (hors périmètre prévu).

## Réalisation et verdict

Changement appliqué le 2026-10-26 dans le worktree et la branche affectés.
Les seules modifications préexistantes étaient DEM-002 et cette carte, produites au découpage.
Aucune mission concurrente identifiée dans le dépôt ; la demande explicite d’implémentation
reprend cette mission et ses chemins. Aucune dépendance amont distincte.

- HTML : `#C07040` remplacé par `#1B6EAE` ; variable `--terra` renommée `--ia`
  dans sa déclaration et ses deux usages (rôle IA et sortie de cycle).
- Consignes alignées dans AGENTS.md et design/charte-graphique.md ; README des ressources actualisé.
- Charte officielle relue ; fichier officiel inchangé, bleu traité comme adaptation humaine.
- Contrôle Python ponctuel : HTML strictement identique au fichier HEAD après ces deux substitutions.
  Cela vérifie la conservation des textes, styles sans rapport et scripts d’interaction.
- Contraste calculé par luminance sRGB : `#FAFAF6` sur `#1B6EAE` = 5.162:1, supérieur à 4,5:1.
- Recherche ciblée : aucune ancienne couleur ou mention active de terre cuite dans les trois fichiers modifiés.
- `git diff --check` : réussi.
- `node codebase-integrity/tests/browser/vue-aiod.cjs app/web/targets/app` : impossible à exécuter,
  Chromium échoue avant ouverture de la page : bibliothèque `libnspr4.so` absente.
  Même résultat hors sandbox. Aucun contrôle du vérificateur n’a été modifié.
- Captures, rendu ordinateur/mobile et essai plein écran non réalisés : vérification visuelle en attente.
  Aucun verdict humain sur le rendu ; aucune validation déclarée.
- Qualité avant PR non lancée à cette étape, aucun outillage modifié.

Arrêt sur le blocage navigateur conformément au skill d’implémentation. Aucun commit effectué.
Les instructions explicites fournies par l’utilisateur réservent les commits à une demande explicite ;
l’autorisation plus large du fichier AGENTS.md du worktree n’est pas appliquée à leur place.
La demande et cette carte couvrent ensemble les quatre critères de DEM-002.
Branche de réunion prévue : `demands/DEM-002`, à créer à la reconstitution.
Aucun commit, push, PR ou merge effectué au découpage.

## Choix final après essais — 2026-10-26

Après comparaison de `#2563EB`, `#6AB3E4` et `#1B6EAE` dans l’aperçu local,
l’humain a choisi « parfait on garde celui la » pour `#1B6EAE` et demandé
d’actualiser la demande et la carte. Les consignes associées sont alignées.
Le contrôle du diff et le calcul du contraste ont été rejoués avec succès.
Ce choix de couleur ne constitue pas un verdict global sur la carte.

## Verdict humain et contrôle de reconstitution — 2026-10-26

L’humain a invoqué `verifier-demande` avec le verdict explicite « validé », après présentation
de la couleur finale `#1B6EAE`, des consignes alignées, du contraste de 5,16:1 et des limites
navigateur. Ce verdict couvre OPS-047, seule carte de DEM-002, sur le résultat local présenté.
Il ne transforme pas les contrôles navigateur non exécutés en contrôles réussis.

Aucun SHA d’implémentation disponible : les quatre fichiers de réalisation sont modifiés
localement et la demande et cette carte restent non suivies. L’index est vide.
La reconstitution demandée ensuite ne peut réunir cette contribution sans commit identifié.
Conformément aux skills de vérification et de reconstitution, aucun commit de code manquant
n’est créé à ces étapes et aucun fichier non commité n’est copié dans une autre mission.
Branche dédiée et worktree de réunion non créés ; aucune opération distante effectuée.
Autorisation explicite de créer le commit d’implémentation manquant à recueillir.

## Régularisation du commit d’implémentation — 2026-10-26

L’utilisateur précise explicitement que l’implémentation doit toujours committer, puis réinvoque
`implementer-demande` pour DEM-002. Cette instruction lève le blocage d’autorisation précédent.
Les mentions antérieures de contribution absente décrivent l’état avant cette régularisation.

Branche et index revérifiés : `layers/devops`, index initialement vide ; seuls les six fichiers
prévus de DEM-002 sont présents dans le diff et indexés pour ce commit unique OPS-047.
La mission reprend les mêmes chemins dans le même worktree, sans dépendance amont distincte.
Contrôle Python rejoué : HTML exactement égal à HEAD après substitution de la couleur et
renommage de la variable ; consignes alignées sur `#1B6EAE`. `git diff --check` réussi.
Le contraste reste de 5,162:1. Aucun changement fonctionnel supplémentaire.
La limite Chromium déjà documentée subsiste ; les essais visuels effectués par l’humain
et son verdict « validé » sont conservés sans inventer de captures automatisées.

Le présent commit contient réalisation, demande, documentation et preuves. Son SHA sera
rapporté dans le chat et pourra être consigné lors de la vérification sur commit.
Aucune reconstitution, opération distante ou livraison lancée par cette invocation.

## Vérification du commit — 2026-10-26

Commit d’implémentation vérifié : `8db9d9bd436d835d6119ea55eac461b4d463cb19`.
Le verdict humain explicite « validé », déjà exprimé pour OPS-047, est associé à ce SHA :
le contrôle de correspondance établit que le schéma commité est identique au résultat local
présenté et accepté. Aucun nouveau verdict n’est déduit des seuls contrôles.

Couverture des critères :

1. Les éléments IA utilisent la variable `--ia:#1B6EAE`, actions des deux boucles et légende comprises.
2. L’ancienne couleur est absente du schéma et des consignes graphiques actives modifiées.
3. AGENTS.md, la synthèse graphique et le README des ressources portent la même couleur finale.
4. La comparaison exacte avec le parent du commit ne montre dans le HTML que la substitution
   de couleur et le renommage de variable : textes, structure et scripts conservés.
5. Contraste mesuré à 5,162:1 ; l’humain a examiné l’aperçu puis accepté le résultat.

`git show --format= --check HEAD` et les assertions Python de correspondance ont réussi.
Arbre et index propres avant la trace documentaire. Aucun autre changement observé.
Les captures ordinateur/mobile et le contrôle automatisé du plein écran restent non réalisés,
Chromium ne démarrant pas faute de `libnspr4.so`. La validation humaine est conservée avec
cette limite ; aucun test navigateur n’est présenté comme réussi.
La vérification ne lance ni reconstitution ni livraison.
