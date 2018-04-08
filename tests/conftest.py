"""Define fixtures shared by two or more test modules."""


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
    backlog_ = Backlog(
        entries=[
            Backlog.Entry(title='test-1', priority=-100),
            Backlog.Entry(title='test-2', priority=0),
            Backlog.Entry(title='test-3', priority=1),
            Backlog.Entry(title='test-4', priority=2),
            Backlog.Entry(title='test-5', priority=100),
        ],
    )
    random.shuffle(backlog_.entries)
    return backlog_


@pytest.fixture
def backlog_entry(backlog):
    """Get a Backlog and an Entry it contains."""
    return backlog, random.choice(backlog.entries)


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
    path_ = str(tmpdir.join(f'{uuid.uuid4()}.json'))
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
