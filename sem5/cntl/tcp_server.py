
import socket
from _thread import start_new_thread
host = "127.0.0.1"
port = 1234
def sendable_data(data):
 return str(data).rjust(1024, " ").encode("utf-8")
def handle_client_req(client_conn, addr):
 with client_conn:
 print("Connected by: ",addr)

 while True:
 data = client_conn.recv(1024)
 data2 = client_conn.recv(1024)
 data3 = client_conn.recv(1024)
 print (data.decode("utf-8").strip())
 print (data2.decode("utf-8").strip())
 print (data3.decode("utf-8").strip())
 op = data3.decode("utf-8").strip()

 a = float(data.decode("utf-8").strip())
 b = float(data2.decode("utf-8").strip())
 result = 0

 if op == "+":
 result = a + b
 elif op == "-":
 result = a - b
 elif op == "*":
 result = a * b
 elif op == "/":
 result = a / b

 client_conn.sendall(sendable_data("Result of "+op+" operation is:
"+str(result)))
with socket.socket(socket.AF_INET ,socket.SOCK_STREAM) as s:
 s.bind((host, port))
 s.listen(5)
 while True:
 conn, addr = s.accept()
 start_new_thread(handle_client_req, (conn, addr, ))



 
tcp_client.py
import socket
host = "127.0.0.1"
port = 1234
def sendable_data(data):
 return str(data).rjust(1024, " ").encode("utf-8")
if __name__ == "__main__":
 with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
 s.connect((host, port))
 while True:
 input_str = input("Please provide 2 floating point numbers and the
operation:")
 parsed = input_str.split(" ")

 if parsed[0] == "q":
    exit(0)
 s.sendall(sendable_data(parsed[0]))
 s.sendall(sendable_data(parsed[1]))
 s.sendall(sendable_data(parsed[2]))

 data = s.recv(1024)
 print(f'Received:\n{data.decode("utf-8").strip()}')
