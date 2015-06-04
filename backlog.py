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


def json_to_python(path):
    with open(path, 'r') as f:
        return json.load(f)


class Backlog:

    entries = None

    def __init__(self, entries=None):
        self.entries = entries

    def loaded_from(self, json_file=None):
        self.entries = []
        if json_file is not None:
            for entry in json_to_python(json_file):
                self.entries.append(
                    Backlog.Entry(
                        note=entry["note"],
                        priority=entry.get("priority", 1),
                        tags=entry.get("tags", ())
                    )
                )
        return self

    def random_entry(self):
        if self.entries is None or len(self.entries) < 1:
            return None
        selection = []
        priority_shift = 1-self.lowest_priority_entry().priority
        for entry in self.entries:
            selection.extend([entry.note]*(entry.priority+priority_shift))
        return random.choice(selection)

    def highest_priority_entry(self):
        highest = None
        for entry in self.entries:
            if highest is None or entry.priority > highest.priority:
                highest = entry
        return highest

    def lowest_priority_entry(self):
        lowest = None
        for entry in self.entries:
            if lowest is None or entry.priority < lowest.priority:
                lowest = entry
        return lowest

    class Entry:

        note = None
        priority = 1
        tags = ()

        def __init__(self, note, priority=1, tags=()):
            self.note = str(note)
            self.priority = int(priority)
            self.tags = tuple(tags)


if __name__ == "__main__":
    args = parse_cli()
    logger = configure_logging(args.history)
    backlog = Backlog().loaded_from(json_file=args.backlog)
    entry = backlog.random_entry()
    logger.info(entry)
    print(entry)
