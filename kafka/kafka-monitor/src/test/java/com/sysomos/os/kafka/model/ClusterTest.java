package com.sysomos.os.kafka.model;

import com.fasterxml.jackson.databind.ObjectMapper;
import io.dropwizard.jackson.Jackson;
import org.junit.Test;

import static io.dropwizard.testing.FixtureHelpers.fixture;
import static org.assertj.core.api.Assertions.assertThat;


/**
 * Created by kkim on 4/27/16.
 */
public class ClusterTest {

    private static final ObjectMapper MAPPER = Jackson.newObjectMapper();
    private static final String name="firehose";
    private static final String zoo="kfp001.grid.prod.yyz.corp.pvt:2181,kfp002.grid.prod.yyz.corp.pvt:2181,kfp003.grid.prod.yyz.corp.pvt:2181,kfp004.grid.prod.yyz.corp.pvt:2181,kfp005.grid.prod.yyz.corp.pvt:2181";

    public void setup() {

    }
    @Test
    public void serializedToJSON() throws Exception {
        final Cluster firehose = new Cluster(name,zoo);
        final String expected = MAPPER.writeValueAsString(
                MAPPER.readValue(fixture("fixtures/cluster.json"), Cluster.class));

        assertThat(MAPPER.writeValueAsString(firehose)).isEqualTo(expected);
    }

    @Test
    public void deserializesFromJSON() throws Exception {
        final Cluster cluster = new Cluster(name,zoo);
        assertThat(MAPPER.readValue(fixture("fixtures/cluster.json"),Cluster.class)).isEqualTo(cluster);
    }


}