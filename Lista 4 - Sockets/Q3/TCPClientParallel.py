from socket import *
from multiprocessing import Pool
from os import getpid

import time

serverName = 'localhost'
serverPort = 12004

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort)) 

def askServer(sentence):
    clientSocket.send(sentence.encode()) 

    modifiedSentence = clientSocket.recv(1024) 

    print(f"Processo {getpid()} recebeu: {modifiedSentence.decode()}")

    return


if __name__ == '__main__':
    sentences = ["a", "b", "c", "d"]

    with Pool(processes = 4) as pool:
        for sentence in sentences:
            print(pool.map(askServer, sentence))
            time.sleep(2)