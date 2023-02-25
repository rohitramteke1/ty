import math as M
message=int(input("Enter the message to be encrypted:"))
p=11
q=7
e=3
n=p*q
def encrypt(message):
 en=M.pow(message, e)
 c=en% n
 print("Encrypted message is ",c)
 return c

print("Original message is:",message)
c=encrypt(message)
#c=int(input("Enter the encrypted message:"))
def decrypt(c):
 en=M.pow(message, e)
 c=en% n
 print("Encrypted message is ",c)

 a=en/n
 d=(n*a)+c
 f=M.pow(d, 1/e)
 g=M.floor(f)
 print("decrypted message is:",g)
 return g
g=decrypt(c)