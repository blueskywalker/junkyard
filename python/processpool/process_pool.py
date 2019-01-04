from __future__ import print_function
from multiprocessing import Pool, Process, Manager
import time
import sys

queue = Manager().JoinableQueue()

def hang(id, queue):        
    print('start id {}'.format(id))
    while True:        
        try:
            value = queue.get()
            if value < 0:
                break;
            print("hello {id}- {value}".format(**locals()))
            time.sleep(0.1)
        except KeyboardInterrupt:
            break
        finally:
            queue.task_done()

num_process=5
ids = range(num_process)

pool = Pool(processes=num_process)

try:
    for id in ids:
        pool.apply_async(hang, args=(id, queue))
    
    for i in range(100):        
        queue.put(i)

    for i in range(num_process):
        queue.put(-1)
    pool.close()
    pool.join()
except KeyboardInterrupt:
    sys.exit(1)

