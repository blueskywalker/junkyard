package com.sysomos.os.kafka.consumer;


import com.google.common.collect.Lists;
import com.sysomos.os.kafka.model.OffsetInfo;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Date;
import java.util.List;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;


/**
 * Created by kkim on 4/26/16.
 */
public class ConsumerGroupInfo {
    private static final Logger LOGGER = LoggerFactory.getLogger(ConsumerGroupInfo.class);

    private final String kafkaHome;
    private final String basicCmd;
    private final static String unknown="unknown";
    public ConsumerGroupInfo(String kafkaHome) {
        this.kafkaHome = kafkaHome;
        basicCmd = String.format("%s/bin/kafka-run-class.sh kafka.admin.ConsumerGroupCommand ", kafkaHome);
    }

    public List<OffsetInfo> getConsumerGroupOffset(String zookeeper, String group) throws IOException, InterruptedException {
        List<String> output = getGroupOffset(zookeeper, group);

        List<OffsetInfo> ret = Lists.newArrayList();
        if (!output.get(0).split(",")[0].equals("GROUP"))
            return ret;

        int ts = (int) (new Date().getTime() / 1000);

        for (int i = 1; i < output.size(); i++) {
            String[] rs = output.get(i).split(",");
            if (rs.length == 7) {
                if (unknown.equals(rs[3].trim()) ||
                        unknown.equals(rs[4].trim()) ||
                        unknown.equals(rs[5].trim()))
                    continue;

                ret.add(new OffsetInfo(
                        rs[1].trim(),
                        Integer.valueOf(rs[2].trim()),
                        Long.valueOf(rs[3].trim()),
                        Long.valueOf(rs[4].trim()),
                        Long.valueOf(rs[5].trim()),
                        ts));
            }
        }
        return ret;
    }

    public  List<String> getGroupOffset(String zookeeper, String group) throws IOException, InterruptedException {
        String cmd = String.format("%s --zookeeper %s --group %s --describe",
                basicCmd, zookeeper,group);
        return  command(cmd);
    }


    List<String> command(String cmd) throws IOException, InterruptedException {
        Process p = Runtime.getRuntime().exec(cmd);
        String line;
        List<String> output = Lists.newArrayList();


        BufferedReader input = new BufferedReader(new InputStreamReader(p.getInputStream()));

        while ((line = input.readLine()) != null) {
            output.add(line);
        }
        input.close();
        return output;
    }

    public List<String> getConsumerGroup(String zookeeper) throws IOException, InterruptedException {
        String cmd = String.format("%s --zookeeper %s --list", basicCmd, zookeeper);
        return command(cmd);
    }
}
