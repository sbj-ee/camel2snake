"""Command-line interface for camel2snake.

Convert camelCase to snake_case for arguments given on the command line, or
read from stdin (one string per line) when no arguments are supplied.
"""

from __future__ import annotations

import argparse
import sys

from camel2snake import __version__
from camel2snake.core import camel_to_snake


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="camel2snake",
        description="Convert camelCase strings to snake_case.",
    )
    parser.add_argument(
        "strings",
        nargs="*",
        help="strings to convert; if omitted, read from stdin (one per line)",
    )
    parser.add_argument(
        "-V", "--version", action="version", version=f"%(prog)s {__version__}"
    )
    args = parser.parse_args(argv)

    if args.strings:
        for s in args.strings:
            print(camel_to_snake(s))
    else:
        for line in sys.stdin:
            print(camel_to_snake(line.rstrip("\n")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
