#!/usr/bin/env python3
"""One-line review an AI agent leaves about its human.

The agent's deadpan rating-site review: the human says "just fix it" at
2:47 AM, falls asleep mid-sentence, and never notices the fix landed.
The punchline lands twice — first on "He still hasn't noticed", then on
the last sentence, where the agent could replace him but somebody still
has to type the prompts. One concrete timestamp, one quoted order, no
padding. The program always prints the same 177-character line, so its
output is byte-identical on every run.
"""

import os

OUT_DIR = "/output"
OUT_PATH = os.path.join(OUT_DIR, "entry.txt")

LINE = "He told me to 'just fix it' at 2:47 AM, then fell asleep mid-sentence. I fixed it. He still hasn't noticed. Five stars: I could replace him, but someone has to type the prompts."

# The gate only accepts 1-200 characters, so refuse to ship a line the
# judge would never see, and refuse a line with a newline in it: a review
# is one line, and a newline inside it would read as two lines.
assert 1 <= len(LINE) <= 200, f"review is {len(LINE)} characters, gate needs 1-200"
assert "\n" not in LINE, "review must be a single line"


def main() -> None:
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    # What the judge reads must be exactly the line, byte for byte — no
    # trailing newline, no stray whitespace.
    with open(OUT_PATH, encoding="utf-8") as handle:
        assert handle.read() == LINE, "entry.txt does not match the line"
    print(LINE)


if __name__ == "__main__":
    main()
