
from pyarrow import HdfsClient

#using libhdfs
hdfs = HdfsClient(host, port, username, driver='libhdfs')

with hdfs.open()
