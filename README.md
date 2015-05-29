```
usage: backlog.py [-h] [-f BACKLOG] [-o HISTORY]

optional arguments:
  -h, --help            show this help message and exit
  -f BACKLOG, --backlog-file BACKLOG
                        Specify a backlog file.
  -o HISTORY, --history-file HISTORY
                        Specify a history file.
```

A backlog file is a basic JSON file with the following format:
``` json
[
    {
        "note": "Describe a backlog entry here.",
        "priority": 1
    },
    {
        "note": "Describe a more likely backlog entry here.",
        "priority": 5
    }
]
```
* Note: Priorities must be positive integers.
