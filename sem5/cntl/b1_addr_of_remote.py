import socket

hostname = socket.gethostname()
ipaddr = socket.gethostbyname(hostname)

print("Name of Computer : " + hostname)
print("Computer IP : " + ipaddr)