# DEM-007 — Audit du contenu local des six arbres

Date : 2026-10-27. Carte : [OPS-055](../tasks/OPS-055-auditer-contenu-local-couches.md).

## Portée et méthode

Audit en lecture seule du principal et des cinq couches définies dans
`infra/config/layers.json`. Les dépendances, caches, fichiers ignorés, dossiers
vides et liens sont inclus. Les métadonnées `.git` et les worktrees imbriqués sont
exclus ; chaque couche est parcourue séparément. Les anciens worktrees de réunion
ne font pas partie des six cibles. Les liens ne sont pas suivis.

Deux parcours consécutifs comparent pour chaque entrée le type, la taille des
fichiers, le mode, les dates mtime/ctime et la cible des liens. Aucun contenu de
secret n’est publié. Aucune écriture dans les six arbres pendant ces parcours ;
le présent rapport et les mises à jour documentaires sont écrits ensuite.

La comparaison porte sur les métadonnées, pas sur un hash des contenus. Elle ne
constitue ni un verrou contre une activité concurrente, ni une certification de
chaque dépendance installée. Aucun processus ou conteneur n’est arrêté ou modifié.
Aucune erreur de parcours ni changement entre les deux parcours n’est observé.

## Résultat par arbre

| Arbre | Fichiers réguliers | Dossiers | Liens | Erreurs | Entrées modifiées |
| --- | ---: | ---: | ---: | ---: | ---: |
| `.` | 35320 | 6509 | 116 | 0 | 0 |
| `worktree/backoffice` | 14288 | 2219 | 58 | 0 | 0 |
| `worktree/api` | 7342 | 2203 | 0 | 0 | 0 |
| `worktree/web` | 14287 | 2230 | 58 | 0 | 0 |
| `worktree/devops` | 35333 | 6507 | 116 | 0 | 0 |
| `worktree/design` | 212 | 70 | 0 | 0 | 0 |

Les liens sont des entrées observées, pas des sous-arbres audités à travers leur cible.

## Classement des contenus hors arborescence Git

Les groupes ci-dessous sont les chemins maximaux sans fichier ni descendant
suivi par Git. Tout leur contenu a été parcouru sans exclure les dépendances.
Les fichiers suivis et leurs répertoires parents ne sont pas des résidus.

- **Résidu proposé** : cache Python dans `__pycache__` sans source `.py` correspondante.
  Les quatre scripts Python de pilotage ont été retirés selon DEM-005 ; leurs
  caches `infra/` subsistent. Les chemins racine `scripts/` et `tests/` ne sont plus
  les emplacements actifs : les outils et tests sont dans `codebase-integrity/`.
  Il s’agit de candidats au nettoyage, pas d’une règle de suppression arbitrée.
- **Conserver** : dépendances Composer/npm, sorties Nuxt, fichiers Symfony générés,
  `.env`, données et caches applicatifs. Les README applicatifs, `.gitignore`,
  `infra/api-start.sh`, `infra/nuxt-start.sh` et `infra/compose.apps.yaml` en
  établissent les usages. Les dossiers vides servant aux montages ne prouvent
  pas une anomalie et ne sont pas à supprimer systématiquement.
- **Conserver** : `.local/process-check/identity.json`, identité du témoin local ;
  résultats Playwright, preuves de tests ; caches des scripts encore présents.
- **Doute** : `.agents/` et `.aws/`, vides, sans usage établi par cet audit.
  Les chemins sont aussi désignés comme protégés par l’environnement de session.
  Leur présence ne justifie aucune suppression ; vérifier leur provenance.

