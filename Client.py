# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 22:28:25 2020

@author: Jon
"""


import socket
import select

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = '192.168.1.247'
port = 25565
password = "airsoft"



server.connect((host, port))
server.send("password")


while True:
    sockets_list = [server]
    read_sockets,write_sockets,error_socket = select.select(sockets_list,[],[])
    
    for socks in read_sockets:
        if socks == server:
            message = socks.recv(2048)
            print(message)
        else:
            message = "some noise"
            server.send(message.encode(message))
server.close()


    
