
from hdfs3 import HDFileSystem
import os

os.environp['HADOOP_USER_NAME']=hadoop

hdfs = HDFileSystem(host='trevally.amer.nevint.com', port=9000)

print hdfs.ls('/user/hadoop')
