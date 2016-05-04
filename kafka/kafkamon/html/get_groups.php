<?php


require 'kafkaSql.php';

$cluster=$_GET['cluster'];

$db = make_DB_name($cluster);

if(!isset($db))
    exit();

$sql = "show tables in " . $db;

echo kafka_exec_sql($sql);

?>
