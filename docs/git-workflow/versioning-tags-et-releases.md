# Versioning, tags et releases

> Distinguer l’intégration, la publication et les choix de versionnement restant à définir.

L'intégration sur develop prépare une base commune ; elle ne constitue pas une
publication en production. La promotion vers master nécessite une demande distincte.
Une PR intégrée ne prouve pas qu'une version a été déployée.

Aucune politique de versionnement sémantique, de tags de release ou de changelog
automatique n'est adoptée dans cette demande. Le préfixe d'un commit ne déclenche
donc pas à lui seul un changement de version. Le périmètre d'une release, sa
numérotation et sa référence déployée restent à définir avant automatisation.
Un circuit particulier de correctif urgent de production reste également à cadrer.
