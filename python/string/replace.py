
import os

def interpret_camera_name(src_path):
    target=src_path
    if root.find('vdiA') > 0:
        target = src_path.replace('vdiA','trifocal/main')
    elif src_path.find('vdiB') > 0:
        target = src_path.replace('vdiB','trifocal/narrow')
    elif src_path.find('vdiC') > 0:
        target = src_path.replace('vdiC','trifocal/wide')

    return target

for root, dirs, files  in os.walk('/tmp/data/final/MKZ-Grey'):
    print interpret_camera_name(root)

