"""This file defines the API for backlog."""

from pkg_resources import get_distribution

from backlog import api

__all__ = [
    '__version__',
    'Backlog',
]
__version__ = get_distribution(__name__).version
Backlog = api.Backlog
