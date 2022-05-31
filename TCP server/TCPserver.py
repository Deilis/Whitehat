#!/usr/bin/python3

import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostbyname()
port = 123

serversocket.bind((host, port))

serversocket.listen(1)

while True:
    clientsocket, address = serversocket.accept()
    print("Connection " % str(address))
    message = 'Connected' + "\r\n" 
    clientsocket.close()
