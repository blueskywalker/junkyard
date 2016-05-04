<?php

require 'kafkaSql.php';

$cluster = $_GET['cluster'];
$table = $_GET['group'];
$period = $_GET['period'] * 60; // min to sec

if(!isset($cluster)||!isset($table)||!isset($period))
    exit();

$db = make_DB_name($cluster);
$ago = time() - $period;

$sql = sprintf("SELECT * FROM `%s`.`%s` WHERE timestamp > %d;",$db,$table,$ago);

echo kafka_exec_sql($sql);
?>
