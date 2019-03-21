import sys
import time

class SimpleDB(object):
    """ NO Transaction """
    def __init__(self):
        self.db = dict()

    def set(self, name, value):
        self.db[name] = value

    def get(self, name):
        if name in self.db:
            return self.db[name]
        return None

    def delete(self, name):
        if name in self.db:
            del self.db[name]

    def count(self, value):
        count = 0
        for item in self.db:
            if value == self.db[item]:
                count += 1
        return count

    def exit(self):
        sys.exit(0)


class AtomValue(object):
    def __init__(self, tid, value):
        self.tid = tid
        self.value = value


class TransactionValue(object):

    def __init__(self, tid, value):
        self.log = [AtomValue(tid, value)]

    def add(self, tid, value):
        self.log.append(AtomValue(tid, value))

    def get(self):
        if len(self.log) > 0:
            return self.log[-1]
        return None

    def pop(self):
        return self.log.pop()

    def size(self):
        return len(self.log)


class TransactionalSimpleDB(object):
    """ Transactional DB"""

    def __init__(self):
        self.db = dict()
        self.transaction = list()
        self.begin()

    def _get_tid(self):
        return self.transaction[-1]

    def begin(self):
        self.transaction.append(time.time())

    def set(self, name, value):
        if name in self.db:
            self.db[name].add(self._get_tid(), value)
        else:
            self.db[name] = TransactionValue(self._get_tid(), value)

    def get(self, name):
        if name in self.db:
            result = self.db[name].get()
            if result is None:
                return None

            return result.value
            # if result.tid == self._get_tid():
            #     return result.value
            # else:
            #     raise RuntimeError('Transaction messed up')
        return None

    def delete(self, name):
        if name in self.db:
            if len(self.transaction) > 1:
                self.db[name].add(self._get_tid(),None)
            else:
                del self.db[name]

    def count(self, value):
        count = 0
        for item in self.db:
            if value == self.db[item].get().value:
                count += 1
        return count

    def rollback(self):
        if len(self.transaction) == 1:
            return None

        tid = self.transaction.pop()
        for item in self.db:
            if tid == self.db[item].get().tid:
                self.db[item].pop()

    def _flat_table(self):
        tid = time.time()
        self.transaction = [time.time()]
        for item in self.db:
            value = self.db[item].get().value
            self.db[item]=TransactionValue(tid,value)

    def commit(self):
        self._flat_table()

    @staticmethod
    def exit():
        sys.exit(0)
