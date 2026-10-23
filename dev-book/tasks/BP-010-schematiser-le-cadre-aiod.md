# BP-010 — Schématiser le cadre AIOD et ses deux boucles

> Note historique ajoutée lors d’OPS-010 : les mentions de fusion préparée, de fichiers non commités ou d’anciens chemins décrivent l’état lors de cette tâche. Elles ne décrivent pas l’état Git actuel ni un travail restant. Les cartes sont désormais réunies dans `dev-book/tasks/`.

- **Créée le** : 2026-10-18.
- **Session** : non disponible (Codex).
- **Statut** : clôturée le 2026-10-20 — schéma et référence graphique livrés.
- **Type** : docs.
- **Tests** : relecture visuelle Chromium sur ordinateur et mobile ; vérification du SVG, du défilement et de l’impression sur une page.
- **Réf** : docs/aiod/principes.md, sources/AIOD-carrousel-v1.html ; deux inventaires fournis dans la conversation.
- **Mission historique** : maintenance du cadre, sur la branche historique de maintenance, worktree `<depot>`.
- **Chemins autorisés** : `docs/aiod/cadre-aiod.html`, `docs/aiod/README.md`, `docs/aiod/charte-graphique.md`, `AGENTS.md`, cette carte.
- **Base** : `c610bfdb437e9d5feae0eee8aea6fec9884e752b`.

## Contexte

L'utilisateur veut retravailler sa représentation du cadre AIOD à travers un fichier HTML :
le cadre général, la boucle IA d'écriture de code et la boucle de consolidation déterministe.

## Décisions de cadrage

Après la première proposition, l’utilisateur précise vouloir une vue rapide de l’écosystème,
et non un document explicatif illustré. La v2 remplace donc la v1 dans le même fichier.
Un seul schéma SVG dans le HTML : humain, cadre englobant, boucle IA, boucle de consolidation,
contrôles communs, sortie produit et flèches de retour. Libellés courts ; aucun catalogue d’outils,
aucune exploration d’étapes. Impression sur une page paysage.
Sur petit écran, conserver la lisibilité des libellés avec défilement horizontal du schéma.
Aucune modification de gouvernance ni installation d’outils.

## Hors périmètre

Installation d'outils qualité, modification de la gouvernance, applications, Docker, commit, push, déploiement.

## Définition de terminé

- [x] Un fichier HTML autonome représente le cadre et les deux boucles reliées.
- [x] Les responsabilités, retours et preuves sont lisibles.
- [x] Le schéma reste lisible sur mobile et s’imprime sur une page paysage.
- [x] La proposition est liée depuis l'index documentaire et ses vérifications sont consignées.

## Preuves

La v1 détaillée est remplacée à la demande de l’utilisateur.

- Un seul schéma SVG autonome ; libellés courts, deux boucles et contrôles communs.
- Chromium 1366 × 768 : tout le document tient sur un écran, capture relue.
- Mobile 390px : aucun débordement de la page ; schéma défilant horizontalement.
- Impression PDF paysage : une seule page générée et vérifiée.
- Aucune erreur JavaScript pendant le parcours.
- `git diff --check` : OK.
- Fichiers non commités : HTML, index documentaire et carte BP-010.
- Aperçu local conservé : http://127.0.0.1:8090/cadre-aiod.html.

## Ajustement demandé

Le cadre extérieur englobe toute l’illustration, titre et légende compris.
Intitulés : « BOUCLE IA DE CODAGE » et « SESSION DE CONSOLIDATION DÉTERMINISTE ».

## Clarification du cadre conceptuel

Le terme « cadre » désigne l’architecture, les couches, l’isolation et les règles.
La v3 représente ces éléments sur les quatre côtés d’une enveloppe SVG autour des acteurs,
des deux boucles et des contrôles. La bordure décorative de la page est retirée.
La consolidation alimente les règles de l’enveloppe par une flèche « enrichir le cadre ».
Les intitulés « BOUCLE IA DE CODAGE » et « SESSION DE CONSOLIDATION DÉTERMINISTE » sont conservés.

Vérification v3 : capture Chromium relue, un écran à 1366 × 768, défilement mobile
à 390px, PDF d’une page et aucune erreur JavaScript. `git diff --check` : OK.

## Vue plein écran demandée

La v4 utilise toute la fenêtre, sans largeur maximale ni espace réservé à un en-tête externe.
Le titre AIOD, son sous-titre et les deux textes de légende sont intégrés dans l’enveloppe SVG.
Le bouton d’impression est supprimé. Le schéma et les relations existantes sont conservés.

Vérification v4 : Chromium confirme le remplissage exact de la fenêtre à 1918 × 924
et 1366 × 768 ; tous les textes sont dans l’enveloppe, aucun bouton n’est présent.
Capture relue, défilement mobile conservé, PDF d’une page et aucune erreur JavaScript.

## Rôles distingués par couleur

V5 : interventions humaines en bleu, interventions IA en violet et étapes partagées
marquées par deux traits colorés. Les artefacts et l’exécution des contrôles restent neutres.
« Automatiser » désigne la création des contrôles par l’IA, pas leur exécution déterministe.
Le bandeau humain est remplacé par une mention discrète et une légende des deux rôles.

