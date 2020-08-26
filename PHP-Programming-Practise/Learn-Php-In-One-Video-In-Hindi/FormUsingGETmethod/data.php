<?php

$servername = "localhost";
$username = "root";
$password = "";
$database = "FormUsingGET";

//  creating database connection
$connect = mysqli_connect($servername, $username, $password, $database);

//  check connection
if (!$connect) {
    die("Failed to connect". mysqli_connect_error());
    echo "<br>";
}
else {
    echo "Connection successful";
    echo "<br>";
}

//  insert into database
$sql = "INSERT INTO `users` (`Serial`, `Name`, `Age`, `Salary`) VALUES ('4', 'Shuvo', '23', '33330')";

//  checking insertion
if(mysqli_query($connect, $sql)){
    echo "Success";
    echo "<br>";
}
else {
    echo "Error ". mysqli_error($connect);
    echo "<br>";
}

//  close connection
mysqli_close($connect);
?>