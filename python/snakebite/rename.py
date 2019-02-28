#!/usr/bin/env python

from snakebite.client import Client
client = Client("trevally.amer.nevint.com", 9000, use_trash=False)


def list_recursive(path):
    for x in client.ls([path]):
        if x['file_type']=='d':
            list_recursive(x['path'])
        else:
            print x['path']


def walk_hdfs(path, callback):
    for x in client.ls([path]):
        if x['file_type']=='d':
            walk_hdfs(x['path'], callback)
        else:
            if x['path'].find('bounding_box') > 0:
                callback(x['path'])


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

if __name__ == "__main__":
    walk_hdfs('/data/hub/vehicle/MKZ-Grey/2017/08/31/17',print_rename)

