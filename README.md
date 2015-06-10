Backlog is basically a glorified TODO list.

![Build Status](https://codeship.com/projects/3c3bac90-ecbc-0132-3f37-1232bdb5f33c/status?branch=master)

```
$ python -m backlog --help
usage: __main__.py [-h] [-f BACKLOG] [-o HISTORY] [-t TAGS]

optional arguments:
  -h, --help            show this help message and exit
  -f BACKLOG, --backlog-file BACKLOG
                        Specify a backlog file.
  -o HISTORY, --history-file HISTORY
                        Specify a history file.
  -t TAGS, --tag TAGS   Specify one or more entry tags.
```

A backlog file is a basic JSON file with the following format:
``` json
[
    {
        "title": "Titles are always required.",
        "note": "All other attributes are optional.",
        "priority": 1,
        "tags": [
            "tag1",
            "tag2"
        ]
    },
    {
        "title": "Foo",
        "note": "This entry is unlikely to be selected because the priority is relatively low.",
        "priority": -5,
        "tags": [
            "tag1"
        ]
    },
    {
        "title": "Bar",
        "priority": 9000,
        "tags": [
            "tag2",
            "#turndownforwhat"
        ]
    }
]
```

Under the hood, there is no such thing as a duplicate entry.
