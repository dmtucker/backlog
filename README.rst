=======
Backlog
=======

Track prioritized notes with this glorified TODO list.

|Build Status| |Test Coverage| |PyPI Version|

Installation
============

Use `pip <https://pip.pypa.io/>`__ to install Backlog from `PyPI <https://pypi.org/project/backlog/>`__.

.. code:: sh

    pip install backlog

Usage
=====

Backlog can be invoked from a command-line or imported in Python.

CLI
---

::

    $ backlog --help
    Usage: backlog [OPTIONS] COMMAND [ARGS]...

      Manage a Backlog.

    Options:
      --path PATH  Specify the path to use for the backlog file.
      --version    Show the version and exit.
      --help       Show this message and exit.

    Commands:
      add     Add an entry to the backlog.
      random  Select a random entry from the backlog.
      remove  Remove entries from the backlog.
      show    Show entries in the backlog.

API
---

.. code:: python

    >>> from backlog import Backlog
    >>> help(Backlog)

License
-------

Copyright (C) 2016 David Tucker

This library is free software; you can redistribute it and/or modify it
under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation; either version 2.1 of the License, or (at
your option) any later version.

This library is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser
General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with this library; if not, write to the Free Software Foundation,
Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA

.. |Build Status| image:: https://img.shields.io/travis/dmtucker/backlog.svg
   :target: https://travis-ci.org/dmtucker/backlog
.. |Test Coverage| image:: https://img.shields.io/coveralls/dmtucker/backlog.svg
   :target: https://coveralls.io/github/dmtucker/backlog
.. |PyPI Version| image:: https://img.shields.io/pypi/v/backlog.svg
   :target: https://pypi.python.org/pypi/backlog
