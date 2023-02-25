import socket
HOST = "127.0.0.1" 
PORT = 1235

def sendable_data (data):
    return str(data).rjust (1024," ").encode ("utf-8")

serverAddressPort = ("127.0.0.1", 1235)
buffersize = 1024 
UDPClientSocket = socket.socket( family =socket.AF_INET, type= socket.SOCK_DGRAM ) 

while True:
    msg = input () 
    UDPClientSocket.sendto(sendable_data (msg), serverAddressPort) 
    msgFromServer = UDPClientSocket.recvfrom (buffersize) 
    msg = "Message from Server: \n" + msgFromServer [0].decode("utf-8").strip () 
    print (msg)

