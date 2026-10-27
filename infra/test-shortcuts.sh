#!/bin/bash
set -eu -o pipefail
source_root=$(cd "$(dirname "$0")/.." && pwd -P)
trial=$(mktemp -d /tmp/aide-shortcuts-XXXXXX)
trap 'rm -rf -- "$trial"' EXIT
git -C "$trial" init -q
cp "$source_root/Makefile" "$trial/Makefile"
export SHORTCUT_LOG="$trial/observed"
for layer in api web backoffice design devops; do
    mkdir -p "$trial/worktree/$layer"
    cat > "$trial/worktree/$layer/Makefile" <<'FIXTURE'
.PHONY: up down status
up down status:
	@printf '%s|%s|%s\n' '$(notdir $(CURDIR))' '$@' '$(INTERFACE)' >> "$$SHORTCUT_LOG"
FIXTURE
    make --no-print-directory -C "$trial" "docker-up-$layer"
    make --no-print-directory -C "$trial" "docker-stop-$layer"
    make --no-print-directory -C "$trial" "docker-status-$layer"
    printf '%s|up|both\n%s|down|\n%s|status|\n' "$layer" "$layer" "$layer" >> "$trial/expected"
done
make --no-print-directory -C "$trial" docker-up-api INTERFACE=web
printf 'api|up|web\n' >> "$trial/expected"
cmp "$trial/expected" "$SHORTCUT_LOG"
# Preview must not execute a child operation, even with recursive Make.
before=$(wc -l < "$SHORTCUT_LOG")
make --no-print-directory -n -C "$trial" docker-up-api > "$trial/preview"
[[ $(wc -l < "$SHORTCUT_LOG") == "$before" ]]
for target in api web backoffice design devops stop-api status-api docker-up-unknown; do
    if make --no-print-directory -C "$trial" "$target" > "$trial/refused" 2>&1; then
        printf 'Cible sans contexte ou inconnue acceptée : %s\n' "$target" >&2
        exit 1
    fi
done
printf 'OK : cinq raccourcis, arrêt, état, choix interface et aperçu sans action\n'
