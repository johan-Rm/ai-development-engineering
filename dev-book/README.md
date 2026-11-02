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

- Déclarer un seul type : `développement` ou `consolidation`.
- Placer le champ `- Type : ...` dans les métadonnées de la demande.
- Fournir une déclaration `contribution-json` unique pour chaque consolidation à livrer.
- Limiter la déclaration aux champs `version`, `corrections`, `accompagnements` et `sans_correction`.
- Fixer `version` à l’entier `1` et refuser les clés dupliquées.
- Décrire chaque correction par `chemins`, `convention` et `controles`.
- Référencer chaque convention par une ancre de son README source.
- Décrire chaque accompagnement par `chemins` et un `motif` non vide.
- Déclarer chaque chemin modifié exactement une fois, hors demande et cartes référencées.
- Utiliser des chemins explicites relatifs à la racine, sans traversée ni joker.
- Déclarer les deux chemins d’un déplacement et les chemins supprimés.
- Exiger des listes de chemins et de contrôles non vides pour chaque correction.
- Exiger des contrôles présents à la tête et différents de l’ancêtre commun.
- Exclure mutuellement les corrections et le motif `sans_correction`.
- Préfixer ce motif par `sans correction de code : ` et ajouter une justification.
- Ne pas imposer la déclaration aux demandes hors de la plage à livrer.

### Conservation des ressources

- Conserver sans modification les originaux : [carrousel](resources/AIOD-carrousel-v1.html),
  [PDF](resources/AIOD.pdf), [schéma d’approche](resources/aiod-approche_1.png) et
  pictogrammes [SVG](../design/Picto-fond-noir-1000x1000.svg) et
  [JPG](resources/Picto-fond-noir-1000x1000.jpg).
- Relire ensemble le PDF et le schéma d’approche.
- Préserver la [vue interactive](../design/drafts/vue-d-ensemble-ai-development-engineering-v2.html)
  et le nom historique AIOD dans la [vue synthétique](../design/drafts/vue-d-ensemble-ai-development-engineering-v1.html).
- Dans la vue interactive, conserver les chemins personnels des douze skills
  comme texte pour permettre la consultation du dossier seul. Vérifier leur
  disponibilité avant livraison.
- Les couleurs identifient les acteurs selon l’[adaptation graphique](../design/charte-graphique.md).
