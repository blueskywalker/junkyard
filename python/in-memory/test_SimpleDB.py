
import unittest
from simpledb import SimpleDB


class TestSimpleDB(unittest.TestCase):

    def setUp(self):
        self.db = SimpleDB()

    def test_set(self):
        self.db.set('a', 10)
        self.assertEqual(10, self.db.get('a'))

    def test_delete(self):
        self.db.set('a', 10)
        self.db.delete('a')
        self.assertEqual(None, self.db.get('a'))




