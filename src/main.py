"""Entry point for the application."""
from __future__ import annotations

from yolo.app import run


def main() -> int:
    run()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
