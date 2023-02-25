#include <iostream>
using namespace std ;

void calc(int a )
{
    int result = a*a ;
    cout<< result ;
}

void calc(int a , int b)
{
    int result = a + b ;
    cout<< result ;
}

int main()
{
    calc(2,3) ;
    return 0 ;
    
}