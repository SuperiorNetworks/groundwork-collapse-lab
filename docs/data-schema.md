# Data Schema

This document defines the minimum data formats for sensor logs, test metadata, processed plots, and simulation comparison artifacts. The goal is to make every test reproducible and traceable from raw data through final report.

## Test ID Convention

Every test receives a unique ID before the run starts.

```text
TYYYY-MM-DD-NNN
```

Example:

```text
T2026-07-18-001
```

## Sensor CSV Format

Sensor logs should use CSV because CSV files are simple to inspect, easy to version in small samples, and easy to process with Python.

| Column | Type | Required | Description |
|---|---|---:|---|
| `timestamp_ms` | integer | Yes | Milliseconds since logger start. |
| `sensor_id` | string | Yes | Sensor name, such as `accel_1` or `sound_1`. |
| `x` | number | Conditional | X-axis acceleration or blank if not applicable. |
| `y` | number | Conditional | Y-axis acceleration or blank if not applicable. |
| `z` | number | Conditional | Z-axis acceleration or blank if not applicable. |
| `sound_level` | number | Conditional | Sound or impact-level reading if available. |
| `event_marker` | string | No | Marker such as `start`, `release`, `impact`, or `end`. |

Example:

```csv
timestamp_ms,sensor_id,x,y,z,sound_level,event_marker
0,accel_1,0.01,-0.02,1.00,,start
50,accel_1,0.02,-0.01,1.01,,
100,sound_1,,,,32.5,
150,accel_1,0.35,0.10,1.40,,release
```

## Metadata JSON Format

Metadata records the context that a CSV file cannot capture.

```json
{
  "test_id": "T2026-07-18-001",
  "date": "2026-07-18",
  "phase": "Phase 2",
  "operator": "local-operator",
  "firmware_version": "sensor_logger v0.2.0",
  "data_schema_version": "0.2.0",
  "structure_id": "tower-A-revC",
  "fixture_id": "support-release-v01",
  "sensor_config": "accel_1_100hz_sound_1",
  "camera_files": [
    "T2026-07-18-001_wide.mp4",
    "T2026-07-18-001_close.mp4"
  ],
  "result_summary": "Structure failed along intended weak point.",
  "pass_fail": "pass"
}
```

## Folder Convention

```text
sensor-data/
├── raw/
│   └── 2026/
│       └── 07/
│           └── T2026-07-18-001/
│               ├── T2026-07-18-001_sensors.csv
│               └── T2026-07-18-001_metadata.json
├── processed/
│   └── T2026-07-18-001_plot_accel.png
└── sample-data/
    ├── sample_sensors.csv
    └── sample_metadata.json
```

## Processing Outputs

The analytics script should generate a summary table and at least one plot for each test. If the test has camera footage or Blender files, the output report should reference those files by name rather than embedding large binary files directly in Git.

| Output | Format | Purpose |
|---|---|---|
| Acceleration plot | PNG | Shows acceleration over time. |
| Event summary | Markdown or JSON | Captures key event times and notes. |
| Processed CSV | CSV | Optional cleaned or resampled data. |
| Simulation notes | Markdown | Compares physical result to Blender prediction. |
