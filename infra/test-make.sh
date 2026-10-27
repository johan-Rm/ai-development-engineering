#!/bin/bash
set -eu -o pipefail
source_root=$(cd "$(dirname "$0")/.." && pwd -P)
trial=$(mktemp -d /tmp/aide-make-test-XXXXXX)
listener=''
trap '[[ -z "$listener" ]] || kill "$listener" 2>/dev/null || :; rm -rf -- "$trial"' EXIT
main="$trial/main"
mkdir -p "$main/config" "$trial/bin"
cp "$source_root/Makefile" "$main/Makefile"
cp -R "$source_root/infra" "$main/infra"
cp "$source_root/config/layers.json" "$main/config/layers.json"
mkdir -p "$main/app/api/app" "$main/app/web/targets/app" "$main/app/backoffice"
touch "$main/app/api/app/.fixture" "$main/app/web/targets/app/.fixture" "$main/app/backoffice/.fixture"
printf 'APP_ENV=dev\n' > "$main/app/api/app/.env.example"
git -C "$main" init -q -b develop
git -C "$main" add .
git -C "$main" -c user.name='Make test' -c user.email=test@example.invalid commit -qm fixture
cat > "$trial/bin/python3" <<'STUB'
#!/bin/sh
printf 'Python invoqué\n' >&2
exit 99
STUB
chmod +x "$trial/bin/python3"
export PATH="$trial/bin:$PATH"
expect_failure() { if "$@" > "$trial/failure.log" 2>&1; then printf 'Échec attendu : %s\n' "$*" >&2; exit 1; fi; }
expect_failure make --no-print-directory -C "$main" info
grep -q 'worktree de couche' "$trial/failure.log"
printf 'OK : dépôt principal refusé\n'
for layer in backoffice api web devops design; do
    worktree="$trial/$layer"
    git -C "$main" worktree add -qb "layers/$layer" "$worktree"
    info=$(make --no-print-directory -C "$worktree" info)
    grep -q "^layer=$layer$" <<< "$info"
    case "$layer" in backoffice) id=1;; api) id=2;; web) id=3;; devops) id=4;; design) id=5;; esac
    grep -q "^port=$((19300+id))$" <<< "$info"
    for interface in web backoffice both; do
        make --no-print-directory -C "$worktree" config INTERFACE="$interface" > "$trial/config.yaml"
        CONTEXT_ROOT="$worktree" INTERFACE="$interface" bash -eu -o pipefail -c '
            cd "$CONTEXT_ROOT"
            source "$CONTEXT_ROOT/infra/stack-env.sh" "$CONTEXT_ROOT"
            docker compose --env-file /dev/null --project-directory "$AIDE_APP_ROOT" -p "$stack_project" \
              -f "$AIDE_APP_ROOT/infra/compose.apps.yaml" "${stack_profiles[@]}" config --services
        ' | sort > "$trial/services"
        { printf 'api\ncaddy\ninit\n'; [[ "$interface" != both ]] && printf '%s\n' "$interface" || printf 'backoffice\nweb\n'; } | sort > "$trial/expected"
        cmp "$trial/services" "$trial/expected"
    done
