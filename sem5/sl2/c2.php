<html>

<body>

<?php

$arr1= array("<b>Country</b>"=>"<b>City</b>" , "India"=>"New Delhi", "Uk" => "London", "UAE" => "Dubai" , "Austria" => "Paris");
$twod_arrray = array();
echo"<table border='3px' cellpadding='5px' cellspacing='0'>";

foreach($arr1 as $key => $val){
    $a = array();
    $a[0] = $key;
    $a[1] = $val;
    array_push($twod_arrray,$a);
}

foreach($twod_arrray as $val){
    echo"<tr>";
    echo"<td>".$val[0]."</td>";
    echo"<td>".$val[1]."</td>";
    echo"</tr>";

}

echo"</table>";

?>
</body>
</html>