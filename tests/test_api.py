"""Test backlog.api."""


import os
import uuid

import pytest

import backlog.api as api


def test_backlog_load(saved_backlog):
    """Verify that a saved Backlog is equivalent when re-loaded."""
    backlog, path = saved_backlog
    assert backlog == api.Backlog().load(path)


def test_backlog_random(backlog):
    """Backlog.random() must return an Entry the Backlog contains."""
    assert backlog.random() in backlog


def test_backlog_save(backlog, path):
    """Ensure that saving a Backlog creates a file with data in it."""
    backlog.save(path=path)
    assert os.path.isfile(path) and os.stat(path).st_size > 0


def test_backlog_search(backlog_entry):
    """Searching a Backlog must match Entry objects by title."""
    backlog, entry = backlog_entry
    entries = backlog.search(pattern=entry.title)
    assert len(entries) == 1 and entries[0] == entry


def test_backlog_search_invert(backlog):
    """Doing an inverted Search should not return matches."""
    assert backlog == backlog.search(pattern=str(uuid.uuid4()), invert=True)


def test_entry_equality_duplicate(entry):
    """Backlog.Entry objects are equal if they have the same attributes."""
    assert entry == api.Backlog.Entry(
        note=entry.note,
        title=entry.title,
        priority=entry.priority,
    )


def test_entry_equality_identical(entry):
    """An Entry is equal to itself."""
    assert entry == entry


def test_entry_str(entry):
    """All Entry attributes should be represented by __str__."""
    assert all([
        str(entry.title) in str(entry),
        str(entry.priority) in str(entry),
        str(entry.note) in str(entry),
    ])


def test_entry_summary_is_str(entry):
    """Entry.summary() must return a str."""
    assert isinstance(entry.summary(), str)


@pytest.mark.parametrize('fixture', ['backlog', 'entry'])
def test_repr(request, fixture):
    """Ensure that __repr__ is a valid serialization."""
    value = request.getfixturevalue(fixture)
    locals()['Entry'] = api.Backlog.Entry  # Entry is an inner class.
    assert value == eval(repr(value))  # pylint: disable=eval-used
