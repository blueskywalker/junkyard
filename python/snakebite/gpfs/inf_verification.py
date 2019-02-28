
from snakebite.client import Client
import sys
import os

def getEMP(folder):
    return '{}/{}.emp4'.format(folder,os.path.basename(folder))

def getInf(folder):
    return '{}/EMP.inf'.format(folder)

if __name__ == '__main__':
#    hdfs_host='100.127.6.35'
    hdfs_host='100.127.13.16'
#    hdfs_port=9820
    hdfs_port=8020

    client = Client(host=hdfs_host, port= hdfs_port, use_trash=False, effective_user='hadoop')

    if len(sys.argv) < 2:
        print 'inf_verification.py path'
        sys.exit(0)

    input_dir=sys.argv[1]

    input_files=[]
    for clip in client.ls([input_dir]):
        if clip['file_type'] == 'd':
            input_files.append(clip['path'])

    for folder in sorted(input_files):
        for inf in client.cat([getInf(folder)]):
            for content in inf:
                start=None
                end=None
                for aline in content.split('\n'):
                    if aline.startswith('startTime'):
                        start=aline.strip()
                    elif aline.startswith('endTime'):
                        end=aline.strip()

                print '{}\t{}\t{}'.format(os.path.basename(folder),start, end)
