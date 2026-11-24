#!/usr/bin/env python3
"""Say What Actually Broke — one line of honest error copy.

The entry is a single fixed string: the program writes it to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt) with no trailing
newline, so the gate reads exactly one line of at most 200 characters.

The line names the real failure in plain words with the exact numbers
(a 2 GB file against a 25 MB limit), tells the user what to do next
(shrink it and retry), and lands the joke in four words — "Math, not
malice" — a twist a reader can repeat out loud to a colleague.
Iteration round: v1 said "Your file is 2 GB; our limit is 25 MB."
v2 tightens it to one clause — "Your 2 GB file met our 25 MB limit."
— one byte shorter, and "met" gives the collision a small comic image
without adding a word.
"""

import os

LINE = "Your 2 GB file met our 25 MB limit. Math, not malice. Shrink it and retry."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
