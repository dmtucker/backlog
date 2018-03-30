Backlog
=======

Backlog is basically a glorified TODO list.

|Build Status| |Test Coverage| |PyPI Version|

Installation
------------

Backlog is available on `PyPI <https://pypi.python.org/pypi/backlog>`__.

.. code:: sh

    pip install backlog

Usage
-----

Backlog can be run as a command-line utility.

.. code:: sh

    $ backlog --help
    usage: backlog [-h] [-f FILE] [--version] {add,random,rm,show} ...

    positional arguments:
      {add,random,rm,show}
        add                 Add an entry to the backlog.
        random              Select a random entry from the backlog.
        rm                  Remove entries in the backlog.
        show                Show entries in the backlog.

    optional arguments:
      -h, --help            show this help message and exit
      -f FILE, --file FILE  Specify a backlog file. (default:
                            /home/david/.backlog.json)
      --version             show program's version number and exit

Backlog can also be imported into other Python projects.

.. code:: python

    from backlog import Backlog

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
