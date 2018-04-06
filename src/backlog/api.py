"""This module defines Backlog and Backlog.Entry."""

import json
import random
import re


class Backlog(list):
    """A backlog is a list of Backlog.Entry objects."""

    def __str__(self):
        """Join Backlog.Entry summaries."""
        return '\n'.join(entry.summary() for entry in self)

    def save(self, path):
        """Save a Backlog to a file."""
        with open(path, 'w') as backlog_f:
            backlog_f.write(
                json.dumps(
                    [vars(entry) for entry in self],
                    sort_keys=True,
                    indent=2,
                    separators=(',', ': '),
                ),
            )

    def load(self, path):
        """Load a Backlog from a file."""
        with open(path, 'r') as backlog_f:
            entries = json.load(backlog_f)
        for entry_dict in entries:
            self.append(Backlog.Entry(**entry_dict))
        return self

    def search(self, pattern, invert=False):
        """Find an Entry in the Backlog."""
        backlog = Backlog()
        for entry in self:
            if (re.search(pattern, entry.title) is None) == invert:
                backlog.append(entry)
        return backlog

    def random(self):
        """Randomly pick an Entry from a distribution weighted by priority."""
        selection = []
        for i, entry in enumerate(self):
            selection.extend([i]*entry.priority)
        return self[random.choice(selection)] if selection else None

    class Entry(object):  # pylint: disable=too-few-public-methods
        """A Backlog.Entry is a note with a title and a priority."""

        def __init__(self, title=None, priority=1, note=''):
            """Initialize attributes."""
            self.title = random.randint(0, 1000000) if title is None else title
            self.priority = priority
            self.note = note

        def __eq__(self, item):
            """Check another Backlog.Entry for equality."""
            return all([
                self.title == item.title,
                self.priority == item.priority,
                self.note == item.note,
            ])

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
