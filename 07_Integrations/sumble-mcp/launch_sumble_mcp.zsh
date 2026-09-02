#!/bin/zsh
set -eu

sumble_key=$(/usr/bin/security find-generic-password \
  -a "codex-sumble" \
  -s "codex-sumble-api-key" \
  -w 2>/dev/null) || {
  print -u2 "Sumble API key is missing from macOS Keychain."
  exit 1
}

export SUMBLE_API_KEY="$sumble_key"
unset sumble_key

integration_dir=${0:A:h}
exec /usr/bin/python3 "$integration_dir/sumble_mcp_server.py"
