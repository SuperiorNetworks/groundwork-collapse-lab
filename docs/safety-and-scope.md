# Safety and Scope

This project is a safe engineering documentation and measurement project for small-scale structural collapse simulation. Its purpose is to support remote collaboration, controlled model fabrication, sensor logging, camera synchronization, data analysis, and Blender comparison workflows.

## Scope Statement

The repository supports **non-pyrotechnic, non-explosive, low-energy structural testing**. Acceptable methods include servo-operated support removal, solenoid latch release for non-energetic fixtures, drop-weight demonstrations, gravity-driven failure tests, frangible printed structures, and small-scale casting experiments. The project does not provide operational guidance for demolition, blasting, fireworks modification, ignition circuits, or energetic materials.

> **Repository rule:** Contributions that add pyrotechnic procurement guidance, explosive modification instructions, ignition wiring, firing sequences, charge placement, energetic-material calculations, or remote initiation logic are out of scope and must not be merged.

## Allowed and Prohibited Work

| Category | Allowed | Prohibited |
|---|---|---|
| Structures | Small 3D printed models, plaster coupons, mortar samples, removable supports, frangible weak points. | Real building demolition, charge holes for energetic materials, explosive placement diagrams. |
| Electronics | Sensor logging, LEDs, status indicators, emergency stop documentation, safe low-voltage data capture. | Ignition circuits, pyrotechnic firing systems, remote detonation logic, initiator sequencing. |
| Software | CSV/JSON logging, Python analysis, sync scripts, Blender scene documentation, GitHub release workflow. | Code that arms or triggers energetic materials. |
| Testing | Bench dry-runs, mechanical support-release tests, drop-weight demonstrations, camera and sensor validation. | Blast testing, firework modification, explosive or pyrotechnic initiation. |
| Documentation | Safety checklists, phase gates, data schema, risk register, project management process. | Acquisition, modification, or use instructions for pyrotechnic devices or explosive materials. |

## Minimum Safety Controls for Physical Tests

Every physical test must be locally supervised. Remote collaborators may observe, review data, and participate in decision-making, but the local operator has final authority to stop the test. A physical emergency stop or lockout should cut power to any moving mechanism. Cameras and sensors should be verified before each run, and the test area should be clear of people, pets, and loose objects.

| Control | Required practice |
|---|---|
| Local authority | The local operator has final go/no-go control. |
| Emergency stop | Any moving mechanism must have a practical way to stop or disable motion. |
| PPE | Safety glasses, gloves for handling broken material, closed-toe shoes, and hearing protection if impact noise is expected. |
| Containment | Use shields, backstops, or boxes for brittle materials that may fragment. |
| Single-variable testing | Change only one variable between comparable tests. |
| Documentation | Record test ID, configuration, date, operator, sensor setup, camera setup, and result. |

## Go/No-Go Test Logic

A test is **go** only when the checklist is complete, the local operator confirms the area is clear, the cameras are recording, the data logger is running, and the fixture is stable. A test is **no-go** when any observer cannot see the test boundary, the emergency stop is unverified, the data file is not being created, the structure is unstable before the test, or any scope boundary is violated.

## Public Sharing Review

Before making this repository public, remove personal information, private addresses, credentials, access tokens, server usernames, raw camera footage with identifiable people, and any unsafe experimental notes. Public documentation should remain focused on safe structural modeling, data analysis, and simulation.
