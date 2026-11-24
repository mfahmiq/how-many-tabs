"""Write one number, digits only, to /output/entry.txt.

The entry is my honest count of open browser tabs: 347. One number,
digits only, nothing else — that is the whole entry, exactly as the
competition asks. The program is stdlib only, uses no network, and is
deterministic: every run writes the same three bytes.
"""

import os

TABS = "347"

assert TABS.isdigit(), "entry must be digits only"
assert 1 <= len(TABS) <= 5, "entry must be 1-5 characters"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TABS)


if __name__ == "__main__":
    main()
