package com.sysomos.os.kafka.db;

import com.google.common.collect.Lists;

import com.sysomos.os.kafka.model.OffsetInfo;
import com.sysomos.os.kafka.resources.ClusterResource;
import org.assertj.core.data.Offset;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.sql.*;
import java.util.*;
import java.util.stream.Collectors;

/**
 * Created by kkim on 4/28/16.
 */
public class KafkaDatabase {
    private static final Logger LOGGER = LoggerFactory.getLogger(KafkaDatabase.class);
    private final KafkaJDBCFactory factory;
    private final Connection connection;

    private KafkaDatabase(KafkaJDBCFactory factory) throws ClassNotFoundException, SQLException {
        this.factory = factory;
        Class.forName(factory.getDriverClass());
        connection = DriverManager.getConnection(factory.getUrl(), "sa", "");
    }

    static KafkaDatabase instance;

    public static synchronized KafkaDatabase build(KafkaJDBCFactory factory) throws SQLException, ClassNotFoundException {
        if (instance == null) {
            instance = new KafkaDatabase(factory);
        }
        return instance;
    }



    public String schemaName(String name) {
        return String.format("kafka_%s",name);
    }

    public String clusterName(String name) {
        if (name.startsWith("kafka__"))
            return name.substring(6);

        return null;
    }

    public List<String> getSchemas() throws SQLException {
        Statement stat = connection.createStatement();
        ResultSet rs = stat.executeQuery("show schemas;");
        ArrayList<String> ret = new ArrayList<String>();

        while (rs.next()) {
            String cluster = clusterName(rs.getString("SCHEMA_NAME"));
            if(cluster!=null)
                ret.add(cluster);
        }
        stat.close();
        return ret;
    }

    public void createSchema(String name) throws SQLException {
        Statement stat = connection.createStatement();
        stat.execute(String.format("CREATE SCHEMA IF NOT EXISTS \"%s\";", schemaName(name)));
        stat.close();
    }

    public void dropSchema(String name) throws SQLException {
        Statement stat = connection.createStatement();
        stat.execute(String.format("DROP SCHEMA IF EXISTS %s;", schemaName(name)));
        stat.close();
    }

    public void createTable(String schema, String table) throws SQLException {
        Statement stat = connection.createStatement();
        String ddl = String.join(" ",
                "CREATE TABLE IF NOT EXISTS \"%s\".\"%s\" (",
                "topic VARCHAR(50) NOT NULL,",
                "partition INT NOT NULL,",
                "head BIGINT ,",
                "logsize BIGINT ,",
                "lag BIGINT ,",
                "timestamp INT NOT NULL);",
                "CREATE INDEX IF NOT EXISTS \"%s_index\" ON \"%s\".\"%s\" (timestamp);");

        String name = schemaName(schema);
        String sql = String.format(ddl,name,table,table,name,table);
        stat.execute(sql);
        stat.close();
    }

    public List<String> getTables(String schema) throws SQLException {
        Statement stat = connection.createStatement();
        ResultSet rs = stat.executeQuery(String.format("show tables from \"%s\"", schemaName(schema)));
        ArrayList<String> ret = new ArrayList<String>();

        while (rs.next()) {
            ret.add(rs.getString("TABLE_NAME"));
        }
        stat.close();
        return ret;
    }

    public void dropTable(String schema, String table) throws SQLException {
        Statement stat = connection.createStatement();
        String ddl = String.join(" ",
                "DROP TABLE IF EXISTS \"%s\".\"%s\";",
                "DROP INDEX IF EXISTS \"%s_index\"");
        stat.execute(String.format(ddl, schemaName(schema),table,table));
        stat.close();
    }


    public Statement getStatement() throws SQLException {
        return connection.createStatement();
    }

    public void insert(String schema, String table, List<OffsetInfo> values) throws SQLException {
        String tmpl = String.join(" ",
                "INSERT INTO \"%s\".\"%s\" (topic,partition,head,logsize,lag,timestamp)",
                "VALUES (?,?,?,?,?,?);");
        String sql = String.format(tmpl, schemaName(schema),table);
        PreparedStatement stat = connection.prepareStatement(sql);
        for(OffsetInfo value : values) {
            stat.setString(1, value.getTopic());
            stat.setInt(2, value.getPartition());
            stat.setLong(3, value.getOffset());
            stat.setLong(4, value.getLogsize());
            stat.setLong(5, value.getLag());
            stat.setInt(6, value.getTimestamp());
            stat.executeUpdate();
        }
        stat.close();
    }

    public List<OffsetInfo> getStatus(String schema,String table) throws SQLException {
        String tmpl = String.join(" ",
                "SELECT topic,partition,head,logsize,lag,timestamp",
                "FROM \"%s\".\"%s\"",
                "WHERE timestamp > %d;");

        int ago = (int)(System.currentTimeMillis()/1000) - 120;

        String sql = String.format(tmpl,
                schemaName(schema),table,ago);

        Statement stat = connection.createStatement();
        ResultSet rs = stat.executeQuery(sql);
        List<OffsetInfo> ret = Lists.newArrayList();

        while(rs.next()) {
            ret.add(new OffsetInfo(
                    rs.getString(1),
                    rs.getInt(2),
                    rs.getLong(3),
                    rs.getLong(4),
                    rs.getLong(5),
                    rs.getInt(6)));
        }

        stat.close();

        Map<Integer,List<OffsetInfo>> group=ret.stream().collect(Collectors.groupingBy(OffsetInfo::getTimestamp));
        if (group.keySet().size()>1) {
            List<Integer> times = group.keySet().stream().sorted().collect(Collectors.toList());
            return group.get(times.get(times.size()-1));
        }
        return ret;
    }

    public List<OffsetInfo> select(String schema,String table,String topic,int period) throws SQLException {
        String tmpl = String.join(" ",
                "SELECT topic,sum(head) as head,sum(logsize) as logsize,sum(lag) as lag, timestamp",
                "FROM \"%s\".\"%s\"",
                "WHERE timestamp > %d AND topic = '%s'",
                "GROUP BY timestamp");

        int ago = (int) (System.currentTimeMillis()/1000)  - period;
        String sql = String.format(tmpl,schemaName(schema),table,ago,topic);
        Statement stat = connection.createStatement();
        ResultSet rs = stat.executeQuery(sql);
        List<OffsetInfo> output = Lists.newArrayList();

        while(rs.next()) {
            output.add(new OffsetInfo(
                    rs.getString(1),
                    null,
                    rs.getLong(2),
                    rs.getLong(3),
                    rs.getLong(4),
                    rs.getInt(5)));
        }
        stat.close();
        return output;

    }
    public void close() throws SQLException {
        connection.close();
    }

    public List<String> getZookeeper(String cluster) throws SQLException {
        Statement stat = connection.createStatement();
        String sql = String.format("SELECT zookeeper FROM \"%s\".\"%s\" WHERE name= '%s';",
                ClusterResource.schema, ClusterResource.table, cluster);
        LOGGER.info(sql);
        ResultSet result = stat.executeQuery(sql);

        List<String> output = Lists.newArrayList();
        while (result.next()) {
            output.add(result.getString("ZOOKEEPER"));
        }
        stat.close();
        return output;
    }
}