| Arbre | Chemin | Fichiers / dossiers / liens | Classement |
| --- | --- | --- | --- | --- |
| `.` | `.agents` | 0 / 1 / 0 | Doute, préserver |
| `.` | `.aws` | 0 / 1 / 0 | Doute, préserver |
| `.` | `app/api/app/.env` | 1 / 0 / 0 | Conserver |
| `.` | `app/api/app/config/reference.php` | 1 / 0 / 0 | Conserver |
| `.` | `app/api/app/public/bundles` | 59 / 7 / 0 | Conserver |
| `.` | `app/api/app/var` | 1921 / 1299 / 0 | Conserver |
| `.` | `app/api/app/vendor` | 5016 / 847 / 0 | Conserver |
| `.` | `app/backoffice/.nuxt` | 45 / 5 / 0 | Conserver |
| `.` | `app/backoffice/.output` | 138 / 66 / 0 | Conserver |
| `.` | `app/backoffice/node_modules` | 13871 / 2075 / 58 | Conserver |
| `.` | `app/backoffice/test-results` | 3 / 1 / 0 | Conserver |
| `.` | `app/web/targets/app/.nuxt` | 45 / 5 / 0 | Conserver |
| `.` | `app/web/targets/app/.output` | 134 / 65 / 0 | Conserver |
| `.` | `app/web/targets/app/node_modules` | 13871 / 2075 / 58 | Conserver |
| `.` | `app/web/targets/app/test-results` | 3 / 1 / 0 | Conserver |
| `.` | `scripts` | 1 / 2 / 0 | Résidu proposé, arbitrage requis |
| `.` | `tests` | 1 / 2 / 0 | Résidu proposé, arbitrage requis |
| `worktree/backoffice` | `.agents` | 0 / 1 / 0 | Doute, préserver |
| `worktree/backoffice` | `.aws` | 0 / 1 / 0 | Doute, préserver |
| `worktree/backoffice` | `.local` | 1 / 2 / 0 | Conserver |
| `worktree/backoffice` | `app/api/app/var` | 0 / 1 / 0 | Conserver |
| `worktree/backoffice` | `app/api/app/vendor` | 0 / 1 / 0 | Conserver |
| `worktree/backoffice` | `app/backoffice/.nuxt` | 53 / 7 / 0 | Conserver |
| `worktree/backoffice` | `app/backoffice/.output` | 138 / 66 / 0 | Conserver |
| `worktree/backoffice` | `app/backoffice/node_modules` | 13882 / 2078 / 58 | Conserver |
| `worktree/backoffice` | `app/backoffice/test-results` | 3 / 1 / 0 | Conserver |
| `worktree/backoffice` | `app/web/targets/app/.nuxt` | 0 / 1 / 0 | Conserver |
| `worktree/backoffice` | `app/web/targets/app/.output` | 0 / 1 / 0 | Conserver |
| `worktree/backoffice` | `app/web/targets/app/node_modules` | 0 / 1 / 0 | Conserver |
| `worktree/backoffice` | `infra/__pycache__` | 1 / 1 / 0 | Résidu proposé, arbitrage requis |
| `worktree/api` | `.agents` | 0 / 1 / 0 | Doute, préserver |
| `worktree/api` | `.aws` | 0 / 1 / 0 | Doute, préserver |
| `worktree/api` | `.local` | 1 / 2 / 0 | Conserver |
| `worktree/api` | `app/api/app/.env` | 1 / 0 / 0 | Conserver |
| `worktree/api` | `app/api/app/.env.dev` | 1 / 0 / 0 | Conserver |
| `worktree/api` | `app/api/app/config/reference.php` | 1 / 0 / 0 | Conserver |
| `worktree/api` | `app/api/app/public/bundles` | 59 / 7 / 0 | Conserver |
| `worktree/api` | `app/api/app/var` | 2052 / 1281 / 0 | Conserver |
| `worktree/api` | `app/api/app/vendor` | 5016 / 847 / 0 | Conserver |
| `worktree/api` | `app/backoffice/.nuxt` | 0 / 1 / 0 | Conserver |
| `worktree/api` | `app/backoffice/.output` | 0 / 1 / 0 | Conserver |
| `worktree/api` | `app/backoffice/node_modules` | 0 / 1 / 0 | Conserver |
| `worktree/api` | `app/web/targets/app/.nuxt` | 0 / 1 / 0 | Conserver |
| `worktree/api` | `app/web/targets/app/.output` | 0 / 1 / 0 | Conserver |
| `worktree/api` | `app/web/targets/app/node_modules` | 0 / 1 / 0 | Conserver |
| `worktree/api` | `infra/__pycache__` | 1 / 1 / 0 | Résidu proposé, arbitrage requis |
| `worktree/web` | `.agents` | 0 / 1 / 0 | Doute, préserver |
| `worktree/web` | `.aws` | 0 / 1 / 0 | Doute, préserver |
| `worktree/web` | `.local` | 1 / 2 / 0 | Conserver |
| `worktree/web` | `app/api/app/var` | 0 / 1 / 0 | Conserver |
| `worktree/web` | `app/api/app/vendor` | 0 / 1 / 0 | Conserver |
| `worktree/web` | `app/backoffice/.nuxt` | 0 / 1 / 0 | Conserver |
| `worktree/web` | `app/backoffice/.output` | 0 / 1 / 0 | Conserver |
| `worktree/web` | `app/backoffice/node_modules` | 0 / 1 / 0 | Conserver |
| `worktree/web` | `app/web/targets/app/.nuxt` | 56 / 7 / 0 | Conserver |
| `worktree/web` | `app/web/targets/app/.output` | 134 / 65 / 0 | Conserver |
| `worktree/web` | `app/web/targets/app/node_modules` | 13882 / 2090 / 58 | Conserver |
| `worktree/web` | `app/web/targets/app/test-results` | 3 / 1 / 0 | Conserver |
| `worktree/web` | `infra/__pycache__` | 1 / 1 / 0 | Résidu proposé, arbitrage requis |
| `worktree/devops` | `.agents` | 0 / 1 / 0 | Doute, préserver |
| `worktree/devops` | `.aws` | 0 / 1 / 0 | Doute, préserver |
| `worktree/devops` | `.local` | 1 / 2 / 0 | Conserver |
| `worktree/devops` | `app/api/app/.env` | 1 / 0 / 0 | Conserver |
| `worktree/devops` | `app/api/app/config/reference.php` | 1 / 0 / 0 | Conserver |
| `worktree/devops` | `app/api/app/public/bundles` | 59 / 7 / 0 | Conserver |
| `worktree/devops` | `app/api/app/var` | 1921 / 1299 / 0 | Conserver |
| `worktree/devops` | `app/api/app/vendor` | 5016 / 847 / 0 | Conserver |
| `worktree/devops` | `app/backoffice/.nuxt` | 50 / 5 / 0 | Conserver |
| `worktree/devops` | `app/backoffice/.output` | 138 / 66 / 0 | Conserver |
| `worktree/devops` | `app/backoffice/node_modules` | 13871 / 2075 / 58 | Conserver |
| `worktree/devops` | `app/web/targets/app/.nuxt` | 50 / 5 / 0 | Conserver |
| `worktree/devops` | `app/web/targets/app/.output` | 134 / 65 / 0 | Conserver |
| `worktree/devops` | `app/web/targets/app/node_modules` | 13871 / 2075 / 58 | Conserver |
| `worktree/devops` | `codebase-integrity/scripts/__pycache__` | 2 / 1 / 0 | Conserver |
| `worktree/devops` | `infra/__pycache__` | 4 / 1 / 0 | Résidu proposé, arbitrage requis |
| `worktree/design` | `.agents` | 0 / 1 / 0 | Doute, préserver |
| `worktree/design` | `.aws` | 0 / 1 / 0 | Doute, préserver |
| `worktree/design` | `.local` | 1 / 2 / 0 | Conserver |
| `worktree/design` | `app/api/app/var` | 0 / 1 / 0 | Conserver |
| `worktree/design` | `app/api/app/vendor` | 0 / 1 / 0 | Conserver |
| `worktree/design` | `app/backoffice/.nuxt` | 0 / 1 / 0 | Conserver |
| `worktree/design` | `app/backoffice/.output` | 0 / 1 / 0 | Conserver |
| `worktree/design` | `app/backoffice/node_modules` | 0 / 1 / 0 | Conserver |
| `worktree/design` | `app/web/targets/app/.nuxt` | 0 / 1 / 0 | Conserver |
| `worktree/design` | `app/web/targets/app/.output` | 0 / 1 / 0 | Conserver |
| `worktree/design` | `app/web/targets/app/node_modules` | 0 / 1 / 0 | Conserver |
| `worktree/design` | `infra/__pycache__` | 1 / 1 / 0 | Résidu proposé, arbitrage requis |

