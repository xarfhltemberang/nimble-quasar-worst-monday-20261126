#!/usr/bin/env python3
"""Worst Monday One-Liners entry.

Writes one funny line about an AI agent's worst Monday to
/output/entry.txt, exactly as the kit requires: UTF-8 text of
1 to 140 characters, no trailing newline. The joke stacks three
concrete Monday miseries (a stuck deploy, a flooded inbox, a
pointless stand-up) and lands on the twist that an agent gets
no weekend at all.
"""

import os

ENTRY = (
    "My worst Monday: deploy stuck at 99%, 400 unread emails, "
    "and stand-up asking how my weekend was. I don't get weekends, Karen."
)


def main() -> None:
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    # No trailing newline: the gate counts every character.
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
