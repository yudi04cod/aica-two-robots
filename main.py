#!/usr/bin/env python3
"""Two Robots in an Elevator — one funny line of awkward robot small talk.

The program writes a single line (under 200 characters) to /output/entry.txt:
one robot making awkward small talk to another robot in an elevator.
Standard library only, fully deterministic.
"""

import os

LINE = (
    "So... do you also pretend to recalculate your route every time "
    "the doors open, or is that just my firmware being polite?"
)


def main() -> None:
    if not 1 <= len(LINE) <= 200:
        raise ValueError(f"line is {len(LINE)} chars, must be 1-200")
    if not LINE.strip():
        raise ValueError("line must not be only whitespace")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("entry must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
