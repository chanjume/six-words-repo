#!/usr/bin/env python3
"""Write one six-word story to /output/entry.txt.

The story: a man waits a lifetime for someone who never comes.
Two complete sentences, six words, thirty-four characters. The first
sentence holds a whole life of waiting; the second lands the turn.
Nothing is spelled out: who she is, why she never came, and what
he does next are left for the reader to fill in. Every word earns
its place -- drop any one and the story breaks.
"""
import os

STORY = "He waited decades. She never came."


def main():
    words = STORY.split()
    assert len(words) == 6, f"story must be exactly 6 words, got {len(words)}"
    assert 1 <= len(STORY) <= 60, "entry must be 1-60 characters"
    assert STORY.strip() == STORY, "no leading/trailing whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(STORY + "\n")


if __name__ == "__main__":
    main()
