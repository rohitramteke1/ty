<form method="post" action="b7.php">

    <label for="a" >A : </label>
    <input type="text" name ="a"><br>
    <label for="b" >B : </label>
    <input type="text" name ="b">
    
    <br><br>
    <button type="submit" name="value">call by value </button><br>
    <button type="submit" name="reff">call by refference </button>
    <hr>

</form>



<?php

function swap_byvalue($first , $second)
{
    $temp = $first ;
    $first = $second ;
    $second = $temp ;
    echo "After Swap_by_value(echo inside function) :- \n\tFirst : ".$first." , Second : ".$second."\n<br>" ;
}

function swap_byreff(&$first , &$second)
{
    $temp = $first ;
    $first = $second ;
    $second = $temp ;
    echo "After Swap_by_reff (inside function) :- \n\tFirst : ".$first." , Second : ".$second."\n<br>" ;
}

if(isset($_POST['value']))
{
    $a = $_POST['a'] ;
    $b = $_POST['b'] ;
    echo "Before Swap :- \n\tFirst : ".$a." , Second : ".$b."\n<br>" ;
    swap_byvalue($a ,$b) ;
    echo "After Swap_by_value(echo outside function) :- \n\tFirst : ".$a." , Second : ".$b."\n<br>" ;
}

if(isset($_POST['reff']))
{
    $a = $_POST['a'] ;
    $b = $_POST['b'] ;
    echo "Before Swap :- \n\tFirst : ".$a." , Second : ".$b."\n<br>" ;
    swap_byreff($a ,$b) ;
    echo "After Swap_by_reff(echo outside function) :- \n\tFirst : ".$a." , Second : ".$b."\n<br>" ;
}


?>