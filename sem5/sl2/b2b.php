<p><h2>Fibonacci Series : </h2></p>
<hr>

<form method="post" action="b2b.php" >
    <label for="a"> Fibo. Upto  : </label>
    <input type="number" name ="a">
    <br>
    <input type="submit" name="submit" >
</form>


<?php

if(isset($_POST['submit']))
{
    $n = $_POST['a'] ;
    $first = 0 ;
    $second = 1 ;
    $temp = $first +$second ;
    echo $first." ".$second." " ;

    while($temp <= $n)
    {
        echo $temp." " ;
        $first = $second ;
        $second = $temp ;
        $temp = $first + $second ;

    }
}

?>