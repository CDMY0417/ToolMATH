#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SOURCE_DIR="${SOURCE_DIR:-$ROOT_DIR}"
REMOTE_URL="${REMOTE_URL:-}"
BRANCH="${BRANCH:-main}"
COMMIT_MESSAGE="${COMMIT_MESSAGE:-Update ToolMATH github_publish snapshot}"
TMP_PARENT="${TMP_PARENT:-/tmp}"

usage() {
  cat <<'EOF'
Usage:
  REMOTE_URL="https://github.com/<user>/<repo>.git" \
  BRANCH="main" \
  COMMIT_MESSAGE="Update published ToolMATH files" \
  bash github_publish/push_to_github_repo.sh

Optional environment variables:
  SOURCE_DIR      Source directory to publish. Defaults to github_publish/.
  REMOTE_URL      Target Git repository URL. Required.
  BRANCH          Target branch. Defaults to main.
  COMMIT_MESSAGE  Commit message to use. Defaults to "Update ToolMATH github_publish snapshot".
  TMP_PARENT      Parent directory for the temporary clone. Defaults to /tmp.

Notes:
  - The script publishes the CONTENTS of SOURCE_DIR to the repository root.
  - The target repository should already exist.
  - Authentication must already be configured, for example through:
      - gh auth login
      - an HTTPS token in REMOTE_URL
      - SSH keys with an ssh remote URL
EOF
}

if [[ "${1:-}" == "-h" || "${1:-}" == "--help" ]]; then
  usage
  exit 0
fi

if [[ -z "$REMOTE_URL" ]]; then
  echo "ERROR: REMOTE_URL is required."
  usage
  exit 1
fi

if [[ ! -d "$SOURCE_DIR" ]]; then
  echo "ERROR: SOURCE_DIR does not exist: $SOURCE_DIR"
  exit 1
fi

for cmd in git rsync mktemp; do
  if ! command -v "$cmd" >/dev/null 2>&1; then
    echo "ERROR: required command not found: $cmd"
    exit 1
  fi
done

TMP_DIR="$(mktemp -d "$TMP_PARENT/github_publish_push.XXXXXX")"
cleanup() {
  rm -rf "$TMP_DIR"
}
trap cleanup EXIT

echo "Cloning $REMOTE_URL (branch: $BRANCH) into temporary directory..."
git clone --depth 1 --branch "$BRANCH" "$REMOTE_URL" "$TMP_DIR"

echo "Syncing published files from $SOURCE_DIR ..."
rsync -a --delete \
  --exclude '.git' \
  --exclude '.DS_Store' \
  --exclude '__pycache__' \
  "$SOURCE_DIR"/ "$TMP_DIR"/

cd "$TMP_DIR"

git add -A

if git diff --cached --quiet; then
  echo "No changes to commit."
  exit 0
fi

echo "Creating commit..."
git commit -m "$COMMIT_MESSAGE"

echo "Pushing to $REMOTE_URL ($BRANCH) ..."
git push origin "$BRANCH"

echo "Done."
