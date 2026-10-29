SHELL := /bin/bash
.SHELLFLAGS := -eu -o pipefail -c
.ONESHELL:
.DEFAULT_GOAL := help
.PHONY: setup-worktrees
setup-worktrees:
	@python3 codebase-integrity/scripts/setup_worktrees.py

STACK_ROOT := $(abspath $(dir $(lastword $(MAKEFILE_LIST))))
export INTERFACE AIDE_APP_PORT_BASE RELOAD EXPECT_EMPTY
CONTEXT = source "$(STACK_ROOT)/infra/stack-env.sh" "$(STACK_ROOT)"
COMPOSE = docker compose --env-file /dev/null --project-directory "$${AIDE_APP_ROOT}" -p "$${stack_project}" -f "$${AIDE_APP_ROOT}/infra/compose.apps.yaml"
LAYERS := api web backoffice design devops
# Resolve siblings from Git, so aliases work from the main checkout after integration
# and from a layer worktree while the change is being reviewed.
MAIN_ROOT = $(shell dirname "$$(git -C "$(STACK_ROOT)" rev-parse --path-format=absolute --git-common-dir)")
.PHONY: $(addprefix docker-up-,$(LAYERS)) $(addprefix docker-stop-,$(LAYERS)) $(addprefix docker-status-,$(LAYERS))

$(addprefix docker-up-,$(LAYERS)):
	+@$(MAKE) --no-print-directory -C "$(MAIN_ROOT)/worktree/$(patsubst docker-up-%,%,$@)" up INTERFACE=$(if $(INTERFACE),$(INTERFACE),both)

$(addprefix docker-stop-,$(LAYERS)):
	+@$(MAKE) --no-print-directory -C "$(MAIN_ROOT)/worktree/$(patsubst docker-stop-%,%,$@)" down

$(addprefix docker-status-,$(LAYERS)):
	+@$(MAKE) --no-print-directory -C "$(MAIN_ROOT)/worktree/$(patsubst docker-status-%,%,$@)" status

.PHONY: help info config prepare up status down test test-browser test-runtime

help:
	@printf '%s\n' 'make setup-worktrees : préparer les worktrees, le workspace et son alias Bash' \
	  'make docker-up-api | docker-up-web | docker-up-backoffice | docker-up-design | docker-up-devops : démarrer une couche avec ses deux interfaces' \
	  'make docker-stop-<couche> : arrêter une couche' \
	  'make docker-status-<couche> : consulter une couche' \
	  'make prepare | up [INTERFACE=web|backoffice|both] | status | down : worktree courant' \
	  'make info | config [INTERFACE=...] | test | test-browser [RELOAD=1] | test-runtime [EXPECT_EMPTY=1]' \
	  'AIDE_APP_PORT_BASE=19300 par défaut. down conserve les volumes.'

info:
	@$(CONTEXT)
	stack_info

config:
	@$(CONTEXT)
	$(COMPOSE) "$${stack_profiles[@]}" config

prepare:
	@$(CONTEXT)
	$(COMPOSE) --profile '*' build api
	$(COMPOSE) --profile '*' pull init web backoffice caddy

up:
	@$(CONTEXT)
	own=$$($(COMPOSE) --profile '*' ps -q caddy)
	published=''
	if [[ -n "$$own" ]]; then published=$$(docker port "$$own" 80/tcp); fi
	if [[ "$$published" != "127.0.0.1:$$AIDE_APP_PORT" ]]; then
	    listeners=$$(ss -H -ltn "sport = :$$AIDE_APP_PORT")
	    [[ -z "$$listeners" ]] || stack_fail "Port $$AIDE_APP_PORT occupé ; choisir AIDE_APP_PORT_BASE sans arrêter le service tiers."
	fi
	stack_mountpoints
	$(COMPOSE) "$${stack_profiles[@]}" up -d --build --wait --wait-timeout 600
	stack_info
	printf '%s\n' 'Seules les interfaces démarrées répondent ; les autres peuvent renvoyer 502.'

status:
	@$(CONTEXT)
	$(COMPOSE) --profile '*' ps -a
	stack_info

down:
	@$(CONTEXT)
	$(COMPOSE) --profile '*' down

test:
	@bash "$(STACK_ROOT)/infra/test-make.sh"
	bash "$(STACK_ROOT)/infra/test-shortcuts.sh"

test-browser:
	@$(CONTEXT)
	case "$${RELOAD:-0}" in 0|1) ;; *) stack_fail 'RELOAD doit valoir 0 ou 1.' ;; esac
	artifacts=/tmp/DEM-005-make-browser-artifacts
	mkdir -p -- "$$artifacts"
	mounts=()
	arguments=()
	if [[ "$${RELOAD:-0}" == 1 ]]; then
	    mounts+=(-e AIDE_RELOAD_SOURCE_DIR=/sources)
	    mounts+=(--mount "type=bind,source=$$AIDE_APP_ROOT/app/web/targets/app/app/app.vue,target=/sources/web.vue")
	    mounts+=(--mount "type=bind,source=$$AIDE_APP_ROOT/app/backoffice/app/app.vue,target=/sources/backoffice.vue")
	    mounts+=(--mount "type=bind,source=$$AIDE_APP_ROOT/app/api/app/public/router.php,target=/sources/router.php")
	    arguments+=(--reload)
	fi
	docker build -f "$$AIDE_APP_ROOT/infra/Dockerfile.browser" -t "aide-app-browser:$$AIDE_APP_IMAGE_KEY" "$$AIDE_APP_ROOT/infra"
	docker run --rm --network host --ipc host --user "$$AIDE_APP_UID:$$AIDE_APP_GID" -e HOME=/tmp \
	  -e AIDE_PLAYWRIGHT_MODULE=/opt/aide-browser/node_modules/@playwright/test \
	  -e AIDE_BROWSER_ARTIFACT_DIR=/artifacts \
	  --mount "type=bind,source=$$AIDE_APP_ROOT/infra/test-browser.cjs,target=/recipe/test-browser.cjs,readonly" \
	  --mount "type=bind,source=$$artifacts,target=/artifacts" \
	  --add-host "api.$$AIDE_APP_DOMAIN:127.0.0.1" --add-host "web.$$AIDE_APP_DOMAIN:127.0.0.1" \
	  --add-host "backoffice.$$AIDE_APP_DOMAIN:127.0.0.1" -w /tmp "$${mounts[@]}" \
	  "aide-app-browser:$$AIDE_APP_IMAGE_KEY" node /recipe/test-browser.cjs "$$stack_layer" "$$AIDE_APP_PORT" "$${arguments[@]}"

test-runtime:
	@$(CONTEXT)
	case "$${EXPECT_EMPTY:-0}" in 0|1) ;; *) printf '%s\n' 'EXPECT_EMPTY doit valoir 0 ou 1.' >&2; exit 1 ;; esac
	node "$(STACK_ROOT)/infra/test-runtime.cjs"
