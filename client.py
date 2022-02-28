import socket
import os
import time

header = 64
port = 80
format = 'utf-8'
disconnectMessage = "!exit"

def send(message): # Function to find the length of the message, send that, then send the message
    Message = message.encode(format)
    MessageLength = len(Message)
    sendLength = str(MessageLength).encode(format)
    sendLength += b' ' * (header - len(sendLength)) # Pads the message length with the necessary number of empty bytes
    client.send(sendLength)
    client.send(Message)

def connection():
    connected = True
    while connected:
        message = str(input("Enter file to download: > "))
        #print(message)
        #time.sleep(10)
        #dir = os.getcwd()
        #print(str(dir))
        #time.sleep(10)
        send(message)
        if message == disconnectMessage:
            connected = False
            client.close()
            break
        else:
            file = open("Downloads/" + message, "wb")
            while True:
                print("Receiving bytes...")
                bytesRead = client.recv(4096)
                if bytesRead == b'0':
                    print("Finished receiving.")
                    break
                file.write(bytesRead)
            file.close()
            print("Finished getting file.")
            # with open(f, "wb") as f:
            #     while True:
            #         bytesRead = client.recv(1024)
            #         if not bytesRead:
            #             break
            #         f.write(bytesRead)

if __name__ == "__main__":

    #downloadsFile = r"~/Project 1/Downloads/"

    #try:
    #    os.mkdir(downloadsFile)
    #except OSError as error:
    #    pass

    server = socket.gethostbyname(socket.gethostname())
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = (server, port)
    client.connect(address)
    connection()