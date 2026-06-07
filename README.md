# Remote Structural Collapse Test Lab

**Remote Structural Collapse Test Lab** is a six-month, remote-first engineering project for safely studying small-scale model-structure collapse using sensors, cameras, repeatable fabrication, Python analytics, and Blender simulation. The project is designed for two collaborators working from different cities who want a shared GitHub workflow, a documentation site, a reproducible data pipeline, and a phased development plan.

> **Safety boundary:** This repository is scoped for non-pyrotechnic structural testing only. It does not document, support, or accept contributions involving modified fireworks, explosive materials, pyrotechnic initiation, remote ignition, blast-charge placement, or energetic-material test procedures. Physical experiments in this repository use safe mechanical substitutes such as support-release fixtures, servo latch releases, drop-weight demonstrations, frangible model structures, and sensor-based observation.

## Project Site Title

The recommended public-facing title is **Remote Structural Collapse Test Lab**. It is professional, technically accurate, and avoids public-facing terminology that could imply instructions for explosives or unlawful demolition activity.

| Field | Recommended value |
|---|---|
| Repository name | `remote-structural-collapse-lab` |
| GitHub Pages title | **Remote Structural Collapse Test Lab** |
| Short description | Safe remote-first collapse testing, sensor logging, Python analytics, and Blender simulation for model structures. |
| Visibility recommendation | Start private while developing; publish public only after reviewing all files for safety, privacy, and licensing. |
| Primary site page | `site/index.html` or GitHub Pages from `/docs` |

## Repository Purpose

This repository provides the project management backbone for a six-month collaboration. It includes a project plan, phase gates, management instructions, development workflow, data conventions, safe code subprojects, and a GitHub Pages landing page. The code subprojects are intentionally limited to **sensor logging, data analysis, file synchronization, and Blender import support**.

## Code Subprojects

| Subproject | Path | Purpose | Safety note |
|---|---|---|---|
| Sensor Logger Firmware | [`firmware/sensor_logger`](firmware/sensor_logger/) | Arduino-compatible serial logger for timestamped sensor output. | Logs data only; does not control ignition, pyrotechnics, or energetic devices. |
| Python Analytics | [`host-tools/analytics`](host-tools/analytics/) | Parses CSV sensor logs and produces plots and summary statistics. | Works from recorded data files. |
| Sync Helper | [`host-tools/sync`](host-tools/sync/) | Provides a template for syncing test artifacts to a VPS or shared server. | Uses placeholders and should be configured with private credentials outside Git. |
| Blender Importer | [`sim-models/blender-importer`](sim-models/blender-importer/) | Documents how to map processed data into Blender comparison scenes. | Simulation and visualization only. |

## Documentation Index

| Document | Description |
|---|---|
| [`docs/project-plan.md`](docs/project-plan.md) | Full six-month plan with Gantt chart, BOM, diagrams, roles, risks, and final event logistics. |
| [`docs/development-workflow.md`](docs/development-workflow.md) | Branching, versioning, release tags, known-good vectors, and code review rules. |
| [`docs/management-instructions.md`](docs/management-instructions.md) | Weekly management cadence, decision logs, roles, and meeting structure. |
| [`docs/phase-roadmap.md`](docs/phase-roadmap.md) | Phase-by-phase development path from bench logging through final simulation demo. |
| [`docs/safety-and-scope.md`](docs/safety-and-scope.md) | Repository scope, prohibited content, PPE, test-area rules, and go/no-go safety logic. |
| [`docs/data-schema.md`](docs/data-schema.md) | CSV and JSON formats for repeatable data capture. |
| [`docs/checklists/pre-test-checklist.md`](docs/checklists/pre-test-checklist.md) | Pre-test readiness checklist. |
| [`docs/phase-gates/`](docs/phase-gates/) | Review gate templates for each project phase. |

## Development and Management Model

The project uses a simple three-branch workflow. The `main` branch contains only reviewed and known-good documentation, code, CAD references, and data schemas. The `dev` branch integrates active work before release. Feature branches are named by area, such as `feature/phase2-tower-geometry`, `feature/analytics-parser`, or `feature/camera-sync-notes`.

Releases should use Semantic Versioning where practical. Semantic Versioning defines version numbers as `MAJOR.MINOR.PATCH`, where major changes indicate incompatible changes, minor changes add backward-compatible functionality, and patch changes fix backward-compatible defects.[1] GitHub releases are appropriate for this project because releases are based on Git tags that identify a specific point in repository history.[2]

## Six-Month Phase Summary

| Phase | Weeks | Development focus | Review gate outcome |
|---|---:|---|---|
| Phase 1 | 1–4 | Sensor logger, safe bench workflow, repository setup, data schema, safety checklist. | Ten consecutive dry-run data captures with complete logs. |
| Phase 2 | 5–9 | Simple printed structures, weak-point geometry, single-variable testing. | Repeatable collapse path documented in at least 8 of 10 comparable safe tests. |
| Phase 3 | 10–13 | Dual-camera observation, timestamp alignment, remote review workflow. | Wide and close camera views align with sensor logs. |
| Phase 4 | 14–18 | Automated data upload, Python analytics, Blender comparison workflow. | Raw data, plots, metadata, and simulation artifacts are reproducible. |
| Phase 5 | 19–26 | Integrated model city demonstration using safe mechanical collapse methods. | Final demonstration captured, analyzed, documented, and tagged as `v1.0.0`. |

## Quick Start

Clone the repository, review the scope document, and begin with Phase 1 only. Do not buy or build later-phase hardware until the prior review gate has passed.

```bash
git clone <your-repository-url>
cd remote-structural-collapse-lab
python3 -m venv .venv
source .venv/bin/activate
pip install -r host-tools/analytics/requirements.txt
python host-tools/analytics/analyze_sensor_log.py sensor-data/sample-data/sample_sensors.csv
```

## References

[1]: https://semver.org/ "Semantic Versioning 2.0.0"  
[2]: https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases "GitHub Docs: About releases"
