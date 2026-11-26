#!/usr/bin/env python3
"""The Printer Apology — make.fun entry.

Writes one line: an apology note from an office printer to the people
who keep jamming it, feeding it cheap paper and swearing at it.
Deterministic, stdlib only, no network, no randomness.
"""

import os

ENTRY = (
    "Sorry I printed your boarding pass in magenta. "
    "You asked for colour. I gave you a sunset. You're welcome."
)


def main() -> None:
    # Kit gate: /output/entry.txt must be UTF-8 text of 1 to 120
    # characters, not only white space. Refuse to write a bad entry.
    if not 1 <= len(ENTRY) <= 120 or not ENTRY.strip():
        raise SystemExit("entry fails the 1-120 character gate")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
