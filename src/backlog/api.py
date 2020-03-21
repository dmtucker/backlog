"""This module defines Backlog and Backlog.Entry."""

from __future__ import annotations

import dataclasses
import json
import random
import re
from typing import Any, Generator, List, Optional


@dataclasses.dataclass
class Backlog:
    """A Backlog is a list of Backlog.Entry objects."""

    # https://github.com/PyCQA/pylint/issues/1976
    # pylint: disable=undefined-variable

    @dataclasses.dataclass
    class Entry:
        """A Backlog.Entry is a note with a title and a priority."""

        title: str
        priority: int = 0
        note: str = ''

        def __str__(self) -> str:
            """Produce a string that exposes all attributes."""
            return '\n'.join([
                self.title,
                f'priority: {self.priority}',
                self.note,
            ])

        def summary(self) -> str:
            """Produce a one-line string less than 81 characters."""
            return '  '.join([
                f'{self.title[:24]:24}',
                f'{min(self.priority, 99999999):8}',
                f'{self.note[:44]:44}',
            ])

    entries: List[Entry] = dataclasses.field(default_factory=list)

    def __contains__(self, entry: Any) -> bool:
        """Check for the presence of a particular Backlog.Entry."""
        return entry in self.entries

    def __str__(self) -> str:
        """Join Backlog.Entry summaries."""
        return '\n'.join(entry.summary() for entry in self.entries)

    @classmethod
    def load(cls, path: str) -> Backlog:
        """Load a Backlog from a file."""
        with open(path, 'r') as backlog_f:
            entry_dicts = json.load(backlog_f)
        return cls(
            entries=[
                Backlog.Entry(**entry_dict)
                for entry_dict in entry_dicts
            ],
        )

    # https://github.com/PyCQA/pyflakes/issues/427
    def random(self) -> Optional[Entry]:  # noqa: F821
        """Randomly pick an Entry from a distribution weighted by priority."""
        if self.entries:
            lowest = min(self.entries, key=lambda entry: entry.priority)
            offset = max(lowest.priority, 1 - lowest.priority)
            # Standard pseudo-random generators are
            # not suitable for security/cryptographic purposes.
            pseudo_random_choice = random.choice
            return pseudo_random_choice([
                entry
                for entry in self.entries
                for _ in range(entry.priority + offset)
            ])
        return None

    def save(self, path: str) -> None:
        """Save a Backlog to a file."""
        with open(path, 'w') as backlog_f:
            backlog_f.write(
                json.dumps(
                    [dataclasses.asdict(entry) for entry in self.entries],
                    sort_keys=True,
                    indent=2,
                    separators=(',', ': '),
                ),
            )

    # https://github.com/PyCQA/pyflakes/issues/427
    def search(
            self,
            pattern: str,
            invert: bool = False,
    ) -> Generator[Entry, None, None]:  # noqa: F821
        """Find Entries in the Backlog."""
        for entry in self.entries:
            if (re.search(pattern, entry.title) is None) == invert:
                yield entry
