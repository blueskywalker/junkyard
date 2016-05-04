<?php

require 'kafkaSql.php';

$sql = $_GET['sql'];

if(!isset($sql))
    exit();

echo kafka_exec_sql($sql);
?>
