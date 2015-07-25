Backlog is basically a glorified git-like TODO list.

[![Build Status](https://img.shields.io/codeship/3c3bac90-ecbc-0132-3f37-1232bdb5f33c/master.svg)](https://codeship.com/projects/83804)

```
$ python backlog --help
usage: backlog [-h] [-f FILE] {add,random,rm,show} ...

positional arguments:
  {add,random,rm,show}
    add                 Add an entry to the backlog.
    random              Select a random entry from the backlog.
    rm                  Remove entries in the backlog.
    show                Show entries in the backlog.

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Specify a backlog file.
```

Under the hood, `Backlog` extends `list` which means there is no such thing as a duplicate entry.
