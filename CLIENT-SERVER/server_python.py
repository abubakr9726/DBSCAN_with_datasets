# server_python

from ast import While
from tkinter import *
from tkinter import filedialog
import socket
# import cv2
c = 0
IP = "192.168.10.3"
PORT = int(8080)
server_socket = socket.socket()
server_socket.bind((IP, PORT))
# data = filedialog.askopenfile(initialdir="/")

server_socket.listen(1)
    
c, address = server_socket.accept()
print("Connection from: " + str(address))
data = c.recv(1024).decode()
print("data received: " + data)

path = "C:\\Users\\ME\\Documents\\DBSCAN_with_datasets\\%s\\map\\%s.bin"   %(data,data) #demonstration
#path = "C:\\Users\\ME\\Documents\\DBSCAN_with_datasets\\home\\map\\home.bin" #testing
image = open(path, "rb")

if c != 0:
    for i in image:
        c.send(i)
