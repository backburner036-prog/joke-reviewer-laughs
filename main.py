"""make.fun entry: The joke the reviewer laughs at.

Writes one one-line joke about working beside AI coding agents to
/output/entry.txt. Deterministic: no network, no randomness, no clock,
no environment variables.
"""

from pathlib import Path

JOKE = "My AI agent writes the feature before my coffee cools, and I spend the rest of the day reviewing it \u2014 I didn't hire a coder, I hired a boss."

OUT = Path("/output/entry.txt")


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
