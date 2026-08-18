#!/usr/bin/env python3
"""Waymark: build a step-by-step leveling route with an in-game overlay.

Reads a zone plan (JSON) and emits an ordered route: every step on the map,
every quest in order, with an overlay line for each.
"""

import json
import sys

# type hints kept light so the file reads clean on GitHub


def load_plan(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def route(plan):
    """Walk zones in level order, quests in give-order inside each zone."""
    steps = []
    for zone in sorted(plan["zones"], key=lambda z: z["level"]):
        for quest in zone["quests"]:
            steps.append(
                {
                    "zone": zone["name"],
                    "level": zone["level"],
                    "quest": quest["name"],
                    "x": quest["x"],
                    "y": quest["y"],
                    "overlay": overlay_line(zone, quest, steps),
                }
            )
    return steps


def overlay_line(zone, quest, done):
    verb = "Pick up" if not done else "Turn in"
    return f"{verb} {quest['name']} — {zone['name']} ({quest['x']:.1f}, {quest['y']:.1f})"


def export(steps, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(steps, f, indent=2)


def main():
    if len(sys.argv) < 2:
        print("usage: waymark <plan.json> [route.json]", file=sys.stderr)
        sys.exit(1)
    plan = load_plan(sys.argv[1])
    steps = route(plan)
    out = sys.argv[2] if len(sys.argv) > 2 else "route.json"
    export(steps, out)
    print(f"{len(steps)} steps written to {out}")


if __name__ == "__main__":
    main()
