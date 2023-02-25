<p><h2>Sum of Digits : </h2></p>
<hr>

<form method="post" action="b2a.php" class='form' >
    <label for="a"> A   : </label>
    <input type="number" name ="a">
    <br>
    <input type="submit" name="submit" >
</form>

<?php

if(isset($_POST['submit']))
{
    $x = (int)$_POST['a'] ;
    $sum = 0 ;

    while($x > 0)
    {
        $res = $x%10 ;
        $sum += $res ;
        $x /= 10 ; 
    }

    echo "<hr><b>OUTPUT : </b><br>Sum of Digits of ".$_POST['a']." = ".$sum ;

}

?>