#!/bin/bash

LIBJARS=/usr/lib/avro/avro-1.7.6-cdh5.4.7.jar,/usr/lib/avro/avro-compiler-1.7.6-cdh5.4.7.jar,/usr/lib/avro/avro-compiler.jar,/usr/lib/avro/avro-ipc-1.7.6-cdh5.4.7.jar,/usr/lib/avro/avro-ipc-1.7.6-cdh5.4.7-tests.jar,/usr/lib/avro/avro-ipc.jar,/usr/lib/avro/avro-ipc-tests.jar,/usr/lib/avro/avro.jar,/usr/lib/avro/avro-mapred-1.7.6-cdh5.4.7-hadoop2.jar,/usr/lib/avro/avro-mapred-1.7.6-cdh5.4.7.jar,/usr/lib/avro/avro-mapred-hadoop2.jar,/usr/lib/avro/avro-mapred.jar,/usr/lib/avro/avro-maven-plugin-1.7.6-cdh5.4.7.jar,/usr/lib/avro/avro-maven-plugin.jar,/usr/lib/avro/avro-protobuf-1.7.6-cdh5.4.7.jar,/usr/lib/avro/avro-protobuf.jar,/usr/lib/avro/avro-service-archetype-1.7.6-cdh5.4.7.jar,/usr/lib/avro/avro-service-archetype.jar,/usr/lib/avro/avro-thrift-1.7.6-cdh5.4.7.jar,/usr/lib/avro/avro-thrift.jar,/usr/lib/avro/avro-tools-1.7.6-cdh5.4.7.jar,/usr/lib/avro/avro-tools-1.7.6-cdh5.4.7-nodeps.jar,/usr/lib/avro/avro-tools.jar,/usr/lib/avro/avro-tools-nodeps.jar,/usr/lib/avro/trevni-avro-1.7.6-cdh5.4.7-hadoop2.jar,/usr/lib/avro/trevni-avro-1.7.6-cdh5.4.7.jar,/usr/lib/avro/trevni-avro-hadoop2.jar,/usr/lib/avro/trevni-avro.jar,/usr/lib/avro/trevni-core-1.7.6-cdh5.4.7.jar,/usr/lib/avro/trevni-core.jar,/usr/lib/solr/contrib/mr/search-mr.jar,commons-utilities-0.1.0.BUILD-SNAPSHOT.jar,commons-solr-0.1.0.BUILD-SNAPSHOT.jar


yarn jar /usr/lib/solr/contrib/mr/search-mr-*-job.jar org.apache.solr.hadoop.MapReduceIndexerTool \
-D 'mapred.child.java.opts=-Xmx500m' \
-libjars $LIBJARS \
--log4j /root/kkim/log4j.properties \
--morphline-file /root/kkim/morphline.conf \
--output-dir hdfs://alnn01.lab.dev.yyz.corp.pvt:8020/data/solr/outdir --verbose \
--solr-home-dir  /root/kkim/solrHome \
--shards 10 hdfs://alnn01.lab.dev.yyz.corp.pvt:8020/data/hbase/post_TT_201601