Vérification v5 : capture relue, couleurs et rôle partagé légendés. Plein écran aux deux
résolutions vérifiées, textes dans le cadre, mobile défilant et PDF une page : OK.

## Charte Graines Digitales et couleurs de rôle — 2026-10-20

V6 : référence lue dans `<ancienne-source-externe>/Brand Guidelines - Graines Digitales (standalone).html`, édition 5, août 2026.
Palette olive #6B7A4A, blanc cassé #FAFAF6, noir #212121 et gris de la charte.
Inter pour le texte ; Newsreader pour le titre, remplacement explicitement autorisé de Rationale.
Polices latines issues du document de référence et intégrées au HTML pour rester autonome.
L’humain et le cadre sont olive ; l’IA utilise #C07040, extension explicitement demandée par l’utilisateur.
Les étapes partagées combinent fond olive pâle et bordure terre cuite. Les traits de rôle sont supprimés ;
les flèches fonctionnelles des boucles restent présentes. Aucun logo n’est ajouté ni modifié.

Vérification v6 : polices Inter et Newsreader chargées depuis les données intégrées,
aucun élément `role-line` restant. Captures relues, plein écran à 1918 × 924 et 1366 × 768,
textes dans le cadre, mobile défilant, PDF d’une page et aucune erreur JavaScript : OK.

## Référence de marque mémorisée — 2026-10-20

L’utilisateur désigne `design/Brand Guidelines - Graines Digitales (standalone).html` comme
source officielle. Ce fichier préexistant reste intact. Son empreinte SHA-256 est
`21c90482e82d2ce8db416d635c55a3a513ad34bb25a743e0fd91a690d6f3df64`.
Vérification : il est identique octet pour octet à la copie externe consultée précédemment ;
l’écart signalé relève de l’application graphique, pas d’une différence entre les fichiers.
Consigne persistante ajoutée à AGENTS.md et synthèse opérationnelle dans
`docs/aiod/charte-graphique.md`. Les adaptations explicites humain/IA y sont distinguées
des règles de la marque. La mise en page du schéma n’est pas redessinée dans cette étape.

## Police Rationale — 2026-10-20

V7 : à la demande explicite de l’utilisateur, Rationale Regular remplace Newsreader
pour le titre AIOD et les titres des deux boucles. Inter reste utilisée pour les blocs et textes.
Le fichier TTF et sa licence SIL OFL ont été lus dans `<ancienne-source-de-polices>/`.
La police et sa licence sont intégrées dans le HTML autonome, sans requête réseau.

Vérification v7 : chargement de Rationale confirmé dans Chromium et styles calculés des titres vérifiés.
Position du titre adaptée aux métriques de la police ; captures relues. Plein écran aux deux résolutions,
textes dans le cadre, mobile défilant, PDF une page et aucune erreur JavaScript : OK.

## Intitulé long

Ajout de « AI Orchestrated Development » à côté du titre AIOD, en Rationale,
sur la même ligne et à l’intérieur du cadre.

## Zone principale sans padding

Suppression de la marge SVG extérieure de 8 unités. Le cadre conceptuel atteint les
quatre bords de la fenêtre ; la zone principale a explicitement une marge et un padding nuls.
Les bandes du cadre portant les notions architecture, couches, isolation et règles sont conservées.

Coins arrondis du cadre rétablis à `rx="24"` à la demande de l’utilisateur ;
coordonnées bord à bord et padding principal nul conservés.

## Suppression du rôle partagé

V8 : l’utilisateur refuse l’état « Humain + IA ». Chaque action est attribuée à un acteur unique.
Consolidation : signaler (humain), analyser (IA), arbitrer (humain), documenter (IA),
valider la règle (humain), automatiser (IA). Seule la règle validée alimente le cadre.
Codage : l’humain valide le changement avant la livraison par l’IA ; l’IA exécute les vérifications.
La légende et le CSS du rôle partagé sont supprimés ; la référence graphique mémorisée est actualisée.

Vérification v8 : aucune classe ni légende de rôle partagé restante ; chaque action possède
un rôle humain ou IA unique, le code restant un artefact. Capture relue, plein écran,
textes dans le cadre, défilement mobile, PDF une page et absence d’erreur JavaScript : OK.

## Actions en aplats opaques

V9 : suppression des bordures des actions. Fonds olive #6B7A4A pour l’humain et
terre cuite #C07040 pour l’IA, opacité et opacité de remplissage à 1.
Texte blanc cassé sur l’olive et noir sur la terre cuite.

Texte des actions IA et de leur légende passé en blanc cassé #FAFAF6 sur terre cuite,
à la demande de l’utilisateur.

## Clôture

Commit explicitement demandé par l’utilisateur. Le fichier officiel de charte dans `design/` est inclus comme référence du schéma. Tests automatisés sans objet pour cette maquette SVG statique ; les vérifications navigateur ci-dessus constituent ses preuves visuelles. Les nouvelles réflexions sur les quatre thèmes restent dans le chat et ne sont pas appliquées au schéma.
