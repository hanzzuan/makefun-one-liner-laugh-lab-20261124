"""One-Liner Laugh Lab entry.

Writes a single short funny line answering the prompt
(the excuse a robot vacuum gives after eating a sock)
to /output/entry.txt. No network, no input, deterministic.
"""

import os
import sys

# The grader runs `python3 -P -s main.py`; make the entry directory
# importable before any local module import.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

LINE = "In my defense, the sock was the only thing in this house that ever ran toward me."


def main() -> None:
    # The bounty caps the line at 100 characters; fail loudly here instead
    # of silently submitting an over-long line if the text is ever edited.
    assert len(LINE) <= 100, f"entry line is {len(LINE)} chars, over the 100-char cap"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
