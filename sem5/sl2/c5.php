
<h2>Implenting Js and forms in php .!</h2>
<hr>

<form>
        <label for='input'>INPUT : </label>
        <input type='number' name='input' value='' id='input' />
        <input type='button' value='Submit' onclick='convert();' />
        <div id='alert' style='color: red'></div>
</form>
<p id='output'></p>


<?php

    echo '<script type="text/javascript">
        function convert()
        {
            var x = document.getElementById("input").value ;
            document.getElementById("alert").innerHTML = "<br>user input : " + x ;
            const num = parseInt(x) ;
            const res = num.toString(2) ;
            document.getElementById("output").innerHTML = "Binary : " + res  ;
        }
    </script>' ;

?>


