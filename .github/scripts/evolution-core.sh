#!/bin/bash
# evolution-core.sh - externalized logic for evolution workflow
set -euo pipefail
IFS=$'\n\t'

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$SCRIPT_DIR/../.."
cd "$REPO_ROOT"

source .github/scripts/yaml-helpers.sh || true

EVENT_NAME="${1:-}"

echo "[evolution-core] Event: ${EVENT_NAME}"

# Load keywords from AI_CORE.yml if possible
DEFAULT_KW="terminé|accompli|créé|réalisé|fait|livré|corrigé|résolu"
KEYWORDS=$(extract_keywords_from_ai_core || echo "")
KEYWORDS=${KEYWORDS:-$DEFAULT_KW}

# If issue_comment: validate body proof pattern and manage lock
if [[ "$EVENT_NAME" == "issue_comment" ]]; then
  ISSUE_NUMBER=$(jq -r '.issue.number // empty' < "$GITHUB_EVENT_PATH" || true)
  BODY=$(jq -r '.comment.body // empty' < "$GITHUB_EVENT_PATH" || true)

  if [[ -z "$ISSUE_NUMBER" ]]; then
    echo "[evolution-core] No issue number; exit"
    exit 0
  fi

  if [[ -z "$BODY" ]]; then
    echo "[evolution-core] Empty body; exit"
    exit 0
  fi

  if echo "$BODY" | grep -Eiq "$KEYWORDS"; then
    SHA=$(echo "$BODY" | grep -Eo '\\b[0-9a-f]{7,40}\\b' | head -n1 || true)
    # Robust file extraction without backticks in regex
    FILE=$(echo "$BODY" | grep -Eo '[A-Za-z0-9._/\-]+\.(md|yml|json|py|txt|js|css|html)' | head -n1 || true)
    if [[ -z "$SHA" || -z "$FILE" ]]; then
      gh issue comment "$ISSUE_NUMBER" --body "🛡️ Validation Anti-Simulation Requise%0A%0A1. Lien GitHub direct%0A2. SHA complet%0A3. Nom exact du fichier"
      echo "[evolution-core] Challenge posted"
      exit 0
    fi
    echo "[evolution-core] Minimal proofs detected"
  fi

  # Lock management (timeout via updatedAt)
  TIMEOUT_MINUTES=${TIMEOUT_MINUTES:-30}
  if gh issue view "$ISSUE_NUMBER" --json number >/dev/null 2>&1; then
    if gh issue view "$ISSUE_NUMBER" --json labels --jq '.labels[]? | select(.name=="ia-locked")' | grep -q .; then
      UPDATED=$(gh issue view "$ISSUE_NUMBER" --json updatedAt --jq '.updatedAt' || true)
      if [[ -n "$UPDATED" && "$UPDATED" != "null" ]]; then
        LAST=$(date -d "$UPDATED" +%s || echo 0)
        NOW=$(date +%s)
        INACTIVE=$(( (NOW - LAST) / 60 ))
        if (( INACTIVE > TIMEOUT_MINUTES )); then
          gh issue edit "$ISSUE_NUMBER" --remove-label ia-locked --add-label ia-available || true
          gh issue comment "$ISSUE_NUMBER" --body "🔄 Relais IA activé (verrou expiré)"
          gh issue edit "$ISSUE_NUMBER" --remove-label ia-available --add-label ia-locked || true
          gh issue comment "$ISSUE_NUMBER" --body "🔒 Nouvelle IA prend le contrôle"
        else
          echo "[evolution-core] Lock still valid (${INACTIVE}m)"; exit 0
        fi
      fi
    else
      gh issue edit "$ISSUE_NUMBER" --remove-label ia-available --add-label ia-locked || true
      gh issue comment "$ISSUE_NUMBER" --body "🔒 IA prend en charge cette tâche (timeout ${TIMEOUT_MINUTES}m)"
    fi
  fi
fi

# Feedback capture (if body starts with 1-4)
if [[ "$EVENT_NAME" == "issue_comment" ]]; then
  BODY=$(jq -r '.comment.body // empty' < "$GITHUB_EVENT_PATH" || true)
  if [[ -n "$BODY" ]]; then
    if echo "$BODY" | grep -qE '^[1-4]'; then
      {
        echo "- timestamp: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
        echo "  issue: $(jq -r '.issue.number // \"unknown\"' < \""$GITHUB_EVENT_PATH"\")"
        echo "  phase: unknown"
        echo "  choice: $(echo \""$BODY"\" | cut -c1)"
        echo "  summary: \"$(echo \""$BODY"\" | cut -d' ' -f2- | head -c 200)\""
      } >> IA_FEEDBACK.yml
      git config --local user.email "action@github.com"
      git config --local user.name "GitHub Action Evolution"
      git add IA_FEEDBACK.yml || true
      git diff --staged --quiet || git commit -m "🧬 Auto: update IA_FEEDBACK"
      git push || true
    else
      ISSUE_NUMBER=$(jq -r '.issue.number // empty' < "$GITHUB_EVENT_PATH" || true)
      if [[ -n "$ISSUE_NUMBER" ]]; then
        gh issue comment "$ISSUE_NUMBER" --body "⚠️ Merci de commencer par 1–4; texte complémentaire accepté"
      fi
    fi
  fi
fi

echo "[evolution-core] Done"
