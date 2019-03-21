#!/usr/bin/env python

from snakebite.client import Client
from datetime import datetime
import pytz

client = Client("trevally.amer.nevint.com", 9000, use_trash=False)


def list_recursive(path,callback):
    result=[]
    for x in client.ls([path]):
        if x['file_type']=='d':
            list_recursive(x['path'],callback)
        else:
            callback(x['path'])




def print_item(item):
    la=pytz.timezone('America/Los_Angeles')

    old=item[47:66]
    sec, rest = old[:10], old[10:]
    ts=int(old[:10]) + (7 * 3600)
    dt= datetime.fromtimestamp(ts)
    utc_dt=la.localize(dt).astimezone(pytz.utc)
    tz = int((utc_dt - datetime(1970,1,1, tzinfo=pytz.utc)).total_seconds())

    new_ts = str(tz) + rest
    print item, item.replace(old, new_ts)
    #now=datetime.now(la)
    # tuple= map(int,old.split('/'))
    # ts=now.replace(tuple[0],tuple[1],tuple[2],tuple[3],tuple[4],tuple[5])
    # utc_time=ts.astimezone(pytz.utc)
    # target= "%04d/%02d/%02d/%02d/%02d/%02d" % (utc_time.year,utc_time.month,utc_time.day, utc_time.hour, utc_time.minute, utc_time.second)
    # print item, item.replace(old,target)

list_recursive('/data/hub/vehicle/MKZ-Grey/2017/08/31/17', print_item)
list_recursive('/data/hub/vehicle/MKZ-Grey/2017/08/31/18', print_item)
list_recursive('/data/hub/vehicle/MKZ-Grey/2017/08/31/19', print_item)
