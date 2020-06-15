# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 22:21:40 2020

@author: Jon
"""
import socket
import threading 


server = None
HOST_ADDR = '192.168.1.247'
HOST_PORT = 25565
client_name = ' '
clients = []
clients_names = []

def start_server():
    global server, HOST_ADDR, HOST_PORT

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST_ADDR,HOST_PORT))
    server.listen(10)
    threading._start_new_thread(accept_new_clients, (server, ' '))
    print ("Server Started")
    
    #1b1Host["text"] = "Host: " + HOST_ADDR
    #1b1Port["text"] = "Port: " + str(HOST_PORT)
    
def stop_server():
     global server, HOST_ADDR, HOST_PORT
     server.close()
     print("Server Stopped")
    
def accept_new_clients(the_server, y):
    while True:
        client, addr = the_server.accept()
        print('Client Accepted')
        clients.append(client)
        
        threading._start_new_thread(send_receive_client_messages, (client, addr))
        print('thread started')

def send_receive_client_messages(client_connection, client_IP_addr):
    global server, client_name, clients, client_addr
    client_msg = " " 
    
    client_name = client_connection.recv(4096)
    print ('message recieved')
    client_connection.send(bytes("Welcome ",'utf-8') + client_name)
    print ('sent welcome')
    clients_names.append(client_name)

    while True:
        data = client_connection.recv(4096) 
        if not data: break
        if data == "quitButton": break
    
        client_msg = data
        
        idx = get_client_index(clients, client_connection)
        sending_client_name = clients_names[idx]
        
        for c in clients:
            if c != client_connection:
                c.send(sending_client_name + "> " + client_msg)
                
        idx = get_client_index(clients, client_connection)
        del clients_names[idx]
        del clients[idx]
        client_connection.close()
    
def get_client_index(client_list, curr_client):
        
    idx=0
    for conn in client_list:
        if conn == curr_client:
            break
        idx = idx + 1
    return idx
                
    
