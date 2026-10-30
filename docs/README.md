# Documentation

Documentation du cadre et de ses boucles de travail.

## Rôle et responsabilités

- Documenter les évolutions au fur et à mesure des développements.
- Organiser les thématiques principales dans les sous-dossiers directement sous `docs/`.
- Créer les niveaux de sous-dossiers nécessaires à chaque thématique.
- Expliquer chaque sujet dans un seul document et y renvoyer par un lien depuis les autres pages.
- Détailler les points qui nécessitent des explications complémentaires.

## Conventions techniques

### Noms et navigation

Ces règles permettent de trouver les documents et de parcourir leurs sujets.

- Nommer sans numéro les dossiers de thématiques directement sous `docs/`,
  comme `architecture/`. Les numéros restent permis dans les sous-dossiers et
  fichiers, notamment pour les piliers et étapes des boucles.
- Réserver `index.md` aux sommaires : titres, listes de liens et tableaux de
  navigation. Chaque entrée contient un lien et, si utile, un libellé bref.
- Placer les explications et commandes dans un document nommé par sujet,
  accessible depuis le sommaire.

### Rédaction et source de référence

Chaque information doit être facile à comprendre et avoir une seule source.

- Commencer chaque document explicatif par une courte citation Markdown (`>`)
  après son titre principal. Les README et sommaires sont exemptés ; aucune
  citation supplémentaire n’est exigée dans les sous-sections.
- Utiliser des titres précis et des paragraphes courts. Supprimer répétitions,
  détails inutiles et formulations superflues.
- Employer « convention technique » pour désigner une règle technique du projet.
- Présenter « Rôle et responsabilités » des README comme une liste de responsabilités,
  sans renvoi documentaire ni inventaire de scripts ou de fichiers de tests.
- Définir les conventions techniques dans le README concerné. Les guides les
  expliquent et y renvoient sans les recopier.

### Références et vérifications

Les contrôles protègent la navigation ; la relecture humaine vérifie la clarté.

- Lors d’un déplacement, actualiser les liens et les renvois aux sections,
  y compris dans les demandes et cartes. Conserver les chemins écrits comme
  preuves historiques, les identifiants de commits, les résultats et les verdicts.
- Vérifier aussi les liens du dev-book. Toute exception doit préciser son fichier
  source, sa cible et son motif avant adoption ; aucune n’est configurée.
- Exécuter `python3 codebase-integrity/scripts/check_docs.py` : ce contrôle bloquant
  vérifie les noms, sommaires et citations de `docs/`, ainsi que les liens locaux
  du Markdown du dépôt et leurs renvois aux sections Markdown ou HTML.
- Examiner les fichiers suivis ou non ignorés, sans parcourir les copies de
  worktrees, les dépendances ignorées ou les `.env`.
- Inclure les liens HTML présents dans le Markdown. Les liens sortants des fichiers
  HTML et les destinations externes ne sont pas vérifiés. Le contrôle signale les
  références dynamiques pour examen humain.
- Relire humainement les titres, citations et paragraphes pour vérifier leur
  précision, leur concision et l’absence de répétitions.
