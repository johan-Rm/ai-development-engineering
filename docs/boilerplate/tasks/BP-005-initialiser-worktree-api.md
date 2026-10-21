# BP-005 — Initialiser le worktree api

- **Créée le** : 2026-10-05.
- **Session** : non disponible (Codex).
- **Statut** : clôturée le 2026-10-06.
- **Type** : outillage.
- **Tests** : contrôles Git locaux et relance sans perte ; les tests de l’outil sont exécutés
  si celui-ci change. Aucun test applicatif : aucun code applicatif produit.
- **Réf** : BP-003 ; commit develop contenant codebase-quality-control/scripts/worktrees.py et codebase-quality-control/scripts/aiod.json ; `docs/aiod/couches.md`, `docs/aiod/gouvernance.md`.
- **Rattachement** : maintenance du cadre, sur la branche historique de maintenance, préfixe BP.
- **Dossier de coordination** : `<depot>`.
- **Affectation d’exécution** : non attribuée ; à vérifier au démarrage.

## Contexte

Les cinq couches sont définies mais leurs worktrees n’existent pas. Le dépôt ne possède pour
l’instant que `main` et la branche historique de maintenance. L’utilisateur demande une tâche d’initialisation
pour chaque couche, ainsi que les branches `master` et `develop`.

## Périmètre

Créer ou réutiliser le worktree `<depot>/worktree/api` sur `layers/api` depuis un SHA identifié
de `develop`. Ajouter ou compléter `api/README.md` dans ce worktree pour décrire
le rôle de la couche : contrats et services serveur.

## Décisions de cadrage

Commande prévue :

```sh
python3 codebase-quality-control/scripts/worktrees.py add --layer api --branch layers/api --base develop
```

La commande est exécutée depuis le dépôt principal ou un arbre enregistré, après vérification
des missions. Le préfixe opérationnel de cette couche sera `API` ; la présente carte BP
porte le bootstrap coordonné du blueprint. Les consignes locales sont écrites sur `layers/api`,
avec la carte clôturée dans le même commit lorsque son exécution et son commit seront demandés.
Le dossier représente un environnement de travail Git ; requêtes, réponses et tests de contrat futurs ne sont pas annoncées comme testées.
Aucun `.env` n’est copié ou généré automatiquement.

## Règles et cas limites

Préserver tous les fichiers et missions actifs. Réutiliser les références et worktrees compatibles ;
refuser un dossier occupé, un lien symbolique ou une branche inattendue. Ne pas stasher, supprimer,
réinitialiser ou forcer un push. Un arbre propre ne prouve pas une couche libre.

## Hors périmètre

Installation de framework, services applicatifs, secrets, DNS réel, déploiement, push et PR.
Le conteneur témoin commun de BP-009 sert uniquement à vérifier le processus.
La stack et l’exemple applicatif seront définis séparément ; ils ne bloquent pas le socle Git.

## Documentation impactée

`api/README.md` dans le worktree cible ; `docs/aiod/couches.md` seulement si le routage doit être précisé ; carte courante pour les preuves.

## Définition de terminé

- [x] Le worktree enregistré porte exactement `layers/api` et partage le dépôt Git commun attendu.
- [x] Le chemin absolu est vérifié ; une branche déjà sortie est réutilisée au bon chemin.
- [x] La branche nouvellement créée démarre sur le SHA develop consigné.
- [x] Pour une branche existante, toute divergence est inventoriée sans réécriture.
- [x] Une relance réutilise le worktree sans modifier ses fichiers ni son environnement.
- [x] `api/README.md` décrit le périmètre, les limites et les preuves applicables.
- [x] Les exclusions du parent empêchent la recherche et les tests de parcourir cette copie.
- [x] La carte est conservée pour sa clôture dans l’arbre cible sans reprendre une mission tierce.
- [x] Les commandes, chemins absolus et SHA observés sont consignés dans la carte.
- [x] Le travail préexistant reste intact ; aucun accès distant ou déploiement n’a lieu.

## Première étape d’implémentation

Vérifier BP-003, la disponibilité de api, les arbres enregistrés et le SHA develop.

## Preuves et livraison

Vérification du 2026-10-06 :

- Worktree : `<depot>/worktree/api` ; branche `layers/api` ; dépôt commun `<depot>/.git`.
- Base identifiée : `c6e3302ffd6e71449d0bac22ccfc0773f034cd69` (develop, contient BP-001, BP-003 et BP-009).
- Relance du créateur : même chemin, aucun fichier modifié.
- Endpoint local : `http://127.0.0.1:18102/`, identité `api` observée.
- Projet Docker : `aiod-d10fdac8-api` ; volume `aiod-d10fdac8-api_state`.
- Marqueur `/data/init-proof` : `api`, conservé après relance.
- `.env` préservé ; artefacts `.aiod/` exclus de Git ; aucune copie de secret.
- `api/README.md` décrit les responsabilités et la recette.
- Les contrôles Python ciblent tests/ et n’explorent pas worktree/ ; Git ignore la copie.

L’utilisateur a autorisé un commit d’initialisation par couche. La stack applicative reste hors
périmètre, conformément à son arbitrage. Une tâche, un commit demandé explicitement, avec sa carte
clôturée et sa documentation. Les opérations Git locales sont prouvées par les références,
branches et chemins observés ; leur simple présence dans la carte n’est pas une exécution.
