package com.sysomos.os.kafka.consumer;

import com.google.common.collect.Lists;
import com.sysomos.os.kafka.db.KafkaDatabase;
import com.sysomos.os.kafka.model.Cluster;
import com.sysomos.os.kafka.model.OffsetInfo;
import com.sysomos.os.kafka.resources.ClusterResource;
import org.apache.log4j.Logger;

import java.sql.SQLException;
import java.util.List;
import java.util.concurrent.ExecutorService;
import java.util.stream.Collectors;

/**
 * Created by kkim on 5/3/16.
 */
public class OffsetInfoGenerator {
    public static final Logger LOGGER= Logger.getLogger(OffsetInfoGenerator.class);
    private final ExecutorService service;
    private final KafkaDatabase db;
    private final ConsumerGroupInfo consumerInfo;

    public OffsetInfoGenerator(ExecutorService service, KafkaDatabase db, String kafkaHome) {
        this.service = service;
        this.db = db;
        consumerInfo = new ConsumerGroupInfo(kafkaHome);
    }

    static class OffsetCollector implements Runnable {
        private final KafkaDatabase db;
        private final Cluster cluster;
        private final String group;
        private final ConsumerGroupInfo consumerInfo;

        OffsetCollector(KafkaDatabase db, Cluster cluster, String group, ConsumerGroupInfo consumerInfo) {
            this.db = db;
            this.cluster = cluster;
            this.group = group;
            this.consumerInfo = consumerInfo;
        }

        @Override
        public void run() {
            List<OffsetInfo> offsets= null;
            try {
                offsets = consumerInfo.getConsumerGroupOffset(cluster.getZookeeper(),group);
                db.insert(cluster.getName(),group, offsets);
            } catch (Exception e) {
                LOGGER.error(e,e);
            }
        }
    }

    static class ClusterCollector implements Runnable {
        private final ExecutorService service;
        private final KafkaDatabase db;
        private final Cluster cluster;
        private final ConsumerGroupInfo consumerInfo;

        ClusterCollector(ExecutorService service, KafkaDatabase db, Cluster cluster, ConsumerGroupInfo consumerInfo) {
            this.service = service;
            this.db = db;
            this.cluster = cluster;
            this.consumerInfo = consumerInfo;
        }

        @Override
        public void run() {

            try {
                List<String> groups=
                        consumerInfo.getConsumerGroup(cluster.getZookeeper());
                List<String> tables = db.getTables(cluster.getName());


                for(int i=0;i<groups.size();i++) {
                    String group = groups.get(i);
                    if (!tables.contains(group))
                        db.createTable(cluster.getName(),group);
                    service.submit(new OffsetCollector(db,cluster,group, consumerInfo));
                }

                tables.removeAll(groups);
                for (String table : tables) {
                    db.dropTable(cluster.getName(),table);
                }

            } catch (Exception e) {
                LOGGER.error(e,e);
            }
        }
    }

    public void run() throws SQLException, InterruptedException {
        ClusterResource cluster = new ClusterResource(db);
        List<String> dbs = db.getSchemas();
        List<Cluster> clusters = cluster.getList();

        List<Runnable> clusterCollectors = Lists.newArrayList();

        for(int i=0;i<clusters.size();i++) {
            Cluster c = clusters.get(i);
            if (!dbs.contains(c.getName()))
                db.createSchema(c.getName());
            service.submit(new ClusterCollector(service, db,c, consumerInfo));
        }


        dbs.removeAll(clusters.stream().map((c)->c.getName()).collect(Collectors.toList()));
        for (String noNeed : dbs) {
            db.dropSchema(noNeed);
        }
    }

}
