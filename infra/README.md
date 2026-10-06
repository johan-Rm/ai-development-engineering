# Infrastructure de recette AIOD

`compose.process.yaml` fournit un conteneur témoin BusyBox par couche, sans application.
Il sert une page locale décrivant sa couche et monte un volume privé pour vérifier les écritures.
Le port est lié exclusivement à `127.0.0.1` ; aucun domaine, proxy ou DNS public n’est nécessaire.

Le script `scripts/process.py`, lancé depuis un worktree de couche, impose sa branche,
son identité Compose et le chemin absolu des artefacts. Il ne lit ni ne modifie les `.env`.
Les paramètres de Compose sont explicitement fournis par l’outil.

Les identifiants stables sont dans `scripts/aiod.json` ; leur ordre dans le fichier ne change
pas les ports. Les noms des projets incluent un hash du chemin du dépôt principal et la couche.
Deux clones ont des noms distincts ; leurs ports doivent aussi être configurés avec des bases
différentes s’ils tournent sur le même hôte. Changer `process.port_base` avant le premier démarrage.

L’image BusyBox est un outil de recette, pas un choix de stack applicative.
Les volumes ne sont pas supprimés par la commande d’arrêt.

Références : [projets Compose](https://docs.docker.com/compose/intro/compose-application-model/),
[services et montages](https://docs.docker.com/reference/compose-file/services/).
