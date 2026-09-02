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

exec /usr/bin/python3 "/Users/will.richardson/Desktop/ALL AI /07_Integrations/sumble-mcp/sumble_mcp_server.py"
