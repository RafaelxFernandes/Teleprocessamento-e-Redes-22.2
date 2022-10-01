from socket import *

serverPort = 12007
serverSocket = socket(AF_INET,SOCK_STREAM) 
serverSocket.bind(('', serverPort)) 
serverSocket.listen(1)

print('The server is ready to receive')

while True:
    connectionSocket, addr = serverSocket.accept()

    print(f"Connection established with: {addr}")

    while True:
        number = connectionSocket.recv(1024).decode() 
        print(f"Client says: {number}")