list = ['a','a','a','a','a','a' ,'b'] 
n = len(list)
i = 0

while(i < n):
    if(list[i]=='a'):
        list.remove('a')
        i -=1
        n -=1
    i += 1
print(list)
