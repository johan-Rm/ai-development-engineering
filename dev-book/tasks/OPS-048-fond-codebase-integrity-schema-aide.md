# OPS-048 — Recolorer le bloc Codebase Integrity du schéma AIDE

- État : validée.
- Date : 2026-10-26.
- Demande d’origine : [DEM-003](../demand/DEM-003-fond-codebase-integrity-schema-aide.md).
- Couche : devops, maintenance du schéma du cadre.
- Session : référence de session indisponible ; mission confiée dans ce chat.
- Worktree : `worktree/devops`.
- Branche : `layers/devops`, conservée à `2c9aeb348af37e9858df4144e00576ee3425bf3b`.

## Objectif et périmètre autorisé

Appliquer au seul bloc Codebase Integrity un fond opaque `#C07040` et des textes
`#FAFAF6`, puis documenter cette adaptation sans modifier son rôle de contrôles sans IA.

Chemins autorisés :

- `dev-book/resources/vue-d-ensemble-ai-development-engineering.html` ;
- `design/charte-graphique.md` ;
- la présente carte et la demande DEM-003 pour leurs preuves et leur suivi.

La synthèse graphique partagée est rattachée à cette mission consommatrice du cadre.
Lire les README racine, dev-book, ressources et design ainsi que la charte officielle
`design/Brand Guidelines - Graines Digitales (standalone).html` avant implémentation.
Si une règle locale doit changer, mettre à jour le README concerné après lecture ;
aucun changement de règle locale n’est prévu ici.

## Exclusions

Conserver les autres couleurs, notamment le bleu IA `#1B6EAE`, les textes, la sémantique,
la disposition, les interactions, les polices et le plein écran. Ne pas modifier la charte
originale, les sources historiques, les applications, l’infrastructure ou les skills personnels.
Ne pas changer globalement la couleur des éléments humains pour recolorer ce bloc.

## Dépendances par commit et ordre

Dépendance graphique existante : `8db9d9bd436d835d6119ea55eac461b4d463cb19`
(OPS-047, bleu IA de DEM-002), déjà ancêtre de la tête locale vérifiée.
Base locale : `2c9aeb348af37e9858df4144e00576ee3425bf3b`. Aucune tâche amont à produire.
Le document DEM-003 non commité appartient à cette même mission et à ce même worktree ;
aucune copie inter-worktrees n’est nécessaire. Carte unique, sans parallélisation.

## Critères d’acceptation

1. Le fond effectif du bloc Codebase Integrity est `#C07040`, à pleine opacité.
2. Le titre et le sous-texte sont en `#FAFAF6`.
3. Textes, rôle sans IA, interactions et autres éléments sont conservés.
4. La synthèse graphique décrit la nouvelle adaptation de ce bloc et préserve le bleu IA.
5. Les couleurs effectives et le rendu visuel, y compris les états interactifs existants,
   sont vérifiés ; toute limite d’exécution est indiquée dans la preuve.

## Vérifications et preuve attendues

Comparer le diff HTML avec la base pour vérifier la portée locale des styles et l’absence
de changement du contenu et des scripts. Inspecter les couleurs calculées du bouton,
du titre et du sous-texte, au repos et dans ses états interactifs existants.
Relire le rendu dans le navigateur : lisibilité, ouverture/fermeture du panneau de détails,
focus clavier et conservation du plein écran. Conserver une capture ou une référence
précise d’aperçu et les résultats de contrôle dans cette carte. Mesurer le contraste et
rapporter la valeur sans annoncer une conformité non vérifiée.
Exécuter `git diff --check`. Aucun test applicatif nouveau requis pour cette modification
CSS locale ; les contrôles avant PR restent `python3 codebase-integrity/scripts/quality.py`
et les tests de l’outillage `python3 codebase-integrity/scripts/check.py` selon les changements.

## Documentation et réalisation

Documentation prévue : adaptation du bloc dans `design/charte-graphique.md`, preuves dans
cette carte. Modifications réalisées ; aucun verdict humain anticipé.

## Preuve du découpage

Historique de toutes les références Git locales et fichiers des worktrees examinés sans
fetch : maximum OPS-047 avant attribution d’OPS-048. Branche et tête vérifiées dans le
worktree absolu ; seul DEM-003 était non suivi avant découpage. Les cartes consultées
n’indiquent aucune autre mission active sur ces chemins ; la disponibilité devra être
revérifiée avant écriture de l’implémentation. Branche existante conservée, aucun rebase,
fetch, commit ou opération distante. La branche de réunion est prévue dans DEM-003.

## Réalisation et preuves — 2026-10-26

