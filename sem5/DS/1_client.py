import Pyro4 
import os 
import datetime 

Client = Pyro4.Proxy("PYRONAME:RMI.concatter")    
name =input("What is your name? ").strip() 
now=datetime.datetime.now() 
print('date: '+now.strftime('%d-%m-%y')+' Time: '+now.strftime('%H:%M:%S')) 
print(Client.get_usid(name)) 

""" 
print("Enter the number of calculations to be done") 
n=int(input("Enter n: ")) 
while (n>0):

    n=n-1 
    print("Enter number for desired calculations: \n" +'1.ADD \n'+ '2.SUBTRACT  \n'+  '3.MULTIPLY  \n'+  '4.DIVISION  \n'+ '5.EXPONENTIATION \n')   
    c=int(input('Enter your choice: '))    
    if (c==1):      
        print(Client.add(a,b))   
    elif (c==2):     
        print(Client.subtract(a,b))   
    elif (c==3):     
        print(Client.multiply(a,b))   
    elif (c==4):     
        print(Client.division(a,b))   
    elif (c==5):     
        print(Client.exp(a))               
    else:                             
        print('invalid input')
"""
print("Enter Details :- ")
a = input("Enter a: ") 
b = input("Enter b: ") 

print(Client.concat(a,b))



    