package com.sysomos.os.kafka.conf;

import com.fasterxml.jackson.annotation.JsonProperty;
import com.sysomos.os.kafka.db.KafkaJDBCFactory;
import io.dropwizard.Configuration;
import io.dropwizard.client.JerseyClientConfiguration;
import org.glassfish.jersey.client.JerseyClient;


import javax.validation.Valid;
import javax.validation.constraints.NotNull;

/**
 * Created by kkim on 4/27/16.
 */
public class KafkaMonitoringConfiguration extends Configuration {

    @Valid
    @NotNull
    private KafkaJDBCFactory database = new KafkaJDBCFactory();

    @JsonProperty("database")
    public KafkaJDBCFactory getDatabase() {
        return database;
    }

    @JsonProperty("database")
    public void setDatabase(KafkaJDBCFactory database) {
        this.database = database;
    }

    @Valid
    @NotNull
    private JerseyClientConfiguration jerseyClient = new JerseyClientConfiguration();

    @JsonProperty("jerseyClient")
    public JerseyClientConfiguration getJerseyClientConfiguration() {
        return jerseyClient;
    }

    @Valid
    @NotNull
    private String kafkaHome;

    @JsonProperty("kafka.home")
    public String getKafkaHome() {
        return kafkaHome;
    }

    @JsonProperty("kafka.home")
    public void setKafkaHome(String kafkaHome) {
        this.kafkaHome = kafkaHome;
    }
}
