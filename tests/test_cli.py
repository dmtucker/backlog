"""Test backlog.cli."""


import importlib
import unittest.mock

import pytest

import backlog.cli


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
            backlog.cli.main()
        assert excinfo.value.code == 0


def test_show(tmpdir):
    """Test an invocation of show."""
    with pytest.raises(SystemExit) as excinfo:
        backlog.cli.main([
            '--path', str(tmpdir.join('backlog.json')),
            'show',
        ])
    assert excinfo.value.code == 0


def test_random(tmpdir):
    """Test an invocation of random."""
    with pytest.raises(SystemExit) as excinfo:
        backlog.cli.main([
            '--path', str(tmpdir.join('backlog.json')),
            'random',
        ])
    assert excinfo.value.code == 0


def test_add_remove(tmpdir):
    """Test an invocation of add and remove."""
    path = str(tmpdir.join('backlog.json'))
    with pytest.raises(SystemExit) as excinfo:
        backlog.cli.main([
            '--path', path,
            'add', 'example',
        ])
    assert excinfo.value.code == 0
    with pytest.raises(SystemExit) as excinfo:
        backlog.cli.main([
            '--path', path,
            'show',
        ])
    assert excinfo.value.code == 0
    with pytest.raises(SystemExit) as excinfo:
        backlog.cli.main([
            '--path', path,
            'remove', '--dont-ask', 'example',
        ])
    assert excinfo.value.code == 0
