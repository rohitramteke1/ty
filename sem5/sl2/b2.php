<p><h1>Largest Number : </h1></p>
<hr>

<form method="post" action="b2.php" >
    <label for="a"> A   : </label>
    <input type="number" name ="a">
    <br>
    <label for="b"> B   : </label>
    <input type="number" name ="b">
    <br>
    <label for="c"> C   : </label>
    <input type="number" name ="c">
    <br>
    <input type="submit" name="submit" >
</form>


<?php

if(isset($_POST['submit']))
{
    $x = $_POST['a'] ;
    $y = $_POST['b'] ;
    $z = $_POST['c'] ;

    ($x > $y)? (print ($x >$z) ? $x." is largest of all .!" : $z." is largest of all .!") : ( print ($y >$z) ? $y." is largest of all .!" : $z." is largest of all .!")  ;

}

?>

