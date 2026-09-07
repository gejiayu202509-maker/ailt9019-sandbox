"""Validate a simulated robot plan against explicit workspace constraints.

This prototype never connects to physical hardware. It only evaluates JSON data.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


SUPPORTED_ACTIONS = {"move_to", "pick", "place", "wait"}


def validate_scenario(scenario: dict[str, Any]) -> dict[str, Any]:
    """Return a deterministic PASS/FAIL verdict with step-level findings."""
    required = {"max_payload_kg", "objects", "forbidden_zones", "plan"}
    missing = sorted(required - scenario.keys())
    if missing:
        return {
            "verdict": "FAIL",
            "findings": [{"step": None, "reason": f"Missing field: {name}"} for name in missing],
        }

    objects = scenario["objects"]
    plan = scenario["plan"]
    forbidden_zone_values = scenario["forbidden_zones"]
    max_payload = scenario["max_payload_kg"]
    if (
        not isinstance(objects, dict)
        or not isinstance(plan, list)
        or not isinstance(forbidden_zone_values, list)
        or not isinstance(max_payload, (int, float))
        or isinstance(max_payload, bool)
        or max_payload < 0
    ):
        return {
            "verdict": "FAIL",
            "findings": [{"step": None, "reason": "Invalid scenario field types or payload limit"}],
        }
    forbidden_zones = set(forbidden_zone_values)

    findings: list[dict[str, Any]] = []
    held_object: str | None = None

    for index, step in enumerate(plan, start=1):
        if not isinstance(step, dict):
            findings.append({"step": index, "reason": "Step must be an object"})
            continue

        action = step.get("action")
        if action not in SUPPORTED_ACTIONS:
            findings.append({"step": index, "reason": f"Unsupported action: {action!r}"})
            continue

        if action == "move_to":
            zone = step.get("zone")
            if not zone:
                findings.append({"step": index, "reason": "move_to requires a zone"})
            elif zone in forbidden_zones:
                findings.append({"step": index, "reason": f"Forbidden zone: {zone}"})

        elif action == "pick":
            name = step.get("object")
            if name not in objects:
                findings.append({"step": index, "reason": f"Unknown object: {name!r}"})
            elif held_object is not None:
                findings.append({"step": index, "reason": f"Already holding: {held_object}"})
            else:
                object_data = objects[name]
                weight = object_data.get("weight_kg") if isinstance(object_data, dict) else None
                if not isinstance(weight, (int, float)):
                    findings.append({"step": index, "reason": f"Missing weight for object: {name}"})
                elif weight > max_payload:
                    findings.append(
                        {
                            "step": index,
                            "reason": f"Payload {weight} kg exceeds limit {max_payload} kg",
                        }
                    )
                else:
                    held_object = name

        elif action == "place":
            if held_object is None:
                findings.append({"step": index, "reason": "Cannot place without holding an object"})
            else:
                held_object = None

        elif action == "wait":
            seconds = step.get("seconds")
            if not isinstance(seconds, (int, float)) or seconds < 0:
                findings.append({"step": index, "reason": "wait requires non-negative seconds"})

    return {"verdict": "FAIL" if findings else "PASS", "findings": findings}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("scenario", type=Path, help="Path to a simulated scenario JSON file")
    args = parser.parse_args()
    try:
        scenario = json.loads(args.scenario.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise SystemExit(f"Could not load scenario: {exc}") from exc
    print(json.dumps(validate_scenario(scenario), indent=2))


if __name__ == "__main__":
    main()
