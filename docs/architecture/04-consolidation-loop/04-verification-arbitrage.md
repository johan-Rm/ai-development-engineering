# Vérification / arbitrage

> L’humain vérifie l’application de son arbitrage et la fiabilité des preuves présentées.

## Entrée

Corrections, documentation et résultats des contrôles.

## Déroulement

L’humain confronte le résultat à la décision : périmètre couvert, exceptions, écarts détectés et cas conformes acceptés. Il valide, ajuste, diffère ou rejette ; il arbitre l’adéquation de la règle et
des contrôles au résultat observé. Les corrections reviennent à l’implémentation,
les changements de règle à l’analyse / découpage.

## Sortie

Un verdict humain sur les corrections et leurs garde-fous. Les tâches validées produisent leurs commits distincts.

## Procédure associée

`verifier-consolidation`.

Après validation humaine explicite, le skill crée un commit local distinct par carte
validée, sans confirmation supplémentaire, avec ses changements, tests, documentation,
preuves et verdict. Il vérifie le périmètre et l’index, puis consigne les SHA créés.
Aucun push, PR ou fusion à cette étape.
