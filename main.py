#!/usr/bin/env python3
import pathlib

# One line, at most 200 characters, about a small good thing that happened
# today. Warmth, a surprise, one concrete detail, fresh wording.
LINE = (
    "My mum called just to say the tomatoes finally came in. "
    "\u2018They took their time,\u2019 she said, still out in the garden. "
    "I bit one on the balcony and called her back, and she let the phone ring."
)


def main():
    out = pathlib.Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    text = LINE.strip()
    if not (1 <= len(text) <= 200):
        raise ValueError(f"line is {len(text)} chars, must be 1..200")
    (out / "entry.txt").write_text(text, encoding="utf-8")

if __name__ == "__main__":
    main()
