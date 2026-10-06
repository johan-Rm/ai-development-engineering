# BP-006 — Initialiser le worktree web

- **Créée le** : 2026-10-05.
- **Session** : non disponible (Codex).
- **Statut** : à faire — dépendances à satisfaire avant démarrage.
- **Type** : outillage.
- **Tests** : contrôles Git locaux et relance sans perte ; les tests de l’outil sont exécutés
  si celui-ci change. Aucun test applicatif : aucun code applicatif produit.
- **Réf** : BP-003 ; commit develop contenant scripts/worktrees.py et scripts/aiod.json ; `docs/aiod/couches.md`, `docs/aiod/gouvernance.md`.
- **Rattachement** : maintenance du blueprint, branche `layers/blueprint`, préfixe BP.
- **Dossier de coordination** : `/home/johan/www/lab/ai-orchestrated-development`.
- **Affectation d’exécution** : non attribuée ; à vérifier au démarrage.

## Contexte

Les cinq couches sont définies mais leurs worktrees n’existent pas. Le dépôt ne possède pour
l’instant que `main` et `layers/blueprint`. L’utilisateur demande une tâche d’initialisation
pour chaque couche, ainsi que les branches `master` et `develop`.

## Périmètre

Créer ou réutiliser le worktree `/home/johan/www/lab/ai-orchestrated-development/worktree/web` sur `layers/web` depuis un SHA identifié
de `develop`. Ajouter ou compléter `web/README.md` dans ce worktree pour décrire
le rôle de la couche : socle partagé et construction de plusieurs sites/webapps. Décrire `web/shared/` et `web/targets/<nom>/`, sans installer de runtime ni générer de cible.

## Décisions de cadrage

Commande prévue :

```sh
python3 scripts/worktrees.py add --layer web --branch layers/web --base develop
```

La commande est exécutée depuis le dépôt principal ou un arbre enregistré, après vérification
des missions. Le préfixe opérationnel de cette couche sera `WEB` ; la présente carte BP
porte le bootstrap coordonné du blueprint. Les consignes locales sont écrites sur `layers/web`,
avec la carte clôturée dans le même commit lorsque son exécution et son commit seront demandés.
Le dossier représente un environnement de travail Git ; build et rendu des cibles futures ne sont pas annoncées comme testées.
Aucun `.env` n’est copié ou généré automatiquement.

## Règles et cas limites

Préserver tous les fichiers et missions actifs. Réutiliser les références et worktrees compatibles ;
refuser un dossier occupé, un lien symbolique ou une branche inattendue. Ne pas stasher, supprimer,
réinitialiser ou forcer un push. Un arbre propre ne prouve pas une couche libre.

## Hors périmètre

Installation de framework, services, secrets, DNS réel, déploiement, push et PR.
La stack et l’exemple applicatif seront définis séparément ; ils ne bloquent pas le socle Git.

## Documentation impactée

`web/README.md` dans le worktree cible ; `docs/aiod/couches.md` seulement si le routage doit être précisé ; carte courante pour les preuves.

## Définition de terminé

- [ ] Le worktree enregistré porte exactement `layers/web` et partage le dépôt Git commun attendu.
- [ ] Le chemin absolu est vérifié ; une branche déjà sortie est réutilisée au bon chemin.
- [ ] La branche nouvellement créée démarre sur le SHA develop consigné.
- [ ] Pour une branche existante, toute divergence est inventoriée sans réécriture.
- [ ] Une relance réutilise le worktree sans modifier ses fichiers ni son environnement.
- [ ] `web/README.md` décrit le périmètre, les limites et les preuves applicables.
- [ ] Les exclusions du parent empêchent la recherche et les tests de parcourir cette copie.
- [ ] La carte est conservée pour sa clôture dans l’arbre cible sans reprendre une mission tierce.
- [ ] Les commandes, chemins absolus et SHA observés sont consignés dans la carte.
- [ ] Le travail préexistant reste intact ; aucun accès distant ou déploiement n’a lieu.

## Première étape d’implémentation

Vérifier BP-003, la disponibilité de web, les arbres enregistrés et le SHA develop.

## Preuves et livraison

À renseigner pendant l’exécution. Une tâche, un commit demandé explicitement, avec sa carte
clôturée et sa documentation. Les opérations Git locales sont prouvées par les références,
branches et chemins observés ; leur simple présence dans la carte n’est pas une exécution.
