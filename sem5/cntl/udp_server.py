udp_server.py
import socket
from _thread import start_new_thread
HOST = "127.0.0.1"
PORT = 54321
def sendable_data(data):
 return str(data).rjust(1024, " ").encode("utf-8")


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST, PORT))
print("UDP server started.......")
while True:
 bytesAddressPair = s.recvfrom(1024)
 addr_client = bytesAddressPair[1]
 data = bytesAddressPair[0]
 print("Connection request from client: ", addr_client)
 msg_from_client = data.decode("utf-8").strip()
 data = msg_from_client.split(" ")
 num1 = int(data[0])
 num2 = int(data[1])
 if data[2] == "+":
 res = num1 + num2
 elif data[2] == "-":
 res = num1 - num2
 elif data[2] == "/":
 res = num1 / num2
 elif data[2] == "*":
 res = num1 * num2

 final_result = "Operation from client is: " + data[2] + " \nResult of
operation: " + str(res)
 s.sendto(sendable_data(final_result), addr_client)
udp_client.py
import socket
HOST = "127.0.0.1"
PORT = 54321
def sendable_data(data):
 return str(data).rjust(1024, " ").encode("utf-8")


serverAddressPort = ("127.0.0.1", 54321)
bufferSize = 1024
UDPClientSocket = socket.socket(family = socket.AF_INET, type =
socket.SOCK_DGRAM)
while True:
 msg = input("Please provide inputs (num1, num2 and Operator): ")
 UDPClientSocket.sendto(sendable_data(msg), serverAddressPort)
 msgFromServer = UDPClientSocket.recvfrom(bufferSize)
 msg = "Message from Server:\n" + msgFromServer[0].decode("utf-8").strip()
 print(msg)