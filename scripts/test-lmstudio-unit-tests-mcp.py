#!/usr/bin/env python3

import json
import os
import subprocess
import sys


SERVER = "/home/justdolt/Projects/Finanse/Obsidian Vault/scripts/lmstudio-unit-tests-mcp.py"


def encode_message(payload: dict) -> bytes:
    body = json.dumps(payload).encode("utf-8")
    return f"Content-Length: {len(body)}\r\n\r\n".encode("ascii") + body


def read_message(stream) -> dict:
    headers = {}

    while True:
        line = stream.readline()
        if not line:
            raise RuntimeError("Unexpected EOF while reading MCP headers.")
        if line in (b"\r\n", b"\n"):
            break
        key, _, value = line.decode("utf-8").partition(":")
        headers[key.strip().lower()] = value.strip()

    length = int(headers["content-length"])
    body = stream.read(length)
    return json.loads(body.decode("utf-8"))


def send_and_receive(process, payload: dict) -> dict:
    process.stdin.write(encode_message(payload))
    process.stdin.flush()
    return read_message(process.stdout)


def main() -> int:
    env = dict(os.environ)
    env["LMSTUDIO_UNIT_TEST_TIMEOUT_SECONDS"] = "5"

    process = subprocess.Popen(
        [sys.executable, SERVER],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=env,
    )

    assert process.stdin is not None
    assert process.stdout is not None

    init_response = send_and_receive(
        process,
        {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "initialize",
            "params": {
                "protocolVersion": "2024-11-05",
                "capabilities": {},
                "clientInfo": {
                    "name": "smoke-test",
                    "version": "0.1.0",
                },
            },
        },
    )

    tools_response = send_and_receive(
        process,
        {
            "jsonrpc": "2.0",
            "id": 2,
            "method": "tools/list",
            "params": {},
        },
    )

    error_response = send_and_receive(
        process,
        {
            "jsonrpc": "2.0",
            "id": 3,
            "method": "tools/call",
            "params": {
                "name": "lmstudio_unit_tests",
                "arguments": {
                    "file_under_test": "src/shared/utils/date.ts",
                    "test_runner": "not configured yet",
                    "request_mode": "list_cases",
                    "context": "export function isIsoDate(value: string) { return /^\\\\d{4}-\\\\d{2}-\\\\d{2}$/.test(value); }",
                },
            },
        },
    )

    process.terminate()
    process.wait(timeout=5)

    summary = {
        "initialize_ok": "result" in init_response,
        "tools_list_ok": tools_response.get("result", {}).get("tools", [{}])[0].get("name")
        == "lmstudio_unit_tests",
        "tool_error_mode": error_response.get("result", {}).get("isError", False),
        "tool_error_excerpt": error_response.get("result", {})
        .get("content", [{}])[0]
        .get("text", "")[:200],
    }

    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
