from socket import *

serverPort = 12009
serverSocket = socket(AF_INET, SOCK_STREAM) 
serverSocket.bind(('', serverPort)) 
serverSocket.listen(1)

user1_username = "aluno"
user1_password = "senha"

print('The server is ready to receive')

while True:
    connectionSocket, addr = serverSocket.accept()
    print(f"Connection established with: {addr}")

    while True:
        username = connectionSocket.recv(1024).decode()
        password = connectionSocket.recv(1024).decode() 

        if username == user1_username and password == user1_password:
            success = "Você está logado agora!"
            connectionSocket.send(success.encode())
            connectionSocket.close()
        else:
            error = "Erro no nome de usuário ou senha"
            connectionSocket.send(error.encode())