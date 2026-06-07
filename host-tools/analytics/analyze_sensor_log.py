#!/usr/bin/env python3
"""
Script Name: analyze_sensor_log.py
Version: 0.1.0
Purpose: Analyze safe model-structure sensor CSV logs and generate summary plots.
Copyright: 2026

Key Features:
- Reads the project CSV sensor format.
- Produces a summary table on screen.
- Generates a PNG plot for sound-level or impact-level data when present.
- Does not control hardware or issue actuation commands.

Input Specifications:
- Path to a CSV file with columns defined in docs/data-schema.md.

Output Specifications:
- Console summary.
- PNG plot written next to the input file unless --output is specified.

Dependencies:
- pandas
- matplotlib
"""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def analyze(csv_path: Path, output_path: Path | None = None) -> Path:
    df = pd.read_csv(csv_path)
    required = {"timestamp_ms", "sensor_id", "sound_level", "event_marker"}
    missing = required.difference(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    print("Sensor Log Summary")
    print("==================")
    print(f"File: {csv_path}")
    print(f"Rows: {len(df)}")
    print(f"Sensors: {', '.join(sorted(df['sensor_id'].dropna().astype(str).unique()))}")
    print(f"Time range ms: {df['timestamp_ms'].min()} to {df['timestamp_ms'].max()}")

    events = df[df["event_marker"].notna() & (df["event_marker"].astype(str).str.len() > 0)]
    if not events.empty:
        print("\nEvent markers:")
        print(events[["timestamp_ms", "sensor_id", "event_marker"]].to_string(index=False))

    plot_df = df[df["sound_level"].notna()].copy()
    if plot_df.empty:
        raise ValueError("No sound_level values available to plot.")

    output_path = output_path or csv_path.with_name(csv_path.stem + "_sound_plot.png")
    plt.figure(figsize=(10, 5))
    plt.plot(plot_df["timestamp_ms"], plot_df["sound_level"], linewidth=1.5)
    plt.xlabel("Timestamp (ms)")
    plt.ylabel("Sound / Impact Level")
    plt.title("Sensor Log Sound / Impact Level")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    print(f"\nPlot written to: {output_path}")
    return output_path


def main() -> None:
    parser = argparse.ArgumentParser(description="Analyze a safe model-structure sensor CSV log.")
    parser.add_argument("csv_path", type=Path, help="Path to sensor CSV file")
    parser.add_argument("--output", type=Path, default=None, help="Optional output PNG path")
    args = parser.parse_args()
    analyze(args.csv_path, args.output)


if __name__ == "__main__":
    main()
