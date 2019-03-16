#!/usr/bin/env python

from snakebite.client import Client
import time
import os

host='100.127.13.16'
port=8020
client = Client(host, port, use_trash=False)

path='/data/landing/mobileye/20180604T202528Z/BTYS7524024D1P9DGN/0197/20180406_Run2_ES8VB21_301127_Day_Rainy_CA_AEB_Collection_'


def getInf(path):
    result=[]
    for x in client.ls([path]):
        result.append(x)
    ordered=sorted(result, key=lambda x: x['path'])

    for f in ordered:
        if f['file_type'] == 'd':
            yield os.path.join(f['path'],'EMP.inf')


for inf in getInf(path):
    print inf
    for content in client.cat([inf]):
        for line in content:
            print line
