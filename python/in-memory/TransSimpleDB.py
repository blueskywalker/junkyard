import time


class Session(object):
    def __init__(self, tid):
        self.tid = tid
        self.db = dict()


class TransSimpleDB(object):

    def __init__(self):
        self.db = dict()
        self.sessions=list()

    def begin(self):
        self.sessions.append(Session(time.time()))

    def set(self, name, value):
        db = self.sessions[-1].db if len(self.sessions) > 0 else self.db
        db[name] = value

    def get(self, name):
        for i in reversed(range(len(self.sessions))):
            if name in self.sessions[i].db:
                return self.sessions[i].db[name]

        if name in self.db:
            return self.db[name]

        return None

    def delete(self, name):
        if len(self.sessions) > 0:
            db = self.sessions[-1].db
            if name in db:
                item = db[name]
                db[name] = None
                return item
            else:
                db[name] = None
                return None
        else:
            db = self.db
            if name in db:
                item = db[name]
                del db[name]
                return item
        return None

    def rollback(self):
        if len(self.sessions) > 0:
            return self.sessions.pop()
        else:
            return None

    def commit(self):
        while len(self.sessions):
            session = self.sessions[0]
            del self.sessions[0]
            for item in session.db:
                self.db[item] = session.db[item]
                if self.db[item] is None:
                    del self.db[item]

    def count(self, value):
        count = dict()
        for item in self.db:
            if value == self.db[item]:
                count[item]=value

        for session in self.sessions:
            for item in session.db:
                if session.db[item] == value:
                    count[item] = value
                else:
                    if item in count:
                        del count[item]

        return len(count)

