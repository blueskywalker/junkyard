package com.sysomos.os.kafka.resources;

import com.sysomos.os.kafka.db.KafkaDatabase;
import com.sysomos.os.kafka.model.Cluster;
import io.dropwizard.testing.junit.ResourceTestRule;
import org.junit.After;
import org.junit.Before;
import org.junit.ClassRule;
import org.junit.Test;

import static org.assertj.core.api.Assertions.assertThat;
import static org.mockito.Matchers.eq;
import static org.mockito.Mockito.*;

/**
 * Created by kkim on 4/27/16.
 */
public class ClusterResourceTest {
    private static final String name="osdev";
    private static final String zoo="devkf354.os.dev.yyz.corp.pvt:2181,devkf353.os.dev.yyz.corp.pvt:2181,devkf351.os.dev.yyz.corp.pvt:2181,devkf350.os.dev.yyz.corp.pvt:2181,devkf352.os.dev.yyz.corp.pvt:2181";

    private static final KafkaDatabase database = mock(KafkaDatabase.class);

    @ClassRule
    public static final ResourceTestRule resources = ResourceTestRule.builder()
            .addResource(new ClusterResource(database)).build();


    private final Cluster cluster = new Cluster(name,zoo);

    @Before
    public void setup() {

        
    }

    @After
    public void tearDown() {
        reset(database);
    }

    @Test
    public void testGetCluster() {
        resources.client().target("/cluster").request();
        //System.out.println(cluster);
        //assertThat(resources.client().target("/cluster").request().get(Cluster.class)).isEqualTo(cluster);
        //verify(dao).getCluster(name);
    }

    public void testList() {

    }

}