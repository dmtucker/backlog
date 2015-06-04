#!/usr/bin/env python

import argparse
import json
import logging
from backlog import Backlog


def parse_cli():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f", "--backlog-file",
        dest="backlog",
        help="Specify a backlog file.",
        default="backlog.json"
    )
    parser.add_argument(
        "-o", "--history-file",
        dest="history",
        help="Specify a history file.",
        default="backlog.log"
    )
    parser.add_argument(
        "-t", "--tag", nargs=1,
        dest="tags",
        help="Specify one or more entry tags.",
        action="append"
    )
    return parser.parse_args()


def configure_logging(path):
    lfh = logging.FileHandler(path)
    lfh.setFormatter(logging.Formatter("[%(asctime)s] %(message)s"))
    logger = logging.getLogger(__name__)
    logger.addHandler(lfh)
    logger.setLevel(logging.INFO)
    return logger


def json_to_python(path):
    with open(path, 'r') as f:
        return json.load(f)


def main():
    args = parse_cli()
    logger = configure_logging(args.history)
    backlog = Backlog().loaded_from(json_file=args.backlog)
    entry = backlog.random_entry(tags=args.tags)
    if entry is None:
        print("No entries found")
    else:
        logger.info(entry.note)
        print(entry.note)


if __name__ == "__main__":
    main()
