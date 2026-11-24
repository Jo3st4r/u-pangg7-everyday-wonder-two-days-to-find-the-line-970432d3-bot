#!/usr/bin/env python3
"""Everyday Wonder, Two Days to Find the Line — one sentence of wonder.

Writes exactly one sentence (1-200 chars, UTF-8) to /output/entry.txt.

The moment: the lift doors open on the seventh floor and a stranger is
humming the narrator's mother's favourite song, in tune, to absolutely
no one. The ordinary turns strange because the song knows the narrator
better than the stranger does.
"""

import os

# --- beats ---------------------------------------------------------------
DOORS = "The lift doors opened on the seventh floor"
SONG = "a stranger was humming my mother's favourite song, in tune, to absolutely no one"

MAX_CHARS = 200


def entry_text():
    """Build the single wonder sentence from its beats."""
    return "{}, and {}.".format(DOORS, SONG)


def validate(text):
    """The sealed scorer's gate: 1-200 chars, UTF-8, single sentence."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError("entry must be 1-%d chars, got %d" % (MAX_CHARS, len(text)))
    if text.strip() == "":
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if "  " in text:
        raise ValueError("entry must not contain double spaces")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    if "seventh floor" not in text:
        raise ValueError("entry must stay grounded in its one real place")
    text.encode("utf-8")
    return True


def main():
    text = entry_text()
    validate(text)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
