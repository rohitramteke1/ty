from xmlrpc.client import ServerProxy
client = ServerProxy("http://localhost:8000/") 

n = int(input("Number of customers : "))

while n > 0 :
    room = int(input("Room number : ")) 
    guest = input("Guest name : ")
    client.book(room , guest)
    n -= 1
    print()


print("List of all bookings : " , client.list() )

ch = int(input("Want to cancel booking (0/1) : "))

if ch == 0 :
    print("ok")
else:
    room = int(input("Room number : ")) 
    guest = input("Guest name : ")
    client.popper(room,guest)