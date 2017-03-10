from socket import *
serverPortIn = 12000
serverPortOut = 13000
serverName = "localhost"

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPortOut))

serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPortIn))
serverSocket.listen(1)

while 1:
	connectionSocket, addr = serverSocket.accept()
	sentence = connectionSocket.recv(1024)
	modifiedSentence = sentence.upper()
	clientSocket.send(modifiedSentence)
	connectionSocket.close()

clientSocket.close()