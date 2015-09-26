#!/usr/bin/env python

from __future__ import print_function
import argparse
import logging
import os
from pprint import pprint
from backlog import Backlog


def print_backlog(backlog):
    if len(backlog) > 0:
        print(backlog if len(backlog) > 1 else backlog[0])


def show(args):
    backlog = Backlog().load(db=args.file).search(args.pattern)
    print('total {}'.format(len(backlog)))
    print_backlog(backlog)


def add(args):
    backlog = Backlog().load(db=args.file)
    backlog.append(
        Backlog.Entry(
            title=args.title,
            priority=args.priority,
            note=args.note
        )
    )
    backlog.save(db=args.file)


def random(args):
    print(Backlog().load(db=args.file).random())


def rm(args):
    backlog = Backlog().load(db=args.file)
    results = backlog.search(args.pattern)
    print_backlog(results)
    if raw_input("delete {} entries? ".format(len(results))).lower().startswith("y"):
        backlog.search(args.pattern, invert=True).save(db=args.file)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(prog="backlog")
    parser.add_argument(
        "-f", "--file",
        help="Specify a backlog file.",
        default=".backlog.json"
    )
    subparsers = parser.add_subparsers()
    
    add_parser = subparsers.add_parser(
        "add",
        help="Add an entry to the backlog."
    )
    add_parser.add_argument(
        "title",
        help="Specify a title."
    )
    add_parser.add_argument(
        "-p", "--priority", type=int,
        help="Specify a priority level.",
        default=1
    )
    add_parser.add_argument(
        "-n", "--note",
        help="Specify a note.",
        default=""
    )
    add_parser.set_defaults(func=add)

    random_parser = subparsers.add_parser(
        "random",
        help="Select a random entry from the backlog."
    )
    random_parser.set_defaults(func=random)

    rm_parser = subparsers.add_parser(
        "rm",
        help="Remove entries in the backlog."
    )
    rm_parser.add_argument(
        "pattern",
        help="Specify a search pattern for entry titles."
    )
    rm_parser.set_defaults(func=rm)
    
    show_parser = subparsers.add_parser(
        "show",
        help="Show entries in the backlog."
    )
    show_parser.add_argument(
        "-p", "--pattern",
        help="Specify a search pattern for entry titles.",
        default=".*"
    )
    show_parser.set_defaults(func=show)

    args = parser.parse_args()
    if not os.path.isfile(args.file):
        with open(args.file, "a") as f:
            f.write("[]")
    args.func(args)
