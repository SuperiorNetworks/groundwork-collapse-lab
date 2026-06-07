# Phase Roadmap

This roadmap converts the six-month plan into a development sequence that can be managed with GitHub Issues, phase-gate templates, and release tags. The roadmap is designed for safe non-pyrotechnic model testing, sensor measurement, camera synchronization, data analytics, and Blender comparison.

## Phase Overview

| Phase | Weeks | Primary goal | Main release |
|---|---:|---|---|
| Phase 1 | 1–4 | Establish safe bench logging, data schema, repository structure, and dry-run workflow. | `v0.1.0` |
| Phase 2 | 5–9 | Test simple printed structures and repeatable weak-point geometry. | `v0.2.0` |
| Phase 3 | 10–13 | Add dual-camera observation and timestamp validation. | `v0.3.0` |
| Phase 4 | 14–18 | Automate data sync, analytics, plotting, and Blender comparison. | `v0.4.0` |
| Phase 5 | 19–26 | Build and demonstrate the integrated model city environment. | `v1.0.0` |

## Phase 1: Bench Logging and Project Foundation

Phase 1 creates the foundation. The team should not begin physical structure testing until the sensor logger, file naming convention, repository workflow, and pre-test checklist are working.

| Workstream | Tasks | Exit evidence |
|---|---|---|
| Repository | Create README, docs, issue templates, branch rules, and project board. | Repository can guide a new collaborator. |
| Firmware | Upload sensor logger firmware and verify serial CSV output. | Ten consecutive dry-run logs. |
| Data | Define CSV and JSON schemas. | Example files stored in `sensor-data/sample-data/`. |
| Safety | Review `docs/safety-and-scope.md` and pre-test checklist. | Checklist accepted by both collaborators. |
| Management | Create first decision log and Phase 1 issues. | `v0.1.0-rc.1` candidate release. |

## Phase 2: Basic Structure Tests

Phase 2 introduces small safe physical models. The rule is to change only one variable at a time, such as wall thickness, notch depth, support placement, or infill percentage.

| Workstream | Tasks | Exit evidence |
|---|---|---|
| Fabrication | Print towers, beams, and support fixtures. | CAD notes and photos. |
| Testing | Run comparable support-release tests. | 8 of 10 comparable tests follow expected failure path. |
| Data | Capture sensor logs and test metadata for each run. | Complete CSV and JSON files by test ID. |
| Documentation | Write Phase 2 test report. | Known-good vector tag. |

## Phase 3: Cameras and Remote Review

Phase 3 makes the project easier to collaborate on remotely. The purpose is not remote unsafe actuation; the purpose is remote observation, playback, and joint review.

| Workstream | Tasks | Exit evidence |
|---|---|---|
| Cameras | Mount wide and close cameras. | Placement guide and sample views. |
| Timing | Align camera time with sensor time. | Timestamp validation report. |
| Storage | Confirm upload of video references and data files. | Complete test package. |
| Review | Conduct remote playback review. | Phase 3 release notes. |

## Phase 4: Analytics and Blender Comparison

Phase 4 builds the analysis pipeline. The team should be able to start from a raw CSV and metadata JSON file, run a script, produce plots, and document how the result compares with the Blender scene.

| Workstream | Tasks | Exit evidence |
|---|---|---|
| Sync | Upload files to shared storage or VPS. | No manual SD-card transfer needed. |
| Analytics | Parse CSV, plot acceleration and event markers. | PNG plot and summary metrics. |
| Simulation | Link test ID to Blender scene notes. | Comparison report. |
| Release | Package raw data, plots, metadata, and docs. | `v0.4.0` release. |

## Phase 5: Integrated Model City Demonstration

Phase 5 integrates the tested pieces into a final safe model-city demonstration. The demonstration should be rehearsed before the final event.

| Workstream | Tasks | Exit evidence |
|---|---|---|
| Fabrication | Build modular base, aboveground structures, and safe void-collapse modules. | Build photos and structure list. |
| Rehearsal | Run full dry-run and safe physical rehearsal. | Final go/no-go report. |
| Demonstration | Capture wide video, close video, sensor logs, and metadata. | Complete final event package. |
| Debrief | Compare predictions with results. | `v1.0.0` release and final report. |

## Phase Gate Rule

Every phase ends with a written review. The phase passes only when the deliverables exist, the success metrics are met, the budget is still viable, and both collaborators agree to move forward. If a phase fails, the team should document the reason, create corrective issues, and repeat only the minimum work needed to regain a known-good vector.
