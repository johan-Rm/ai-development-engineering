# OPS-065 — Alléger AGENTS.md et centraliser ses références

- Date : 2026-10-28 ; état : validée et commitée localement ; à reconstituer et livrer.
- Session de création : `01a1820d-ecd1-7600-8d49-1422ef8b8f1b`.
- Demande : DEM-012 ; référence actuelle depuis le dépôt principal :
  `tmp/demande-alleger-agents.md` (brouillon local, non copié ici).
- Lien définitif prévu à la reconstitution : `../demand/DEM-012-alleger-agents.md`
  (fichier inexistant au découpage).
- Couche : devops ; worktree : `worktree/devops` ; branche : `layers/devops`.
- Base locale vérifiée : `2bd2a014dbfb41643a2ad8bc42c1cebb12fd5f74` ; aucun fetch.
- Dépendances : aucune carte amont ; une seule contribution atomique.

## Objectif et périmètre

Réaliser les critères de DEM-012, qui fait référence pour le besoin et la
formulation humaine à intégrer. Ne pas recopier cette formulation dans la carte.

Chemins autorisés : `AGENTS.md`, cette carte, `docs/index.md`,
`docs/02-cadre/documentation.md`, `docs/02-cadre/ia-engineering.md`,
`docs/02-cadre/couches/index.md`, `docs/03-developpement-loop/*.md`,
`docs/04-consolidation-loop/*.md`, `dev-book/README.md`.
Limiter chaque changement à la centralisation des consignes retirées et à leurs liens.

Réutiliser les guides existants : documentation pour les README et leur revue,
IA Engineering pour les skills et sessions, guides des étapes pour les procédures,
couches pour le routage et l’isolation. Conserver dans AGENTS.md les décisions
essentielles et les limites d’autorisation, avec liens vers les détails.

Exclusions : applications, infrastructure exécutable, contrôles automatisés,
skills personnels, demandes et cartes historiques ; aucun changement de workflow
ou d’autorisation. Ne pas résoudre une contradiction préexistante par une nouvelle
décision implicite : la signaler si elle empêche une reformulation fidèle.

## Critères et vérification

- Couvrir les cinq critères de la demande dans un ensemble cohérent ; la cible
  d’environ 60 lignes ne justifie aucune perte de garde-fou.
- Vérifier les liens entrants vers les titres modifiés, notamment ceux des guides.
- Relire chaque règle retirée et noter sa destination ou son caractère redondant
  dans les preuves ci-dessous, par groupes sans recopier les règles.
- Depuis le worktree affecté : `git diff --check`, puis
  `python3 codebase-integrity/scripts/quality.py` ; vérifier les liens et ancres
  modifiés avec l’outil existant adapté, ou par inspection explicite.
- Pas de nouveau test de jugement rédactionnel ni de test applicatif nécessaire.
  Ne pas affaiblir un contrôle pour accepter le texte raccourci.

## Preuves et verdict

Base présentée : HEAD ci-dessus, branche inchangée. Dix fichiers suivis modifiés :
AGENTS.md et les références regroupées ci-dessous ; seule cette carte est non suivie.
Aucun fichier applicatif, contrôle ou skill modifié.

| Règles retirées d’AGENTS.md | Référence conservée ou complétée |
| --- | --- |
| Procédures, dépendances, verdicts et corrections | Guides des étapes de développement ; autorisations maintenues dans AGENTS.md |
| Alignement, merges ciblés et suppression des branches temporaires | Guide de livraison, complété pour fetch et stratégie de merge |
| Tableaux des skills | Pages des étapes des deux boucles ; liens des index ajustés |
| Disponibilité des skills et définition des missions | IA Engineering |
| Session et rangement DEM | dev-book/README.md ; guides interview et découpage liés à cette source |
| Structure des README et revue | Guide documentation, exceptions et revue complétées |
| Création de worktree et isolation | Guide des couches, commande déplacée |
| Référence graphique | Liens vers charte et adaptations existantes ; copie de palette retirée du guide documentation |

AGENTS.md : 175 → 44 lignes, 1 580 → 678 mots (−57 %). Formulation humaine
intégrale présente dans la règle prioritaire. Pas de nouvelle duplication normative
nécessaire ; les traces de cadrage et cette preuve restent les traces obligatoires.

Contrôles le 2026-10-28 :
- `git diff --check` : réussi.
- Inspection ponctuelle des liens Markdown locaux des dix fichiers suivis modifiés :
  50 cibles et ancres vérifiées, aucune erreur ; lien entrant de concision conservé.
- `python3 codebase-integrity/scripts/quality.py` : code 0 ; 23 tests d’outillage,
  contrat et contrôles API, types et builds web/backoffice réussis.
  Première tentative bloquée par le serveur HTTP interdit dans le sandbox ;
  relance autorisée hors sandbox réussie. Journal local : `/tmp/dem012-quality.log`.

Réserve préexistante hors correctif : les guides interview/reconstitution décrivent
encore la demande versionnée et un worktree de couche, tandis que les skills
personnels prescrivent le brouillon local et la reconstitution dans le principal.
Aucune nouvelle règle de workflow n’a été décidée pour résoudre cet écart.

Retour humain du 2026-10-28 : pas de travaux sur les conventions techniques pour
le moment, après examen des ajouts au README dev-book. Correction demandée :
laisser ce README inchangé, conserver les règles concernées sans intervenir sur
les conventions techniques et adapter les liens. Retour à l’implémentation requis,
puis nouvelle présentation. Aucun résultat validé ni commit créé.


Correction réalisée : README dev-book rétabli exactement à HEAD ; règles de
rangement et de session conservées dans AGENTS.md, liens des guides adaptés.
Aucun travail sur les conventions techniques. Cette correction remplace la
centralisation session/rangement et les mesures de la première présentation.
Contrôles de correction : `git diff --check` réussi ; 50 liens et ancres locaux
vérifiés sans erreur ; `git diff -- dev-book/README.md` vide. AGENTS.md compte
49 lignes et 751 mots (−52 % par rapport à HEAD). Le contrôle qualité déjà réussi
reste applicable : seuls les textes et liens documentaires ont changé depuis.
État corrigé : neuf fichiers suivis modifiés et cette carte non suivie, même HEAD
et branche que la première présentation. Verdict sur cette version en attente.


## Verdict humain sur la correction

Le 2026-10-28, validation explicite dans le chat : « validé », après présentation
de la version corrigée et de sa réserve préexistante. Contenu vérifié inchangé
avant commit ; README dev-book inchangé. Base : `2bd2a014dbfb41643a2ad8bc42c1cebb12fd5f74`.
Empreinte du relevé présenté :
`b2e5173a8f46aecadd74beda189304630b834d591faf4b2f75e742adc251276b`.

Commit local de la carte validée : `b502f0d00e05b9f1f5e1ea1bb37a0239052ce785`.
