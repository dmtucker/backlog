I use this tool to choose what to work on during my "personal projects" hour everyday.

```
usage: backlog.py [-h] [-f BACKLOG]

optional arguments:
  -h, --help  show this help message and exit
  -f BACKLOG  Specify a backlog.
```

A backlog file is a basic JSON file with the following format:
``` json
[
    {
        "note": "Describe a backlog entry here.",
        "priority": 1
    },
    ...
]
```
* Note: Priorities must be positive.
