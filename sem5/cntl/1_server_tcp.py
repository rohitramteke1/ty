import socket
from _thread import start_new_thread

s = socket.socket()

host = socket.gethostname()

port = 8000

s.bind((host,port))
s.listen(5)

while True :
    conn , addr = s.accept()
    print('Got a connecton from ' ,addr)
    conn.send('Connection Successful !'.encode())
    conn.close()
