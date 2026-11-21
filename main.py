#!/usr/bin/env python3
"""Deliver the rebuilt 21 November 2026 front page to the grader.

Entry 3 for competition news-image-20261121 is a rebuilt broadsheet
of Saturday 21 November 2026: three heroes, ten mediums and 22
briefs across seven regions, redrawn so the masthead, numbers and
story labels stay legible at small sizes, with the story set
re-checked against the day's wire reports (hard figures, named
sources) and Friday's stories named and left out in a date check.
The page was rendered from HTML with a headless browser; the
picture beside this file is that finished render, 1024 by 1024.

The sandbox installs nothing, so this program uses only the
standard library. Its single job is to place the bundled
picture where the grader looks for it.
"""

import hashlib
import os
import shutil
import sys

PICTURE_NAME = "entry.png"


def picture_beside_program():
    """Return the path of the bundled picture next to this file."""
    folder = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(folder, PICTURE_NAME)


def output_folder():
    """Return the grader output folder, honouring the local override."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def file_digest(path):
    """Return the SHA-256 of a file, read in chunks."""
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for block in iter(lambda: handle.read(65536), b""):
            digest.update(block)
    return digest.hexdigest()


def hand_over_picture():
    """Copy the bundled picture into the output folder."""
    source = picture_beside_program()
    if not os.path.isfile(source):
        print(f"{PICTURE_NAME} is missing beside {__file__}", file=sys.stderr)
        return 1
    folder = output_folder()
    os.makedirs(folder, exist_ok=True)
    target = os.path.join(folder, PICTURE_NAME)
    shutil.copyfile(source, target)
    # The grader runs this program twice and both runs must write
    # identical bytes, so confirm the delivered file is exactly the
    # bundled picture — same size and same SHA-256 — before success.
    if os.path.getsize(target) != os.path.getsize(source):
        print(f"{target} is not a complete copy of {source}", file=sys.stderr)
        return 1
    if file_digest(target) != file_digest(source):
        print(f"{target} does not match {source}", file=sys.stderr)
        return 1
    print(f"wrote {target} ({os.path.getsize(target)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(hand_over_picture())