## Caches sans source correspondante

- `.` : `scripts/__pycache__/apps.cpython-312.pyc`.
- `.` : `tests/__pycache__/test_apps.cpython-312.pyc`.
- `worktree/backoffice` : `infra/__pycache__/apps.cpython-312.pyc`.
- `worktree/api` : `infra/__pycache__/apps.cpython-312.pyc`.
- `worktree/web` : `infra/__pycache__/apps.cpython-312.pyc`.
- `worktree/devops` : `infra/__pycache__/apps.cpython-312.pyc`.
- `worktree/devops` : `infra/__pycache__/browser.cpython-312.pyc`.
- `worktree/devops` : `infra/__pycache__/test-runtime.cpython-312.pyc`.
- `worktree/devops` : `infra/__pycache__/test_apps.cpython-312.pyc`.
- `worktree/design` : `infra/__pycache__/apps.cpython-312.pyc`.

Total : dix fichiers candidats. La détection examine uniquement la forme
`__pycache__/nom.<suffixe>.pyc` et recherche `nom.py` dans le parent ; elle ne
suffit pas à autoriser seule une suppression. Aucun fichier candidat supprimé.

## Dossiers vides

### .

- `.agents`.
- `.aws`.
- `app/api/app/vendor/symfony/validator/Resources/bin`.
- `app/api/app/vendor/symfony/string/Resources/bin`.
- `app/api/app/var/cache/dev/pools/system/3iSXBxQOlR`.
- `app/api/app/var/cache/dev/pools/system/9PkmafrYfG`.
- `app/api/app/var/cache/dev/pools/system/M3EWB61nOO`.
- `app/api/app/var/cache/dev/pools/system/MVAXU9MHrF`.
- `app/api/app/var/cache/dev/pools/system/NpfHYfkB4k`.
- `app/api/app/var/cache/dev/pools/system/RiETchsUSf`.
- `app/api/app/var/cache/dev/pools/system/YJQ2jwxaEO`.
- `app/api/app/var/cache/dev/pools/system/bvOaegaahP`.
- `app/api/app/var/cache/dev/pools/system/h0Uton5JFw`.
- `app/api/app/var/cache/dev/pools/system/teUOGtAKhz`.
- `app/api/app/var/cache/dev/pools/system/tqm1Qf6sLd`.
- `app/web/targets/app/node_modules/.cache/jiti`.
- `app/backoffice/node_modules/.cache/jiti`.

