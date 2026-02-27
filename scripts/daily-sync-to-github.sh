#!/usr/bin/env bash
# Daily sync: commit and push Charlie PM brain to GitHub.
# Run by launchd daily, or manually: ./scripts/daily-sync-to-github.sh

set -e
REPO_DIR="/Users/charlie.wildish/Charlie PM brain"
cd "$REPO_DIR"

# Only commit and push if there are changes
if git diff --quiet && git diff --staged --quiet; then
  echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) No changes to sync."
  exit 0
fi

git add -A
git commit -m "Daily sync: $(date +%Y-%m-%d)" || true
git push origin main

echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) Synced to GitHub."
