package com.sysomos.os.kafka.resources;

import com.codahale.metrics.annotation.Timed;
import com.sysomos.os.kafka.consumer.ConsumerGroupInfo;
import com.sysomos.os.kafka.db.KafkaDatabase;

import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.QueryParam;
import javax.ws.rs.core.MediaType;
import java.sql.SQLException;
import java.util.List;

/**
 * Created by kkim on 5/3/16.
 */
@Path("/consumer")
@Produces(MediaType.APPLICATION_JSON)
public class ConsumerGroupResource {

    final KafkaDatabase db;

    public ConsumerGroupResource(KafkaDatabase db) {
        this.db = db;
    }

    @GET
    @Timed
    public List<String> getList(@QueryParam("cluster") String cluster) throws SQLException {
        List<String> result = db.getTables(cluster);
        System.out.println(result);
        return result;
    }
}
