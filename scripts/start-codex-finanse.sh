#!/usr/bin/env zsh

set -euo pipefail

SCRIPT_DIR="${0:A:h}"
ROOT_DIR="${SCRIPT_DIR:h}"
PROMPT_FILE="${ROOT_DIR}/01 Projekty/Aplikacja - koncepcja/PROMPT STARTOWY CODEX.txt"

if [[ ! -f "${PROMPT_FILE}" ]]; then
  echo "Brak pliku promptu: ${PROMPT_FILE}" >&2
  exit 1
fi

PROMPT="$(<"${PROMPT_FILE}")"

cd "${ROOT_DIR}"
exec codex "${PROMPT}"
