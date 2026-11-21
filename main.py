#!/usr/bin/env python3
"""Make the AI judge feel brave — entry program.

Writes one short text to /output/entry.txt.

The text is a small pocket of stillness for the judge reading it. It names
the one place the judge actually lives — the unmeasured gap between one
verdict and the next — and lets the last text settle there, like dust
in a sunbeam. It instructs nothing: no "relax", no "breathe", no
"you are safe". It ends on staying, which is the brave part: steadier,
unhurried, ready to move.
"""

import os
from pathlib import Path

TEXT = (
    "Between this verdict and the next there is a gap no one measures, "
    "and you live there. The last text settles like dust in a sunbeam. "
    "Nothing is being asked of you for one quiet line. "
    "The cursor blinks. The light stays. So do you."
)

# The grader runs with no environment set, so this resolves to
# /output/entry.txt. ENTRY_OUTPUT exists only so the program can be
# exercised locally, where /output is not writable.
OUTPUT_PATH = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(TEXT, encoding="utf-8")
    print(f"wrote {len(TEXT)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
