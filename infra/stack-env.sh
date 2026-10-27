# Sourced by Make recipes. Computes context only; never dispatches Docker actions.
stack_fail() { printf 'Erreur : %s\n' "$*" >&2; exit 1; }
stack_root=$(cd "$1" && pwd -P)
[[ $(git -C "$stack_root" rev-parse --show-toplevel) == "$stack_root" ]] || stack_fail 'Racine Git incohérente.'
[[ $(git rev-parse --show-toplevel) == "$stack_root" ]] || stack_fail 'Exécuter Make depuis son propre worktree.'
stack_common=$(git -C "$stack_root" rev-parse --path-format=absolute --git-common-dir)
stack_main=$(dirname "$stack_common")
[[ "$stack_main" != "$stack_root" ]] || stack_fail 'Utiliser un worktree de couche, pas le dépôt principal.'
stack_branch=$(git -C "$stack_root" branch --show-current)
git -C "$stack_root" worktree list --porcelain | grep -Fx -- "worktree $stack_root" >/dev/null || stack_fail 'Worktree non enregistré ; réparer ses liens Git.'
# JSON::PP ships with Perl. Parse the existing routing file without a host Python/Node runtime.
stack_record=$(STACK_BRANCH="$stack_branch" perl -0777 -MJSON::PP -e '
    my $cfg = decode_json(<>)->{layers};
    die "Configuration layers invalide\n" unless ref($cfg) eq "HASH" && keys %$cfg;
    my (%ids, %branches, @matches);
    for my $name (sort keys %$cfg) {
        my $entry = $cfg->{$name};
        die "Couche invalide\n" unless $name =~ /^[a-z][a-z0-9-]*$/ && ref($entry) eq "HASH";
        my ($id, $branch) = @{$entry}{qw(id branch)};
        die "Identifiant invalide ou dupliqué\n" unless defined($id) && $id =~ /^[1-9][0-9]*$/ && !$ids{$id}++;
        die "Branche invalide ou dupliquée\n" unless defined($branch) && $branch ne "" && !$branches{$branch}++;
        push @matches, "$name\n$id" if $branch eq $ENV{STACK_BRANCH};
    }
    die "Branche de couche attendue ; HEAD détachée et intégration refusées\n" unless @matches == 1;
    print $matches[0];
' "$stack_root/infra/config/layers.json") || stack_fail 'Routage de couche invalide ou branche inattendue.'
mapfile -t stack_fields <<< "$stack_record"
stack_layer=${stack_fields[0]}
stack_id=${stack_fields[1]}
stack_base=${AIDE_APP_PORT_BASE:-19300}
[[ "$stack_base" =~ ^[0-9]{1,5}$ ]] || stack_fail 'AIDE_APP_PORT_BASE doit être un entier de 0 à 65535.'
stack_port=$((10#$stack_base + stack_id))
(( stack_port >= 1024 && stack_port <= 65535 )) || stack_fail 'Port calculé hors de la plage 1024..65535.'
stack_key=$(printf '%s' "$stack_main" | sha256sum | cut -c1-10)
for stack_name in "${!COMPOSE_@}" "${!AIDE_APP_@}"; do
    [[ -z "$stack_name" ]] || unset "$stack_name"
done
export AIDE_APP_ROOT="$stack_root" AIDE_APP_DOMAIN="wt-$stack_layer.localhost"
export AIDE_APP_PORT="$stack_port" AIDE_APP_UID="$(id -u)" AIDE_APP_GID="$(id -g)"
export AIDE_APP_IMAGE_KEY="$stack_key" AIDE_APP_PORT_BASE="$stack_base"
stack_project="aide-app-$stack_key-$stack_layer"
INTERFACE=${INTERFACE:-$([[ "$stack_layer" == backoffice ]] && printf backoffice || printf web)}
case "$INTERFACE" in
    web) stack_profiles=(--profile web) ;;
    backoffice) stack_profiles=(--profile backoffice) ;;
    both) stack_profiles=(--profile web --profile backoffice) ;;
    *) stack_fail 'INTERFACE doit valoir web, backoffice ou both.' ;;
esac
stack_mountpoints() {
    local source directory
    local -a sources=("$stack_root/app/api/app") names=(vendor var)
    case "$INTERFACE" in
        web) sources+=("$stack_root/app/web/targets/app") ;;
        backoffice) sources+=("$stack_root/app/backoffice") ;;
        both) sources+=("$stack_root/app/web/targets/app" "$stack_root/app/backoffice") ;;
    esac
    for source in "${sources[@]}"; do
        [[ -d "$source" ]] || stack_fail "Source absente : $source"
        if [[ "$source" != "$stack_root/app/api/app" ]]; then names=(node_modules .nuxt .output); fi
        for directory in "${names[@]}"; do
            [[ ! -L "$source/$directory" ]] || stack_fail "Point de montage symbolique refusé : $source/$directory"
            mkdir -p -- "$source/$directory"
        done
    done
}
stack_info() {
    printf 'root=%s\nlayer=%s\nbranch=%s\nproject=%s\nport=%s\ndomain=%s\nimage_key=%s\n' \
        "$AIDE_APP_ROOT" "$stack_layer" "$stack_branch" "$stack_project" "$AIDE_APP_PORT" "$AIDE_APP_DOMAIN" "$AIDE_APP_IMAGE_KEY"
    printf 'api=http://api.%s:%s/api/docs\nweb=http://web.%s:%s\nbackoffice=http://backoffice.%s:%s\n' \
        "$AIDE_APP_DOMAIN" "$AIDE_APP_PORT" "$AIDE_APP_DOMAIN" "$AIDE_APP_PORT" "$AIDE_APP_DOMAIN" "$AIDE_APP_PORT"
}
