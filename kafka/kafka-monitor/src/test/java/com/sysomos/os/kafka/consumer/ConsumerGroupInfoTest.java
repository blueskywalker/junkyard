package com.sysomos.os.kafka.consumer;

import com.google.common.collect.Lists;
import com.sysomos.os.kafka.model.OffsetInfo;
import org.junit.Test;

import java.io.IOException;
import java.util.List;

/**
 * Created by kkim on 5/3/16.
 */
public class ConsumerGroupInfoTest {

    static final String kafkaHome="/Users/kkim/local/share/kafka_2.11-0.9.0.1";

    static final String zookeeper="devkf354.os.dev.yyz.corp.pvt:2181,devkf353.os.dev.yyz.corp.pvt:2181,devkf351.os.dev.yyz.corp.pvt:2181,devkf350.os.dev.yyz.corp.pvt:2181,devkf352.os.dev.yyz.corp.pvt:2181";


    @Test
    public void testGroup() throws IOException, InterruptedException {
        ConsumerGroupInfo consumerInfo = new ConsumerGroupInfo(kafkaHome);
        List<String> output=consumerInfo.getConsumerGroup(zookeeper);
        System.out.println(output);
    }

    @Test
    public void testOffset() throws IOException, InterruptedException {
        ConsumerGroupInfo consumerInfo = new ConsumerGroupInfo(kafkaHome);
        List<String> output=consumerInfo.getGroupOffset(zookeeper,"FirehoseSinker");
        System.out.println(output);
    }

    @Test
    public void testClusterInfo() throws IOException, InterruptedException {
        ConsumerGroupInfo consumerInfo = new ConsumerGroupInfo(kafkaHome);
        List<OffsetInfo> output=consumerInfo.getConsumerGroupOffset(zookeeper,"FirehoseSinker");
        System.out.println(output);
    }

    static class Collector implements Runnable {
        private final String group;
        private final ConsumerGroupInfo consumerInfo;

        Collector(String group, ConsumerGroupInfo consumerInfo) {
            this.group = group;
            this.consumerInfo = consumerInfo;
        }

        @Override
        public void run() {
            List<OffsetInfo> offsets= null;
            try {
                System.out.println(group);
                offsets = consumerInfo.getConsumerGroupOffset(zookeeper,group);
                for(OffsetInfo offset: offsets) {
                    System.out.println(offset);
                }
            } catch (IOException e) {
                e.printStackTrace();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }

    @Test
    public void testTotal() throws IOException, InterruptedException {
        ConsumerGroupInfo consumerInfo = new ConsumerGroupInfo(kafkaHome);
        List<String> output=consumerInfo.getConsumerGroup(zookeeper);

        List<Runnable> workers = Lists.newArrayList();

        for(int i=0;i<output.size();i++) {
            new Collector(output.get(i),consumerInfo).run();
            //workers.add(new Collector(output.get(i),consumerInfo)) ;
        }
        //ThreadGroup service = new ThreadGroup(workers);
        //service.start();
        //service.join();

    }
}