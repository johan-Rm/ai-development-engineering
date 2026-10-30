# Nettoyage des branches

> Terminer le suivi sans perdre les contributions, les worktrees ou leurs données.

Actualiser develop local par avance rapide, dans le dossier principal disponible.
Pour les couches locales libres et propres : avancer par avance rapide si possible.
Si seuls les SHA réécrits empêchent l’avance rapide, vérifier que chaque contribution
locale est bien incluse dans la PR intégrée, sans commit inédit, puis consigner
l’ancien SHA. Un rebase local sans commit à rejouer peut repositionner cette seule
branche sur le develop vérifié (`git rebase --onto <develop-vérifié> <ancien-tip> <couche>`).
Cette autorisation concerne uniquement les couches locales non partagées et confirmées
libres ; elle n’autorise ni rebase d’une branche occupée ni force-push. Au moindre
doute de provenance ou d’équivalence, préserver la branche et signaler le suivi bloqué.
Ne pas utiliser reset, stash ou suppression de worktree pour atteindre l’alignement.

Vérifier l’égalité des SHA de develop et de toutes les couches avant de clôturer
le suivi. Conserver les worktrees, données et `.env` ; ne jamais publier les layers/*.
Une couche sale, occupée ou portant un commit inédit reste intacte et empêche la clôture.

Revenir sur develop dans le dossier principal après l’intégration vérifiée. Supprimer
la branche temporaire distante livrée seulement sans autre PR ouverte ni travail inédit.
Pour la suppression locale sans forcer, vérifier d’abord l’intégration réelle et la
correspondance de tous ses commits ; sur la branche temporaire libre et propre,
un rebase sans commit à rejouer peut la placer sur le develop vérifié, puis revenir
sur develop et exécuter `git branch -d demands/<identifiant>`. Sinon la conserver et
signaler le suivi incomplet. Ne jamais supprimer develop, master ou une couche.

Consigner le suivi après intégration dans le brouillon local de la même demande,
s’il existe, sans modifier directement les fichiers suivis de develop ni créer
un rapport supplémentaire. La promotion vers master nécessite une demande distincte.
