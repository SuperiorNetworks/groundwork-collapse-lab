# Project Management Instructions

This document explains how to manage the project through planning, development, testing, review gates, and final demonstration. It is written for a two-person remote team using one primary physical test rig and a shared GitHub repository.

## Operating Model

The project should be managed as a staged engineering program. Each phase has a defined objective, a review gate, and go/no-go criteria. The team should not proceed to the next phase until the current phase has been documented and reviewed.

| Management area | Practice |
|---|---|
| Work tracking | Use GitHub Issues for every task, bug, design decision, and phase gate. |
| Documentation | Keep current documentation in `docs/`; do not rely on private chats as the record of truth. |
| Decision-making | Record decisions in issue comments or `docs/management/decision-log.md`. |
| Phase gates | Use the templates in `docs/phase-gates/` and close the phase only after pass criteria are met. |
| Releases | Tag known-good vectors and phase releases so physical results can be reproduced later. |
| Safety review | Run the pre-test checklist before every physical test. |

## Weekly Meeting Cadence

The team should hold one short weekly review and one phase-gate review at the end of each phase. The weekly review keeps both collaborators aligned without creating unnecessary overhead.

| Meeting | Duration | Agenda | Output |
|---|---:|---|---|
| Weekly build review | 30 minutes | Progress, blockers, next tests, open issues, budget status. | Updated issues and task assignments. |
| Pre-test review | 15 minutes | Checklist, camera view, data logger status, local safety confirmation. | Go/no-go decision. |
| Phase-gate review | 45 minutes | Review pass criteria, artifacts, lessons learned, remaining risks. | Release tag or repeat-phase decision. |
| Final debrief | 60 minutes | Compare prediction vs. result, review data package, decide next project. | Final report and `v1.0.0` release notes. |

## Role Split

The project assumes one collaborator owns most fabrication and the other owns project coordination, repository management, data pipeline, and logistics. These roles can change as needed, but every issue should have one owner.

| Role | Responsibilities |
|---|---|
| Fabrication lead | 3D printing, casting, fixtures, camera mounts, physical setup photos, repair kit. |
| Project and data lead | GitHub repository, VPS or sync workflow, documentation, phase gates, release tags, final event logistics. |
| Joint responsibilities | CAD review, sensor interpretation, Blender comparison, test reports, lessons learned. |

## Issue Labels

Use labels so the project board stays readable.

| Label | Meaning |
|---|---|
| `phase-1` through `phase-5` | Phase ownership. |
| `docs` | Documentation work. |
| `firmware` | Sensor logger firmware or Arduino-related work. |
| `analytics` | Python parsing, plots, and metrics. |
| `simulation` | Blender or model comparison work. |
| `fabrication` | 3D printing, casting, fixtures, mounts. |
| `safety-review` | Requires scope or pre-test safety review. |
| `blocked` | Cannot proceed without another action. |
| `known-good-vector` | Candidate artifact set for release tagging. |

## Budget Management

The total planning budget is capped at **$500**. The team should buy by phase rather than buying everything up front. Purchases should be entered in a simple budget table in the repository.

| Rule | Description |
|---|---|
| Gate purchases | Buy only the items required for the active phase. |
| Track running total | Update the budget table after every purchase. |
| Prefer reuse | Reuse cameras, laptops, USB cables, clamps, and power supplies where safe. |
| Defer upgrades | Do not buy optional upgrades until the prior phase passes. |
| Preserve contingency | Keep at least $25 unspent until the final phase if possible. |

## Decision Log Template

Use the following structure in `docs/management/decision-log.md`.

```markdown
## YYYY-MM-DD — Decision Title

**Decision:** State the decision in one paragraph.

**Reason:** Explain the problem, alternatives, and why this option was selected.

**Impact:** Explain which phase, files, budget items, or tests are affected.

**Follow-up:** List any issues or release tags connected to the decision.
```

## Management Principle

The repository should always answer four questions: what are we building, why are we building it, what exact configuration was tested, and whether it is safe and reproducible to repeat.
