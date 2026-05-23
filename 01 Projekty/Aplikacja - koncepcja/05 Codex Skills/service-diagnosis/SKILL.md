---
name: service-diagnosis
description: Use when the task is to diagnose why an existing server, container, or service behavior is failing. Trigger for requests about server diagnostics, container checks, service analysis, logs, health, or incident-like runtime evidence gathering where the cause is unknown. Primary goal: evidence-backed root cause, not feature delivery.
---

# Service Diagnosis

Use this skill only for diagnosis of servers, containers, and services.

## Progressive disclosure

Load this skill only when the task is about server diagnostics, checking containers, or analyzing services.

Do not load it for pure feature implementation, pure refactoring, code review, or content work.

## Touch boundaries

Diagnose the requested failure surface only. Do not modify unrelated systems, propose opportunistic rewrites, or apply broad fixes before the cause is evidenced.

Do not change production-like state unless the user asked for remediation or the diagnosis procedure explicitly requires a safe, reversible check.

`Safe, reversible check` means:

- no destructive data mutation
- no restart of shared services
- no config change persisting beyond the session

If a check violates any of the above, ask the user first.

## Process over prose

Execute this procedure in order, without skipping steps:

1. State the failing symptom exactly.
2. State the first inspection boundary exactly: one server, one container, one service, one log stream, or one health check surface.
3. Gather direct evidence from that boundary only.
4. Write a checkpoint with:
   - symptom
   - inspected boundary
   - evidence gathered
   - next hypothesis
5. Form one hypothesis that matches the gathered evidence.
6. Test that hypothesis with the least invasive check available.
7. Repeat evidence -> hypothesis -> test until either:
   - one hypothesis survives a direct check tied to the symptom
   - the exact missing evidence blocking further narrowing is named
8. Only after the cause is supported, apply a fix only if the user asked for remediation; otherwise stop at evidenced root cause.
9. If a fix was applied, verify and record:
   - exact command, check, or observation
   - pass/fail outcome
   - symptom change covered

## Anti-rationalization table

| Rationalization to reject | Required response |
| --- | --- |
| "I've seen this before, it's probably X." | Gather local evidence before naming a root cause. |
| "I'll restart everything first." | Start with the least invasive inspection that preserves evidence. |
| "The logs are noisy, I'll guess." | Narrow the boundary and keep collecting direct signals. |
| "I found one anomaly, that's the cause." | Test the hypothesis before claiming root cause. |
| "The fix seems obvious, I'll apply it now." | Support the cause first, then change only what the diagnosis justifies and only if remediation was requested. |
| "I can't reproduce it, so I'll infer the cause." | Name the missing evidence explicitly instead of guessing. |
| "This check should be safe." | If it mutates data, restarts shared services, or persists config, ask the user first. |

## Definition of done

The task is done only when all are true:

- the symptom was stated concretely
- evidence was collected from the real failing surface
- at least one tested hypothesis was used to narrow or confirm cause
- the root cause is stated with supporting evidence, or the exact missing evidence blocking further narrowing is stated
- if a fix was applied, post-fix verification is included
- the final report states any required step that could not be completed, why it could not be completed, and what was deferred instead of guessed

## Final output contract

In the final response include:

- the symptom
- the evidence gathered
- the tested hypothesis or hypotheses
- the supported root cause or exact missing evidence
- any applied fix and post-fix verification
