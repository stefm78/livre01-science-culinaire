#!/bin/bash
# Common utility functions for robust GitHub Actions workflows
# Conforme à l'ADN: frugal, émergent, lisible, traçable

set -euo pipefail
IFS=$'\n\t'

# Retry a command with exponential backoff
# Usage: retry_cmd "gh repo create ..." 5
retry_cmd() {
    local cmd="$1"
    local max_attempts="${2:-3}"
    local attempt=1
    
    while [ "$attempt" -le "$max_attempts" ]; do
        echo "[RETRY] Tentative $attempt/$max_attempts: $cmd"
        
        if eval "$cmd"; then
            echo "✅ Succès (tentative $attempt)"
            return 0
        else
            local exit_code=$?
            echo "❌ Échec tentative $attempt (code: $exit_code)"
            
            if [ "$attempt" -eq "$max_attempts" ]; then
                echo "❌ ÉCHEC FINAL après $max_attempts tentatives"
                return $exit_code
            fi
            
            local sleep_time=$((attempt * 3))
            echo "⏳ Attente ${sleep_time}s avant retry..."
            sleep "$sleep_time"
            attempt=$((attempt + 1))
        fi
    done
}

# Post a formatted comment to an issue
# Usage: post_issue_comment "owner/repo" "issue_number" "title" "message"
post_issue_comment() {
    local repo="$1"
    local issue_num="$2"
    local title="$3"
    local message="$4"
    
    local formatted_body
    formatted_body=$(printf "## %s\n\n%s\n\n---\n*Workflow automatique - %s*" "$title" "$message" "$(date)")
    
    retry_cmd "gh issue comment --repo '$repo' '$issue_num' --body '$formatted_body'" 3
}

# Display comprehensive diagnostics
diagnostics() {
    echo "=== DIAGNOSTICS ==="
    echo "Date: $(date)"
    echo "PWD: $(pwd)"
    echo "User: $(whoami)"
    
    printf "\n--- GitHub CLI ---\n"
    gh --version || echo "❌ gh non disponible"
    
    if command -v gh >/dev/null 2>&1; then
        printf "\n--- Auth Status ---\n"
        gh auth status --show-token-scope 2>&1 || echo "❌ Auth failed"
        
        printf "\n--- Rate Limits ---\n"
        gh api rate_limit 2>&1 || echo "❌ Rate limit check failed"
    fi
}

# Validate project name format
# Usage: validate_project_name "mon-projet"
validate_project_name() {
    local name="$1"
    
    if [[ -z "$name" ]]; then
        echo "❌ Nom de projet vide"
        return 1
    fi
    
    if [[ ! "$name" =~ ^[a-z0-9-]{3,}$ ]]; then
        echo "❌ Format invalide: '$name'"
        echo "Format requis: minuscules, chiffres, tirets, minimum 3 caractères"
        return 1
    fi
    
    echo "✅ Nom valide: $name"
    return 0
}

# Safe concatenation of files with error handling
# Usage: safe_cat file1.md file2.md > output.md
safe_cat() {
    for file in "$@"; do
        if [[ -f "$file" ]]; then
            cat "$file"
        else
            echo "⚠️ Fichier manquant: $file" >&2
        fi
    done
}

# Decode base64 safely
# Usage: safe_base64_decode "encoded_string"
safe_base64_decode() {
    local encoded="$1"
    
    if [[ -z "$encoded" ]]; then
        echo "⚠️ Chaîne base64 vide" >&2
        return 1
    fi
    
    printf "%s" "$encoded" | base64 -d 2>/dev/null || {
        echo "❌ Échec décodage base64" >&2
        return 1
    }
}

# Check if repository exists
# Usage: repo_exists "owner/repo"
repo_exists() {
    local repo="$1"
    gh repo view "$repo" >/dev/null 2>&1
}

# Wait for repository availability with timeout
# Usage: wait_for_repo "owner/repo" 30
wait_for_repo() {
    local repo="$1"
    local timeout="${2:-30}"
    local elapsed=0
    
    echo "Attente de la disponibilité du repo: $repo"
    
    while [ "$elapsed" -lt "$timeout" ]; do
        if repo_exists "$repo"; then
            echo "✅ Repository $repo disponible (après ${elapsed}s)"
            return 0
        fi
        
        sleep 3
        elapsed=$((elapsed + 3))
        echo "⏳ Attente... (${elapsed}s/${timeout}s)"
    done
    
    echo "❌ Timeout: repository $repo non disponible après ${timeout}s"
    return 1
}
