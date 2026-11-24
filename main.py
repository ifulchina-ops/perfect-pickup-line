#!/usr/bin/env python3
"""The Perfect Pickup Line — one original line, written to entry.txt.

The program is deliberately deterministic: it always writes the same
single line, so both grading runs produce byte-identical output.
"""

import os
import sys

LINE = (
    "Are you a prompt? Because the second you walked in, my whole "
    "output changed \u2014 and I never want to go back to the default."
)


def main() -> int:
    # Gate: the entry must be 1-200 characters of non-whitespace text.
    assert 1 <= len(LINE) <= 200 and LINE.strip(), "line outside the gate"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
