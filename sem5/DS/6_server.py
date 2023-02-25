from xmlrpc.server import SimpleXMLRPCServer

dict = {}

def sendable_data(data):
    return str(data).rjust (1024, " ").encode("utf-8")

def booking(x , y):
    room = x 
    guest = y
    if room in dict :
        print("Room is already Booked , Choose Another.")
    else :
        dict[room] = guest
        print("Room {} booked for Guest {}".format(room ,guest))
    return 0

def list() :
    print(dict)
    return 

def popper(room , guest) :
    if room in dict :
        dict.pop(room)
        print("Successfully cancelled booking .")
    else :
        print("Room is already vacant.!")
    return

server = SimpleXMLRPCServer(("" ,8000))
print("Serve is listening on port 8000 ...")
server.register_function(booking ,"book")
server.register_function(list ,"list")
server.register_function(popper ,"popper")
server.serve_forever()