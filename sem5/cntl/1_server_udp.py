import socket 
from _thread import start_new_thread

HOST = "127.0.0.1" 
PORT = 1235

def sendable_data(data):
    return str(data).rjust (1024, " ").encode("utf-8")

s = socket.socket (socket.AF_INET, socket.SOCK_DGRAM) 
s.bind ( (HOST, PORT)) 
print ("UDP server started..........") 

while True :
    bytesAddressPair = s.recvfrom(1024) 
    addr_client = bytesAddressPair[1] 
    data = bytesAddressPair[0] 
    print("Connection request from client: ", addr_client) 
    msg_from_client = data.decode ("utf-8").strip () 
    data = msg_from_client.split(" ") 
    numl = int(data[0]) 
    num2 = int (data[1]) 
    if data [2] == "+":
        res = numl + num2 
    elif data [2] == "-":
        res = numl - num2 
    elif data[2] == "/":
        num2 = float (num2) 
        res = numl/num2
    elif data [3] == "*":
        res = num1*num2 
    
    final_result = "Operation from client is : " + data[2] + " \nResult of operation: " + str(res)
    s.sendto(sendable_data (final_result), addr_client)
