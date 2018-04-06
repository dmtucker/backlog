"""Test backlog.cli."""


import importlib
import unittest.mock
import uuid

import pytest

import backlog.cli as cli


# @click.command changes function parameters at runtime:
# pylint: disable=no-value-for-parameter


def test_python_m():
    """Test python -m functionality."""
    with unittest.mock.patch('sys.argv', []):
        with pytest.raises(SystemExit) as excinfo:
            importlib.import_module('backlog.__main__')
        assert excinfo.value.code == 0


def test_empty():
    """Test invocation with no arguments."""
    with unittest.mock.patch('sys.argv', []):
        with pytest.raises(SystemExit) as excinfo:
            cli.main()
        assert excinfo.value.code == 0


def test_show(saved_backlog):
    """Test an invocation of show."""
    _, path = saved_backlog
    with pytest.raises(SystemExit) as excinfo:
        cli.main(['--path', path, 'show'])
    assert excinfo.value.code == 0


def test_show_empty(path):
    """Test an invocation of show with no entries."""
    with pytest.raises(SystemExit) as excinfo:
        cli.main(['--path', path, 'show'])
    assert excinfo.value.code == 0


def test_random(path):
    """Test an invocation of random."""
    with pytest.raises(SystemExit) as excinfo:
        cli.main(['--path', path, 'random'])
    assert excinfo.value.code == 0


def test_add(path):
    """Test an invocation of add and remove."""
    with pytest.raises(SystemExit) as excinfo:
        cli.main(['--path', path, 'add', str(uuid.uuid4())])
    assert excinfo.value.code == 0


def test_remove(saved_backlog):
    """Test an invocation of add and remove."""
    _, path = saved_backlog
    with pytest.raises(SystemExit) as excinfo:
        cli.main(['--path', path, 'remove', '--dont-ask', '.*'])
    assert excinfo.value.code == 0
