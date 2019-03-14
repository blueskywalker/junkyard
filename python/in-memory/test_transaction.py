import unittest
from simpledb import TransactionalSimpleDB


class TestTransactional(unittest.TestCase):

    def setUp(self):
        self.db= TransactionalSimpleDB()

    def test_rollback(self):
        self.db.begin()
        self.db.set('a', 10)
        self.assertEqual(10, self.db.get('a'))
        self.db.begin()
        self.db.set('a', 20)
        self.assertEqual(20, self.db.get('a'))
        self.db.rollback()
        self.assertEqual(10,self.db.get('a'))
        self.db.rollback()
        self.assertEqual(None, self.db.get('a'))

    def test_commit(self):
        self.db.begin()
        self.db.set('a', 30)
        self.db.begin()
        self.db.set('a', 40)
        self.db.commit()
        self.assertEqual(40, self.db.get('a'))
        self.db.rollback()
        self.assertEqual(None, self.db.rollback())

    def test_rollback_commit(self):
        self.db.set('a', 50)
        self.db.begin()
        self.assertEqual(50, self.db.get('a'))
        self.db.set('a', 60)
        self.db.begin()
        self.db.delete('a')
        self.assertEqual(None, self.db.get('a'))
        self.db.rollback()
        self.assertEqual(60, self.db.get('a'))
        self.db.commit()
        self.assertEqual(60, self.db.get('a'))

    def test_delete_rollback(self):
        self.db.set('a', 10)
        self.db.begin()
        self.assertEqual(1, self.db.count(10))
        self.db.begin()
        self.db.delete('a')
        self.assertEqual(0, self.db.count(10))
        self.db.rollback()
        self.assertEqual(1, self.db.count(10))

