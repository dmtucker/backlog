Backlog is a glorified TODO list.

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
        "note": "Describe a backlog entry here.",
        "priority": 1,
        "tags": [
            "tag1"
        ]
    },
    {
        "note": "Describe a more likely backlog entry here.",
        "priority": 5,
        "tags": [
            "tag1",
            "tag2"
        ]
    },
    {
        "note": "Describe a most likely backlog entry here.",
        "priority": 10,
        "tags": [
            "tag2"
        ]
    }
]
```
