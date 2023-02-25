<form method="POST" action="c1.php">

    <label for="input">INPUT : </label>
    <input type="text" name="input">
    <br><br>
    <button type="submit" name="new">Process</button>
    <hr>
</form>

<?php

if(isset($_POST['new']))
{
    $input = $_POST['input'] ;
    $arr = explode(' ' , $input) ;
    $n = count($arr) ;
    $str = "Output : " ;

    for($i=0 ; $i < $n ; $i++)
    {
        if($arr[$i] % 2 ==0)
        {
            $new[$i] = $arr[$i]/2 ;
        }
        else
        {
            $new[$i] = $arr[$i]*3 ;
        }
        
        $str .= $new[$i]." " ;
    }

    echo $str ;
    
}

?>