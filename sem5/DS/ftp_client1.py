# saved as client.py
import Pyro4
FileTransfer = Pyro4.Proxy("PYRONAME:file_sender")    # use name server object lookup uri shortcut

# fname = input("Enter filename to transfer: ").strip()
fname = "myfile.txt"
x = 
if (x):
    f = open(str(fname), 'r')
    print("Contents in the file are:\n")
    print(f.read())
else:
	print("File not found")