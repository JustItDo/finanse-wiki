---
name: feature-implementation
description: Use when the task is to add net-new user-visible behavior or extend an existing product capability in an existing codebase. Trigger for requests about new flows, screens, endpoints, integrations, or business logic that intentionally changes behavior.
---

# Feature Implementation

Use this skill only for feature delivery work that intentionally changes behavior.

## Progressive disclosure

Load this skill only when the task is about implementing a new capability or extending an existing one.

Do not load it for restoring previously intended behavior, runtime failures, unknown-cause bugs, pure refactoring, or review-only work.

## Touch boundaries

Touch only:

- implementation files directly on the execution path
- existing test files covering that path, or one new narrow test file if none exists
- type or wiring files whose omission would make the change non-functional

Do not touch docs unless the user asked or the change would otherwise be misleading.

Do not broaden scope into unrelated cleanup, opportunistic refactors, speculative architecture changes, or extra product ideas.

## Process over prose

Execute this procedure in order, without skipping steps:

1. Restate the requested behavior in one sentence.
2. Name the exact files or entry points to inspect before editing.
3. Inspect those files, their direct call path, and the tests already covering that path.
4. Write a checkpoint with:
   - in scope
   - out of scope
   - inspected files
   - next edit target
5. Define the smallest complete implementation slice that satisfies the request.
6. Edit only the files allowed by the touch boundary.
7. Add or update tests unless no executable test path exists in that area; if none exists, state that explicitly.
8. Run verification and record:
   - exact command, test, or manual check
   - pass/fail outcome
   - behavior covered
9. Report the implemented behavior, evidence, and any deferred item instead of guessing.

## Anti-rationalization table

| Rationalization to reject | Required response |
| --- | --- |
| "I already know the pattern, I don't need to inspect files first." | Inspect the real local implementation before writing code. |
| "I'll clean up this other thing while I'm here." | Ignore unrelated cleanup unless the user asked for it. |
| "The feature is obvious, tests can wait." | Add or update tests unless no executable test path exists, and state that gap explicitly. |
| "I changed a lot because the architecture wanted it." | Reduce scope to the smallest complete slice that solves the asked feature. |
| "I couldn't verify it, but the code looks right." | Verification is invalid unless the exact check and result are recorded; otherwise state the external blocker. |
| "The scope is fuzzy, I'll decide as I go." | Freeze scope in the checkpoint with in-scope and out-of-scope lists before editing. |
| "There are no tests here, so I can't prove behavior." | Add one narrow test if practical; if not practical, name the exact uncovered path and why. |

## Definition of done

The task is done only when all are true:

- the requested behavior is exercised by a specific verification step
- all necessary wiring for that behavior is present
- tests were added or updated unless no executable test path exists in that area, and that absence was stated explicitly
- the verification record includes exact check, outcome, and covered behavior
- the final report states any required step that could not be completed, why it could not be completed, and what was deferred instead of guessed

## Final output contract

In the final response include:

- implemented behavior
- changed areas at a high level
- verification record
- any uncompleted required step and the exact blocker
