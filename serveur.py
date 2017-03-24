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
	modifiedSentence = sentence.upper()
	connectionSocketIn.send(modifiedSentence)
	
	connectionSocketOut, addr = socketOut.accept()
	msg = modifiedSentence+"\n"
	connectionSocketOut.send(msg)

	connectionSocketIn.close()
	connectionSocketOut.close()

socketIn.close()
socketOut.close()
