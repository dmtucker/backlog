import json
import random
import re


def json_to_python(path):
    with open(path, 'r') as f:
        return json.load(f)


class Backlog(list):


    def __eq__(this, that):
        for entry in that:
            if not this.contains(entry):
                return False
        return True


    def __init__(self, *args, **kwargs):
        super(Backlog, self).__init__(*args, **kwargs)


    def __repr__(self):
        entries = []
        for entry in self:
            entries.append(entry.summary())
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


    def contains(self, entry):
        for e in self:
            if e == entry:
                return True
        return False


    def search(self, pattern, invert=False):
        backlog = Backlog()
        for entry in self:
            if (re.search(pattern, entry['title']) is None) == invert:
                backlog.append(entry)
        return backlog


    def random(self):
        selection = []
        for i in range(len(self)):
            entry = self[i]
            selection.extend([i]*entry['priority'])
        return self[random.choice(selection)] if len(selection) > 0 else None


    class Entry(dict):

        def __eq__(this, that):
            return (
                int(this['priority']) == int(that['priority']) and
                str(this['note'])     == str(that['note'])     and
                str(this['title'])    == str(that['title'])
            )

        def __init__(self, *args, **kwargs):
            super(Backlog.Entry, self).__init__(*args, **kwargs)
            self['priority'] = int(self.get('priority', 1))
            self['note'] = str(self.get('note', ''))
            self['title'] = str(self.get('title', random.randint(0, 1000000)))

        def __repr__(self):
            return '\n'.join(
                [
                    self['title'],
                    'priority: {}'.format(self['priority']),
                    self['note']
                ]
            )

        def from_dict(self, d):
            for k, v in d.items():
                self[k] = v
            return self

        def summary(self):
            return \
                '{title:24}{separator}{priority:8}{separator}{note:44}'.format(
                    separator=(' '*2),
                    title=self['title'][:24],
                    priority=min(self['priority'], 99999999),
                    note=self['note'][:44]
                )
