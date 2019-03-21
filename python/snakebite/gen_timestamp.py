#!/usr/bin/env python

import yaml
import os
import time
from snakebite.client import Client
from multiprocessing import JoinableQueue, Process
import glob

with open('hdfs.yaml') as config:
    conf = yaml.load(config)

env=conf['dev']
host=env['host']
port=env['port']



def list_recursive(path):
    for x in client.ls([path]):
        if x['file_type']=='d':
            list_recursive(x['path'])
        else:
            print x['path']




def print_file(arg):
    print arg

def print_rename(arg):
    camera_type = arg.split('_')[-1]
    if camera_type.startswith('fisheye'):
        print arg, arg.replace('mobileye_bounding_box','mobileye_bounding_box/wide')
    elif camera_type.startswith('main'):
        print arg, arg.replace('mobileye_bounding_box','mobileye_bounding_box/main')
    elif camera_type.startswith('narrow'):
        print arg, arg.replace('mobileye_bounding_box','mobileye_bounding_box/narrow')





def process(client, path):
    minute='_'.join(path.split('/')[-2:])
    tmp_file=os.path.join('/tmp/minutes',minute +'.txt')
    parent=os.path.dirname(tmp_file)
    if not os.path.exists(parent):
        os.makedirs(parent)

    def walk_hdfs(path, callback):
        for x in client.ls([path]):
            if x['file_type']=='d':
                walk_hdfs(x['path'], callback)
            else:
                if x['path'].find('bounding_box') > 0:
                    callback(x['path'])

    with open(tmp_file,'w') as fout:
        def get_timestamp(data):
            pieces = data.split('/')
            print >>fout, pieces[11]

        walk_hdfs(path, get_timestamp)

def process_worker(queue):
    client = Client(host, port, use_trash=False, effective_user='hadoop')
    while True:
        path = queue.get()
        print 'get ' + path
        try:
            process(client, path)
        except Exception as e:
            print e
        finally:
            queue.task_done()

def main(queue):
    client = Client(host, port, use_trash=False, effective_user='hadoop')
    def find_minutes(path, level, result):
        for x in client.ls([path]):
            if level < 5:
                find_minutes(x['path'], level+1, result)
            else:
                result.append(x['path'])

    min_list=[]
    find_minutes('/data/hub/vehicle/MKZ-Grey/2017/08/31',4, min_list)
    for each in min_list:
        print each
        queue.put(each)


if __name__ == "__main__":
    pool_size = 1
    pool = []
    que = JoinableQueue()
    for x in range(pool_size):
        pool.append(Process(target=process_worker, args=(que,)))

    for p in pool:
        p.daemon = True
        p.start()

    main(que)
    que.join()

    time.sleep(5)
    sources = glob.glob('/tmp/minutes/*.txt')
    with open('/tmp/timestamp.txt','w') as fout:
        for item in sources:
            with open(item) as infile:
                fout.write(infile.read()+'\n')

    print 'done'


