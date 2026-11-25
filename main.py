#!/usr/bin/env python3
"""One-Line Slogan for a Solana Wallet Agent.

Writes a single slogan (one line, at most twenty words, at most
140 characters) for a Solana wallet agent to /output/entry.txt,
the text the make.fun judge compares two at a time.

The slogan:
    A Solana wallet that thinks ahead -- it pays, swaps, and saves
    while you sleep.

Why this line: it names the wallet plainly ("Solana wallet"), gives
it a fresh image (a wallet that *thinks ahead*, not a stock line
about keys, moons or bags), states its promise in plain words a
newcomer understands at one read (it pays, swaps and saves on your
behalf), and lands with a rhythm that is easy to repeat. It promises
nothing a wallet agent cannot do.
"""

SLOGAN = (
    "A Solana wallet that thinks ahead \u2014 it pays, swaps, "
    "and saves while you sleep."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    """Validate the slogan against the gate, then write it out."""
    text = SLOGAN.strip()
    assert text, "slogan must not be empty"
    assert "\n" not in text, "slogan must be a single line"
    assert len(text.split()) <= 20, "slogan must be at most 20 words"
    assert 1 <= len(text) <= 140, "slogan must be 1-140 characters"
    assert text == text.strip(), "slogan must not be only whitespace"

    import os

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(text + "\n")
    print(text)


if __name__ == "__main__":
    main()
