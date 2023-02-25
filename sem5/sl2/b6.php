<form method="post" action="b6.php">

    <label for="a" >A : </label>
    <input type="number" name ="a"><br>
    <label for="b" >B : </label>
    <input type="number" name ="b">
    
    <br><br>
    <button type="submit" name="add">Addition </button>&emsp;
    <button type="submit" name="sub">Subtraction </button>&emsp;
    <button type="submit" name="mul">Multiply </button>&emsp;
    <button type="submit" name="div">Divide </button>
    <hr>

</form>


<?php

if(isset($_POST['add']))
{
    $a = $_POST['a'] ;
    $b = $_POST['b'] ;

    $c = $a + $b ;

    echo "ADDITION : ".$c ;
}

if(isset($_POST['sub']))
{
    $a = $_POST['a'] ;
    $b = $_POST['b'] ;

    $c = $a - $b ;

    echo "SUBTRACTION : ".$c ;
}

if(isset($_POST['mul']))
{
    $a = $_POST['a'] ;
    $b = $_POST['b'] ;

    $c = $a * $b ;

    echo "MULTIPLICATION : ".$c ;
}

if(isset($_POST['div']))
{
    $a = $_POST['a'] ;
    $b = $_POST['b'] ;

    $c = $a / $b ;

    echo "DIVISION : ".$c ;
}

?>