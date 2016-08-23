package com.sysomos.os.kafka.resources;

import com.codahale.metrics.annotation.Timed;
import com.fasterxml.jackson.annotation.JsonFormat;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.google.common.collect.Sets;
import com.sysomos.os.kafka.db.KafkaDatabase;
import com.sysomos.os.kafka.model.Cluster;

import javax.ws.rs.*;
import javax.ws.rs.core.MediaType;
import java.io.IOException;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;

/**
 * Created by kkim on 4/27/16.
 */

@Path("/cluster")
@Produces(MediaType.APPLICATION_JSON)
@Consumes(MediaType.APPLICATION_JSON)
public class ClusterResource {

    final KafkaDatabase database;
    public final static String schema = "CLUSTER";
    public final static String table = "CLUSTER";

    public ClusterResource(KafkaDatabase database) {
        this.database = database;
    }


    public void initialize() throws SQLException {
        List<String> schemas = database.getSchemas();
        if (!schemas.contains(schema)) {
            database.createSchema(schema);
            createTable();
        } else {
            createTable();
        }
    }

    public String getSchema() {
        return schema;
    }

    public String getTable() {
        return table;
    }

    @GET
    @Timed
    public List<Cluster> getList() {
        ArrayList<Cluster> clusters = new ArrayList<>();

        try {
            Statement stat = database.getStatement();
            ResultSet rs = stat.executeQuery(String.format("SELECT * FROM \"%s\".\"%s\"", schema, table));

            while (rs.next()) {
                clusters.add(new Cluster(rs.getString("name"), rs.getString("zookeeper")));
            }

            stat.close();

        } catch (SQLException e) {
            e.printStackTrace();
        }
        return clusters;
    }

    public void createTable() throws SQLException {
        Statement stat = database.getStatement();
        String sql = "CREATE TABLE IF NOT EXISTS \"%s\".\"%s\" (name varchar(64) not null primary key, zookeeper varchar(2048) not null);";
        stat.execute(String.format(sql, schema, table));
        stat.close();

    }

    public void dropTable() throws SQLException {
        database.dropTable(schema, table);
    }

    @PUT
    @Timed
    public void insertCluster(@FormParam("name") String name,@FormParam("zookeeper") String zookeeper) throws SQLException {
        Statement stat = database.getStatement();
        String sql = "INSERT INTO \"%s\".\"%s\" (name ,zookeeper) VALUES ( '%s' , '%s' )";
        stat.execute(String.format(sql, schema, table, name, zookeeper));
        stat.close();
    }

    @POST
    @Timed
    public void updateCluster(@JsonFormat String json) throws SQLException, IOException {
        ObjectMapper mapper = new ObjectMapper();
        Cluster[] clusters = mapper.readValue(json,Cluster[].class);
        List<Cluster>  info = getList();
        Set<String> exists = Sets.newHashSet(info.stream().map((e)->e.getName()).collect(Collectors.toList()));

        for(Cluster c : clusters) {
            if (exists.contains(c.getName()))
                delete(c.getName());
            insertCluster(c.getName(),c.getZookeeper());
        }
        exists.removeAll(Arrays.asList(clusters).stream().map((e)->e.getName()).collect(Collectors.toList()));

        for(String c: exists) {
            delete(c);
        }
    }

    @DELETE
    @Timed
    public void delete(@QueryParam("name") String name) throws SQLException {
        Statement stat = database.getStatement();
        String sql = String.format("DELETE FROM \"%s\".\"%s\" WHERE name = '%s'",schema,table,name);
        System.out.println(sql);
        stat.execute(sql);
        stat.close();
    }

}
