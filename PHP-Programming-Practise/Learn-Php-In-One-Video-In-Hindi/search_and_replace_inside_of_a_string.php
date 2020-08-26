<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php

    $name = "This is a string";   //  NULL keyword is used to declare NULL value

    echo str_replace('is', 'are', $name), "<br>";   //  str_replace('value_to_search, 'value_to_replace', $variable_name) is used to search inside a string and replace the search value if matched
    ?>
</body>
</html>