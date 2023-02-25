<?php

class Student
{
    public $roll ;
    public $name ;
    public $branch ;
    public $year ;

    function setdata($roll , $name  ,$branch , $year)
    {
        $this->roll = $roll ;
        $this->name = $name ;
        $this->branch = $branch ;
        $this->year = $year ;

    }

    function getdata($index)
    {
        echo "<b>Student ".$index ." : </b><br><br>" ;
        echo "PRN : ".$this->roll."<br>" ;
        echo "Name : ".$this->name."<br>" ;
        echo "Branch : ".$this->branch."<br>" ;
        echo "Year : ".$this->year."<br><br><hr>" ;

    }

}

        $s1 = new Student() ;
        $s2 = new Student() ;
        $s3 = new Student() ;

        echo "<h2>Student Info :</h2><br><hr>" ;
        $s1 -> setdata(1 , "Arun" , "Computer" , 1) ;
        $s2 -> setdata(2 , "Binod" , "ENTC" , 2) ;
        $s3 -> setdata(3 , "Chinmay" , "Civil" , 3) ;

        $s1 -> getdata(1) ;
        $s2 -> getdata(2) ;
        $s3 -> getdata(3) ;

?>