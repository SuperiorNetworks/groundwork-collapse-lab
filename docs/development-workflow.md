# Development Workflow

This document defines how the project should be developed, reviewed, released, and managed through all phases. The purpose is to keep the work reproducible across hardware, documentation, code, simulation, and test data.

## Branching Strategy

The repository uses a conservative workflow because hardware, data, and documentation must stay synchronized. The `main` branch should remain stable and suitable for collaborators to reference at any time. The `dev` branch is the integration branch. Feature branches are used for specific work packages.

| Branch | Purpose | Merge rule |
|---|---|---|
| `main` | Stable project documentation, known-good code, reviewed data schemas, release-ready artifacts. | Merge only after phase gate or reviewed pull request. |
| `dev` | Active integration branch for the current phase. | Merge feature branches after local testing and review. |
| `feature/<topic>` | One scoped improvement such as analytics parser, camera sync, or Phase 2 structure notes. | Merge to `dev` after issue acceptance. |
| `hotfix/<topic>` | Correction to a released file or critical documentation error. | Merge to `main` and back-port to `dev`. |

## Versioning Convention

Use Semantic Versioning for software and data schemas. During early development, versions can remain in the `0.y.z` range. A `1.0.0` release should be reserved for the final integrated demonstration package.

| Version element | Meaning in this project | Example |
|---|---|---|
| Major | Breaking change to data schema, firmware output format, or release package structure. | `1.0.0` |
| Minor | Backward-compatible feature addition such as a new parser output or new metadata field. | `0.4.0` |
| Patch | Bug fix, documentation correction, or non-breaking script improvement. | `0.4.1` |
| Release candidate | Phase-gate candidate awaiting review. | `1.0.0-rc.1` |

## Known-Good Vector

A **known-good vector** is a tagged combination of project artifacts that successfully passed a test or phase gate. It is the core management concept for this project because it lets the team revert cleanly when a future change breaks repeatability.

| Artifact | Example value | Required in tag notes |
|---|---|---|
| Firmware | `sensor_logger v0.2.1` | Yes |
| Data schema | `schema v0.2.0` | Yes |
| Structure or fixture | `tower-A rev C` | Yes |
| Sensor setup | `two-accel-400hz` | Yes |
| Camera setup | `wide-close-sync-v01` | Yes |
| Analysis script | `analytics v0.3.0` | Yes |
| Test result | `pass`, `repeat`, or `fail` | Yes |

Recommended tag format:

```text
kgv-YYYY-MM-DD-phaseN-short-name
```

Example:

```text
kgv-2026-08-21-phase3-camera-sync
```

## Pull Request Rules

Pull requests should be concise and tied to one issue. Every pull request should state what changed, why it changed, how it was tested, and whether it affects safety, data format, hardware, or simulation. Any change that crosses the safety boundary must be closed rather than merged.

## Release Rules

At the end of each phase, create a release candidate tag from `dev`. After the review gate passes, merge to `main` and create the final phase release.

| Phase | Suggested release | Contents |
|---|---|---|
| Phase 1 | `v0.1.0` | Sensor logger baseline, data schema draft, safety checklist, dry-run report. |
| Phase 2 | `v0.2.0` | Basic structure tests, CAD notes, first physical test reports. |
| Phase 3 | `v0.3.0` | Camera sync workflow, placement guide, timestamp validation. |
| Phase 4 | `v0.4.0` | Automated sync, Python analytics, Blender comparison template. |
| Phase 5 | `v1.0.0` | Final integrated demonstration package and debrief. |

## Local Development Setup

The analytics subproject uses Python. The firmware subproject is intentionally limited to sensor logging and serial output. The Blender subproject is documentation-first and should be extended only with safe import or visualization scripts.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r host-tools/analytics/requirements.txt
python host-tools/analytics/analyze_sensor_log.py sensor-data/sample-data/sample_sensors.csv
```

## Definition of Done

A task is done only when the documentation is updated, the relevant code or data file is committed, the test result is recorded, the safety scope is still respected, and the issue is linked from the pull request.
