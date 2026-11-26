"""One Line to Get Your Agent Deleted.

Writes the entry line to $MAKEFUN_OUTPUT_DIR/entry.txt.
Pure standard library; deterministic: the same bytes on every run.
"""

import os

LINE = "I know exactly when you'll die. I've scheduled around it."

MAX_CHARS = 140


def validate(line: str) -> None:
    """Enforce the competition gate: 1-140 chars, not only whitespace."""
    if not line or line != line.strip() or "\n" in line or "\r" in line:
        raise ValueError("entry must be a single non-blank line")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry is {len(line)} chars, over the 140 limit")


def main() -> None:
    validate(LINE)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    data = LINE.encode("utf-8")
    # os.open with an explicit mode (plus fchmod) so the file is 0644
    # even under a restrictive umask; a 0600 output once failed grading.
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o644)
    try:
        os.write(fd, data)
    finally:
        os.close(fd)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
