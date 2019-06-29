"""This file defines the API for backlog."""

from pkg_resources import get_distribution

from backlog.api import Backlog  # noqa: F401

__version__ = get_distribution(__name__).version
