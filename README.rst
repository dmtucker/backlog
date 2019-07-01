=======
Backlog
=======

Track prioritized notes with this glorified TODO list.

Installation
============

Use `pip <https://pip.pypa.io/>`__ to install Backlog.

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

::

    $ backlog add --priority 100 'Pay the water bill'
    $ backlog add --priority 200 --note "eggs, bread, milk" 'Buy groceries'
    $ backlog add 'Clean out the freezer'
    $ backlog show
    total 3
    Pay the water bill             100
    Buy groceries                  200  eggs, bread, milk
    Clean out the freezer            0

::

    $ backlog random
    Buy groceries
    priority: 200
    eggs, bread, milk

::

    $ backlog show --pattern bill
    total 1
    Pay the water bill             100

API
---

.. code:: python

    >>> from backlog import Backlog
    >>> help(Backlog)

.. code:: python

    >>> backlog = Backlog(
    ...     entries=[
    ...         Backlog.Entry('Pay the water bill', priority=100),
    ...         Backlog.Entry('Buy groceries', priority=200, note='eggs, bread, milk'),
    ...         Backlog.Entry('Clean out the freezer'),
    ...     ],
    ... )

.. code:: python

    >>> backlog.random()
    Backlog.Entry(title='Buy groceries', priority=200, note='eggs, bread, milk')

.. code:: python

    >>> list(backlog.search('bill'))
    [Backlog.Entry(title='Pay the water bill', priority=100, note='')]
