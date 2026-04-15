#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ENV_FILE="$ROOT/.env.local"

if [[ ! -f "$ENV_FILE" ]]; then
  echo "Missing $ENV_FILE"
  echo "Create it with: BRAVE_API_KEY=..."
  exit 1
fi

set -a
source "$ENV_FILE"
set +a

if [[ -z "${BRAVE_API_KEY:-}" ]]; then
  echo "BRAVE_API_KEY is empty in $ENV_FILE"
  exit 1
fi

QUERY="${1:-Selective Reality Theory}"

curl -sS --get "https://api.search.brave.com/res/v1/web/search" \
  --data-urlencode "q=$QUERY" \
  -H "Accept: application/json" \
  -H "X-Subscription-Token: $BRAVE_API_KEY" \
  | head -n 60
