#!/usr/bin/env python3
"""The Meeting That Should Have Been an Email.

Writes the entry - one single-line joke about a meeting that should have
been an email - to /output/entry.txt. Standard library only, fully
deterministic: the same line is written on every run.
"""

import os

ENTRY = (
    "We spent 45 minutes in a meeting reading the email aloud, "
    "then emailed everyone a summary of the meeting about the email "
    "they already read."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert all(ord(c) < 128 for c in ENTRY), "entry must be plain ASCII"
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    directory = os.path.dirname(out_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
