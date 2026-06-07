# Phase Gate Review Template

Copy this file for each phase review and replace the bracketed fields. A phase should not close until the evidence is complete and the go/no-go decision is recorded.

## Phase Information

| Field | Value |
|---|---|
| Phase | `[Phase number and name]` |
| Review date | `[YYYY-MM-DD]` |
| Reviewers | `[Names or roles]` |
| Release candidate | `[Tag or commit hash]` |
| Decision | `[Go / No-Go / Repeat with changes]` |

## Objective

Write one paragraph explaining what the phase was intended to prove. The objective should match the roadmap and the project plan.

## Required Deliverables

| Deliverable | Location | Complete? | Notes |
|---|---|---:|---|
| Documentation updated | `[path]` |  |  |
| Code or tool updated | `[path]` |  |  |
| Test data captured | `[path]` |  |  |
| Safety checklist completed | `[path]` |  |  |
| Known-good vector identified | `[tag or issue]` |  |  |

## Success Metrics

| Metric | Target | Actual | Pass? |
|---|---|---|---:|
| `[Metric 1]` | `[Target]` | `[Actual]` |  |
| `[Metric 2]` | `[Target]` | `[Actual]` |  |
| `[Metric 3]` | `[Target]` | `[Actual]` |  |

## Safety and Scope Review

Confirm that the phase remained within the safe non-pyrotechnic scope of the repository. Any proposed work involving energetic materials, modified fireworks, ignition circuits, or remote initiation logic is outside scope and must be rejected.

| Check | Pass? | Notes |
|---|---:|---|
| Work remained inside safe repository scope. |  |  |
| No prohibited procedures were added. |  |  |
| Pre-test checklist was used for physical tests. |  |  |
| Risks and mitigations were updated. |  |  |

## Decision

State the final decision in one paragraph. If the decision is go, identify the release tag. If the decision is no-go or repeat, list corrective issues.

## Follow-Up Issues

| Issue | Owner | Due date |
|---|---|---|
| `[Issue link]` | `[Owner]` | `[YYYY-MM-DD]` |
