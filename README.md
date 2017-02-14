# TP1
Etienne PROT

## 1) Découverte du Markdown :
- '#' pour un titre
- '##' pour des sous titres
- '-' pour une liste
Pour plus de renseignement :
https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet 

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
	serverSocket.sendto(modifiedMessage, clientAddress)
```

En plus : 
- si on veut discuter avec une autre machine il faut remplacer le nom de la machine (ici localhost) par une adresse IP.
