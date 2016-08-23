package com.sysomos.os.kafka.resources;

import com.codahale.metrics.annotation.Timed;
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
 * Created by kkim on 5/5/16.
 */
@Path("/timeseries")
@Produces(MediaType.APPLICATION_JSON)

public class TimeseriesOffsetResource {
    private final KafkaDatabase db;


    public TimeseriesOffsetResource(KafkaDatabase db) {
        this.db = db;
    }

    @GET
    @Timed
    public List<OffsetInfo> timeseries(@QueryParam("cluster") String cluster,
                                       @QueryParam("group") String group,
                                       @QueryParam("topic") String topic,
                                       @QueryParam("period")Integer period) throws SQLException {

        return db.select(cluster,group,topic,period);
    }
}
