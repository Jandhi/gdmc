#!/usr/bin/env python3
"""Runs the Grimoire generator."""

import argparse as ap
import logging
import sys
from logging import warn
from traceback import format_exc
from typing import Literal

from colored import Fore, Style

# ==== LOGGING SETUP ====

logging.addLevelName(
    logging.DEBUG,
    f"{Fore.dark_gray} {logging.getLevelName(logging.DEBUG)} {Style.reset}",
)
logging.addLevelName(
    logging.INFO,
    f"{Fore.cyan} {logging.getLevelName(logging.INFO)} {Style.reset}",
)
logging.addLevelName(
    logging.WARNING,
    f"{Fore.yellow} {logging.getLevelName(logging.WARNING)} {Style.reset}",
)
logging.addLevelName(
    logging.ERROR,
    f"{Fore.light_red} {logging.getLevelName(logging.ERROR)} {Style.reset}",
)
logging.addLevelName(
    logging.CRITICAL,
    f"{Fore.red} {logging.getLevelName(logging.CRITICAL)} {Style.reset}",
)

# ==== ARGUMENT HANDLING ====
argparser = ap.ArgumentParser(
    prog="Grimoire",
    description="A settlement generator using GDMC-HTTP for Minecraft 1.20.",
)
argparser.add_argument(
    "-l",
    "--log-level",
    type=str,
    default="WARNING",
    help="Logging level: DEBUG, INFO, WARNING, ERROR or CRITICAL "
    "(defaults to WARNING)",
)
argparser.add_argument(
    "-d",
    "--debug",
    help="Use as an argument for `python` for debugging!",
    action="store_true",
)
args: ap.Namespace = argparser.parse_args()


# ==== MAIN ====
def main() -> str | Literal[0]:
    """Run the generator."""
    try:
        # TODO: implement/call generator here!
        import main  # FIXME: Just a temporary bridge

    except KeyboardInterrupt:
        warn("Manually interrupted!")
    except Exception:
        return format_exc()
    return 0


if __name__ == "__main__":
    # runs when package is called
    if args.debug:
        warn("Use `python3 -dm grimoire` to make use of debug features!")
    sys.exit(main())
