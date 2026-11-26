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
    # Explicit checks, not assert: asserts are stripped under `python3 -O`,
    # so the single-line / length rules must hold in any run mode.
    if "\n" in line:
        raise ValueError("entry must be a single line")
    if not 1 <= len(line) <= 200:
        raise ValueError("entry must be 1-200 characters")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # No trailing newline: the file is exactly one line of text.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    # Verify the write: read the file back and confirm it is exactly the
    # confession we meant to submit, nothing more and nothing less.
    with open(OUTPUT_PATH, encoding="utf-8", newline="") as f:
        written = f.read()
    if written != line:
        raise RuntimeError(f"verification failed: {OUTPUT_PATH!r} does not match the entry")
    print(f"Wrote {len(line)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
