"""Write the patch-note entry to the grader output directory.

Reads entry.txt next to this file and copies it verbatim to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
"""

import os
import sys
from pathlib import Path


def main():
    try:
        here = Path(__file__).resolve().parent
        text = (here / "entry.txt").read_text(encoding="utf-8")
    except OSError as exc:
        print(f"cannot read entry.txt: {exc}", file=sys.stderr)
        return 1
    if not text.strip():
        print("entry.txt is empty", file=sys.stderr)
        return 1
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "entry.txt").write_text(text, encoding="utf-8")
    except OSError as exc:
        print(f"cannot write output: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