### worktree/backoffice

- `.agents`.
- `.aws`.
- `app/api/app/var`.
- `app/api/app/vendor`.
- `app/web/targets/app/.nuxt`.
- `app/web/targets/app/.output`.
- `app/web/targets/app/node_modules`.
- `app/backoffice/node_modules/.cache/jiti`.
- `app/backoffice/.nuxt/dist`.

### worktree/api

- `.agents`.
- `.aws`.
- `app/api/app/vendor/symfony/validator/Resources/bin`.
- `app/api/app/vendor/symfony/string/Resources/bin`.
- `app/api/app/var/cache/dev/pools/system/1J3ZtEcbJC`.
- `app/api/app/var/cache/dev/pools/system/DtuV4FTOZe`.
- `app/api/app/var/cache/dev/pools/system/EC61fTPh7J`.
- `app/api/app/var/cache/dev/pools/system/W6oD5R3sBe`.
- `app/api/app/var/cache/dev/pools/system/Y+w77Jv88p`.
- `app/api/app/var/cache/dev/pools/system/kx7xA8CB0t`.
- `app/web/targets/app/.nuxt`.
- `app/web/targets/app/.output`.
- `app/web/targets/app/node_modules`.
- `app/backoffice/.nuxt`.
- `app/backoffice/.output`.
- `app/backoffice/node_modules`.

### worktree/web

- `.agents`.
- `.aws`.
- `app/api/app/var`.
- `app/api/app/vendor`.
- `app/web/targets/app/node_modules/@kwsites`.
- `app/web/targets/app/node_modules/@oxc-minify`.
- `app/web/targets/app/node_modules/@oxc-parser`.
- `app/web/targets/app/node_modules/@oxc-transform`.
- `app/web/targets/app/node_modules/@simple-git`.
- `app/web/targets/app/node_modules/.cache/jiti`.
- `app/web/targets/app/node_modules/youch/node_modules`.
- `app/web/targets/app/node_modules/nitropack/node_modules/.bin`.
- `app/web/targets/app/node_modules/vite-dev-rpc/node_modules`.
- `app/web/targets/app/node_modules/is-inside-container/node_modules/.bin`.
- `app/web/targets/app/node_modules/wsl-utils/node_modules`.
- `app/web/targets/app/node_modules/@poppinss/colors/node_modules`.
- `app/web/targets/app/.nuxt/dist`.
- `app/backoffice/.nuxt`.
- `app/backoffice/.output`.
- `app/backoffice/node_modules`.

### worktree/devops

