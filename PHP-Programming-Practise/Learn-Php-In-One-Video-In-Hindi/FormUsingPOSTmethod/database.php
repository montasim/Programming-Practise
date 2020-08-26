<?php
$servername = "localhost";
$serverusername = "root";
$serveruserpassword = "";
$databasename = "FormUsingPOST";

$connectdatabse = mysqli_connect($servername, $serverusername, $serveruserpassword, $databasename);

//  check database connection
if (!$connectdatabse) { //$connectdatabse returns 1. so if not seccessfull it will show error
    die("Database connection unsuccessful <br>". mysqli_connect_error($connectdatabse));
    echo "<br>";
}
else {
    echo "Database connection successful <br>";
}

//  insert into database
$insertintodatabase = "INSERT INTO `users` (`Serial`, `Name`, `Age`, `Salary`) VALUES ('4', 'Shuvo', '23', '44444');";

if(mysqli_query($connectdatabse, $insertintodatabase)){
    echo "Success <br>";
}
else {
    echo " Error <br>";
}

?>

