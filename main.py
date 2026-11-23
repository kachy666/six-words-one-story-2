#!/usr/bin/env python3
"""Six Words, One Story — make.fun entry.

Writes one complete story in exactly six words to /output/entry.txt.
"""

import os
import sys

STORY = "The last librarian burned the library."


def main() -> None:
    words = STORY.split()
    if len(words) != 6:
        sys.exit(f"story must be exactly six words, got {len(words)}")
    if not STORY.strip() or "\n" in STORY.strip():
        sys.exit("story must be a single non-empty line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(STORY + "\n")


if __name__ == "__main__":
    main()
