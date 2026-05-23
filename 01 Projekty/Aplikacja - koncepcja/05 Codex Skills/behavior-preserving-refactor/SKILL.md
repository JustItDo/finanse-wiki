---
name: behavior-preserving-refactor
description: Use when the task is to restructure existing code without changing observable behavior. Trigger for requests about cleanup, simplification, extraction, naming improvements, duplication removal, or improved internal structure, readability, or modularity under unchanged runtime outcomes.
---

# Behavior-Preserving Refactor

Use this skill only for refactoring work.

## Progressive disclosure

Load this skill only when the task is about internal code improvement with unchanged observable behavior.

Do not load it for net-new features, runtime diagnosis, intentional bug fixes, or review-only tasks.

## Touch boundaries

Touch only:

- implementation files directly on the execution path
- existing test files covering that path, or one new narrow regression test file if none exists
- type or wiring files whose omission would make the refactor non-functional

Do not touch docs unless the user asked or the change would otherwise be misleading.

Do not mix refactor with feature work or intended behavior changes.

## Process over prose

Execute this procedure in order, without skipping steps:

1. State the exact observable behavior that must remain unchanged.
2. Name the files, call sites, and tests to inspect before editing.
3. Inspect those files, their direct call path, and current regression coverage.
4. Write a checkpoint with:
   - in scope
   - out of scope
   - preserved behavior
   - inspected files
   - next edit target
5. Choose the smallest refactor that improves the requested area.
6. Make the refactor in controlled steps that preserve behavior.
7. Add or update regression tests unless no executable test path exists in that area; if none exists, state that explicitly.
8. Run verification and record:
   - exact command, test, or manual check
   - pass/fail outcome
   - preserved behavior covered
9. Report the structural improvement and the evidence that behavior stayed stable.

## Anti-rationalization table

| Rationalization to reject | Required response |
| --- | --- |
| "I'm already here, I'll also add a feature." | Keep feature work out unless explicitly requested. |
| "The refactor is cleaner if I rewrite the module." | Prefer the smallest change that improves the target area safely. |
| "Behavior should be the same." | Verification is invalid unless the exact check and result are recorded. |
| "The old code is ugly, so broad churn is justified." | Limit edits to the requested or necessary structural change. |
| "There were no tests, so I can't prove anything." | Add one narrow regression test if practical; otherwise state the exact uncovered path and why. |
| "The scope is fuzzy, so I refactored adjacent code too." | Freeze scope in the checkpoint with in-scope and out-of-scope lists before editing. |
| "This also fixes a bug, so I'll keep it." | Remove behavior-changing edits unless the user explicitly asked for them. |

## Definition of done

The task is done only when all are true:

- the requested internal improvement was made
- preserved behavior is covered by an unchanged or added regression check, or the exact uncovered path is named
- the verification record includes exact check, outcome, and covered behavior
- change scope stayed tight and did not absorb unrelated work
- the final report states any required step that could not be completed, why it could not be completed, and what was deferred instead of guessed

## Final output contract

In the final response include:

- what was refactored
- what behavior was intended to stay unchanged
- verification record
- any uncompleted required step and the exact blocker
