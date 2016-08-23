package com.sysomos.os.kafka.model;

import java.util.UUID;

/**
 * Created by kkim on 4/28/16.
 */
public abstract class BaseModel {

    public UUID randomUUID() {
        return UUID.randomUUID();
    }
}
