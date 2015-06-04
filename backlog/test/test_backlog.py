import logging
import random
import unittest
from backlog import Backlog


class BacklogTest (unittest.TestCase):

    def setUp(self):
        self.log = logging.getLogger(__name__)
        self.log.debug("Initializing a BacklogTest...")
        self.backlog = Backlog(
            entries=[
                Backlog.Entry(
                    note="test-1",
                    priority=-100
                ),
                Backlog.Entry(
                    note="test-2",
                    priority=0
                ),
                Backlog.Entry(
                    note="test-3",
                    priority=1
                ),
                Backlog.Entry(
                    note="test-4",
                    priority=2
                ),
                Backlog.Entry(
                    note="test-5",
                    priority=100
                )
            ]
        )
        random.shuffle(self.backlog.entries)

    def test_highest_priority_entry(self):
        self.assertEqual(self.backlog.highest_priority_entry().note, "test-5")

    def test_lowest_priority_entry(self):
        self.assertEqual(self.backlog.lowest_priority_entry().note, "test-1")


class BacklogEntryTest (unittest.TestCase):

    def setUp(self):
        tags = [
            "apple",
            "banana",
            "kiwi",
        ]
        random.shuffle(tags)
        self.entry = Backlog.Entry(
            note="test-entry",
            priority="5",
            tags=tags
        )

    def test_has_any_of(self):
        self.assertFalse(self.entry.has_any_of(("blackberry",)))
        self.assertFalse(self.entry.has_any_of(("grape", "blueberry")))
        self.assertTrue(self.entry.has_any_of(("kiwi", "pineapple")))
        self.assertTrue(self.entry.has_any_of(("strawberry", "banana")))
        self.assertTrue(self.entry.has_any_of(("apple", "kiwi")))
