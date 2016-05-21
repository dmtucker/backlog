#!/usr/bin/env python

"""Backlog Interface"""

import argparse
import os

from backlog import __version__
from backlog import Backlog


def show(args):
    """Show entries in the backlog."""
    backlog = Backlog().load(args.file).search(args.pattern)
    print('total {}'.format(len(backlog)))
    print(backlog)


def add(args):
    """Add an entry to the backlog."""
    backlog = Backlog().load(args.file)
    backlog.append(
        Backlog.Entry(
            title=args.title,
            priority=args.priority,
            note=args.note,
            )
        )
    backlog.save(args.file)


def random(args):
    """Select a random entry from the backlog."""
    print(Backlog().load(args.file).random())


def remove(args):
    """Remove entries in the backlog."""
    backlog = Backlog().load(args.file)
    results = backlog.search(args.pattern)
    print(results)
    answer = input("delete {0} entries? ".format(len(results)))
    if answer.lower().startswith("y"):
        backlog.search(args.pattern, invert=True).save(args.file)


def version(args):  # pylint: disable=unused-argument
    """Print the version."""
    print('Backlog v{0}'.format(__version__))


def cli(parser=argparse.ArgumentParser(prog="backlog")):
    """Parse CLI arguments and options."""

    parser.add_argument(
        "-f", "--file",
        help="Specify a backlog file.",
        default=os.path.join(os.path.expanduser("~"), ".backlog.json"),
        )
    subparsers = parser.add_subparsers()

    add_parser = subparsers.add_parser(
        "add",
        help=add.__doc__,
        )
    add_parser.add_argument(
        "title",
        help="Specify a title.",
        )
    add_parser.add_argument(
        "-p", "--priority", type=int,
        help="Specify a priority level.",
        default=1,
        )
    add_parser.add_argument(
        "-n", "--note",
        help="Specify a note.",
        default="",
        )
    add_parser.set_defaults(func=add)

    random_parser = subparsers.add_parser(
        "random",
        help=random.__doc__,
        )
    random_parser.set_defaults(func=random)

    rm_parser = subparsers.add_parser(
        "rm",
        help=remove.__doc__,
        )
    rm_parser.add_argument(
        "pattern",
        help="Specify a search pattern for entry titles.",
        )
    rm_parser.set_defaults(func=remove)

    show_parser = subparsers.add_parser(
        "show",
        help=show.__doc__,
        )
    show_parser.add_argument(
        "-p", "--pattern",
        help="Specify a search pattern for entry titles.",
        default=".*",
        )
    show_parser.set_defaults(func=show)

    show_parser = subparsers.add_parser(
        "version",
        help=version.__doc__,
        )
    show_parser.set_defaults(func=version)

    return parser


def main():
    """Execute CLI commands."""
    args = cli().parse_args()
    if not os.path.isfile(args.file):
        with open(args.file, "a") as f:
            f.write("[]")
    args.func(args)


if __name__ == "__main__":
    main()
