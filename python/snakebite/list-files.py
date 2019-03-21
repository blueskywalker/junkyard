#!/usr/bin/env python

from snakebite.client import Client
client = Client("10.118.205.8", 9000, use_trash=False)


results=set()

def list_recursive(path):
    for x in client.ls([path]):
        if x['file_type']=='d':
            list_recursive(x['path'])
        else:
            results.add(x['path'].split('/')[11])

list_recursive('/data/hub/vehicle/MKZ-Grey/2017/08/31/17')
list_recursive('/data/hub/vehicle/MKZ-Grey/2017/08/31/18')
list_recursive('/data/hub/vehicle/MKZ-Grey/2017/08/31/19')

print len(results)
