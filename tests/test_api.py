"""Test backlog.api."""


import os
import random
import uuid

import pytest

from backlog import Backlog


# @pytest.fixture denotes a function that is meant to be redefined:
# pylint: disable=redefined-outer-name


@pytest.fixture
def backlog():
    """Get a Backlog with at least 1 Entry."""
    backlog_ = Backlog([
        Backlog.Entry(title='test-1', priority=-100),
        Backlog.Entry(title='test-2', priority=0),
        Backlog.Entry(title='test-3', priority=1),
        Backlog.Entry(title='test-4', priority=2),
        Backlog.Entry(title='test-5', priority=100),
    ])
    random.shuffle(backlog_)
    return backlog_


@pytest.fixture
def backlog_entry(backlog):
    """Get a Backlog and an Entry it contains."""
    return backlog, random.choice(backlog)


@pytest.fixture
def entry():
    """Get a Backlog.Entry."""
    return Backlog.Entry(
        title='test-foo',
        priority=10,
    )


@pytest.fixture
def path(tmpdir):
    """Get the path of a writable file."""
    path_ = str(tmpdir.join('{0}.json'.format(uuid.uuid4())))
    yield path_
    try:
        os.remove(path_)
    except FileNotFoundError:
        pass


@pytest.fixture
def saved_backlog(backlog, path):
    """Get a Backlog and a path to a file where it has been saved."""
    backlog.save(path=path)
    return backlog, path


def test_backlog_load(saved_backlog):
    """Verify that a saved Backlog is equivalent when re-loaded."""
    backlog, path = saved_backlog
    assert backlog == Backlog().load(path)


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
    assert entry == Backlog.Entry(
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
    locals()['Entry'] = Backlog.Entry  # Entry is an inner class.
    assert value == eval(repr(value))  # pylint: disable=eval-used
