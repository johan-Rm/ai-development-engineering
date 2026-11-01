# Dev-book

Le journal opérationnel du projet : besoins, tâches et traces de réalisation.

## Rôle et responsabilités

- `demand/` conserve les besoins, le contexte et les décisions de cadrage.
- `tasks/` décrit les tâches, leurs critères d’acceptation et leurs preuves.
- `runbooks/` décrit les opérations exceptionnelles après une livraison, avec leur état d’exécution et leurs preuves.
- `resources/` rassemble les ressources d’appui à la réalisation et à la vérification.

Les guides et références durables du cadre sont dans [docs/architecture/](../docs/architecture/index.md).

## Conventions techniques

### Types de demandes

Chaque demande indique `- Type : développement` ou `- Type : consolidation`.

Une consolidation à livrer porte un seul bloc clôturé `contribution-json`, objet
JSON strict de version 1 : `version` (entier), `corrections` et `accompagnements`
(listes), `sans_correction` (texte). Aucun champ ni clé dupliquée n’est accepté.
Chaque correction contient `chemins` (liste non vide de chemins corrigés),
`convention` (`chemin/README.md#ancre`, depuis la racine, dans les conventions
techniques) et `controles` (liste non vide de fichiers ajoutés ou modifiés).
Chaque accompagnement contient `chemins` et `motif` non vide.

Tous les chemins modifiés par les commits sont déclarés exactement une fois,
hors demande et cartes référencées, prises en compte automatiquement.
Les chemins sont explicites, relatifs à la racine et sans joker ni traversée.
Une suppression ou un déplacement déclare aussi l’ancien chemin.
Les corrections et le motif `sans_correction` s’excluent ; sans correction,
ce dernier commence par `sans correction de code : ` suivi de sa justification.
Les accompagnements restent obligatoirement couverts dans ce cas.
Les fichiers de contrôle doivent exister à la tête et leur contenu différer
de l’ancêtre commun avec la base. Le contrôle de présence ne prouve pas leur
adéquation : appliquer la [revue des contributions](../docs/git-workflow/README.md#vérification).
Les anciennes demandes non livrées dans la plage examinée ne sont pas migrées.

### Conservation des ressources

Les ressources regroupent les sources de l’auteur et les représentations du cadre.

- Conserver sans modification les originaux : [carrousel](resources/AIOD-carrousel-v1.html),
  [PDF](resources/AIOD.pdf), [schéma d’approche](resources/aiod-approche_1.png) et
  pictogrammes [SVG](../design/Picto-fond-noir-1000x1000.svg) et
  [JPG](resources/Picto-fond-noir-1000x1000.jpg).
- Le carrousel a servi à rédiger les principes ; le PDF et le schéma restent à
  relire ensemble. Consulter la documentation pour le fonctionnement actuel.
- La [vue interactive](../design/drafts/vue-d-ensemble-ai-development-engineering-v2.html)
  présente le cadre actuel ; la [vue synthétique](../design/drafts/vue-d-ensemble-ai-development-engineering-v1.html)
  conserve le nom historique AIOD.
- Dans la vue interactive, conserver les chemins personnels des douze skills
  comme texte pour permettre la consultation du dossier seul. Vérifier leur
  disponibilité avant livraison.
- Les couleurs identifient les acteurs selon l’[adaptation graphique](../design/charte-graphique.md).
  Un skill de vérification ne remplace pas le verdict humain.
