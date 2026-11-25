#!/usr/bin/env python3
"""Notes From a Passive-Aggressive Fridge entry: writes a single one-line
comedy joke to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

Stdlib only. The joke is a fixed, authored line: no network, no file reads
outside this repository, no randomness.
"""

import os
import sys

LINE = ("The cheese you swore you'd eat has outlived two relationships and "
        "a houseplant. I have given it a name. It answers to Gerald.")

MAX_CHARS = 200


def output_dir():
    env = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env:
        return env
    if os.path.isdir("/output"):
        return "/output"
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")


def main():
    line = LINE.strip()
    if not line:
        print("entry is empty", file=sys.stderr)
        return 1
    if len(line) > MAX_CHARS:
        print(f"entry is {len(line)} chars, over the {MAX_CHARS} limit",
              file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("entry must be a single line", file=sys.stderr)
        return 1
    outdir = output_dir()
    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")
    print(f"wrote {len(line)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
