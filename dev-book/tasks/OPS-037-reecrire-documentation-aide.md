# OPS-037 — Réécrire la documentation de l’écosystème AIDE

- **Créée le** : 2026-10-24.
- **Session** : non disponible (Codex).
- **Statut** : ✅ fait le 2026-10-24.
- **Type** : docs.
- **Tests** : sans objet pour de nouveaux tests exécutables — contenu Markdown ; vérification des liens, des chapitres, de la terminologie et du diff. Les tests existants de l’outillage seront exécutés pour le lot accumulé.
- **Mission** : devops, `layers/devops`, `worktree/devops`.
- **Périmètre** : README racine, SETUP.md, docs/, sauvegarde docs_save/, AGENTS.md et liens documentaires entrants ; cohérence des textes du schéma AIDE si obsolètes.
- **Dépendances** : décisions OPS-034 et OPS-036 ; aucune copie de travail d’une autre session.

## Cadrage et décisions

L’utilisateur autorise la rédaction complète sans validations intermédiaires, avec relecture ultérieure et commit. Arborescence validée : 01-codebase-quality-control, 02-cadre, 03-developpement-loop, 04-consolidation-loop ; index.md et aucun README sous docs/. Présentation dans le README racine, installation dans SETUP.md. Textes courts ; premier paragraphe en citation. Toujours écrire « convention technique », jamais « convention » seule.

Le Codebase Quality Control est la pierre angulaire du système, vivante pendant la construction du projet. La boucle de développement ne modifie aucun élément de son dossier. La validation des PR de développement exige des tests réussis. Son évolution relève de la consolidation et de l’arbitrage humain.

## Hors périmètre

Modification des skills personnels, applications, charte officielle, configuration des protections GitHub, déploiement, push et PR. Les cartes et ressources sources historiques restent conservées. La sauvegarde temporaire est conservée intégralement avec son vocabulaire historique.

## Définition de terminé

- [x] Tous les chapitres de l’arborescence sont rédigés sans texte d’attente.
- [x] SETUP.md et README racine donnent les points d’entrée utiles.
- [x] Les anciens guides sont retirés de docs/ et les liens actifs corrigés.
- [x] Principes humains, étapes des boucles et limites des skills sont explicites.
- [x] Liens, terminologie et diff vérifiés ; preuves consignées.

## Réalisation et vérification

- 22 fichiers Markdown rédigés dans les quatre thèmes validés. Le chapitre fondamental validé est conservé et sa terminologie harmonisée.
- README racine et SETUP.md ; anciens guides retirés de docs/ ; liens entrants actualisés. La synthèse graphique est déplacée dans design/charte-graphique.md, la charte officielle reste intacte.
- docs_save/ conserve les neuf fichiers de sauvegarde, sans réécriture ni harmonisation du vocabulaire historique.
- Schéma interactif : seuls les textes actifs sont corrigés (instructions Codex, conventions techniques et interdiction de modifier le dossier de contrôle dans la boucle de développement) ; structure et styles inchangés.
- Vérification des liens locaux des 33 documents actifs concernés, de la terminologie et des citations des 22 chapitres, absence de texte d’attente et de README sous docs/ : réussie.
- Parsing TOML et syntaxe JavaScript : réussis ; données des 24 panneaux du schéma chargées et vérifiées. Test navigateur non relancé : dépendances Playwright non installées dans ce worktree ; aucun changement de présentation.
- Tests existants : 18 réussis, avec permission étendue pour le port local temporaire ; le bac à sable interdit les sockets. Pas de contrôle applicatif complet : aucun code applicatif modifié.
- `git diff --check` réussi. L’utilisateur a autorisé la rédaction sans validations intermédiaires et fera sa relecture après commit.

## Répartition du travail accumulé

Les changements OPS-034 et OPS-036 dans AGENTS.md et les liens ont évolué au fil de la discussion. Leur état final est intégré ici avec la nouvelle documentation. Les commits séparés OPS-034 et OPS-036 portent respectivement le socle Codex/retrait Claude et la suppression de ia-engineering/ ; leurs cartes signalent ce partage. Aucun historique intermédiaire non commité n’est inventé.
