# OPS-077 — Finaliser le rangement des ressources

- Date : 2026-10-30
- Session de création : `01a18c1a-ab5a-7940-b95d-8e44ac3b92fc`
- Demande : DEM-025 ; brouillon `tmp/demande-ranger-ressources-design.md`, relatif au dépôt principal.
- Demande définitive future : `dev-book/demand/DEM-025-ranger-ressources-design.md`, non créée.
- Couche : devops ; worktree : `worktree/devops` ; branche : `layers/devops` conservée.
- HEAD observé : `e43b8461146522e0e7645e6e1692424acfd9f0ce`.
- État : validée ; commit local à effectuer, à livrer.

## Objectif et périmètre

Exécuter les suppressions et actualisations de références définies dans le brouillon,
sans recopier son tableau de destinations. Chemins autorisés : les cinq fichiers
sources à retirer de `dev-book/resources/`, `README.md`, `dev-book/README.md`,
les index et guides Markdown concernés, les liens actifs des demandes/cartes concernées,
`codebase-integrity/tests/browser/vue-aiod.cjs` (chemin cible uniquement), son README
si nécessaire et cette carte. Respecter strictement la structure des README.
Préserver les preuves historiques et verdicts ; convertir les liens des rapports
supprimés en mentions historiques explicites. Exclure toute refonte graphique,
modification des ressources conservées ou évolution générale des conventions/contrôles.

## Dépendances

UX-002 validée : `1faf42c8f0d0110414dca347a774c78d6351946a` ; trace :
`e015fd70323f2006172607f99d82571c4a1787be`.
Transmission explicitement autorisée et effectuée : `1faf42c` → `82a79f6` ;
`e015fd7` → `50a4d34` (HEAD après transmission). Changements DEM-025 préservés.
OPS-076 est indépendante ; ne pas embarquer son changement AGENTS dans cette carte.

## Critères, contrôles et preuve

Après transmission, vérifier les empreintes des destinations selon UX-002,
l’absence des cinq sources et la conservation du JPG, carrousel, PDF et PNG.
Vérifier les liens actifs et `git diff --check`, puis exécuter :
`python3 codebase-integrity/scripts/check_docs.py` et
`node codebase-integrity/tests/browser/vue-aiod.cjs app/web/targets/app`.
Consigner commandes, résultats et limites ici ; aucun succès présumé si dépendance
ou navigateur absent. Qualité complète à la livraison, selon le dépôt.

## Verdict

Non implémentée, aucun verdict. Commit seulement après validation humaine.

## Contrôle préalable — 2026-10-31

Comparaison SHA-256 avant suppression : v1 identique ; v2 différente de la source actuelle.
Source : `5520ce5dd59082f3069cda840dc4d58e053a636986674dcac423c286781aed94` ;
v2 validée : `298f385417fe687a243692fc952ba84a0c4a8c2f49cfabd6f584c270c6376c73`.
La source a évolué dans `ce396be` (OPS-074, harmonisation des boucles), après le
commit source retenu par UX-002. Aucun fichier source supprimé, aucun lien modifié.
La mise à jour de la destination design sort du périmètre de cette carte et modifie
le contenu validé : arbitrage nécessaire avant poursuite. Aucun nouveau commit
d’implémentation créé ; seuls les deux cherry-picks autorisés ont été effectués.

## Décision humaine complémentaire — 2026-10-31

« recommandation validé » : conserver la source actuelle comme v2 pour préserver
OPS-074. Le périmètre inclut donc `design/drafts/vue-d-ensemble-ai-development-engineering-v2.html`,
remplacé à l’identique par la source actuelle avant suppression. La v1 et le SVG
restent identiques aux fichiers validés dans UX-002. Ce choix de contenu ne vaut
pas validation du résultat implémenté.

## Réalisation et preuves — 2026-10-31

Base de reprise après transmission : `50a4d34cf41e4e6494797553ef4dbbe8f0af864a`.
Les cinq anciennes sources sont retirées. Destination v2 identique octet par octet
à la source actuelle de ce HEAD (SHA-256 `5520ce5dd59082f3069cda840dc4d58e053a636986674dcac423c286781aed94`).
SVG et v1 identiques aux empreintes UX-002. JPG, carrousel, PDF et PNG comparés
à `git show HEAD:<chemin>` : inchangés. Titres des README racine, dev-book et design
comparés au HEAD : structure et ordre inchangés. Liens actifs vers les destinations
actualisés ; quatre liens vers les rapports supprimés convertis en mentions historiques.
Chemins en preuves historiques, verdicts et SHA conservés. Test navigateur : seuls
les deux chemins de chargement sont modifiés.

- `python3 codebase-integrity/scripts/check_docs.py` : réussi ; limite signalée
  par l’outil : `docs/README.md` (référence dynamique), sans exception ajoutée.
- `git diff --check` : réussi.
- `node codebase-integrity/tests/browser/vue-aiod.cjs app/web/targets/app` :
  lancement local impossible, bibliothèque système `libnspr4.so` absente.
- Reprise dans l’image locale `aide-app-browser:ec4e123090`, sans réseau, test et HTML
  montés seuls en lecture seule : échec ligne 213, « Aucun contenu masqué verticalement ».
  Comparaison avec test et HTML extraits du HEAD avant déplacement, même image :
  même échec, même ligne. Échec préexistant établi ; aucun test affaibli ni rendu modifié.

Périmètre non commité : cinq suppressions, destination v2 actualisée, deux chemins
du test, liens dans README racine, dev-book, index architecture et les quatre
demandes/cartes historiques concernées, plus cette carte non suivie.
AGENTS et OPS-076 préservés, distincts du périmètre OPS-077. Aucun commit
d’implémentation créé. Qualité complète non exécutée ; test navigateur non réussi.
Le contenu est à vérifier ; la demande n’est pas déclarée terminée.

## Verdict humain — 2026-10-31

« validé » après présentation conjointe d’OPS-076 et OPS-077 ; validation des deux
cartes avec la limite navigateur préexistante présentée. Empreinte globale du contenu
soumis revérifiée : `4a6bde5f4e5c0467e06c93042f75c7cedbf4c07f62053674c7e8c700aa764813`.
Aucun changement fonctionnel depuis la présentation ; seules ces traces sont ajoutées.
Le contrôle navigateur reste en échec : cette validation ne vaut pas réussite du contrôle.
