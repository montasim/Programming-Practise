<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php

    $num = array(1,2,3,4,5,6,7,8,9,0);

    sort($num);   //  sort(variable_name) function is used to sort array size

    for ($i=0; $i < count($num) ; $i++) { 
        echo "$num[$i] <br>";
    }
    ?>
</body>
</html>