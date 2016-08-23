package com.sysomos.os.kafka.monitor.main;


import com.sysomos.os.kafka.conf.KafkaMonitoringConfiguration;

import com.sysomos.os.kafka.consumer.OffsetInfoGenerator;
import com.sysomos.os.kafka.db.KafkaDatabase;
import com.sysomos.os.kafka.healthCheck.ClusterServiceCheck;
import com.sysomos.os.kafka.resources.ClusterResource;
import com.sysomos.os.kafka.resources.ConsumerGroupResource;
import com.sysomos.os.kafka.resources.OffsetStatusResource;
import com.sysomos.os.kafka.resources.TimeseriesOffsetResource;
import io.dropwizard.Application;
import io.dropwizard.assets.AssetsBundle;

import io.dropwizard.setup.Bootstrap;
import io.dropwizard.setup.Environment;

import io.dropwizard.forms.MultiPartBundle;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.sql.SQLException;
import java.util.Timer;
import java.util.TimerTask;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

/**
 * Created by kkim on 4/26/16.
 */
public class Main extends Application<KafkaMonitoringConfiguration> {
    private static final Logger LOGGER = LoggerFactory.getLogger(Main.class);

    @Override
    public String getName() {
        return "Kafka-Monitor";
    }

    public void initialize(Bootstrap<KafkaMonitoringConfiguration> bootstrap) {
        bootstrap.addBundle(new AssetsBundle("/assets","/","index.html"));
        bootstrap.addBundle(new MultiPartBundle());
    }

    private KafkaDatabase db;
    private String kafkaHome;
    private  final ExecutorService service;

    public Main() {
        service = Executors.newCachedThreadPool();
    }

    @Override
    public void run(KafkaMonitoringConfiguration configuration, Environment environment) throws Exception {
        db = KafkaDatabase.build(configuration.getDatabase());
        kafkaHome = configuration.getKafkaHome();

        environment.jersey().register(new ClusterResource(db));
        environment.jersey().register(new ConsumerGroupResource(db));
        environment.jersey().register(new OffsetStatusResource(db));
        environment.jersey().register(new TimeseriesOffsetResource(db));
        environment.healthChecks().register("clusterdb",new ClusterServiceCheck(db));


        Timer timer = new Timer();
        timer.scheduleAtFixedRate(new TimerTask() {
            @Override
            public void run() {
                try {
                    new OffsetInfoGenerator(service,db, kafkaHome).run();
                } catch (SQLException e) {
                    LOGGER.error(e.getMessage(),e);
                } catch (InterruptedException e) {
                    LOGGER.error(e.getMessage(),e);
                }
            }
        }, 0, 2*60*1000);

        Runtime.getRuntime().addShutdownHook(new Thread() {
            @Override
            public void run() {
                timer.cancel();
            }
        });
    }

    public static void main(String[] args) {

        try {
            new Main().run(args);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
