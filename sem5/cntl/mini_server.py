from socket import *
from threading import *
from tkinter import *
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
hostIp = "127.0.0.3"
portNumber = 9001
clientSocket.connect((hostIp, portNumber))

def sendMessage():
 clientMessage = txtYourMessage.get()
 txtMessages.insert(END, "\n" + "You: "+ clientMessage)
 clientSocket.send(clientMessage.encode("utf-8"))
btnSendMessage = Button(window, text="Send", width=20, command=sendMessage)
btnSendMessage.grid(row=4, column=0, padx=20, pady=20)
def recvMessage():

    while True:
        serverMessage = clientSocket.recv(1024).decode("utf-8")
        print(serverMessage)
        txtMessages.insert(END, "\n"+serverMessage)


recvThread = Thread(target=recvMessage)
recvThread.daemon = True
recvThread.start()


window = Tk()
window.title("Connected To: "+ hostIp+ ":"+str(portNumber))
txtMessages = Text(window, width=50)
txtMessages.grid(row=0, column=0, padx=20, pady=20)
txtYourMessage = Entry(window, width=50)
txtYourMessage.insert(0,"Your message")
txtYourMessage.grid(row=1, column=0, padx=10, pady=10)
window.mainloop()