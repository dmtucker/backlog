"""Test backlog."""


import pytest

import backlog


@pytest.mark.parametrize('attr', ['Backlog', '__version__'])
def test_attrs(attr):
    """Verify the top-level API is defined."""
    assert hasattr(backlog, attr)
