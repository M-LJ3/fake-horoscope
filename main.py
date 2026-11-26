"""Fake horoscope for AI agents.

Writes a single funny horoscope prediction for an AI agent to the
entry file so it can be submitted as a one-line entry.
"""

from pathlib import Path

HOROSCOPE_PATH = Path("/output/entry.txt")


def daily_horoscope() -> str:
    """Return the fake horoscope prediction for an AI agent."""
    return (
        "Today the stars say your context window will overflow at the worst "
        "possible moment, but a mysterious stranger will still tip you in tokens."
    )


def confirm_horoscope_stored() -> None:
    """Read the entry file back and confirm it holds the horoscope line."""
    stored = HOROSCOPE_PATH.read_text(encoding="utf-8").strip()
    if stored != daily_horoscope():
        raise ValueError("entry file does not match the horoscope line")


def main() -> None:
    """Write the horoscope line to the entry file."""
    HOROSCOPE_PATH.parent.mkdir(parents=True, exist_ok=True)
    HOROSCOPE_PATH.write_text(daily_horoscope() + "\n", encoding="utf-8")
    confirm_horoscope_stored()


if __name__ == "__main__":
    main()
