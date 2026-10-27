#!/bin/sh
set -eu
lock=$(sha256sum package-lock.json | cut -d ' ' -f 1)
if [ ! -f node_modules/.aide-lock ] || [ "$(cat node_modules/.aide-lock)" != "$lock" ]; then
    npm ci --no-audit --no-fund
    printf '%s' "$lock" > node_modules/.aide-lock
fi
exec node_modules/.bin/nuxt dev --host 0.0.0.0 --port 3000