- `.agents`.
- `.aws`.
- `app/api/app/vendor/symfony/validator/Resources/bin`.
- `app/api/app/vendor/symfony/string/Resources/bin`.
- `app/api/app/var/cache/dev/pools/system/49nhAC8Soq`.
- `app/api/app/var/cache/dev/pools/system/BqPTqrDW6s`.
- `app/api/app/var/cache/dev/pools/system/DGeQINl0TE`.
- `app/api/app/var/cache/dev/pools/system/Ei0git7AK+`.
- `app/api/app/var/cache/dev/pools/system/HYXBNa-QTT`.
- `app/api/app/var/cache/dev/pools/system/MrshuoTIxq`.
- `app/api/app/var/cache/dev/pools/system/Rnil6bOT5Q`.
- `app/api/app/var/cache/dev/pools/system/alyFzKBGmt`.
- `app/api/app/var/cache/dev/pools/system/oTByWz6kL3`.
- `app/api/app/var/cache/dev/pools/system/v00df9niZ1`.
- `app/api/app/var/cache/dev/pools/system/zrD81E+rP3`.
- `app/web/targets/app/node_modules/.cache/jiti`.
- `app/backoffice/node_modules/.cache/jiti`.

### worktree/design

- `.agents`.
- `.aws`.
- `app/api/app/var`.
- `app/api/app/vendor`.
- `app/web/targets/app/.nuxt`.
- `app/web/targets/app/.output`.
- `app/web/targets/app/node_modules`.
- `app/backoffice/.nuxt`.
- `app/backoffice/.output`.
- `app/backoffice/node_modules`.

## États et protections observés

Tous les arbres sont propres à l’instant du relevé. Devops contient le commit
de cadrage `e7e0c4f` ajouté par cette invocation. Aucun index préexistant occupé.
Le commit devops antérieur `7511267` est ancêtre du develop local `98932aa` ;
la branche est conservée sans synchronisation. DEM-006 porte des verdicts humains
déjà commités. Aucune nouvelle écriture de cette mission n’est observée pendant
l’audit ; une nouvelle coordination sera nécessaire pour tout nettoyage réel.
La lecture des autres couches ne réserve pas leur disponibilité pour la suite.

- `.` : HEAD `98932aa154eb92f82b9b8583d72c67fe5e154959` ; `## develop`.
  Empreinte des métadonnées avant : `e50b43cc6139ca5032509e3be86e1bbcbe951e250d4669030cad73c6cc2686b5`.
  Fichiers d’environnement recensés : 4 ; aucune lecture de contenu ni mutation.
- `worktree/backoffice` : HEAD `98932aa154eb92f82b9b8583d72c67fe5e154959` ; `## layers/backoffice`.
  Empreinte des métadonnées avant : `7520353e7753eb6f875a9a974d26af4bada27b9062b707736cfd3f7be72ddf47`.
  Fichiers d’environnement recensés : 3 ; aucune lecture de contenu ni mutation.
- `worktree/api` : HEAD `98932aa154eb92f82b9b8583d72c67fe5e154959` ; `## layers/api`.
  Empreinte des métadonnées avant : `ec3ef6ed6d1662a591b11b3e89d68491316e09109797329cf6aed2009eafd212`.
  Fichiers d’environnement recensés : 5 ; aucune lecture de contenu ni mutation.
- `worktree/web` : HEAD `98932aa154eb92f82b9b8583d72c67fe5e154959` ; `## layers/web`.
  Empreinte des métadonnées avant : `1919b6663c640aed05a617998fe0843f6483c0a0d3731ea466a7cda5594e5d3c`.
  Fichiers d’environnement recensés : 3 ; aucune lecture de contenu ni mutation.
- `worktree/devops` : HEAD `e7e0c4ff3810cd6bd728a14f9cb0e9883af216d0` ; `## layers/devops`.
  Empreinte des métadonnées avant : `78567ff347ffc4c4bbb61166eaa8d1410346581b9b06212de66d15987efe6af1`.
  Fichiers d’environnement recensés : 4 ; aucune lecture de contenu ni mutation.
- `worktree/design` : HEAD `98932aa154eb92f82b9b8583d72c67fe5e154959` ; `## layers/design`.
  Empreinte des métadonnées avant : `ebe18de0536c306b7dba7b062e51213ab8b4236083773e630d66d92700dc63cb`.
  Fichiers d’environnement recensés : 3 ; aucune lecture de contenu ni mutation.

Les `.env.example` suivis sont compris dans ce décompte des noms `.env*`.
Aucun fichier spécial observé. Préserver les bases et ressources des services,
même absentes du disque hôte parce que stockées dans des volumes Docker.

## Préparation de l’analyse et de l’arbitrage

Proposition à examiner : reconnaître les caches sans source et sans consommateur
encore actif, puis retirer uniquement ces fichiers et leurs parents effectivement
vides et autorisés. L’absence d’un chemin dans Git ou son caractère ignoré ne
constitue pas un critère suffisant. Les dossiers de dépendances, montages, données
et outils d’environnement ont besoin d’exceptions explicites.

