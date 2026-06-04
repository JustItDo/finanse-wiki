#!/usr/bin/env python3

import json
import os
import subprocess
import sys
from typing import Any


SERVER_NAME = "lmstudio-unit-tests"
SERVER_VERSION = "0.1.0"
TOOL_NAME = "lmstudio_unit_tests"
DEFAULT_MODEL = os.environ.get("LMSTUDIO_UNIT_TEST_MODEL", "qwen/qwen3.5-9b")
TIMEOUT_SECONDS = int(os.environ.get("LMSTUDIO_UNIT_TEST_TIMEOUT_SECONDS", "240"))


def write_message(payload: dict[str, Any]) -> None:
    body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    header = f"Content-Length: {len(body)}\r\n\r\n".encode("ascii")
    sys.stdout.buffer.write(header)
    sys.stdout.buffer.write(body)
    sys.stdout.buffer.flush()


def read_message() -> dict[str, Any] | None:
    headers: dict[str, str] = {}

    while True:
        line = sys.stdin.buffer.readline()
        if not line:
            return None
        if line in (b"\r\n", b"\n"):
            break
        key, _, value = line.decode("utf-8").partition(":")
        headers[key.strip().lower()] = value.strip()

    content_length = int(headers.get("content-length", "0"))
    if content_length <= 0:
        return None

    body = sys.stdin.buffer.read(content_length)
    return json.loads(body.decode("utf-8"))


def build_prompt(arguments: dict[str, Any]) -> str:
    file_under_test = arguments["file_under_test"].strip()
    context = arguments["context"].strip()
    test_runner = arguments.get("test_runner", "not configured yet").strip()
    request_mode = arguments.get("request_mode", "generate_tests").strip()
    constraints = arguments.get("constraints", "").strip()

    mode_block = {
        "generate_tests": (
            "Task:\n"
            "- generate unit tests for the provided function or module\n"
            "- cover normal cases, edge cases, and invalid input where relevant\n"
            "- keep mocks minimal\n"
            "- return only the test file content\n"
        ),
        "list_cases": (
            "Task:\n"
            "- list the best unit test cases for the provided function or module\n"
            "- cover normal cases, edge cases, and invalid input where relevant\n"
            "- return only a concise flat bullet list of test cases\n"
        ),
        "fix_tests": (
            "Task:\n"
            "- repair or rewrite the unit tests for the provided function or module\n"
            "- preserve the production code contract from the provided context\n"
            "- keep mocks minimal\n"
            "- return only the updated test file content\n"
        ),
    }.get(
        request_mode,
        (
            "Task:\n"
            "- generate unit tests for the provided function or module\n"
            "- cover normal cases, edge cases, and invalid input where relevant\n"
            "- keep mocks minimal\n"
            "- return only the test file content\n"
        ),
    )

    constraints_block = f"Constraints:\n{constraints}\n\n" if constraints else ""

    return (
        "You are writing unit tests only.\n\n"
        "Project:\n"
        "- Expo + React Native + TypeScript\n"
        "- Write tests only for the provided file\n"
        "- Do not redesign production code\n"
        "- Do not explain the solution\n\n"
        "Target:\n"
        f"- file under test: {file_under_test}\n"
        f"- test runner: {test_runner}\n\n"
        f"{mode_block}\n"
        f"{constraints_block}"
        "Output rules:\n"
        "- do not modify unrelated files\n"
        "- keep the answer compact\n\n"
        "Context:\n"
        f"{context}\n"
    )


