# Interview

> Transformer la demande en besoin clair avant de décider comment la réaliser.

## Entrée

Demande humaine et contexte du projet.

## Déroulement

L’IA clarifie le problème, le résultat attendu, les utilisateurs concernés et les contraintes. Elle expose les ambiguïtés ; l’humain tranche les choix et les exclusions.

Après confirmation humaine du cadrage, l’IA crée ou reprend une demande de type `développement` sous
`dev-book/demand/DEM-NNN-<sujet>.md`, selon les [règles de rangement](../../../AGENTS.md#demandes-et-cartes).
Elle recherche d’abord le fichier existant pour éviter les doublons ; une nouvelle identité
est attribuée après examen des références locales et des worktrees concernés, sans fetch implicite.

Ce fichier fait référence pour le besoin, le contexte, les critères observables, les contraintes,
les décisions et les questions restantes. Le chat sert à préciser le besoin ; son lien est
conservé si disponible, sinon son indisponibilité est explicite. Une carte externe de suivi
reste facultative : conserver son lien ne nécessite aucune connexion et sa création ou
sa modification exige une instruction explicite. Aucune référence n’est inventée.

La demande doit rester compréhensible lorsque la documentation du projet évolue.
Elle consigne le besoin et les décisions utiles sans recopier les procédures ni
ajouter de chemins ou de liens vers les guides et leurs sections pour les rappeler.
Les identifiants de cartes, SHA et références nécessaires aux preuves sont conservés.

## Sortie

Une demande cadrée et enregistrée, avec des critères observables de réussite, la confirmation
humaine et le chemin du document. Aucun découpage automatique ; confirmer le besoin ne valide
pas un résultat implémenté.

## Procédure associée

`interviewer-demande`.

Avant création, appliquer les [règles de session](../../../AGENTS.md#demandes-et-cartes).
