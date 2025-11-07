#!/bin/bash
# issue-orchestrate.sh - externalized logic for issue orchestration
set -euo pipefail
IFS=$'\n\t'

EVENT_NAME="${1:-}"

echo "[issue-orchestrate] Event: ${EVENT_NAME}"

if [[ "$EVENT_NAME" == "issues" ]]; then
  ACTION=$(jq -r '.action // empty' < "$GITHUB_EVENT_PATH" || true)
  if [[ "$ACTION" == "closed" ]]; then
    LABELS=$(jq -r '.issue.labels[].name? // empty' < "$GITHUB_EVENT_PATH" | tr '\n' ' ')
    NEXT=""
    TITLE=""
    TEMPLATE=""
    if echo "$LABELS" | grep -q "phase-recherche"; then
      NEXT="conception"; TITLE="[CONCEPTION] Conception et Design"; TEMPLATE="conception.yml"
    elif echo "$LABELS" | grep -q "phase-conception"; then
      NEXT="production"; TITLE="[PRODUCTION] Réalisation"; TEMPLATE="production.yml"
    elif echo "$LABELS" | grep -q "phase-production"; then
      NEXT="validation"; TITLE="[VALIDATION] Tests et Validation"; TEMPLATE="validation.yml"
    elif echo "$LABELS" | grep -q "phase-validation"; then
      NEXT="finalisation"; TITLE="[FINALISATION] Livraison Finale"; TEMPLATE="finalisation.yml"
    fi

    if [[ -n "$NEXT" ]]; then
      BODY=$'## 🔄 Phase Suivante Auto-Générée\n\n'
      BODY+="Cette issue a été créée automatiquement suite à la clôture de l'issue #$(jq -r '.issue.number' < "$GITHUB_EVENT_PATH").\n\n"
      BODY+="**Phase précédente** : $(jq -r '.issue.title' < "$GITHUB_EVENT_PATH")\n"
      BODY+=$'**Statut** : ✅ Terminée\n\n---\n\n'
      BODY+=$"**Instructions pour l'IA** :\n1. Consultez \`PROJECT_META.yml\` pour le contexte\n2. Lisez \`WORKFLOW_STATE.yml\` pour l'état actuel\n3. Utilisez le template \`.github/ISSUE_TEMPLATE/$TEMPLATE\`\n4. Mettez à jour les fichiers de suivi après traitement\n\n"
      BODY+=$'⚡ **Prochaine action** : Traiter cette phase selon les spécifications du template associé.'

      gh issue create \
        --title "$TITLE" \
        --body "$BODY" \
        --label "phase-$NEXT" --label "à-traiter" --label "auto-généré"

      echo "[issue-orchestrate] Next phase created: $NEXT"
    else
      echo "[issue-orchestrate] No next phase"
    fi
  fi
fi

echo "[issue-orchestrate] Done"
