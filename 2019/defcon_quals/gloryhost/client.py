#!/usr/bin/python3
# TCP client example
import socket
import base64
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 9999))
# client_socket.connect(('gloryhost.quals2019.oooverflow.io', 9999))

print(client_socket.recv(10000).decode())
# data = input ( "SEND( TYPE q or Q to Quit):" )
data = base64.b64encode(open('./main.wasm', 'rb').read())
# print(data)
client_socket.send(data)
# print(client_socket.recv(4096).decode())
print ("socket colsed... END.")
