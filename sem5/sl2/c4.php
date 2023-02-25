
        <h1>Login Page</h1>
        <form method="post" action="c4.php" >
        <label for="user"><b>Username : </b></label>
        <input type="text" name="user">
        <br>
        <label for="pswd"><b>Password : </b></label>
        <input type="text" name="pswd">
        <br>
        <input type="submit" name="button" >
        </form> 


<?php

if(isset($_POST['button']))
{
    $x = $_POST['user'] ;
    $y = $_POST['pswd'];
    
    if($x=='Galgotias' && $y == 'university')
    {
        echo "<script> location.href='welcome.html'; </script>";
    }
    else
    {
        echo "<script> location.href='sorry.html'; </script>";
    }
}
?>

