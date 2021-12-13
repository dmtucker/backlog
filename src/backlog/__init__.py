"""This file defines the API for backlog."""

from importlib.metadata import version

from backlog import api

__all__ = [
    "__version__",
    "Backlog",
]
__version__ = version(__name__)
Backlog = api.Backlog