def run_lmstudio(arguments: dict[str, Any]) -> str:
    model = arguments.get("model", DEFAULT_MODEL).strip()
    prompt = build_prompt(arguments)

    try:
        completed = subprocess.run(
            ["lms", "chat", model, "-p", prompt, "-y"],
            capture_output=True,
            text=True,
            timeout=TIMEOUT_SECONDS,
            check=False,
        )
    except subprocess.TimeoutExpired as exc:
        raise RuntimeError(
            "LM Studio did not answer before the timeout. Make sure the LM Studio desktop app or daemon is running "
            f"and that model `{model}` can be loaded. Timeout: {TIMEOUT_SECONDS}s."
        ) from exc

    stdout = completed.stdout.strip()
    stderr = completed.stderr.strip()

    if completed.returncode != 0:
        hint = (
            "LM Studio call failed. Make sure the LM Studio desktop app or daemon is running, "
            f"and that the configured model key exists. Current model: {model}."
        )
        detail = stderr or stdout or f"Process exited with code {completed.returncode}."
        raise RuntimeError(f"{hint}\n\n{detail}")

    if not stdout:
        raise RuntimeError(
            "LM Studio returned no output. Make sure the daemon is running and the selected model is usable."
        )

    return stdout


def tool_definition() -> dict[str, Any]:
    return {
        "name": TOOL_NAME,
        "description": (
            "Use the local LM Studio model to draft narrow unit tests, test cases, or test repairs "
            "for a single module with minimal context."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "file_under_test": {
                    "type": "string",
                    "description": "Path of the file or module that should be tested.",
                },
                "context": {
                    "type": "string",
                    "description": "Only the minimal code context needed for the test generation.",
                },
                "test_runner": {
                    "type": "string",
                    "description": "Expected test runner, for example Jest or Vitest.",
                    "default": "not configured yet",
                },
                "request_mode": {
                    "type": "string",
                    "enum": ["generate_tests", "list_cases", "fix_tests"],
                    "default": "generate_tests",
                    "description": "Whether to generate a test file, list test cases, or repair tests.",
                },
                "constraints": {
                    "type": "string",
                    "description": "Optional extra constraints for the generated tests.",
                },
                "model": {
                    "type": "string",
                    "description": "Optional LM Studio model key override.",
                },
            },
            "required": ["file_under_test", "context"],
        },
    }


def success_result(request_id: Any, text: str) -> dict[str, Any]:
    return {
        "jsonrpc": "2.0",
        "id": request_id,
        "result": {
            "content": [
                {
                    "type": "text",
                    "text": text,
                }
            ]
        },
    }


def error_result(request_id: Any, message: str) -> dict[str, Any]:
    return {
        "jsonrpc": "2.0",
        "id": request_id,
        "result": {
            "content": [
                {
                    "type": "text",
                    "text": message,
                }
            ],
            "isError": True,
        },
    }


def jsonrpc_error(request_id: Any, code: int, message: str) -> dict[str, Any]:
    return {
        "jsonrpc": "2.0",
        "id": request_id,
        "error": {
            "code": code,
            "message": message,
        },
    }


def handle_request(message: dict[str, Any]) -> dict[str, Any] | None:
    method = message.get("method")
    request_id = message.get("id")

    if method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": request_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {
                    "tools": {},
                },
                "serverInfo": {
                    "name": SERVER_NAME,
                    "version": SERVER_VERSION,
                },
            },
        }

    if method == "notifications/initialized":
        return None

    if method == "ping":
        return {
            "jsonrpc": "2.0",
            "id": request_id,
            "result": {},
        }

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": request_id,
            "result": {
                "tools": [tool_definition()],
            },
        }

    if method == "tools/call":
        params = message.get("params", {})
        tool_name = params.get("name")
        arguments = params.get("arguments", {})

        if tool_name != TOOL_NAME:
            return error_result(request_id, f"Unknown tool: {tool_name}")

        try:
            result = run_lmstudio(arguments)
        except Exception as exc:
            return error_result(request_id, str(exc))

        return success_result(request_id, result)

    if request_id is not None:
        return jsonrpc_error(request_id, -32601, f"Method not found: {method}")

    return None


def main() -> int:
    while True:
        message = read_message()
        if message is None:
            return 0

        response = handle_request(message)
        if response is not None:
            write_message(response)


if __name__ == "__main__":
    raise SystemExit(main())
