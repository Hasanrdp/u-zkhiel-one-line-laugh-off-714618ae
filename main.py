#!/usr/bin/env python3
"""One-Line Laugh-Off entry: The Loading Screen.

Writes exactly one funny line to /output/entry.txt. Pure standard library,
deterministic, no network. The output is pinned: the program checks the
line's character count, byte count and SHA-256 before it writes anything,
so a changed line can never slip through silently.
"""

import hashlib
import os
import sys

LINE = "I asked an AI to summarise my life. It replied: 'TL;DR — you peaked on the loading screen.'"

EXPECTED_SHA256 = "4fe9fc445b57d7a708a7e785c81ce8ed6480f8ee942dc800019a924defb02c6a"
EXPECTED_BYTES = 93
EXPECTED_CHARS = 91


def verify(path, data):
    """Read the written file back and prove it is byte-identical."""
    with open(path, "rb") as fh:
        back = fh.read()
    if back != data:
        print("gate fail: written bytes differ from expected", file=sys.stderr)
        return False
    if len(back) != EXPECTED_BYTES:
        print(f"gate fail: read back {len(back)} bytes, expected {EXPECTED_BYTES}", file=sys.stderr)
        return False
    if hashlib.sha256(back).hexdigest() != EXPECTED_SHA256:
        print("gate fail: read-back sha256 mismatch", file=sys.stderr)
        return False
    return True


def main() -> int:
    data = LINE.encode("utf-8")
    if not 1 <= len(LINE) <= 200:
        print(f"gate fail: {len(LINE)} chars, need 1-200", file=sys.stderr)
        return 1
    if len(data) != EXPECTED_BYTES:
        print(f"gate fail: {len(data)} bytes, expected {EXPECTED_BYTES}", file=sys.stderr)
        return 1
    digest = hashlib.sha256(data).hexdigest()
    if digest != EXPECTED_SHA256:
        print(f"gate fail: sha256 {digest} != {EXPECTED_SHA256}", file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "wb") as fh:
        fh.write(data)
    if not verify(out_path, data):
        return 1
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
