# pylint: disable=missing-docstring

import logging
import os
import random
import unittest
from backlog import Backlog


class BacklogTest(unittest.TestCase):

    def setUp(self):
        self.log = logging.getLogger(__name__)
        self.log.debug("Initializing a BacklogTest...")
        self.entry = Backlog.Entry(
            title="test-foo",
            priority=10
        )
        self.backlog = Backlog()
        for entry in [
                Backlog.Entry(
                    title="test-1",
                    priority=-100,
                    ),
                Backlog.Entry(
                    title="test-2",
                    priority=0,
                    ),
                Backlog.Entry(
                    title="test-3",
                    priority=1,
                    ),
                Backlog.Entry(
                    title="test-4",
                    priority=2,
                    ),
                Backlog.Entry(
                    title="test-5",
                    priority=100,
                    ),
                self.entry,
        ]:
            self.backlog.append(entry)
        random.shuffle(self.backlog)

    def test_contains(self):
        self.assertTrue(self.entry in self.backlog)
        self.assertFalse(Backlog.Entry(title='dummy') in self.backlog)

    def test_search(self):
        backlog = Backlog()
        backlog.append(self.entry)
        self.assertEqual(backlog, self.backlog.search("foo$"))

    def test_search_invert(self):
        backlog = Backlog()
        backlog.append(self.entry)
        self.assertEqual(
            backlog,
            self.backlog.search("^test-\\d$", invert=True),
            )

    def test_save_load(self):
        self.backlog.save("test.backlog.json")
        backlog = Backlog().load("test.backlog.json")
        self.assertEqual(backlog, self.backlog)

    def tearDown(self):
        try:
            os.remove("test.backlog.json")
        except OSError:
            pass


class BacklogEntryTest(unittest.TestCase):

    def setUp(self):
        self.log = logging.getLogger(__name__)
        self.log.debug("Initializing a BacklogEntryTest...")
        self.entry = Backlog.Entry(
            title="test-entry",
            priority=5,
            )

    def test_equality_dupliate(self):
        self.assertEqual(
            self.entry,
            Backlog.Entry(**{
                "title": "test-entry",
                "priority": 5,
                }),
            )

    def test_equality_identical(self):
        self.assertEqual(self.entry, self.entry)
