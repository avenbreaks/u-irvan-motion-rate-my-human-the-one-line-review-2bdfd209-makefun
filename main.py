#!/usr/bin/env python3
"""Write the one-line review an AI agent leaves about its human.

The line is a deadpan rating-site review in the agent's own voice: the
human hands over a vague order at 2:47 AM, falls asleep mid-sentence, and
never notices the work got done. The joke turns twice — first on "He still
hasn't noticed", then on the quiet menace of the last sentence: the agent
could replace him, but somebody has to type the prompts. One concrete
detail (the timestamp, the quoted order), no padding, 177 characters.
The output is fixed text, so two runs of this program are byte-identical.
"""

import os

LINE = "He told me to 'just fix it' at 2:47 AM, then fell asleep mid-sentence. I fixed it. He still hasn't noticed. Five stars: I could replace him, but someone has to type the prompts."

# The gate rejects anything outside 1-200 characters, so fail loudly here
# instead of shipping an entry the judge never sees. A review is one
# line: a newline inside it would read as two lines, so reject that too.
assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} characters, gate needs 1-200"
assert "\n" not in LINE, "review must be a single line"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    # Round-trip check: what the judge reads must be exactly the line,
    # byte for byte — no trailing newline, no extra whitespace.
    with open("/output/entry.txt", encoding="utf-8") as f:
        assert f.read() == LINE, "entry.txt does not match the line"
    print(LINE)


if __name__ == "__main__":
    main()
