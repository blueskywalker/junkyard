#!/usr/bin/env python

from snakebite.client import Client
client = Client("trevally.amer.nevint.com", 9000, use_trash=False)


results=set()

def list_recursive(path):
    for x in client.ls([path]):
        if x['file_type']=='d':
            list_recursive(x['path'])
        else:
            results.add(x['path'].split('/')[11])

list_recursive('/data/hub/vehicle/MKZ-Grey/2017/08/31/17')

for item in results:
    print item
