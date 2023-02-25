<form method="post" action="b5.php" >
    <label for="a"> Input String   : </label>
    <input type="text" name ="a">
    <br><br>
    <button type="submit" name="strlen" > String Length </button> 
    <button type="submit" name="strrev" > String Reverse</button>
    <button type="submit" name="strupper" > Convert Uppercase </button>
    <button type="submit" name="strlower" > Convet Lowercase </button>
    <button type="submit" name="replace" > String Replace </button>
    <hr>
</form>


<?php

if(isset($_POST['strlen']))
{
    $str = $_POST['a'] ;
    echo "Length of String : ".strlen($str) ;
}
elseif(isset($_POST['strrev']))
{
    $str = $_POST['a'] ;
    echo "Reversed String : ".strrev($str) ;
}

elseif(isset($_POST['strupper']))
{
    $str = $_POST['a'] ;
    echo "String in Uppercase : ".strtoupper($str) ;
}
elseif(isset($_POST['strlower']))
{
    $str = $_POST['a'] ;
    echo "String in Uppercase : ".strtolower($str) ;
}

elseif(isset($_POST['replace']))
{
    $str = $_POST['a'] ;

    echo "Replacing I with You : ".str_replace("i" , "You" ,$str) ;
}


?>