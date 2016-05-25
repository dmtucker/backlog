"""Backlog Definition"""

import json
import random
import re


class Backlog(list):

    """A Collection of Entries"""

    def __init__(self, *args, **kwargs):
        super(Backlog, self).__init__(*args, **kwargs)

    def __contains__(self, item):
        for entry in self:
            if entry == item:
                return True
        return False

    def __eq__(self, item):
        for entry in item:
            if entry not in self:
                return False
        return True

    def __str__(self):
        entries = []
        for entry in self:
            entries.append(entry.__str__(short=True))
        return '\n'.join(entries)

    def save(self, path):
        """Save a Backlog to a file."""
        with open(path, 'w') as f:
            f.write(
                json.dumps(
                    [entry.__dict__ for entry in self],
                    sort_keys=True,
                    indent=2,
                    separators=(',', ': ')
                )
            )
        return self

    def load(self, path):
        """Load a Backlog from a file."""
        with open(path, 'r') as f:
            entries = json.load(f)
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
        return self[random.choice(selection)] if len(selection) > 0 else None

    class Entry(object):  # pylint: disable=too-few-public-methods

        """A Prioritized Note"""

        def __init__(self, note='', title=None, priority=1):
            self.note = note
            self.title = random.randint(0, 1000000) if title is None else title
            self.priority = priority

        def __eq__(self, item):
            return (
                self.priority == item.priority and
                self.note == item.note and
                self.title == item.title
            )

        def __str__(self, short=False):
            if short:
                return \
                    '{title:24}{sep}{priority:8}{sep}{note:44}'.format(
                        sep=(' '*2),
                        title=self.title[:24],
                        priority=min(self.priority, 99999999),
                        note=self.note[:44]
                    )
            else:
                return '\n'.join([
                    self.title,
                    'priority: {}'.format(self.priority),
                    self.note,
                    ])
