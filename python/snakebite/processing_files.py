from snakebite.client import Client
import os

def scan_files(env):
    hdfs=env['hdfs']
    host, port = hdfs.split(':')
    client = Client(host, int(port), use_trash=False, effective_user='hadoop')
    input_files=[]
    for item in client.ls([env['input']]):
        if item['file_type'] == 'd':
            input_files.append(item['path'])
    return input_files

def scan_event_files(env):
    hdfs=env['hdfs']
    host, port = hdfs.split(':')
    client = Client(host, int(port), use_trash=False, effective_user='hadoop')
    event_files=[]

    basename = '_'.join(os.path.basename(env['first_clip']).split('_')[:-1])
    event_dir=os.path.join(env['event_dir'],basename)

    if not client.test(event_dir, exists=True, directory=True):
        return event_files

    for item in client.ls([event_dir]):
        if item['file_type'] == 'f':
            event_files.append(os.path.basename(item['path']))
    return event_files


def processing_files(args):
    input_files=map(lambda x:os.path.basename(x),scan_files(args))
    event_files=map(lambda x: x[:-4],scan_event_files(args))
    if len(input_files) > len(event_files):
        diff_files = set(input_files) - set(event_files)
        return map(lambda x: '/'.join([args['input'], x]), sorted(diff_files))
    else:
        return []



if __name__ == "__main__":
    env = {
            'hdfs' : "10.118.31.8:9000",
            'input' : "/data/landing/mobileye/20170918/MKZ-Black/20170918_MKZ-Black_EPM4Trifocal_Day-Clear_Clear_SanJose_GDC",
            'first_clip' : "/data/landing/mobileye/20170918/MKZ-Black/20170918_MKZ-Black_EPM4Trifocal_Day-Clear_Clear_SanJose_GDC/17-09-19_20170918_MKZ-Black_EPM4Trifocal_Day-Clear_Clear_SanJose_GDC_0001",
            'event_dir' : "/tmp"
    }

    print processing_files(env)
