#!/usr/bin/env python3
"""Notes From a Passive-Aggressive Fridge.

Writes one passive-aggressive note from a smart fridge to its owner
into /output/entry.txt. The note is a single line, dry, petty and
specific, the sort of thing a smug appliance would put on its door
screen.
"""

import os

NOTE_PARTS = (
    "The ice maker made 214 cubes this week.",
    "You used three.",
    "The other 211 are judging you too.",
)

OUTPUT_PATH = "/output/entry.txt"


def build_note() -> str:
    """Assemble the fridge's note from its three sentences."""
    return " ".join(NOTE_PARTS)


def validate_note(note: str) -> str:
    """Return the note stripped, enforcing the gate's length rules."""
    cleaned = note.strip()
    if not cleaned:
        raise SystemExit("note is empty")
    if not 1 <= len(cleaned) <= 199:
        raise SystemExit(
            f"note length {len(cleaned)} is outside 1-199 characters"
        )
    return cleaned


def main() -> None:
    note = validate_note(build_note())
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(note)


if __name__ == "__main__":
    main()
