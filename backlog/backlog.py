import json
import random
import re


def json_to_python(path):
    with open(path, 'r') as f:
        return json.load(f)


class Backlog(list):


    def __init__(self, *args, **kwargs):
        super(Backlog, self).__init__(*args, **kwargs)


    def __repr__(self):
        entries = []
        for entry in self:
            entries.append(str(entry))
        return '\n'.join(entries)


    def load(self, db='backlog.json'):
        with open(db, 'r') as f:
            entries = json.load(f)
        for entry in entries:
            self.append(Backlog.Entry().from_dict(entry))
        return self


    def save(self, db='backlog.json'):
        with open(db, 'w') as f:
            f.write(
                json.dumps(
                    self,
                    sort_keys=True,
                    indent=2,
                    separators=(',', ': ')
                )
            )
        return self


    def search(self, pattern, invert=False):
        backlog = Backlog()
        for entry in self:
            if (re.search(pattern, entry['title']) is None) == invert:
                backlog.append(entry)
        return backlog


    def random(self):  # TODO
        selection = []
        priority_shift = 1-self.lowest_priority_entry().priority
        for i in range(len(self)):
            entry = self[i]
            if tags is None or entry.has_any_of(tags=tags):
                selection.extend([i]*(entry.priority+priority_shift))
        return self[random.choice(selection)] if len(selection) > 0 else None


    class Entry(dict):

        def __init__(self, *args, **kwargs):
            super(Backlog.Entry, self).__init__(*args, **kwargs)

        def __repr__(self):
            return \
                '{title:24}{separator}{priority:8}{separator}{note:44}'.format(
                    separator=(' '*2),
                    title=self['title'][:24],
                    priority=min(self['priority'], 99999999),
                    note=self['note'][:44]
                )

        def from_dict(self, d):
            for k, v in d.items():
                self[k] = v
            return self
