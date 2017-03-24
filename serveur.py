from socket import *
serverPortIn = 12000
serverPortOut = 13000
serverName = "localhost"

socketOut = socket(AF_INET, SOCK_STREAM)
socketIn = socket(AF_INET,SOCK_STREAM)

socketOut.bind(('',serverPortOut))
socketIn.bind(('',serverPortIn))

socketIn.listen(1)
socketOut.listen(1)

while 1:
	connectionSocketIn, addr = socketIn.accept()
	sentence = connectionSocketIn.recv(2048)
	modifiedSentenceA = sentence.upper()
	connectionSocketIn.send(modifiedSentenceA)
	
	connectionSocketOut, addr = socketOut.accept()
	connectionSocketOut.send(modifiedSentenceA)

	connectionSocketIn.close()
	connectionSocketOut.close()

socketIn.close()
socketOut.close()