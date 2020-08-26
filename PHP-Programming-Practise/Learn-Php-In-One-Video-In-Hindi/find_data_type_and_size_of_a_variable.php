<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php
    // var_dump((variable_name)) is used to find datatype and size of a variable

    $int = 10;
    $float = 99.99;
    $char = 'M';
    $string = "Hello";

    echo "integer = $int<br>";
    echo "float = $float<br>";
    echo "char = $char<br>";
    echo "string = $string<br>";

    var_dump(($int));
    echo "<br>"; 
    var_dump(($float));
    echo "<br>";
    ?>
</body>
</html>