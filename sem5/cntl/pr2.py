import socket 
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
print("Your computer name is: " +hostname)
print("Your Computer IP Addres is: " + IPAddr) 