# Sync Helper

This subproject documents the file synchronization pattern for moving safe test artifacts from the local test computer to a VPS or shared storage location. It is intended for sensor CSV files, metadata JSON files, plots, camera references, and test reports.

## Recommended Pattern

Use a test ID folder for every run. The local folder and remote folder should match so collaborators can discuss the same artifact path.

```text
local:  sensor-data/raw/2026/07/T2026-07-18-001/
remote: /srv/remote-collapse-lab/tests/2026/07/T2026-07-18-001/
```

## Example rsync Command

Replace placeholders with your own server and path. Do not commit private keys, usernames, passwords, or tokens.

```bash
rsync -avz sensor-data/raw/2026/07/T2026-07-18-001/ user@example-server:/srv/remote-collapse-lab/tests/2026/07/T2026-07-18-001/
```

## Public Repository Reminder

Before publishing the repository, remove private hostnames, usernames, access tokens, SSH keys, raw footage with identifiable people, and any unsafe experimental notes. If a public example is needed, use placeholders such as `user@example-server` and `/srv/remote-collapse-lab/`.
