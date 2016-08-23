package com.sysomos.os.kafka.resources;

import com.codahale.metrics.annotation.Timed;
import com.sysomos.os.kafka.consumer.ConsumerGroupInfo;
import com.sysomos.os.kafka.db.KafkaDatabase;
import com.sysomos.os.kafka.model.OffsetInfo;

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

@Path("/status")
@Produces(MediaType.APPLICATION_JSON)
public class OffsetStatusResource {

    private final KafkaDatabase db;

    public OffsetStatusResource(KafkaDatabase db) {
        this.db = db;
    }

    @GET
    @Timed
    public List<OffsetInfo> getList(@QueryParam("cluster") String cluster, @QueryParam("group") String group) throws SQLException {
        return db.getStatus(cluster,group);
    }
}
