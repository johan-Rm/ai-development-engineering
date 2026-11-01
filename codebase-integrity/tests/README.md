# Tests de l’outillage

Les tests Python exercent la création des worktrees dans des dépôts jetables,
l’identité et l’isolation du processus ainsi que la préservation des environnements
et la propagation des échecs par les commandes applicatives.
Ils couvrent aussi les contributions selon leur boucle, les déclarations de
consolidation et l’exécution du vérificateur depuis une base de confiance.

Exécution : `python3 codebase-integrity/scripts/check.py` depuis la racine. Aucun remote ni Docker requis.
Les tests applicatifs restent dans leurs applications respectives.
