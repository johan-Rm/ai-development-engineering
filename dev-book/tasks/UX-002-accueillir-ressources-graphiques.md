# UX-002 — Accueillir les ressources graphiques

- Date : 2026-10-30
- Session de création : `01a18c1a-ab5a-7940-b95d-8e44ac3b92fc`
- État : validée ; commit local en cours, à livrer.
- Demande : DEM-025, brouillon `tmp/demande-ranger-ressources-design.md` relatif au dépôt principal.
- Lien définitif futur : `../demand/DEM-025-ranger-ressources-design.md`, à créer à la reconstitution.
- Couche : design ; worktree : `worktree/design` ; branche : `layers/design` conservée.
- Base observée : `b40faca917b01074d078e49ad1cad6f7fb2ff7b6`.

## Objectif et périmètre

Accueillir les trois destinations graphiques définies dans le brouillon DEM-025 et
maintenir les trois dossiers versionnables. Chemins autorisés :
`design/Picto-fond-noir-1000x1000.svg`, les deux HTML v1/v2 de `design/drafts/`,
les `.gitkeep` de drafts/mockups/wireframes, `design/README.md` et cette carte.
Le README conserve strictement sa structure, conformément à la correction humaine.
Les trois `.gitkeep` non suivis sont les seuls changements repris de cette session.

## Dépendances et transmission

Lire les sources exclusivement dans le commit local existant
`181f3ccbc1f1f42fc83cd7d65e8582641d0723b6`, sous `dev-book/resources/`,
selon la correspondance du brouillon. Ne pas copier de fichier non commité.
Aucune opération Git de transmission n’est effectuée au découpage.
Les anciennes sources resteront temporairement présentes jusqu’à la carte devops
consommatrice, qui devra recevoir le commit UX-002 validé avant leur suppression.
Cette coexistence est transitoire ; elle ne crée pas une seconde référence documentaire.

## Critères, contrôles et preuve

Respecter les destinations et l’intégrité définies dans DEM-025. Comparer les empreintes
SHA-256 des trois destinations aux sources du commit indiqué ; vérifier les dossiers
versionnables et `git diff --check`. Consigner résultats et limites ici.
Ne pas modifier les HTML, la charte ni les sources ; ne pas supprimer les fichiers
hors design, changer les tests ou créer un commit à l’implémentation.
Le test navigateur complet sera exécuté dans la carte devops après adaptation du chemin.

## Réalisation et verdict

Réalisée le 2026-10-30 sur le HEAD de base indiqué, sans commit.
Extraction binaire par `git show <commit-source>:dev-book/resources/<source>` ;
comparaison octet par octet et SHA-256 réussies :

- `design/Picto-fond-noir-1000x1000.svg` : SHA-256 `6b15db2d7b869d81cd9d9731f2fb31eec3df3e03fd71b5efd87e509cb7187c50` ; identique au commit source.
- `design/drafts/vue-d-ensemble-ai-development-engineering-v1.html` : SHA-256 `a298d5a4038ccfa10b5b1b2bffcf793b6d4014b94a8c33de0f78910e6f9b17c0` ; identique au commit source.
- `design/drafts/vue-d-ensemble-ai-development-engineering-v2.html` : SHA-256 `298f385417fe687a243692fc952ba84a0c4a8c2f49cfabd6f584c270c6376c73` ; identique au commit source.

`mockups/.gitkeep` et `wireframes/.gitkeep` sont vides ; le `.gitkeep` de drafts,
désormais rempli, a été retiré.
Les anciennes sources sont intactes dans l’attente de la carte devops.
Contrôles initiaux : comparaison binaire, résolution des liens locaux du README,
présence des trois dossiers et `git diff --check` réussis.
Périmètre soumis après correction : README identique au HEAD ; trois ressources, deux `.gitkeep`
et cette carte non suivis. Index inchangé, aucun commit créé.
Le test navigateur reste à exécuter dans OPS-075 ; aucun verdict humain fourni.

## Arbitrage humain — 2026-10-30

Correction demandée : respecter strictement la structure du README ; la rubrique
« Ressources » ajoutée doit être retirée. Retour à l’implémentation, puis nouvelle
présentation et validation nécessaires. Aucun commit autorisé par ce verdict.
Vérification suivante : rubrique toujours présente ; correction non réalisée.

## Correction réalisée — 2026-10-30

Rubrique « Ressources » retirée ; README identique octet par octet à
`git show HEAD:design/README.md`. Les deux rubriques d’origine et leur ordre sont conservés.
Comparaison binaire des trois ressources au commit source répétée : réussie.
`git diff --check` réussi. Aucun autre fichier fonctionnel modifié, aucun commit.
Correction à vérifier ; le verdict précédent ne vaut pas validation de cet état.

## Validation de la correction — 2026-10-30

Verdict humain explicite : « validé », après présentation de UX-002 corrigée.
Empreintes revérifiées identiques à la présentation ; validation limitée à UX-002.
