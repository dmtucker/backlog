"""Test backlog.api."""


import os
import uuid

import pytest

import backlog.api as api


def test_backlog_load(saved_backlog):
    """Verify that a saved Backlog is equivalent when re-loaded."""
    backlog, path = saved_backlog
    assert backlog == api.Backlog.load(path)


def test_backlog_contains(backlog_entry):
    """Backlog.__contains__ returns True when a Backlog contains an entry."""
    backlog, entry = backlog_entry
    assert entry in backlog


def test_backlog_contains_nothing():
    """Backlog.__contains__ returns False when the Backlog is empty."""
    assert None not in api.Backlog()


def test_backlog_eq_bad_type(backlog):
    """Backlog objects are not equal to objects of different types."""
    assert backlog != []


def test_backlog_eq_bad_type_empty():
    """Empty Backlog objects are not equal to objects of different types."""
    assert api.Backlog() != []


def test_backlog_eq_duplicate(backlog):
    """Backlog objects are equal if they have the same entries."""
    assert backlog == api.Backlog(entries=backlog.entries)


def test_backlog_eq_duplicate_empty():
    """Empty Backlog objects are equal if they have the same entries."""
    assert api.Backlog() == api.Backlog()


def test_backlog_eq_identical(backlog):
    """A Backlog is equal to itself."""
    assert backlog == backlog


def test_backlog_eq_identical_empty():
    """An empty Backlog is equal to itself."""
    empty_backlog = api.Backlog()
    assert empty_backlog == empty_backlog


def test_backlog_init(backlog):
    """vars(Backlog()) should be unpackable into Backlog()."""
    assert backlog == api.Backlog(**vars(backlog))


def test_backlog_repr(backlog):
    """Ensure that __repr__ is a valid serialization."""
    locals()['Backlog'] = api.Backlog
    locals()['Entry'] = api.Backlog.Entry
    assert backlog == eval(repr(backlog))  # pylint: disable=eval-used


def test_backlog_repr_empty():
    """Ensure that __repr__ is a valid serialization."""
    empty_backlog = api.Backlog()
    locals()['Backlog'] = api.Backlog
    # pylint: disable=eval-used
    assert empty_backlog == eval(repr(empty_backlog))


def test_backlog_str(backlog):
    """Backlog.__str__ should delimit all entries with a newline."""
    assert len(str(backlog).split('\n')) == len(backlog.entries)


def test_backlog_str_empty():
    """Backlog.__str__ should return an empty string for an empty Backlog."""
    assert str(api.Backlog()) == ''


def test_backlog_random(backlog):
    """Backlog.random() must return an Entry the Backlog contains."""
    assert backlog.random() in backlog.entries


def test_backlog_random_empty():
    """Backlog.random() must return None if the Backlog is empty."""
    assert api.Backlog().random() is None


def test_backlog_save(backlog, path):
    """Ensure that saving a Backlog creates a file with data in it."""
    backlog.save(path=path)
    assert os.path.isfile(path) and os.stat(path).st_size > 0


def test_backlog_save_empty(path):
    """Ensure that saving an empty Backlog creates a file with data in it."""
    api.Backlog().save(path=path)
    assert os.path.isfile(path) and os.stat(path).st_size > 0


def test_backlog_search(backlog_entry):
    """Searching a Backlog must match Entry objects by title."""
    backlog, entry = backlog_entry
    assert backlog.search(pattern=entry.title) == [entry]


@pytest.mark.parametrize('invert', [True, False])
def test_backlog_search_empty(invert):
    """Searching an empty Backlog must not return any Entries."""
    assert api.Backlog().search(pattern='.*', invert=invert) == []


def test_backlog_search_invert(backlog):
    """Doing an inverted Search should not return matches."""
    assert backlog.entries == backlog.search(
        pattern=str(uuid.uuid4()),
        invert=True,
    )


def test_backlog_search_unmatchable(backlog):
    """Searching for nonexistent Entries should not return matches."""
    assert backlog.search(pattern=str(uuid.uuid4())) == []


def test_entry_eq_bad_type(entry):
    """Entry objects are not equal to objects of different types."""
    assert entry != {}


def test_entry_eq_duplicate(entry):
    """Backlog.Entry objects are equal if they have the same attributes."""
    assert entry == api.Backlog.Entry(
        note=entry.note,
        title=entry.title,
        priority=entry.priority,
    )


def test_entry_eq_identical(entry):
    """An Entry is equal to itself."""
    assert entry == entry


def test_entry_init(entry):
    """
    vars(Entry()) should be unpackable into Entry().

    This is used for Backlog.save and Backlog.load.
    """
    assert entry == api.Backlog.Entry(**vars(entry))


def test_entry_repr(entry):
    """Ensure that __repr__ is a valid serialization."""
    locals()['Entry'] = api.Backlog.Entry
    assert entry == eval(repr(entry))  # pylint: disable=eval-used


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
