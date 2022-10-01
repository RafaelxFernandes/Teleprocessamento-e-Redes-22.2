from socket import *

serverName = 'localhost'
serverPort = 12008
clientSocket = socket(AF_INET, SOCK_DGRAM)

while True:
    N = input("Digite o valor de N: ")
    N = int(N)

    for i in range(N):
        i = str(i)
        clientSocket.sendto(i.encode(),(serverName, serverPort)) 