#!/usr/bin/env python3
"""Zeus ...."""

import sys
import logging
import colorlog
import argparse
from colorama import init
from termcolor import cprint
from pyfiglet import figlet_format

init(autoreset=True, strip=not sys.stdout.isatty())


def getLogger():
    # logging
    handler = colorlog.StreamHandler()
    handler.setFormatter(colorlog.ColoredFormatter(
        '%(log_color)s[%(name)s] \u2192 %(message)s',
        datefmt="%d/%m/%Y"))
    logger = colorlog.getLogger("ZEUS")
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger


def get_arguments():
    """Get Arguments command line."""
    parser = argparse.ArgumentParser(
        description=cprint(figlet_format("ZeUs!", font="starwars"),
                           "green", attrs=["bold"]),
        prog="zeus")
    parser.add_argument("--project", "-p", help="Creating project.",
                        type=str, default="")
    parser.add_argument("--module", "-m", help="Creating module.",
                        nargs=2)
    parser.add_argument("--template", "-t", help="Creating template.",
                        nargs=2)
    parser.add_argument("--author", "-a",
                        help="Author of project (default: %(default)s).",
                        type=str, default="Lab804")
    parser.add_argument("--domain", "-do",
                        help="Domain, (default: %(default)s)",
                        type=str, default="lab804.com.br")
    parser.add_argument("--debug", "-d", help="Debug mode.",
                        type=bool, default=False),
    parser.add_argument("--version", "-v", action="version",
                        version="%(prog)s 0.1.2")
    args = parser.parse_args()
    return args
