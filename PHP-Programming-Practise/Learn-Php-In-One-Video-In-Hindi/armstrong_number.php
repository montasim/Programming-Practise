<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php
    $num = 153;
    $sum = 0;
    $temp = num;
    while ($temp % 10) {
        $rem = $temp % 10;
        $sum = $sum + $rem * $rem * $rem;
        $temp = $temp / 10;
    }
    if ($num == $sum) {
        echo "Armstrong number";
    }
    else {
        echo "Not an Armstrong number";
    }
    ?>
</body>
</html>