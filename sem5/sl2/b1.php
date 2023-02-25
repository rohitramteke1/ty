<h2>ODD OR EVEN</h2>

    <form method="post" action="b1.php">
        <label for="input" >Input : </label>
        <input type="number" value="" name="input"/>
        <input type="submit" name="submit" />
    </form>

<?php
# $x = $_POST['input'] ......as it shows warning , as the form isnt submitted yet,,would be ok if separate php file
if(isset($_POST['submit']))
{   if($_POST['input'] < 0)
    {echo "Negative numbers invalaid here!!";}
    else if ($_POST['input']%2 == 0)
    {
        echo $_POST['input']." is Even .!" ;
        echo "<hr><hr>" ;
    }
    else
    {
        echo $_POST['input']." is Odd .!" ;
        echo "<hr><hr>" ;
    }
}

?>