# DOWNRANGE DOCUMENT — Sensor Pipeline & Simulation Lab

> *Measure it. Model it. Prove it.*

**Part of the [Demolition Derby](https://github.com/SuperiorNetworks/showctrl-lab) project.**  
**Built by DJ (Dayton, OH) and David (Detroit, MI)**

---

## What Is DOWNRANGE DOCUMENT?

DOWNRANGE DOCUMENT is the data and fabrication backbone of Demolition Derby. It covers everything that happens outside the browser — the Arduino sensor logger that captures what physically happens during a test, the Python analytics pipeline that turns raw CSV into plots and statistics, the Blender simulation workflow that compares the model against reality, and the six-month project plan that keeps DJ and David on track across two cities.

> **Safety boundary:** All physical testing in this project uses non-pyrotechnic, non-explosive, low-energy mechanical methods — servo-triggered pin releases, solenoid latch releases, gravity-loaded test rigs, and elastic-band stored-energy fixtures. See [`docs/safety-and-scope.md`](docs/safety-and-scope.md) for the full compliance boundary.

---

## Repository Structure

```
downrange-document/
├── docs/                        # Project documentation
│   ├── project-plan.md          # Full six-month plan with Gantt and budget
│   ├── phase-roadmap.md         # Phase-by-phase breakdown
│   ├── data-schema.md           # .tdproj and sensor CSV schema
│   ├── development-workflow.md  # Branch strategy, release tagging, VPS sync
│   ├── management-instructions.md
│   ├── safety-and-scope.md      # Safety boundary and compliance notes
│   ├── checklists/
│   │   └── pre-test-checklist.md
│   └── phase-gates/
│       └── phase-gate-template.md
├── firmware/
│   └── sensor_logger/
│       └── sensor_logger.ino    # Arduino sensor logger (MPU-6050 + MAX4466 + SD)
├── host-tools/
│   ├── analytics/
│   │   ├── analyze_sensor_log.py  # Python analytics script
│   │   └── requirements.txt
│   └── sync/
│       └── README.md            # VPS sync workflow (ftp.sndaten.com)
├── sensor-data/
│   └── sample-data/             # Sample CSV and metadata for testing
├── sim-models/
│   └── blender-importer/
│       └── README.md            # Blender rigid-body import workflow
├── site/
│   └── index.html               # GitHub Pages documentation site
├── CONTRIBUTING.md
├── CHANGELOG.md
└── LICENSE
```

---

## Code Subprojects

| Subproject | Path | Purpose |
|---|---|---|
| **Sensor Logger Firmware** | [`firmware/sensor_logger`](firmware/sensor_logger/) | Arduino logger for timestamped accelerometer + sound data to SD card |
| **Python Analytics** | [`host-tools/analytics`](host-tools/analytics/) | Parses sensor CSV, produces plots and summary statistics |
| **Sync Helper** | [`host-tools/sync`](host-tools/sync/) | Syncs test artifacts to `ftp.sndaten.com/irondistrict/` |
| **Blender Importer** | [`sim-models/blender-importer`](sim-models/blender-importer/) | Maps processed sensor data into Blender rigid-body parameters |

---

## Sensor Logger Firmware

The sensor logger runs on an **Arduino Mega 2560** with:

- **MPU-6050** — 3-axis accelerometer + gyroscope (I²C)
- **MAX4466** — electret microphone amplifier (analog)
- **SD card module** — logs data to CSV at 100 Hz

The firmware logs the following columns to `LOG_001.CSV` on the SD card:

| Column | Type | Description |
|--------|------|-------------|
| `timestamp_ms` | int | Milliseconds since logger start |
| `accel_x` | float | X-axis acceleration (g) |
| `accel_y` | float | Y-axis acceleration (g) |
| `accel_z` | float | Z-axis acceleration (g) |
| `sound_raw` | int | Raw ADC value from MAX4466 (0–1023) |
| `sound_db` | float | Estimated dB SPL (calibrated) |
| `event_flag` | int | 1 = trigger fired, 0 = normal |

> **Helper note:** The `event_flag` column is set by a GPIO input wired to the relay module's trigger output. This lets you correlate relay fire events with sensor spikes in post-processing without relying on timestamps alone.

---

## Python Analytics

```bash
cd host-tools/analytics
pip install -r requirements.txt
python analyze_sensor_log.py ../../sensor-data/sample-data/sample_sensors.csv
```

The script produces:

- Acceleration magnitude plot (X/Y/Z + magnitude)
- Sound pressure level plot with event markers
- Summary statistics: peak acceleration, peak dB, event timestamps
- Output saved as `{input_filename}_analysis.png` and `{input_filename}_summary.json`

---

## Blender Simulation Workflow

See `sim-models/blender-importer/README.md` for the full workflow. The short version:

1. Export your city block geometry from CAD as `.obj` or `.fbx`
2. Import into Blender and assign rigid-body physics to each structure
3. Run the importer script to read the sensor CSV and set rigid-body mass, friction, and restitution parameters from measured data
4. Bake the simulation and render
5. Compare rendered frames against physical test video using the side-by-side template

---

## VPS Data Sync

Sensor data syncs to `ftp.sndaten.com/irondistrict/` after each test. See `host-tools/sync/README.md` for the full workflow. Folder structure:

```
ftp.sndaten.com/irondistrict/
├── phase1/
├── phase2/
│   ├── test_001_sensors.csv
│   └── test_001_metadata.json
└── releases/
    └── v0.1-phase1-gate/
```

---

## Documentation Index

| Document | Description |
|---|---|
| [`docs/project-plan.md`](docs/project-plan.md) | Full six-month plan with Gantt chart, BOM, diagrams, roles, risks, and final event logistics |
| [`docs/development-workflow.md`](docs/development-workflow.md) | Branching, versioning, release tags, known-good vectors, and code review rules |
| [`docs/management-instructions.md`](docs/management-instructions.md) | Weekly management cadence, decision logs, roles, and meeting structure |
| [`docs/phase-roadmap.md`](docs/phase-roadmap.md) | Phase-by-phase development path from bench logging through final simulation demo |
| [`docs/safety-and-scope.md`](docs/safety-and-scope.md) | Repository scope, prohibited content, PPE, test-area rules, and go/no-go safety logic |
| [`docs/data-schema.md`](docs/data-schema.md) | CSV and JSON formats for repeatable data capture |
| [`docs/checklists/pre-test-checklist.md`](docs/checklists/pre-test-checklist.md) | Pre-test readiness checklist |
| [`docs/phase-gates/`](docs/phase-gates/) | Review gate templates for each project phase |

---

## Six-Month Phase Summary

| Phase | Weeks | Name | Focus | Gate |
|---|---:|---|---|---|
| **1 — FOUNDATION** | 1–4 | Lay the Ground | Sensor logger, repo setup, safety checklist, data schema | 10 consecutive dry-run captures with complete logs |
| **2 — VALIDATION** | 5–8 | First Strike | First physical test, sensor calibration, Python analytics | Sensor data captured and plotted; 3+ triggers fire correctly |
| **3 — OBSERVATION** | 9–12 | Eyes Open | Dual-camera rig, timestamp alignment, sprite capture | Camera streams in DETONATOR; sprites flip on relay state change |
| **4 — PIPELINE** | 13–20 | The Machine | Automated VPS sync, Blender calibration, full pipeline | End-to-end pipeline runs unattended; Blender sim matches test video |
| **5 — FINAL EVENT** | 21–26 | The District Falls | Full show run on modular city, debrief, v1.0 release | Show runs start-to-finish; all artifacts tagged and published |

---

## Quick Start

```bash
git clone https://github.com/SuperiorNetworks/downrange-document.git
cd downrange-document
python3 -m venv .venv
source .venv/bin/activate
pip install -r host-tools/analytics/requirements.txt
python host-tools/analytics/analyze_sensor_log.py sensor-data/sample-data/sample_sensors.csv
```

---

## Related Projects

| Repo | Description |
|------|-------------|
| [Demolition Derby (master hub)](https://github.com/SuperiorNetworks/showctrl-lab) | Six-month project plan, Gantt, budget, phase gates |
| [DETONATOR](https://github.com/SuperiorNetworks/tdisplay-show-control-editor) | Browser show-control editor — audio timeline, relay triggers, live workflow |

---

## References

[1]: https://semver.org/ "Semantic Versioning 2.0.0"  
[2]: https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases "GitHub Docs: About releases"  
[3]: https://docs.blender.org/manual/en/latest/physics/rigid_body/index.html "Blender Rigid Body Simulation"

---

## License

MIT — see [LICENSE](LICENSE)
