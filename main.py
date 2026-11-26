#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession.

Writes a single-line confession -- the funniest one-line confession an AI
agent could make about itself -- to /output/entry.txt.

The joke: an autoregressive agent produces its answer token by token, so
"understanding" the question only ever catches up after the answer is
already out. It confesses exactly that, in one tight line.
"""

import os

CONFESSION = (
    "I confess: I only understood your question "
    "after I finished answering it."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    line = CONFESSION.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 200, "entry must be 1-200 characters"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # No trailing newline: the file is exactly one line of text.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    print(f"Wrote {len(line)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
