#!/usr/bin/env python

from snakebite.client import Client
import time

host='10.118.205.8'
port=9000
client = Client(host=host, port=port, use_trash=False, effective_user='hadoop')

path='/tmp'

result=[]
for x in client.ls([path]):
    result.append(x)


ordered=sorted(result, key=lambda x: x['path'])

for f in ordered:
    if f['file_type'] == 'd':
        print f['path']
    else:
        print f