Dans le worktree et la branche affectés, modification de la règle CSS locale
`.shared-checks>.controls` et du sous-texte : fond `#C07040`, texte `var(--paper)`
(`#FAFAF6`). Synthèse graphique mise à jour pour cette exception ; rôle sans IA conservé.
La comparaison Python exacte avec `git show HEAD:<chemin HTML>` après la seule
substitution CSS attendue réussit : contenu, structure, scripts, disposition et couleurs
IA inchangés. `git diff --check` réussit. Contraste calculé par luminance relative sRGB :
3,563:1 entre `#FAFAF6` et `#C07040` ; aucune conformité d’accessibilité annoncée.

Tentative Playwright depuis le worktree avec le module local
`app/web/targets/app/node_modules/playwright-core/index.mjs`, Chromium headless,
viewport 1440 × 1000, cible HTML locale. Échec avant ouverture de page :
`error while loading shared libraries: libnspr4.so: cannot open shared object file`.
Aucune capture produite ; couleurs calculées, focus, panneau de détails et plein écran
non vérifiés au navigateur. Aperçu à ouvrir :
`dev-book/resources/vue-d-ensemble-ai-development-engineering.html` dans ce worktree.
Critères 1 à 4 couverts par inspection statique ; critère 5 incomplet.
Aucun test applicatif ou d’outillage ajouté pour cette modification CSS locale.
Aucun contrôle modifié pour contourner cette limite. Arrêt avant vérification humaine.

Aucun commit : les instructions explicites fournies par l’utilisateur limitent les commits
aux demandes explicites, et priment sur l’autorisation par invocation figurant dans
l’AGENTS.md local. Autorisation explicite du commit à obtenir avant clôture de l’implémentation.
Les documents non suivis DEM-003 et OPS-048 sont conservés dans leur worktree d’origine.
Aucun push, PR ou merge.

## Reprise de la vérification navigateur — 2026-10-26

À la demande de l’humain, tentative `sudo -n apt-get install -y libnspr4` :
installation système impossible sans mot de passe sudo. Alternative locale réalisée :
`apt-get download libnspr4 libnss3 libasound2t64`, puis extraction des paquets avec
`dpkg-deb -x` dans `/tmp/aide-chromium-libs`. Aucun paquet système modifié.
Chromium lancé hors sandbox avec
`LD_LIBRARY_PATH=/tmp/aide-chromium-libs/usr/lib/x86_64-linux-gnu node /tmp/DEM-003-visual.mjs`.

Contrôle Playwright réussi à 1440 × 1000 : fond calculé `rgb(192, 112, 64)`, titre
et sous-texte `rgb(250, 250, 246)` au repos, au survol, au focus et panneau ouvert.
Le clic ouvre le panneau (`aria-expanded=true`), Échap le ferme (`false`).
Capture `/tmp/DEM-003-schema.png` examinée : bloc terre cuite et texte blanc cassé,
panneau Codebase Integrity visible, autres blocs olive et bleus conservés.
La limite de bibliothèque manquante est levée pour cette exécution locale.
Le plein écran navigateur et les formats mobiles n’ont pas été exercés ; leur code reste
inchangé selon la comparaison statique. Aucun verdict humain ni commit ajouté.
Les dépendances et la capture sous `/tmp` sont temporaires et leur présence ne garantit
pas une installation permanente dans les prochaines sessions.

## Passage sur commit — 2026-10-26

Instruction humaine explicite : committer l’implémentation avant la vérification sans
redemander d’autorisation. Le blocage d’autorisation précédent est levé.
Commit de la carte avec DEM-003, le schéma et la synthèse graphique ; SHA communiqué
dans le chat après création du commit. Contrôles ciblés et limites ci-dessus conservés.
Aucun verdict humain inventé ; vérification humaine à lancer séparément.

## Verdict humain — 2026-10-26

Verdict explicite dans le chat : « validé », après présentation du résultat et de ses limites.
Commit d’implémentation accepté : `4930bc99d7678d80f6ddeb2ed6a64b224f5a572a`.
Les cinq critères de DEM-003 sont acceptés pour cette carte unique : couleurs effectives,
conservation du contenu et des autres blocs, documentation et preuves de rendu/interactions.
Le contraste mesuré de 3,563:1 et l’absence de tests mobile et plein écran ont été présentés
avant le verdict ; aucune conformité supplémentaire n’est déduite de cette validation.
Branche `layers/devops`, worktree affecté et index propres vérifiés avant écriture.
Seuls la carte et DEM-003 sont mis à jour pour tracer le verdict ; aucun changement de code.
La reconstitution et la livraison restent à lancer séparément.
