# Infrastructure

La configuration et les outils nécessaires aux environnements d’exécution du projet.

## Rôle et responsabilités

- Fournir les environnements locaux des applications.
- Isoler les services et les ressources utilisés par chaque couche.
- Permettre le démarrage, l’arrêt et la vérification des environnements.
- Fournir les conteneurs témoins servant à vérifier le fonctionnement du cadre.

Aucun déploiement applicatif n’est actuellement configuré.

## Conventions techniques

### Configuration des couches

Cette configuration permet aux outils de reconnaître chaque couche et d’utiliser son environnement.

- Définir les couches dans `config/layers.json` et tenir à jour la
  [table des couches](../docs/architecture/02-cadre/couches/organisation.md).
- Conserver la structure `layers` : chaque couche possède une branche (`branch`),
  un rôle (`role`) et un identifiant stable, entier positif et unique (`id`).
- Lire la configuration de la copie de travail utilisée. Si elle manque ou est
  invalide, arrêter l’outil sans créer de configuration de remplacement.
- Garder la configuration Docker dans `process-check.json`. Les ports dépendent
  des identifiants des couches, pas de leur ordre dans la liste.
- Permettre la création des copies de travail sans Docker.
