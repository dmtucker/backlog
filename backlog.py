#!/usr/bin/env python

import argparse
import json
import random

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f",
        dest="backlog",
        help="Specify a backlog.",
        default="etc/backlog.json"
    )
    args = parser.parse_args()
    with open(args.backlog, 'r') as f:
        backlog = json.load(f)
    selection = []
    for entry in backlog:
        assert entry["priority"] > 0
        selection += [entry["note"]]*entry["priority"]
    print random.choice(selection)
