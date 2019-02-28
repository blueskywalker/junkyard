
import unittest
from jobdatabase import JobDataBase
import json
import time

class TestJobDatabase(unittest.TestCase):

    def setUp(self):
        self.db = JobDataBase()
        self.env = {"msg" : "test env"}
        self.jobid = "1234"
        self.db.insert(self.jobid, json.dumps(self.env))

    def test_env(self):
        cursor = self.db.select("1234")
        env, status, ts = cursor.fetchone()
        #print env, status
        self.assertEqual(env, json.dumps(self.env))
        self.assertEqual(status, 'QUEUED')

    def test_update(self):
        self.db.update_status(self.jobid,'DONE')
        cursor = self.db.select(self.jobid)
        env, status, ts = cursor.fetchone()
        self.assertEqual(status, 'DONE')

    def test_next_job(self):
        cursor = self.db.select_next_job()
        job, env = cursor.fetchone()
        self.assertEqual(job, self.jobid)
        self.assertEqual(env, json.dumps(self.env))

    def test_update_status(self):
        now = time.time()
        self.db.update_status_ts(self.jobid, '1',now)
        cursor = self.db.select(self.jobid)
        env, status, ts = cursor.fetchone()
        self.assertEqual(status, '1')
        self.assertEqual(ts, float("{0:.2f}".format(now)))

    def test_exist(self):
        exists = self.db.exists(self.jobid)
        self.assertEqual(exists, True)

    def test_delete(self):
        self.db.delete(self.jobid)
        self.assertEqual(self.db.exists(self.jobid), False)

if __name__ == '__main__':
    unittest.main()