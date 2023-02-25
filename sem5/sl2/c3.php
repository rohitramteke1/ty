<form method="post" action="c3.php">
    <label for="input">Input : </label>
    <input type="text" name="input">
    <br>
    <button type="submit" name="write">Write </button>
    <br>
    <button type="submit" name="append">Append</button>
    <br>
    <button type="submit" name="read">Read</button>

</form>



<?php

if(isset($_POST['write']))
{
    $txt = $_POST['input'] ;
    $file = fopen("c3.txt" , "w+") ;
    fwrite($file , $txt ) ;
    echo "<br>" ;
    echo "Written Successfully..! : <br>" ;
    fclose($file) ;
}

if(isset($_POST['append']))
{
    $txt = $_POST['input'] ;
    $file = fopen("c3.txt" , "a+") ;
    fwrite($file , " ") ;
    fwrite($file , $txt ) ;
    echo "<br>" ;
    echo "Appended Seccessfuly..! <br>" ;
    fclose($file) ;
}

if(isset($_POST['read']))
{
    $file = fopen("c3.txt" , "r") ;
    echo "<br>" ;
    echo "Text in File : <br>" ;
    echo fread($file , filesize("c3.txt")) ;
    fclose($file) ;
}



?>