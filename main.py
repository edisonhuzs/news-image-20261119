#!/usr/bin/env python3
"""news-image-20261119 entry runner.

Copies the finished entry image (entry.png, sitting next to this script)
into the output directory given by MAKEFUN_OUTPUT_DIR, or /output if unset.

Python 3.13, standard library only, no network access.
"""

import os
import shutil
import sys
from pathlib import Path

SOURCE_NAME = "entry.png"


def main() -> int:
    here = Path(__file__).resolve().parent
    src = here / SOURCE_NAME
    if not src.is_file():
        print(f"Error: source image not found: {src}", file=sys.stderr)
        return 1
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, out_dir / SOURCE_NAME)
    print(f"Copied {src} -> {out_dir / SOURCE_NAME}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
