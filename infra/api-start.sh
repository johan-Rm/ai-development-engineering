#!/bin/sh
set -eu
# Source is read-only. Only vendor, var and the Composer cache are writable volumes.
lock=$(sha256sum composer.lock | cut -d ' ' -f 1)
if [ ! -f vendor/.aide-lock ] || [ "$(cat vendor/.aide-lock)" != "$lock" ]; then
    composer install --no-interaction --prefer-dist --no-scripts
    printf '%s' "$lock" > vendor/.aide-lock
fi
php bin/console doctrine:migrations:migrate --no-interaction
exec php -d opcache.enable=0 -d variables_order=EGPCS -S 0.0.0.0:8000 -t public public/router.php
