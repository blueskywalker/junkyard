<?php
function make_DB_name($cluster) {
    return 'kafka_' . $cluster;
}

function kafka_exec_sql($sql) {
    $servername = "devnn02.os.dev.yyz.corp.pvt";
    $username   = "mysql";
    $password   = "mysql";



    $conn = new mysqli($servername,$username, $password);

    // Check connection
    if (mysqli_connect_errno()) {
        die("Connection failed: " . mysqli_connect_error());
    }

    $result = mysqli_query($conn,$sql);

    if (!$result) {
        echo "DB error, could not get data\n";
        echo "MySQL Error: " . mysqli_error($conn);
        exit;
    }

    $output=array();

    while($row = mysqli_fetch_assoc($result)) {
        array_push($output,$row);
    }

    mysqli_close($conn);
    return json_encode($output);
}
?>
