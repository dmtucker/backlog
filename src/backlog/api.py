"""This module defines Backlog and Backlog.Entry."""

import json
import random
import re

import attr


@attr.s
class Backlog(object):
    """A backlog is a list of Backlog.Entry objects."""

    entries = attr.ib(default=attr.Factory(list))

    def __contains__(self, entry):
        """Check for the presence of a particular Backlog.Entry."""
        return entry in self.entries

    def __str__(self):
        """Join Backlog.Entry summaries."""
        return '\n'.join(entry.summary() for entry in self.entries)

    @classmethod
    def load(cls, path):
        """Load a Backlog from a file."""
        with open(path, 'r') as backlog_f:
            entry_dicts = json.load(backlog_f)
        return cls(
            entries=[
                Backlog.Entry(**entry_dict)
                for entry_dict in entry_dicts
            ],
        )

    def random(self):
        """Randomly pick an Entry from a distribution weighted by priority."""
        if self.entries:
            lowest = min(self.entries, key=lambda entry: entry.priority)
            offset = max(lowest.priority, 1 - lowest.priority)
            return random.choice([
                entry
                for entry in self.entries
                for _ in range(entry.priority + offset)
            ])
        return None

    def save(self, path):
        """Save a Backlog to a file."""
        with open(path, 'w') as backlog_f:
            backlog_f.write(
                json.dumps(
                    [attr.asdict(entry) for entry in self.entries],
                    sort_keys=True,
                    indent=2,
                    separators=(',', ': '),
                ),
            )

    def search(self, pattern, invert=False):
        """Find Entries in the Backlog."""
        return [
            entry for entry in self.entries
            if (re.search(pattern, entry.title) is None) == invert
        ]

    @attr.s  # pylint: disable=too-few-public-methods
    class Entry(object):
        """A Backlog.Entry is a note with a title and a priority."""

        title = attr.ib()
        priority = attr.ib(default=0)
        note = attr.ib(default='')

        def __str__(self):
            """Produce a string that exposes all attributes."""
            return '\n'.join([
                self.title,
                'priority: {}'.format(self.priority),
                self.note,
            ])

        def summary(self):
            """Produce a one-line string less than 81 characters."""
            return '{title:24}{sep}{priority:8}{sep}{note:44}'.format(
                sep=(' '*2),
                title=self.title[:24],
                priority=min(self.priority, 99999999),
                note=self.note[:44],
            )
