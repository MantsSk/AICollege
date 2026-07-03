#!/usr/bin/env bash
set -euo pipefail

# Builds the production stylesheet (app/static/css/app.css) from input.css using
# the Tailwind standalone CLI — no Node/npm required. The CLI binary is fetched
# once into bin/ (gitignored). Pass --watch to rebuild on change.

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BIN_DIR="$ROOT/bin"
TW_VERSION="${TAILWIND_VERSION:-v4.3.1}"
TW="$BIN_DIR/tailwindcss"

detect_target() {
  local os arch
  os="$(uname -s)"
  arch="$(uname -m)"
  case "$os" in
    Darwin) os="macos" ;;
    Linux)  os="linux" ;;
    *) echo "Unsupported OS: $os" >&2; exit 1 ;;
  esac
  case "$arch" in
    x86_64|amd64)  arch="x64" ;;
    arm64|aarch64) arch="arm64" ;;
    *) echo "Unsupported arch: $arch" >&2; exit 1 ;;
  esac
  echo "${os}-${arch}"
}

if [ ! -x "$TW" ]; then
  target="$(detect_target)"
  url="https://github.com/tailwindlabs/tailwindcss/releases/download/${TW_VERSION}/tailwindcss-${target}"
  echo "Downloading Tailwind CLI ${TW_VERSION} (${target})..."
  mkdir -p "$BIN_DIR"
  curl -fsSL -o "$TW" "$url"
  chmod +x "$TW"
fi

exec "$TW" -i "$ROOT/app/static/css/input.css" -o "$ROOT/app/static/css/app.css" --minify "$@"
