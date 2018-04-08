"""This module defines Backlog and Backlog.Entry."""

import json
import random
import re
from typing import Callable, Generator, List, Union

import attr


def _list_of(cls: type) -> Callable:
    def _validator(_, attribute, value):
        if not isinstance(value, list):
            raise TypeError(f'{attribute} must be a list!')
        if not all(isinstance(item, cls) for item in value):
            raise TypeError(
                f'{attribute} must be a list of {cls.__name__} objects!',
            )
    return _validator


@attr.s
class Backlog(object):
    """A Backlog is a list of Backlog.Entry objects."""

    # https://github.com/PyCQA/pylint/issues/1694
    # pylint: disable=unsubscriptable-object
    # pylint: disable=unsupported-membership-test
    # pylint: disable=not-an-iterable

    # https://github.com/PyCQA/pylint/issues/1976
    # pylint: disable=undefined-variable

    @attr.s  # pylint: disable=too-few-public-methods
    class Entry(object):
        """A Backlog.Entry is a note with a title and a priority."""

        title: str = attr.ib(validator=attr.validators.instance_of(str))
        priority: int = attr.ib(
            validator=attr.validators.instance_of(int),
            default=0,
        )
        note: str = attr.ib(
            validator=attr.validators.instance_of(str),
            default='',
        )

        def __str__(self):
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

    entries: List[Entry] = attr.ib(
        validator=_list_of(Entry),
        default=attr.Factory(list),
    )

    def __contains__(self, entry):
        """Check for the presence of a particular Backlog.Entry."""
        return entry in self.entries

    def __str__(self):
        """Join Backlog.Entry summaries."""
        return '\n'.join(entry.summary() for entry in self.entries)

    @classmethod
    def load(cls, path: str):
        """Load a Backlog from a file."""
        with open(path, 'r') as backlog_f:
            entry_dicts = json.load(backlog_f)
        return cls(
            entries=[
                Backlog.Entry(**entry_dict)
                for entry_dict in entry_dicts
            ],
        )

    def random(self) -> Union[Entry, None]:
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

    def save(self, path: str) -> None:
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

    def search(
            self,
            pattern: str,
            invert: bool = False,
    ) -> Generator[Entry, None, None]:
        """Find Entries in the Backlog."""
        for entry in self.entries:
            if (re.search(pattern, entry.title) is None) == invert:
                yield entry