L’arbitrage doit déterminer les preuves de certitude, la politique concernant les
liens et changements concurrents, les restrictions de parcours, les erreurs de
lecture et les cibles occupées. Un résultat incertain doit préserver le contenu
et empêcher de déclarer le suivi de livraison achevé. Aucun arbitrage humain
technique n’a encore été recueilli pour cette demande.

## Reproduire le relevé

Depuis la racine du dépôt principal, enregistrer le script ci-dessous hors dépôt,
puis exécuter `python3 /tmp/dem007-audit.py`. Il écrit uniquement son résultat
dans `/tmp/dem007-audit.json`. Les compteurs peuvent évoluer avec les services
et avec les nouveaux documents. Le script est un instrument de preuve ponctuel,
pas un nouveau contrôle Codebase Integrity ou une autorisation de nettoyage.

```python
import os, stat, hashlib, subprocess, json
from pathlib import Path
root=Path.cwd()
config=json.loads((root/'worktree/devops/infra/config/layers.json').read_text())
trees=['.']+['worktree/'+n for n in config['layers']]
def git(p,*args):
 return subprocess.check_output(['git','-C',str(p),*args]).decode().strip()
def scan(p):
 entries={}; errors=[]
 def error(e): errors.append((os.path.relpath(e.filename,p),e.strerror))
 for cur,dirs,files in os.walk(p,followlinks=False,onerror=error):
  if Path(cur)==p: dirs[:]=[d for d in dirs if d not in ('.git','worktree')]
  dirs[:]=[d for d in dirs if d!='.git']
  for n in sorted(dirs+files):
   q=Path(cur)/n
   if n=='.git': continue
   r=q.relative_to(p).as_posix()
   try:
    s=q.lstat(); kind='dir' if stat.S_ISDIR(s.st_mode) else 'link' if stat.S_ISLNK(s.st_mode) else 'file' if stat.S_ISREG(s.st_mode) else 'special'
    entries[r]=(kind,s.st_size if kind!='dir' else 0,s.st_mtime_ns,s.st_ctime_ns,s.st_mode,os.readlink(q) if kind=='link' else '')
   except OSError as e: error(e)
 return entries,errors
out={}
for rel in trees:
 p=root if rel=='.' else root/rel
 before,errors=scan(p)
 tracked=set(git(p,'ls-files','-z').split('\0'))-{''}
 parent=set()
 for f in tracked:
  for par in Path(f).parents:
   if str(par)!='.': parent.add(par.as_posix())
 untracked=set(before)-tracked-parent
 maximal=[r for r in sorted(untracked) if not any(par.as_posix() in untracked for par in Path(r).parents if str(par)!='.')]
 groups=[]
 for r in maximal:
  desc=[v for k,v in before.items() if k==r or k.startswith(r+'/')]
  groups.append({'path':r,'files':sum(v[0]=='file' for v in desc),'links':sum(v[0]=='link' for v in desc),'dirs':sum(v[0]=='dir' for v in desc)})
 orphans=[]
 for r,v in before.items():
  if v[0]=='file' and '/__pycache__/' in r and r.endswith('.pyc'):
   q=Path(r); source=q.parent.parent/(q.name.split('.')[0]+'.py')
   if not os.path.lexists(p/source): orphans.append(r)
 after,err2=scan(p)
 changed=[r for r in sorted(set(before)|set(after)) if before.get(r)!=after.get(r)]
 payload=json.dumps(before,sort_keys=True).encode()
 out[rel]={'head':git(p,'rev-parse','HEAD'),'status':git(p,'status','--short','--branch'),'files':sum(v[0]=='file' for v in before.values()),'dirs':sum(v[0]=='dir' for v in before.values()),'links':sum(v[0]=='link' for v in before.values()),'empty_dirs':[r for r,v in before.items() if v[0]=='dir' and not any(os.scandir(p/r))],'groups':groups,'orphan_pyc':orphans,'errors':errors+err2,'changed':changed,'metadata_sha256':hashlib.sha256(payload).hexdigest(),'env_files':[r for r in before if Path(r).name=='.env' or Path(r).name.startswith('.env.')],'special':[r for r,v in before.items() if v[0]=='special']}
 print(rel, out[rel]['files'],'fichiers',len(groups),'groupes',len(orphans),'pyc sans source',len(changed),'changements',flush=True)
Path('/tmp/dem007-audit.json').write_text(json.dumps(out,indent=2))
```
