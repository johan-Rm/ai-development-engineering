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
