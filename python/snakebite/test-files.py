#!/usr/bin/env python

from snakebite.client import Client
client = Client("trevally.amer.nevint.com", 9000, use_trash=False)


def list_recursive(path):
    for x in client.ls([path]):
        if x['file_type']=='d':
            list_recursive(x['path'])
        else:
            print x['path']

target = '/data/hub/vehicle/MKZ-Grey'

if  client.test(target,directory=True):
    list_recursive(target)
