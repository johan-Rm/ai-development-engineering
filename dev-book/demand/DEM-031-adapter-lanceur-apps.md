# DEM-031 — Adapter le lanceur à apps

- Type : consolidation
- Date : 2026-11-09
- Session de création et d’analyse : `01a1b040-6627-7b60-a2ec-ab2f985bf83d`
- État : reconstituée et contrôlée ; prête à publier vers develop.
- Décisions humaines : « deux fichiers » pour le transfert ; « confirmé » pour
  la compatibilité et les contrôles proposés, le 2026-11-09.

## Besoin et références

Permettre la livraison séparée du lanceur et du renommage de
DEM-030 (branche locale `demands/DEM-030`, non livrée).
Les deux fichiers transférés proviennent du commit validé
`48eab41ca24a990957f4e178135ea220378ee80e` ; patch conservé dans
`tmp/transfert-codebase-integrity-DEM-031.patch` du principal.
Typage et déclaration : [conventions du dev-book](../README.md#types-de-demandes).

## Analyse et règle confirmée

Le lanceur résout ses applications dans `apps/` si ce dossier existe dans la
racine sélectionnée ; sinon il utilise `app/`. Le choix est commun aux trois
applications et aux actions install, serve et check, y compris avec `--root`.
Si `apps/` est présent mais incomplet, échouer pour l’application manquante sans
repli sur `app/`. Si les deux organisations existent, privilégier `apps/`.
Aucun alias, déplacement local, écrasement de `.env` ni affaiblissement de contrôle.
La compatibilité reste en place après DEM-030 ; son retrait n’est pas inclus.

Le remplacement strict initial empêchait de livrer chaque demande séparément.
La résolution automatique confirmée supprime ce blocage avec un seul lanceur ;
une configuration manuelle ajouterait un paramètre et des adaptations CI inutiles.

Couverture lue : lanceur complet et ses quatre tests, points d’appel de la CI,
`quality.py`, Make et recettes infra sur la base Devops ; résultat renommé de
DEM-030 vérifié séparément. Aucun autre résolveur du lanceur trouvé dans ces zones.
Les chemins directs de Make/Compose/CI sont adaptés par DEM-030 ; ne pas les
modifier ici. Les quatre tests actuels protègent `.env`, les échecs et OpenAPI,
mais ne couvrent ni l’ancien emplacement ni la coexistence des organisations.
La règle de sélection sera documentée dans le README local existant ; elle
n’y figure pas encore. Les tests de résolution constituent le contrôle bloquant.
Aucun test runtime/navigateur nouveau exécuté à l’analyse.

## Découpage

| Carte | Couche / branche | Dépendance de réalisation |
| --- | --- | --- |
| [OPS-082](../tasks/OPS-082-adapter-lanceur-apps.md) | devops / `layers/devops` | Aucune ; base locale `d42251e1dca1c4efd700a6a453f4bec80a2634c3` |

Deux fichiers de code transférés ; `codebase-integrity/README.md` s’ajoute
uniquement pour documenter la règle confirmée dans sa rubrique existante.
La carte conserve les preuves du transfert, de la compatibilité et de sa validation humaine.

## Ordre et reconstitution

Livrer DEM-031 avant DEM-030 : qualité complète sur l’organisation `app/`, puis
preuve du lanceur sur les applications sous `apps/`, sans copie de travail entre
missions. La vérification combinée ne bloque pas l’implémentation d’OPS-082.
La branche `layers/devops` est conservée sans rebase ni fetch ; ses modifications
identifiées appartiennent uniquement au transfert OPS-082, pas à une autre mission.

Créer `demands/DEM-031` depuis develop vérifié dans le principal (`.`) à l’étape 05,
après validation et commit. Le principal est actuellement occupé par
`demands/DEM-030` : coordonner sa libération, sans déplacer cette mission
implicitement. Ne pas créer la branche finale dans un worktree de couche.
Retour sur develop après fusion ; DEM-030 restera à reprendre sur la base intégrée.

## Déclaration de contribution prévue

À porter dans la demande définitive lors de la reconstitution, en vérifiant
les chemins réellement modifiés ; une seule correction et un contrôle renforcé.

```contribution-json
{
  "version": 1,
  "corrections": [{
    "chemins": [
      "codebase-integrity/scripts/apps.py",
      "codebase-integrity/tests/test_apps.py",
      "codebase-integrity/README.md"
    ],
    "convention": "codebase-integrity/README.md#conventions-techniques",
    "controles": ["codebase-integrity/tests/test_apps.py"]
  }],
  "accompagnements": [],
  "sans_correction": ""
}
```

## Suivi d’implémentation

Le 2026-11-09 : compatibilité réalisée ; résultats et limites dans OPS-082,
source unique des preuves. La validation humaine de ce nouveau comportement
reste attendue à l’étape 04 ; aucun commit créé.

## Validation et commits

Verdict humain du 2026-11-09 : « validé ». Empreintes conformes avant commit.
OPS-082 : `0d713f489d2d0027a61174517caa2f8aaae5cf9f` ; trace documentaire : `30c83d0edf2373b1e25463eb63e0a6096f20bc3b`.
Couche Devops propre ; aucun push ni reconstitution effectué.

## Reconstitution

Le 2026-11-09 : utilisation temporaire du principal explicitement confirmée.
DEM-030 conservée sur sa branche à `18051d714b634c2149edcae6c000f5066bfc7da7`. Base develop locale
vérifiée : `d42251e1dca1c4efd700a6a453f4bec80a2634c3` ; retour prévu sur develop après livraison.
Ressources locales conservées et réunies sous `app/`, organisation présente
sur cette base ; aucun transfert entre worktrees.

| Nature | Source | Obtenu |
| --- | --- | --- |
| implementation | `0d713f489d2d0027a61174517caa2f8aaae5cf9f` | `d9638e719bb75d71cee8426f9b4fdb567ff7ca2e` |
| trace | `30c83d0edf2373b1e25463eb63e0a6096f20bc3b` | `d5bc2f2fc31dbd6b7a3de65887263703314f7080` |

## Contrôles de livraison

Le 2026-11-09, base distante après fetch :
`d42251e1dca1c4efd700a6a453f4bec80a2634c3`.
`quality.py --commit-base origin/develop --commit-head HEAD` réussi sur
`b1729a0e37372fbd9ffbfa148298c881501b0b2a` : contribution, messages,
liens, 117 tests d’outillage, API/OpenAPI, typechecks et builds sur `app/`.
Preuves sur les trois applications sous `apps/` conservées dans OPS-082.
Rebase and merge autorisé ; règles de develop consultées, sans modification.
Couches API/Web/Backoffice portant DEM-030 : préserver leurs commits inédits ;
leur réalignement bloque la clôture du suivi global jusqu’à leur livraison.
Aucun test navigateur/runtime supplémentaire exécuté localement.
