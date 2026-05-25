#!/usr/bin/env zsh

set -euo pipefail

SCRIPT_DIR="${0:A:h}"
WIKI_ROOT="${SCRIPT_DIR:h}"
APP_ROOT="${WIKI_ROOT:h}/finanse-app"
PROMPT_FILE="${WIKI_ROOT}/01 Projekty/Aplikacja - koncepcja/PROMPT STARTOWY CODEX.txt"

if [[ ! -f "${PROMPT_FILE}" ]]; then
  echo "Brak pliku promptu: ${PROMPT_FILE}" >&2
  exit 1
fi

if [[ ! -d "${APP_ROOT}" ]]; then
  echo "Brak repo aplikacji obok vaultu: ${APP_ROOT}" >&2
  exit 1
fi

PROMPT="$(<"${PROMPT_FILE}")"

PROMPT="${PROMPT}

Additional app context:
- The implementation workspace is: ${APP_ROOT}
- Project wiki is available in: ${WIKI_ROOT}
- Make code changes in the app repository unless the task explicitly asks to update only the wiki.
- When implementation affects workflow, status, roadmap, decisions, or working rules, update the wiki too."

cd "${APP_ROOT}"
exec codex \
  --model gpt-5.4 \
  -c model_reasoning_effort="medium" \
  --add-dir "${WIKI_ROOT}" \
  "${PROMPT}"
