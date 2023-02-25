import Pyro4
rooms = [0,0,0,0,0]

def isRoomBooked(room_no):
        global rooms
        if(rooms[room_no] == 1):
            return 1
        else:
            return 0

@Pyro4.expose
class Hotel(object):
  
    def bookRoom(self, room_no):
        if(room_no > 5):
            return "Room no Limit Exceeded!!!"
        if(not isRoomBooked(room_no-1)):
            global rooms
            rooms[room_no-1] = 1
            return "Room No. " + str(room_no) + " is now booked for you."
        else:
            return "Room No. " + str(room_no) + " is already booked \nPlease select another room"

    
    def cancelRoom(self, room_no):
        if(room_no > 5):
            return "Room no Limit Exceeded!!!"
        global rooms
        rooms[room_no] = 0 
        return "Room No. " + str(room_no) + " is now vacant."

    def roomBill(self, no_of_days):
        total = 500 * no_of_days
        return "Your Total Bill for " + str(no_of_days) +" is " + str(total) + "."


daemon = Pyro4.Daemon()                # make a Pyro daemon
ns = Pyro4.locateNS()                  # find the name server
uri = daemon.register(Hotel)            # register the greeting maker as a Pyro object
ns.register("example.hotel", uri)       # register the object with a name in the name server

print("Hi. Hotel is now active.")
daemon.requestLoop()