# TP1
Etienne PROT

## 1) Découverte du Markdown :
- '#' pour un titre
- '##' pour des sous titres
- '-' pour une liste
Pour plus de renseignement :
https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet 

Pour lancer un fichier python (en .py), il faut dans une invite de commande taper : python nomDuFichier.py

## 2) Programmation UDP :

###Code pour le client :
```python
from socket import *
serverName = "localhost"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = raw_input('Input lowercase sentence:')
clientSocket.sendto(message,(serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print modifiedMessage
clientSocket.close()
```

###Code pour le serveur :
```python
from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print "The server is ready to receive"
while 1:
	message, clientAddress = serverSocket.recvfrom(2048)
	modifiedMessage = message.upper()
	print modifiedMessage
	serverSocket.sendto(modifiedMessage, clientAddress)
```

En plus : 
- si on veut discuter avec une autre machine il faut remplacer le nom de la machine (ici localhost) par une adresse IP.

## 3) Programmation TCP :

###Code pour le client :
```python
from socket import *
serverName = "localhost"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
sentence = raw_input('Input lowercase sentence:')
clientSocket.send(sentence)
modifiedSentence = clientSocket.recv(1024)
print 'From Server:', modifiedSentence
clientSocket.close()
```

###Code pour le serveur :
```python
from socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print 'The server is ready to receive'
while 1:
	connectionSocket, addr = serverSocket.accept()
	sentence = connectionSocket.recv(1024)
	capitalizedSentence = sentence.upper()
	connectionSocket.send(capitalizedSentence)
	print capitalizedSentence
	connectionSocket.close()
```
### 4) NetCat : 

- en UDP :

Pour le client : ```netcat -u localhost 12000```

Pour le serveur: ```netcat -u -l -p 12000```

- en TDP :

Pour le client : ```netcat -t localhost 12000```

Pour le serveur: ```netcat -t -l -p 12000```
