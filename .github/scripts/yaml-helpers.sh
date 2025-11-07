#!/bin/bash
# yaml-helpers.sh - helpers to parse YAML safely
set -euo pipefail
IFS=$'\n\t'

extract_keywords_from_ai_core() {
  if [[ -f "AI_CORE.yml" ]]; then
    awk '/proof_validation:/,0' AI_CORE.yml | \
      awk '/keywords_trigger:/,0' | \
      sed -n 's/.*keywords_trigger:\s*\[\(.*\)\].*/\1/p' | \
      tr -d '"' | tr ',' '|'
  fi
}
