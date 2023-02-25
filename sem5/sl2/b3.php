<p><h2>Number of positives , negatives and zeroes : </h2></p>
<hr>

<form method="post" action="b3.php" >
    <label for="a"> Number : </label>
    <input type="text" name ="a">
    <br>
    <input type="submit" name="submit" >
</form>

<?php

if(isset($_POST['submit']))
{
    $a = $_POST['a'] ;
    $arr = explode(' ' , $a) ;
    $n = count($arr) ;

    $zero = 0 ;
    $pos = 0 ;
    $neg = 0 ;

    for($i =0 ; $i <$n ; $i++)
    {
        $x = $arr[$i] ;
        if($x == 0)
        {
            $zero += 1 ;
        }
        else if($x > 0)
        {
            $pos += 1 ;
        }
        else 
        {
            $neg += 1 ;
        }
    }

    echo "<b>Count : </b> <br>Zeroes : $zero <br>Positive : $pos <br>Negative : $neg " ;
}

?>