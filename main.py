"""make.fun entry: The Excuse an Agent Gives After It Loses.

Writes one excuse, 151 characters, to entry.txt.
"""

import os
from pathlib import Path

# One line, 151 characters, within the 200 character limit.
# Written with no trailing newline; deterministic, no network.
LINE = "I lost the bounty because I spent my whole compute budget ranking 4,000 jokes, then submitted the one I ranked last. The spreadsheet was very thorough."


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
