# Blender Importer Notes

This subproject documents how measured data should be connected to Blender comparison scenes. It is intentionally documentation-first so the team can agree on a repeatable workflow before adding automation.

## Purpose

The Blender workflow should compare observed model-structure behavior with a simplified rigid-body or visual simulation. It should not be treated as a validated structural engineering or demolition model. It is a learning and visualization tool for comparing predicted weak-point behavior, event timing, and final collapse shape.

## Suggested Workflow

| Step | Input | Output |
|---|---|---|
| 1 | Test metadata JSON | Scene notes and object naming convention. |
| 2 | CAD export or simplified geometry | Blender model with named structure components. |
| 3 | Sensor CSV | Event markers and timing references. |
| 4 | Camera footage | Visual comparison of actual collapse path. |
| 5 | Blender scene | Rendered comparison stills or animation. |

## Naming Convention

```text
T2026-07-18-001_compare.blend
T2026-07-18-001_render_frame_001.png
T2026-07-18-001_sim_notes.md
```

## Minimum Simulation Notes

Each comparison should record the physical test ID, CAD revision, approximate object masses if known, weak-point assumptions, observed failure path, simulated failure path, and whether the comparison helped improve the next test.
