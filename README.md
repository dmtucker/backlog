Backlog is basically a glorified git-like TODO list.

![Build Status](https://codeship.com/projects/3c3bac90-ecbc-0132-3f37-1232bdb5f33c/status?branch=master)

```
$ python backlog --help
usage: backlog [-h] [-f FILE] {add,rm,show} ...

positional arguments:
  {add,rm,show}
    add                 Add an entry to the backlog.
    rm                  Remove entries in the backlog.
    show                Show entries in the backlog.

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Specify a backlog file.
```

Under the hood, `Backlog` extends `list` which means there is no such thing as a duplicate entry.
