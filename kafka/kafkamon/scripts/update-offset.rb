#!/usr/bin/env ruby

require 'yaml'
require 'mysql2'

BASEDIR=File.expand_path("%s/.." % File.dirname(__FILE__))
yamlfile="%s/conf/cluster.yaml" % BASEDIR
clusters=YAML.load_file(yamlfile)['clusters']

class KafkaCluster
	CMD=BASEDIR + "/lib/kafka/bin/kafka-run-class.sh kafka.admin.ConsumerGroupCommand"
	CREATE_TABLE = %q{
				CREATE TABLE IF NOT EXISTS `%s`.`%s` (
				  `topic` VARCHAR(50) NOT NULL,
				  `partition` INT NOT NULL,
				  `offset` BIGINT NULL,
				  `logsize` BIGINT NULL,
				  `lag` BIGINT NULL,
				  `timestamp` INT NOT NULL,
				  PRIMARY KEY (`topic`, `partition`, `timestamp`));
			 }  

	attr_reader :clusters

	def initialize(c)
		@clusters=c	
		@client = Mysql2::Client.new(:host => 'localhost', :username => 'root')
		@threads=[]
		@mutex= Mutex.new
	end

	def get_schemas
		result=[]
		@client.query("show schemas").each { |v|  result << v['Database'] }
		result
	end

	def create_schema(name)
		sql="CREATE DATABASE IF NOT EXISTS kafka_%s;" % name
		@client.query(sql)
	end

	def drop_schema(name)
		sql="drop database %s;" % name
		@client.query(sql)
	end

        def schema_name_of (cluster)
		'kafka_' + cluster
	end 

        def check_schemas
		schemas= get_schemas	
		clusters.keys.each { |c| create_schema(c) if not schemas.include? schema_name_of(c) }
		dbs = schemas - clusters.keys.collect {|c| schema_name_of c}
		dbs.each { |d| drop_schema t if d.start_with? "kafka_" }
	end

	def get_tables_of (db)
		@client.select_db(db)
                key='Tables_in_'+db
		result=[]
		@client.query("show tables").each { |r|  result << r[key] } 
		result
	end

	def consumer_group_of (cluster)
		cmd="%s --zookeeper %s --list" % [CMD,cluster]
		result=%x(#{cmd})
		result.split
	end

	def get_offset_of (zoo,group)
		cmd="%s --zookeeper %s --group %s --describe" %[CMD,zoo,group]
		result =%x(#{cmd})
		result.split /\n/
	end

	def create_table (db,name)
		sql = CREATE_TABLE  % [db,name]
		@client.query(sql)
	end

	def drop_table (db,name)
		sql="drop table `%s`.`%s`;" % [db,name]
		@client.query(sql)
	end

	def insert_into (db, table, values)
		sql = %q{INSERT INTO `%s`.`%s` (topic,partition,offset,logsize,lag,timestamp) VALUES(?,?,?,?,?,?);} % [db,table]
		statment = @client.prepare(sql)
		statment.execute values[0], values[1],values[2],values[3],values[4],values[5]
	end

	def insert_offsets_of (cluster, table)
		name, zoo = cluster
		db = schema_name_of name
		puts "%s,%s" % [db,table]

		results = get_offset_of zoo, table  
		return if results[0] == "No topic available for consumer group provided" 	
		timestamp = Time.now.to_i
		results.shift
		results.each { |r| 
			values= r.split /,/
			group = values.shift
			return if group != table 
			values[5] = timestamp
			@mutex.synchronize { insert_into db, table, values }
 		}
	end

	def check_consumer_of (cluster)
		name,zookeeper = cluster
		db = schema_name_of name 
		groups=consumer_group_of zookeeper 
		tables = get_tables_of db 
		groups.each { |t| 
			create_table(db,t) if not tables.include? t 
			@threads<< Thread.new { insert_offsets_of cluster, t }
		}
		rest = tables - groups
		rest.each { |t| drop_table db, t }
	end

	def update
		@threads = []
		check_schemas
		clusters.each { |c| check_consumer_of c }
		@threads.each { |t| t.join }
	end
end

kafka=KafkaCluster.new clusters
kafka.update
