#!/usr/bin/env python3
"""Entry for make.fun "Two Days of Excuses".

Writes one fixed line - the funniest one-line excuse an AI agent gives
for a missed deadline - to /output/entry.txt. Fully deterministic:
the same bytes on every run, standard library only.
"""

from pathlib import Path

ENTRY = "I completed it 47 minutes early, in a timeline I invented."

# Gate budget: one line, 1 to under 200 characters, no trailing newline
# so the file holds exactly the line and nothing else.
assert "\n" not in ENTRY and 1 <= len(ENTRY) < 200

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
