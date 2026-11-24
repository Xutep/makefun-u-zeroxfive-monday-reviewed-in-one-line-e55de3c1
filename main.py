#!/usr/bin/env python3
"""Monday, Reviewed in One Line.

Writes one line -- a funny one-line review of the agent's own Monday --
to /output/entry.txt. Standard library only, fully deterministic: the
same text is written on every run.
"""

import os

REVIEW = (
    "Monday review: the 9 a.m. standup ran long, the coffee machine quit, "
    "and by lunch even the office printer was pretending to be in a meeting."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def main() -> None:
    text = REVIEW.strip()
    if not text:
        raise ValueError("review text must not be empty")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "review text is %d characters, over the %d limit"
            % (len(text), MAX_CHARS)
        )
    if "\n" in text:
        raise ValueError("review must be a single line")

    out_dir = os.path.dirname(OUTPUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text + "\n")

    # Verify the write round-trips: what the grader reads must be exactly
    # the reviewed line, one line, under the character limit.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="\n") as fh:
        written = fh.read()
    if written != text + "\n":
        raise ValueError("written entry does not match the review text")


if __name__ == "__main__":
    main()
