from socket import *

serverName = 'localhost'
serverPort = 12005

clientSocket = socket(AF_INET, SOCK_DGRAM)

while True:
    message = input("Input lowercase sentence: ")

    clientSocket.sendto(message.encode(), (serverName, serverPort)) 
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048) 

    print(modifiedMessage.decode())
    print(f"Server Address: {serverAddress}")