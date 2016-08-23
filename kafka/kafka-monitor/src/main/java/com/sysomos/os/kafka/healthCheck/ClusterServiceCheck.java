package com.sysomos.os.kafka.healthCheck;


import com.codahale.metrics.health.HealthCheck;
import com.sysomos.os.kafka.db.KafkaDatabase;

import javax.ws.rs.Path;
import java.util.List;

/**
 * Created by kkim on 5/3/16.
 */
public class ClusterServiceCheck extends HealthCheck {
    final KafkaDatabase db;

    public ClusterServiceCheck(KafkaDatabase db) {
        this.db = db;
    }

    @Override
    protected Result check() throws Exception {
        db.getTables("CLUSTER");
        return Result.healthy();
    }
}
