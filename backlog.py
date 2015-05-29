#!/usr/bin/env python

import argparse
import json
import logging
import random


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
    return parser.parse_args()


def configure_logging(path):
    lfh = logging.FileHandler(path)
    lfh.setFormatter(logging.Formatter("[%(asctime)s] %(message)s"))
    logger = logging.getLogger(__name__)
    logger.addHandler(lfh)
    logger.setLevel(logging.INFO)
    return logger


def json_file_to_dict(path):
    with open(path, 'r') as f:
        return json.load(f)


if __name__ == "__main__":

    args = parse_cli()
    logger = configure_logging(args.history)
    backlog = json_file_to_dict(args.backlog)
    
    selection = []
    for entry in backlog:
        assert entry["priority"] > 0
        selection += [entry["note"]]*entry["priority"]
    selected = random.choice(selection)

    logger.info(selected)
    print(selected)
