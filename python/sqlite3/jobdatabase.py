
import sqlite3
import time

class JobDataBase(object):
    '''JobDatabase '''
    def __init__(self):
        self.db = sqlite3.connect(':memory:', check_same_thread=False)
        self.db.execute('''CREATE TABLE JOB (
            ID   TEXT PRIMARY KEY NOT NULL,
            ENV  TEXT NOT NULL,
            STATUS TEXT NOT NULL,
            TS   INTEGER NOT NULL);''')

    def select(self, jobid):
        cmd = "SELECT ENV, STATUS, TS FROM  JOB WHERE ID = '{}'".format(jobid)
        return self.db.execute(cmd)

    def select_next_job(self):
        cmd = "SELECT ID, ENV FROM JOB WHERE STATUS = 'QUEUED' ORDER BY TS ASC LIMIT 1"
        return self.db.execute(cmd)

    def update_status(self, jobid, status):
        cmd = "UPDATE JOB SET STATUS = '{}' WHERE ID = '{}'".format(status, jobid)
        self.db.execute(cmd)


    def update_status_ts(self, jobid, status, ts):
        cmd = "UPDATE JOB SET STATUS = '{}', TS = {} WHERE ID = '{}'".format(status, ts, jobid)
        self.db.execute(cmd)

    def update_ts(self, jobid, ts):
        cmd = "UPDATE JOB SET TS = {} WHERE ID = '{}'".format(ts, jobid)
        self.db.execute(cmd)

    def insert(self, jobid, env ):
        cmd = "INSERT INTO JOB VALUES ('{}', '{}', 'QUEUED', {});".format(jobid, env, time.time())
        self.db.execute(cmd)

    def delete(self, jobid):
        cmd = "DELETE FROM JOB WHERE ID = {}".format(jobid)
        self.db.execute(cmd)

    def exists(self, jobid):
        cursor = self.select(jobid)
        job = cursor.fetchone()
        if job is None:
            return False
        else:
            return True
