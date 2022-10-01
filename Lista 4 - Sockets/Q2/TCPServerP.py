from socket import *

serverPort = 12003
serverSocket = socket(AF_INET,SOCK_STREAM) 
serverSocket.bind(('', serverPort)) 
serverSocket.listen(1)

print('The server is ready to receive')

while(True):
    connectionSocket, addr = serverSocket.accept()

    print(f"Connection established with: {addr}")

    while True:
        sentence = connectionSocket.recv(1024).decode() 
        capitalizedSentence = sentence.upper() 
        connectionSocket.send(capitalizedSentence.encode())