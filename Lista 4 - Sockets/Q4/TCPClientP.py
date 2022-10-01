from socket import *

serverName = 'localhost'
serverPort = 12007

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort)) 

while(True):
    N = input("Digite o valor de N: ")
    N = int(N)

    for i in range(N):
        i = str(i)
        clientSocket.send(i.encode()) 