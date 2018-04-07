"""This module defines Backlog and Backlog.Entry."""

import json
import random
import re


class Backlog(object):
    """A backlog is a list of Backlog.Entry objects."""

    @classmethod
    def load(cls, path):
        """Load a Backlog from a file."""
        with open(path, 'r') as backlog_f:
            entries = json.load(backlog_f)
        return cls(
            entries=[Backlog.Entry(**entry_dict) for entry_dict in entries],
        )

    def __contains__(self, entry):
        """Check for the presence of a particular Backlog.Entry."""
        return entry in self.entries

    def __eq__(self, backlog):
        """Check another Backlog for equality."""
        return isinstance(backlog, self.__class__) and \
            self.entries == backlog.entries

    def __init__(self, entries=None):
        """Intialize the Backlog with a sequence  of entries."""
        self.entries = entries or []

    def __repr__(self):
        """Provide a pretty representation."""
        return '{0}(entries={1!r})'.format(
            self.__class__.__name__,
            self.entries,
        )

    def __str__(self):
        """Join Backlog.Entry summaries."""
        return '\n'.join(entry.summary() for entry in self.entries)

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
                    [vars(entry) for entry in self.entries],
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

    class Entry(object):  # pylint: disable=too-few-public-methods
        """A Backlog.Entry is a note with a title and a priority."""

        def __eq__(self, entry):
            """Check another Backlog.Entry for equality."""
            return isinstance(entry, self.__class__) and all([
                self.title == entry.title,
                self.priority == entry.priority,
                self.note == entry.note,
            ])

        def __init__(self, title=None, priority=1, note=''):
            """Initialize attributes."""
            self.title = random.randint(0, 1000000) if title is None else title
            self.priority = priority
            self.note = note

        def __repr__(self):
            """Provide a pretty representation."""
            return '{0}(title={1!r}, priority={2!r}, note={3!r})'.format(
                self.__class__.__name__,
                self.title,
                self.priority,
                self.note,
            )

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
