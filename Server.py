# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 22:21:40 2020

@author: Jon
"""
import socket
import _thread 
from queue import Queue


number_of_threads = 2
job_number = [1, 2]
connections = []
addresses = []


lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
host = '192.168.1.247'
port = 25565
password = b"airsoft"

print ('Server Started')
print ('Listening on ',host, port)


lsock.bind((host,port))
lsock.listen(5)

def clientthread(conn, addr):
     
    while True:
        try: 
            message = conn.recv(2048)
            if message == password:
                conn.send("Welcome to the Server")
                print ("Welcome")
            else:
                conn.send(" Wrong Password")
                print ("not allowed")
                remove(conn)
                lsock.close()
                
        except:
            continue
        
        
def broadcast(message, connection): 
    for clients in addresses: 
        if clients!= connection: 
            try: 
                clients.send(message) 
            except: 
                clients.close() 
  
                # if the link is broken, we remove the client 
                remove(clients) 
  


def remove(connection): 
    if connection in list_of_clients: 
        list_of_clients.remove(connection) 
   
    
while True:
            conn, addr = lsock.accept()
            addresses.append(conn)
            message = conn.recv(2048)
            print (addr[0] + " is connected")
            if  conn.recv(message) == password:
                conn.send("Welcome to the Server")
                print ("Welcome")
                _thread.start_new_thread(clientthread(conn,addr))
            else:
                conn.send(" Wrong Password")
                print ("not allowed")
                remove(conn)
                lsock.close()
            
    
conn.close()
lsock.close()

print ("end")      


