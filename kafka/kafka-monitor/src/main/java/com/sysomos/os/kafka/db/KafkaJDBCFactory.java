package com.sysomos.os.kafka.db;

import com.fasterxml.jackson.annotation.JsonProperty;
import io.dropwizard.metrics.MetricsFactory;
import org.apache.commons.lang3.builder.ToStringBuilder;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import javax.validation.Valid;
import javax.validation.constraints.NotNull;

/**
 * Created by kkim on 4/28/16.
 */
public class KafkaJDBCFactory {
    private static final Logger LOGGER = LoggerFactory.getLogger(KafkaJDBCFactory.class);

    @Valid
    @NotNull
    private String driverClass;

    @Valid
    @NotNull
    private String url;

    @JsonProperty
    public String getDriverClass() {
        return driverClass;
    }

    @JsonProperty
    public void setDriverClass(String driverClass) {
        this.driverClass = driverClass;
    }

    @JsonProperty
    public String getUrl() {
        return url;
    }

    @JsonProperty
    public void setUrl(String url) {
        this.url = url;
    }


    @Override
    public String toString() {
        return new ToStringBuilder(this)
                .append("driverClass", driverClass)
                .append("url", url)
                .toString();
    }
}
