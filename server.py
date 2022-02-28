import socket
import string
import threading
import os

port = 80
header = 64
format = 'utf-8'
disconnectMessage = "!exit"

def clientHandler(connection, address): # The function that deals with each client that connects to the server

    connected = True
    while connected:
        #print("Receiving message.")
        messageLength = connection.recv(header).decode(format) # Checks for the length of the message
        if messageLength:
            messageLength = int(messageLength)
            #print(str(messageLength))
            message = connection.recv(messageLength).decode(format)
            print("Message received...")
            print(message)
            if message == disconnectMessage:
                connected = False
                break
            fileRetrieval(connection, str(message))
    print("Disconnecting...")
    connection.close()

def start(Server, address):

    Server.listen()
    print("Starting to listen...")
    while True:

        connection, address = Server.accept()
        print(f"Connection from {address}.")
        thread = threading.Thread(target=clientHandler, args=(connection, address))
        thread.start()

def fileRetrieval(connection, fileName):

    #fileName = r"C:\\Users\\jel26\\Documents\\Schoolwork\CCN\Project 1\\" + fileName
    dir = os.getcwd()
    #print(dir + '\n')
    file = open(dir + "\\" + fileName, "rb")
    while True:
        bytesRead = file.read(4096)
        if not bytesRead:
            print("Finished sending bytes.")
            #connection.sendall(bytesRead)
            #connection.send("!finished")
            connection.send(b'0')
            break
        print("Sending bytes...")
        connection.sendall(bytesRead)
    file.close()
    # with open(fileName, "rb") as f:
    #     reading = True
    #     while reading:
    #         bytesRead = f.read(4096)
    #         if not bytesRead:
    #             reading = False
    #             break
    #         connection.sendall(bytesRead)

if __name__ == "__main__":

    #files = os.listdir('serverFiles/')

    server = socket.gethostbyname(socket.gethostname())
    address = (server, port)

    Server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    Server.bind(address)
    start(Server, address)