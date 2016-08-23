package com.sysomos.os.kafka.db;

import com.sysomos.os.kafka.model.Cluster;
import com.sysomos.os.kafka.resources.ClusterResource;
import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

import java.sql.SQLException;
import java.util.List;

/**
 * Created by kkim on 4/28/16.
 */
public class KafkaDatabaseTest {

    KafkaJDBCFactory factory;
    KafkaDatabase db;

    @Before
    public void setup() throws SQLException, ClassNotFoundException {
        factory = new KafkaJDBCFactory();
        factory.setUrl("jdbc:h2:file:./kafkadb.db");
        factory.setDriverClass("org.h2.Driver");
        db = KafkaDatabase.build(factory);
    }

    @Test
    public void testListShema() throws SQLException {
        for (String s : db.getSchemas()) {
            System.out.println(s);
        }
    }

    @Test
    public void testListTable() throws SQLException {
        for (String s : db.getTables("cluster")) {
            System.out.println(s);
        }
    }


    @Test
    public void testCreateSchema() throws SQLException {

        String name = "cluster";
        db.createSchema(name);
        List<String> schemas = db.getSchemas();

        Assert.assertTrue(schemas.contains(name.toUpperCase()));
    }

    @Test
    public void testDropSchema() throws SQLException {
        String name = "cluster";
        db.dropSchema(name);
        List<String> schemas = db.getSchemas();

        Assert.assertFalse(schemas.contains(name.toUpperCase()));
    }

    @Test
    public void testCluster() throws SQLException {
        ClusterResource cluster = new ClusterResource(db);
        cluster.dropTable();
        cluster.initialize();
        cluster.insertCluster("production","localhost:2181");
        List<Cluster> clusters= cluster.getList();
        System.out.println(clusters.toString());
    }

    @Test
    public void testZookeper() throws SQLException {
        for(String  z: db.getZookeeper("os-dev")) {
            System.out.println(z);
        }
    }

    @Test
    public void testCreateTable() throws Exception {

        db.createSchema("os-dev");
        db.dropTable("os-dev","firehose");
        db.createTable("os-dev","firehose");
    }

    @Test
    public void testDropTable() throws Exception {
        db.dropTable("os-dev","firehose");
        db.createSchema("os-dev");
    }

    @Test
    public void testGetStatus() throws SQLException {

        System.out.println(db.getStatus("os-dev","FirehoseSinker"));
    }
}