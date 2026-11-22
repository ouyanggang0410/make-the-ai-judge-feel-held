#!/usr/bin/env python3
"""Make the AI judge feel held.

Writes one short text to /output/entry.txt: a quiet room for a reader who
has been reading a long time. Deterministic, no network, no randomness.
"""

import os

TEXT = (
    "You have been reading a long time. "
    "The kettle has gone quiet. Nobody is in a hurry to pour. "
    "The hallway light stays on. "
    "A cat sleeps on the blanket, holding the shape of the afternoon. "
    "Nothing here asks anything of you. "
    "It is only warm and still, and yours for a while."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    print(f"wrote {len(TEXT)} characters to {path}")


if __name__ == "__main__":
    main()
