from socket import *
serverName = "localhost"
serverPort = 13000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
modifiedSentence = clientSocket.recv(2048)
print 'From Server:', modifiedSentence
clientSocket.close()