done
printf 'OK : 5 identités et 15 configurations Compose, sans Python\n'
api="$trial/api"
printf 'SENTINEL=preserve\n' > "$api/.env"
cp "$api/.env" "$trial/env-before"
COMPOSE_FILE=/foreign COMPOSE_PROFILES='*' make --no-print-directory -C "$api" config INTERFACE=web > "$trial/sanitized.yaml"
cmp "$api/.env" "$trial/env-before"
! grep -q '^  backoffice:' "$trial/sanitized.yaml"
printf 'OK : variables Compose ignorées et .env préservé\n'
expect_failure make --no-print-directory -C "$api" info AIDE_APP_PORT_BASE=bad
expect_failure make --no-print-directory -C "$api" info AIDE_APP_PORT_BASE=65535
expect_failure make --no-print-directory -C "$api" info INTERFACE=foreign
expect_failure make --no-print-directory -C "$api" test-browser RELOAD=bad
expect_failure make --no-print-directory -C "$api" test-runtime EXPECT_EMPTY=bad
# Compact/reordered JSON remains valid; duplicate identifiers are refused.
perl -0777 -MJSON::PP -i -pe '$_=encode_json(decode_json($_))' "$api/config/layers.json"
make --no-print-directory -C "$api" info >/dev/null
cp "$api/config/layers.json" "$trial/routing"
perl -0777 -MJSON::PP -i -pe '$c=decode_json($_);$c->{layers}{api}{id}=1;$_=encode_json($c)' "$api/config/layers.json"
expect_failure make --no-print-directory -C "$api" info
cp "$trial/routing" "$api/config/layers.json"
git -C "$api" checkout --quiet --detach
expect_failure make --no-print-directory -C "$api" info
git -C "$api" checkout --quiet layers/api
printf 'OK : paramètres, HEAD détachée et configuration invalide refusés\n'
# Fake only Docker for lifecycle checks; a real TCP listener must stop up before any mutation.
cat > "$trial/bin/docker" <<'DOCKER'
#!/bin/bash
printf '%s\n' "$*" >> "$FAKE_DOCKER_LOG"
case "$*" in
    *'ps -q caddy') [[ -z "${FAKE_OWN_PORT:-}" ]] || printf 'owned\n' ;;
    'port owned 80/tcp') printf '127.0.0.1:%s\n' "$FAKE_OWN_PORT" ;;
esac
DOCKER
chmod +x "$trial/bin/docker"
export FAKE_DOCKER_LOG="$trial/docker.log"
perl -MIO::Socket::INET -e '$s=IO::Socket::INET->new(LocalAddr=>"127.0.0.1",LocalPort=>0,Listen=>1) or die $!; $|=1; print $s->sockport,"\n"; sleep 120' > "$trial/port" &
listener=$!
for attempt in {1..100}; do [[ ! -s "$trial/port" ]] || break; sleep .02; done
port=$(cat "$trial/port")
base=$((port-2))
expect_failure make --no-print-directory -C "$api" up AIDE_APP_PORT_BASE="$base"
grep -q 'occupé' "$trial/failure.log"
! grep -q ' up ' "$trial/docker.log"
export FAKE_OWN_PORT="$port"
AIDE_APP_PORT_BASE="$base" make --no-print-directory -C "$api" up INTERFACE=both > "$trial/up.log"
grep -q "^port=$port$" "$trial/up.log"
grep -q ' up -d --build --wait' "$trial/docker.log"
[[ -d "$api/app/backoffice/.nuxt" && -d "$api/app/web/targets/app/.output" ]]
[[ ! -e "$api/app/api/app/.env" ]]
cmp "$api/.env" "$trial/env-before"
make --no-print-directory -C "$api" prepare AIDE_APP_PORT_BASE="$base" > "$trial/prepare.log"
grep -q ' build api$' "$trial/docker.log"
grep -q ' pull init web backoffice caddy$' "$trial/docker.log"
make --no-print-directory -C "$api" status AIDE_APP_PORT_BASE="$base" > "$trial/status.log"
grep -q "^port=$port$" "$trial/status.log"
make --no-print-directory -C "$api" down > "$trial/down.log"
before_preview=$(wc -l < "$trial/docker.log")
make --no-print-directory -n -C "$api" up INTERFACE=both > "$trial/preview.log"
make --no-print-directory -n -C "$api" status >> "$trial/preview.log"
[[ $(wc -l < "$trial/docker.log") == "$before_preview" ]]
printf 'OK : make -n ne lance aucune commande Docker\n'
grep -q ' down$'  "$trial/docker.log"
! grep -q -- '--volumes\| down -v' "$trial/docker.log"
printf 'OK : collision réelle refusée, port propre accepté, up/down directs et données préservées\n'
rm -rf -- "$api/app/web/targets/app/node_modules"
ln -s "$api/app/backoffice/node_modules" "$api/app/web/targets/app/node_modules"
expect_failure make --no-print-directory -C "$api" up AIDE_APP_PORT_BASE="$base"
grep -q 'symbolique refusé' "$trial/failure.log"
printf 'OK : montage symbolique refusé\n'
printf 'Tous les contrôles Make sont réussis.\n'
