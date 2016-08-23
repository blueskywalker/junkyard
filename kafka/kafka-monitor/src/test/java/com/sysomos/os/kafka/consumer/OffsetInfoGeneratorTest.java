package com.sysomos.os.kafka.consumer;

import com.sysomos.os.kafka.db.KafkaDatabase;
import com.sysomos.os.kafka.db.KafkaJDBCFactory;
import org.junit.Before;
import org.junit.Test;

import java.sql.SQLException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

/**
 * Created by kkim on 5/4/16.
 */
public class OffsetInfoGeneratorTest {

    KafkaJDBCFactory factory;
    KafkaDatabase db;
    String kafkaHome="/Users/kkim/local/share/kafka_2.11-0.9.0.1";
    private  ExecutorService service;
    @Before
    public void setup() throws SQLException, ClassNotFoundException {
        factory = new KafkaJDBCFactory();
        factory.setUrl("jdbc:h2:file:./kafkadb.db");
        factory.setDriverClass("org.h2.Driver");
        db = KafkaDatabase.build(factory);
        service = Executors.newCachedThreadPool();
    }

    @Test
    public void testGenerator() throws SQLException, InterruptedException {
        OffsetInfoGenerator generator = new OffsetInfoGenerator(service, db, kafkaHome);

        generator.run();
    }
}