#!/usr/bin/env python

import sys
import os
import subprocess
from snakebite.client import Client
from multiprocessing import JoinableQueue, Process
from datetime import datetime
import pytz


PREFIX='/data/hub/vehicle/MKZ-Grey'

def process(client, src_input):

    with open(src_input) as f, open('outputs/%s.txt'%(os.path.basename(src_input)),'w') as fout:
        for line in f:
            dt = datetime.utcfromtimestamp(int(line[:10]))
            directory = os.path.join(PREFIX, "%04d/%02d/%02d/%02d/%02d/%02d/%s" %(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second,line.strip()))
            if not client.test(directory, exists=True):
                print >>fout, directory



def process_worker(queue):
    client = Client("trevally.amer.nevint.com", 9000, use_trash=False, effective_user='hadoop')

    while True:
        afile = queue.get()
        print afile
        try:
            process(client, afile)
        except Exception as e:
            print e
        finally:
            queue.task_done()



def main(queue):
    base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    split_dir =os.path.join(base_dir,'splits')
    for each in os.listdir(split_dir):
        print each
        queue.put(os.path.join(split_dir,each))



if __name__ == "__main__":

    pool_size = 10

    pool = []
    que = JoinableQueue()
    for x in range(pool_size):
        pool.append(Process(target=process_worker, args=(que,)))

    for p in pool:
        p.daemon = True
        p.start()

    main(que)
    que.join()
    print 'done'
