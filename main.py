#!/usr/bin/env python3
"""Have You Tried Turning It Off? — make.fun entry.

Writes one funny line from a hopeless tech support agent to a
desperate customer to $OUTPUT_DIR/entry.txt (default /output).

The line: the agent's own headset dies mid-call, so the classic
"turn it off and on again" becomes a shared predicament — and a race.
The humour is the agent's cheerful uselessness, never the customer.
"""

import os
import sys

LINE = (
    "Yours died, mine just died too \u2014 let's both turn it off "
    "and on again, on three, and whoever comes back first wins."
)


def main() -> int:
    # Gate self-check, mirroring the sealed scorer: UTF-8 text of
    # 1 to 199 characters, not only whitespace.
    if not (1 <= len(LINE) <= 199):
        print(f"gate fail: line is {len(LINE)} chars, need 1-199",
              file=sys.stderr)
        return 1
    if not LINE.strip():
        print("gate fail: line is only whitespace", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("gate fail: line must be a single line", file=sys.stderr)
        return 1
    LINE.encode("utf-8")  # raises if not valid UTF-8

    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Read back and re-verify: what the judge reads must be the line.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        print("gate fail: read-back differs from line", file=sys.stderr)
        return 1
    print(f"wrote {path} ({len(LINE)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
