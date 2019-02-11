"""Test backlog.cli."""


import io
import unittest.mock
import uuid

import pytest

from backlog import cli


# @click.command changes function parameters at runtime:
# pylint: disable=no-value-for-parameter


def test_main_entry_point():
    """Test invocation with no arguments."""
    with unittest.mock.patch('sys.argv', ['--help']):
        with pytest.raises(SystemExit) as excinfo:
            cli.main()
        assert excinfo.value.code == 0


def test_main_version():
    """Test --version."""
    with pytest.raises(SystemExit) as excinfo:
        cli.main(['--version'])
    assert excinfo.value.code == 0


def test_add(saved_backlog):
    """Test an invocation of add."""
    _, path = saved_backlog
    with pytest.raises(SystemExit) as excinfo:
        cli.main(['--path', path, 'add', str(uuid.uuid4())])
    assert excinfo.value.code == 0


def test_add_empty(path):
    """Test an invocation of add on an empty backlog."""
    with pytest.raises(SystemExit) as excinfo:
        cli.main(['--path', path, 'add', str(uuid.uuid4())])
    assert excinfo.value.code == 0


def test_random(saved_backlog):
    """Test an invocation of random."""
    _, path = saved_backlog
    with pytest.raises(SystemExit) as excinfo:
        cli.main(['--path', path, 'random'])
    assert excinfo.value.code == 0


def test_random_empty(path):
    """Test an invocation of random on an empty backlog."""
    with pytest.raises(SystemExit) as excinfo:
        cli.main(['--path', path, 'random'])
    assert excinfo.value.code == 0


def test_remove(saved_backlog):
    """Test an invocation of remove."""
    _, path = saved_backlog
    with unittest.mock.patch('sys.stdin', io.BytesIO(b'y\n')):
        with pytest.raises(SystemExit) as excinfo:
            cli.main(['--path', path, 'remove', '.*'])
        assert excinfo.value.code != 0


def test_remove_ask(saved_backlog):
    """Test an invocation of remove."""
    _, path = saved_backlog
    with unittest.mock.patch('sys.stdin', io.BytesIO(b'y\n')):
        with pytest.raises(SystemExit) as excinfo:
            cli.main(['--path', path, 'remove', '--ask', '.*'])
        assert excinfo.value.code != 0


def test_remove_dont_ask(saved_backlog):
    """Test an invocation of remove with --dont-ask."""
    _, path = saved_backlog
    with pytest.raises(SystemExit) as excinfo:
        cli.main(['--path', path, 'remove', '--dont-ask', '.*'])
    assert excinfo.value.code == 0


@pytest.mark.parametrize('flag', ['--ask', '--dont-ask'])
def test_remove_empty(path, flag):
    """Test an invocation of remove on an empty backlog."""
    with pytest.raises(SystemExit) as excinfo:
        cli.main(['--path', path, 'remove', flag, '.*'])
    assert excinfo.value.code == 0


def test_show(saved_backlog):
    """Test an invocation of show."""
    _, path = saved_backlog
    with pytest.raises(SystemExit) as excinfo:
        cli.main(['--path', path, 'show'])
    assert excinfo.value.code == 0


def test_show_empty(path):
    """Test an invocation of show on an empty backlog."""
    with pytest.raises(SystemExit) as excinfo:
        cli.main(['--path', path, 'show'])
    assert excinfo.value.code == 0
