# DEM-002 — Identifier les interactions IA en bleu dans le schéma AIDE

- Date : 2026-10-26.
- État du cadrage : confirmé par l’humain dans le chat.
- Référence de session indisponible ; aucune carte externe fournie.

## Besoin, contexte et utilisateurs

Les lecteurs du schéma interactif AIDE doivent identifier toutes les actions et interactions
attribuées à l’IA par le bleu `#1B6EAE`, en remplacement de la terre cuite `#C07040`.
Cette décision remplace l’adaptation graphique précédente pour ce schéma.

## Résultat attendu et critères observables

1. Tous les éléments identifiant l’IA, dans les deux boucles et la légende, utilisent `#1B6EAE`.
2. Les consignes graphiques associées décrivent cette nouvelle adaptation sans contradiction.
3. Les couleurs humaines, les textes du schéma, sa disposition et ses interactions sont conservés.
4. Le texte blanc cassé reste lisible sur le bleu ; le rendu des deux boucles et de la légende
   est vérifié visuellement, avec une mesure de contraste.

## Contraintes et exclusions

Conserver la charte officielle Graines Digitales sans modification : le bleu est une adaptation
explicitement demandée pour AIDE. Conserver les aplats, la typographie et l’absence de marqueurs
décoratifs de rôle. Ne pas modifier les sources historiques, les applications ou l’infrastructure.
Ne pas réécrire les anciennes preuves et décisions historiques pour leur appliquer la nouvelle couleur.
Aucune modification des skills personnels n’appartient à cette demande.

## Décisions humaines

Le 2026-10-26, l’humain a initialement demandé `#2563EB`, puis choisi « Oui, tous les éléments IA et les
consignes associées » et répondu « Je confirme ce cadrage » à la restitution des critères ci-dessus.
Il a ensuite confirmé de différer l’enregistrement et l’affectation au découpage.
L’invocation de `decouper-demande` pour DEM-002 lance cette étape, sans implémentation.
La confirmation du besoin ne vaut pas validation du résultat implémenté.

## Questions ouvertes

Aucune question de besoin ouverte. La disponibilité opérationnelle de la couche doit être
revérifiée avant l’implémentation ; aucun registre ne prouve l’absence de mission externe au dépôt.

## Tâches issues du découpage

| Carte | Couche | Couverture | Dépendances |
| --- | --- | --- | --- |
| [OPS-047 — Passer les éléments IA du schéma en bleu](../tasks/OPS-047-couleur-ia-schema-aide.md) | devops | Critères 1 à 4, schéma et consignes associées | Aucune tâche amont distincte |

Carte unique : la documentation graphique partagée est rattachée au schéma du cadre qui la consomme.
Aucune mission design concurrente sur ces chemins n’a été identifiée dans les cartes consultées.

## Réunion prévue

- Branche dédiée : `demands/DEM-002`.
- Worktree prévu : `/home/johan/www/lab/ai-orchestrated-development/worktree/DEM-002`.
- Branche et worktree à créer seulement lors de la reconstitution, à partir des commits validés.
- Ne pas utiliser `layers/devops`, `develop` ou `master` comme branche de réunion.

## Preuve du découpage

Références Git locales et fichiers des worktrees examinés sans fetch : maxima antérieurs
DEM-001 et OPS-046. Aucun doublon correspondant à ce besoin trouvé.
`layers/devops` existe au commit `6477c51f6428bccdd81c08be20edf644e94fee31` ; arbre propre
avant l’enregistrement de ces deux documents. Branche conservée sans rebase ni synchronisation distante.
Aucune carte explicitement en cours identifiée ; cela ne constitue pas une réservation globale de couche.

## Suivi d’implémentation — 2026-10-26

OPS-047 appliquée localement : couleur et documentation alignées, contraste et diff contrôlés.
Vérification navigateur et captures bloquées par la bibliothèque système `libnspr4.so` absente.
Détails et commande de reprise dans la carte. Aucun commit ni verdict humain sur le résultat.

## Couleur finale retenue — 2026-10-26

Après essais dans l’aperçu local, l’humain retient `#1B6EAE` :
« parfait on garde celui la ». Il demande explicitement la mise à jour
du code couleur de la demande et de la tâche. Cette décision remplace
le choix initial `#2563EB` ; les critères ci-dessus utilisent la couleur finale.

## Verdict humain et reconstitution — 2026-10-26

L’humain a explicitement validé le résultat local de l’unique carte OPS-047 par « validé ».
Les limites des contrôles navigateur restent consignées dans la carte.
La reconstitution demandée est bloquée : aucun commit d’implémentation ni SHA à réunir.
Aucun commit de code créé à cette étape, aucun transfert de fichiers non commités,
aucune création de la branche dédiée et aucune livraison. L’autorisation explicite du commit
manquant reste nécessaire selon les instructions utilisateur applicables.

## Régularisation de l’implémentation — 2026-10-26

Après instruction explicite de toujours committer à l’implémentation, OPS-047 est reprise
pour produire son commit unique avec les six fichiers du périmètre. Le blocage d’autorisation
précédent est levé. Le verdict humain déjà exprimé est conservé ; l’association au SHA
pourra être consignée à la vérification. Aucune autre étape lancée ici.

## Vérification sur commit — 2026-10-26

DEM-002 est validée par l’humain pour son unique carte OPS-047.
Verdict explicite antérieur : « validé ». Commit d’implémentation associé après contrôle
de correspondance avec le résultat présenté : `8db9d9bd436d835d6119ea55eac461b4d463cb19`.
Les quatre critères de la demande sont couverts par la carte et les consignes alignées.
Les limites navigateur demeurent documentées dans OPS-047 ; aucun contrôle non exécuté
n’est déclaré réussi. Le blocage pour absence de commit est levé.
La reconstitution et la livraison restent des étapes distinctes, non exécutées ici.
