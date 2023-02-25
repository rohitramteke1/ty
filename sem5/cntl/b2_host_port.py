import socket
ip = socket.gethostbyname (socket.gethostname())

for port in range(65535) :

    try :
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.bind((ip ,port))
    except :
        print('[OPEN] Port Open : ' , port)
    
    s.close()