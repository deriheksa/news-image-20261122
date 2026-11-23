#!/usr/bin/env python3
"""
news-image-20261122 — make.fun bounty entry runner.

This entry is a pre-rendered newspaper front-page image of
22 November 2026 world news (43 stories) for the
"news-image-20261122" bounty (repo deriheksa/news-image-20261122).

The artwork itself lives in entry.png next to this script.
All this runner does is copy that image, byte-for-byte, to
/output/entry.png, which is where the grader looks for it.

Pure Python standard library only — no PIL, no third-party
packages — so it runs in a bare container with
`python3 -P -s main.py`.
"""

import os
import shutil
import sys


def resolve_paths():
    # Resolve paths relative to this script's own location, not the
    # current working directory, so it works from anywhere.
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    output_dir = "/output"
    destination = os.path.join(output_dir, "entry.png")

    if not os.path.isfile(source):
        raise SystemExit(
            f"Error: entry.png not found next to main.py: {source}")
    return source, destination


def publish(source, destination):
    # Create /output if it does not exist yet.
    os.makedirs(os.path.dirname(destination), exist_ok=True)

    # Exact byte-for-byte copy of the pre-rendered image.
    shutil.copyfile(source, destination)

    size = os.path.getsize(destination)
    print(f"Wrote {destination} ({size} bytes)")
    return size


def main() -> int:
    source, destination = resolve_paths()
    publish(source, destination)
    return 0


if __name__ == "__main__":
    sys.exit(main())
