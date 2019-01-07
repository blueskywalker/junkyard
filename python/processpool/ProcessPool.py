from __future__ import print_function
from multiprocessing import Pool, Manager
import time
import sys

def xxxxxxxxxxxxxxxjob_done():
    pass

def process_worker(que):    
    while True:
        try:
            func, args = que.get()
            if func.__name__ == "xxxxxxxxxxxxxxxjob_done":
                break
            func(*args) 
        except KeyboardInterrupt:
            continue
        except Exception  as e:
            print(e.messae)
        finally:
            que.task_done()

class ProcessPool(object):

    def __init__(self, processes=1):
        self.pool = Pool(processes=processes)
        manager = Manager()        
        self.que = manager.JoinableQueue()
        for _ in range(processes):
            self.pool.apply_async(process_worker, args=(self.que,))

    def add(self, func, args=()):
        self.que.put((func,args))
    
    def close(self):
        for _ in range(self.pool._processes):
            self.que.put((xxxxxxxxxxxxxxxjob_done, (1,)))
        self.pool.close()
        self.pool.join()


def count(a):
    print(a)
    time.sleep(1)


num_process=3
pool = ProcessPool(processes=num_process)

for i in range(100):
    pool.add(count,(i,))

pool.close()
