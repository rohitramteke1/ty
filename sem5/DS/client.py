import socket

def client_program():
    host = socket.gethostname() # as both code is running on same pc port 
    port = 5000 #socket server port number

    client_socket = socket.socket() #ceate instance 
    client_socket.connect((host, port)) #connect to the server
    
    message = input (" -> ") # take input

    while message.lower().strip() != 'bye': 
        client_socket.send (message.encode()) 
        data = client_socket.recv (1024).decode()
        print('Received from server: ' + data )
        message= input(" -> ")
    client_socket.close()

if __name__ == '__main__' :
    client_program ()


