# Préparer son environnement de développement **AI-powered**

**AI-powered Development Engineering** est une méthode de développement logiciel avec des agents IA. Elle organise le travail, de la demande à la livraison, avec des étapes guidées, des contributions isolées et des contrôles automatiques. L’humain définit les règles et valide les résultats.

## 1. Installer les prérequis

Ubuntu 24.04 LTS avec interface graphique, accès `sudo`, compte Codex et accès GitHub au dépôt privé des skills.

### Outils système

```bash
sudo apt update
sudo apt install -y git python3 make bash perl iproute2 \
  coreutils curl ca-certificates snapd

git --version
python3 --version
make --version
perl -MJSON::PP -e 'print "$JSON::PP::VERSION\n"'
```

### VS Code et Codex

```bash
sudo snap install code --classic
/snap/bin/code --install-extension openai.chatgpt
```

### Docker

```bash
sudo apt install -y docker.io docker-compose-v2
sudo systemctl enable --now docker
sudo usermod -aG docker "$USER"
```

Fermer puis rouvrir la session Ubuntu.

```bash
docker run --rm hello-world
docker compose version
```

## 2. Cloner le dépôt

```bash
git clone --branch develop \
  https://github.com/johan-Rm/ai-development-engineering.git

cd ai-development-engineering
git status --short --branch
```

## 3. Installer les skills

Dans VS Code, ouvrir Codex et se connecter, puis envoyer :

```text
$skill-installer Installe tous les skills du dépôt
https://github.com/johan-Rm/skills-ai-powered-development-engineering.
Préserve les skills déjà installés et vérifie que les nouveaux sont disponibles.
```

## 4. Créer les worktrees par défaut

```bash
make setup-worktrees
source ~/.bash_aliases
```

## 5. Ouvrir le workspace VS Code

```bash
vscode-worktree-ai-powered-development-engineering
```

## 6. Démarrer et vérifier les applications

```bash
make docker-up-devops
make docker-status-devops
```

Ouvrir dans le navigateur :

```text
http://web.wt-devops.localhost:19304
http://backoffice.wt-devops.localhost:19304
http://api.wt-devops.localhost:19304/api/docs
```

## 7. Commencer une première demande

Dans Codex, envoyer en remplaçant le texte entre crochets :

```text
$interviewer-demande [Décrire le besoin à réaliser]
```

Puis suivre la [boucle de développement](docs/architecture/03-developpement-loop/index.md).
