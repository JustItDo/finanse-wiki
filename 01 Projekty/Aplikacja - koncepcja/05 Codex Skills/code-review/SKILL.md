---
name: code-review
description: Use when the task is to statically review code, a diff, a PR, or technical notes tied to a code change for correctness, regressions, risk, and readiness. Do not use for live failures, incident investigation, logs, runtime debugging, or root-cause analysis.
---

# Code Review

Use this skill only for review work.

## Progressive disclosure

Load this skill only when the task is review, audit, or assessment of static artifacts.

If the task requires gathering runtime evidence from logs, builds, services, or reproduction steps, use `service-diagnosis` instead.

Do not load it for implementation unless the user explicitly asks for fixes after the review.

## Touch boundaries

Do not edit code by default. Review the requested scope and any necessary neighboring context only.

Do not drift into redesign, rewriting, or implementation unless the user asks for fixes.

## Process over prose

Execute this procedure in order, without skipping steps:

1. Identify the exact review scope: files, diff, PR, or technical note set tied to a code change.
2. If the scope is ambiguous, stop and state the ambiguity before continuing.
3. Read only:
   - the requested files or diff
   - directly called code paths
   - tests exercising those paths
4. If any additional file is needed, justify it in one line tied to a specific risk.
5. Write a checkpoint with:
   - requested scope
   - inspected files
   - excluded surfaces
   - next review target
6. Review every file in the requested scope and the minimum direct execution context for each.
7. Check for correctness, regressions, edge cases, missing tests, and scope mismatch.
8. Rank findings by severity and evidence.
9. Report findings first with mandatory file references; if a file reference is unavailable, explain exactly why.
10. If no findings exist, state that explicitly and note residual testing gaps or assumptions.

## Anti-rationalization table

| Rationalization to reject | Required response |
| --- | --- |
| "It generally looks fine." | Review every file in scope and the minimum direct context before claiming no findings. |
| "I found one issue, that's enough." | Continue until the full requested scope has been systematically reviewed. |
| "This is probably intentional." | Mark it as an assumption and explain the risk if it is not intentional. |
| "I would implement it differently." | Focus on bugs, regressions, and risks before style preferences. |
| "No tests were run, but I can still say it's safe." | Call out the missing verification as a review risk. |
| "The scope wasn't clear, so I reviewed more." | Do not infer a broader review surface than the user named. |
| "I needed more context, so I kept reading." | Additional files require a one-line justification tied to a specific finding or risk. |

## Definition of done

The task is done only when all are true:

- the requested scope was actually reviewed
- findings are ordered by severity and backed by evidence
- each finding explains the concrete risk or regression
- file references are included; if unavailable, the reason is stated exactly
- if there are no findings, that is stated explicitly with remaining assumptions or testing gaps
- any scope ambiguity was resolved or explicitly surfaced before review proceeded

## Final output contract

The final response must present:

- findings first
- open questions or assumptions second
- brief summary last, if useful
- any uncompleted required step and the exact blocker
