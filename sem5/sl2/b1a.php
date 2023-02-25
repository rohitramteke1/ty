<form method="post" action="b1a.php">
<br>
<label for="quantity">Quantity   : </label>
<input type="number" name ="quantity">
<br>
<label for="rate">Price    : </label>
<input type="number" name ="rate">
<br>
<input type="submit" name="submit" >
</form>



<?php

if(isset($_POST['submit']))
{
    echo "<hr><hr>" ;
    $x = $_POST['quantity']  ;
    $y = $_POST['rate'] ;

    if($x > 100)
    {
        $res = $x*$y*(0.9) ;
        echo "Net Amount (10% discounted): ".$res ;
    }
    else
    {
        $res = $x*$y ;
        echo "Net Amount : ".$res ;
    }
}

?>