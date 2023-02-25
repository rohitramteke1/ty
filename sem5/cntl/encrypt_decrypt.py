import math

msg = int(input("Message to be encrypted : "))
print("--->")

a = 3 
b = 5
c = 7

n = a*b

def encrypt(me) :
    x = math.pow(me , c)
    y = x/n
    return y

def decrypt(me) :
    m = me*n
    z = round(math.pow(m , 1/c))
    return z


print("Original message : " , msg) 
p = encrypt(msg)
print("Encrypted message is : " , p)
q = decrypt(p)
print("Message After Decrypting : " , q)
