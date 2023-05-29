#client_python

import socket
# import cv2
import time
import sys
import time

IP = "192.168.10.2"
PORT = int(8080)
client_socket = socket.socket()

# r = "bin"
# s = "9." + r
# print(s)

condition = True
client_socket.connect((IP, PORT))
name = input("dataset name: ")
map = name + ".bin"
print(map)

client_socket.send(name.encode())  # send message

f = open(map, "wb")
while condition:
    rec_map = client_socket.recv(1024)
    if str(rec_map) == "b''":
        condition = False
        client_socket.close()
    f.write(rec_map)
