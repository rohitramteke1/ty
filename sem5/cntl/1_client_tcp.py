import socket
host = socket.gethostname()
port = 11

s = socket.socket()
s.connect((host,port))
print (s.recv(1024).decode() )