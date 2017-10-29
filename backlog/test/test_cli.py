# coding: utf-8

"""Tests for backlog.cli"""


import pytest

import backlog.cli


def test___main__():
    """Test python -m functionality."""
    with pytest.raises(SystemExit) as excinfo:
        # pylint: disable=redefined-outer-name, unused-variable
        import backlog.__main__
    assert excinfo.value.code != 0


def test_empty():
    """Test invocation with no arguments."""
    with pytest.raises(SystemExit) as excinfo:
        backlog.cli.main()
    assert excinfo.value.code != 0


def test_show(tmpdir):
    """Test an invocation of show."""
    with pytest.raises(SystemExit) as excinfo:
        backlog.cli.main([
            '-f', str(tmpdir.join('backlog.json')),
            'show',
        ])
    assert excinfo.value.code == 0


def test_random(tmpdir):
    """Test an invocation of random."""
    with pytest.raises(SystemExit) as excinfo:
        backlog.cli.main([
            '-f', str(tmpdir.join('backlog.json')),
            'random',
        ])
    assert excinfo.value.code == 0


def test_add_rm(tmpdir):
    """Test an invocation of add and rm."""
    with pytest.raises(SystemExit) as excinfo:
        backlog.cli.main([
            '-f', str(tmpdir.join('backlog.json')),
            'add', 'example',
        ])
    assert excinfo.value.code == 0
    with pytest.raises(SystemExit) as excinfo:
        backlog.cli.main([
            '-f', str(tmpdir.join('backlog.json')),
            'rm', '-y', 'example',
        ])
    assert excinfo.value.code == 0
