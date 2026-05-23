---
name: skill-router
description: Use when the first task is to decide which project skill should handle the request. Trigger for routing between feature-implementation, code-review, behavior-preserving-refactor, and service-diagnosis.
---

# Skill Router

Use this skill only to choose exactly one of these skills:

- `feature-implementation`
- `code-review`
- `behavior-preserving-refactor`
- `service-diagnosis`

Do not use this skill to execute the task itself.

## Progressive disclosure

Load this skill only when the current job is classification of the request into one project skill.

If the task is already clearly inside one skill and routing is not requested, do not load this skill.

## Touch boundaries

Touch only the user request and the trigger descriptions of the four target skills.

Do not inspect or edit unrelated project files.

Do not start implementation, review, refactor, or diagnosis while routing.

## Process over prose

Execute this procedure in order, without skipping steps:

1. Restate the user request in one sentence.
2. Classify the request by primary intent using this forced order:
   - live server, container, or service failure with unknown cause -> `service-diagnosis`
   - static assessment of code, diff, PR, or technical plan -> `code-review`
   - internal code improvement with unchanged observable behavior -> `behavior-preserving-refactor`
   - new or intentionally changed behavior -> `feature-implementation`
3. Write a checkpoint with:
   - chosen skill
   - rejected skills
   - one-line reason for each rejection
4. If more than one skill still fits, stop and state the exact ambiguity.
5. If no skill fits, stop and state that no existing skill matches.
6. Return exactly one chosen skill only when ambiguity is resolved.

## Conflict rules

- `service-diagnosis` beats every other skill when runtime evidence from servers, containers, services, logs, or health checks is required.
- `code-review` beats `behavior-preserving-refactor` when the user asks to assess before changing.
- `behavior-preserving-refactor` beats `feature-implementation` when the stated goal is internal improvement without intended behavior change.
- `feature-implementation` is valid only when the user wants net-new behavior or an intentional change in behavior.

## Anti-rationalization table

| Rationalization to reject | Required response |
| --- | --- |
| "It sounds partly like two skills, I'll just pick one and continue." | Stop and state the exact ambiguity if one skill cannot be justified as primary intent. |
| "I can start coding and routing will become obvious." | Do not execute the task while routing. |
| "The task mentions a bug, so it must be diagnosis." | Choose `service-diagnosis` only for server, container, or service diagnosis with unknown cause. |
| "The task mentions cleanup, so it must be refactor." | Choose `behavior-preserving-refactor` only if unchanged observable behavior is explicit or required. |
| "The task mentions improvement, so it must be feature." | Choose `feature-implementation` only for net-new or intentionally changed behavior. |
| "The task mentions finding issues, so it must be review." | Choose `code-review` only for static assessment of artifacts, not live runtime investigation. |

## Definition of done

The task is done only when all are true:

- exactly one target skill was chosen, or exact ambiguity was stated
- the choice followed the forced order
- every rejected skill has a one-line rejection reason
- no task execution happened during routing
- the final response contains only the routing outcome and reasoning

## Final output contract

In the final response include:

- chosen skill, or exact ambiguity
- one-sentence reason
- rejected skills with one-line reasons
