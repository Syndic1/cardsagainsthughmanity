
import socket
import select
import threading


client = None
HOST_ADDR = '192.168.1.247'
HOST_PORT = 25565


def connect_to_server(name):
    global client, HOST_PORT, HOST_ADDR
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print (name)
        client.connect((HOST_ADDR, HOST_PORT))
        print ('connected')
        name = bytes(name,'utf-8')
        client.send(name)    
        print ('sent name')
        threading._start_new_thread(receive_message_from_server, (client, 'm'))
        print('thread running')
    except Exception as e:
        print('Failed')
        

def getChatMessage(msg):
    msg = msg.replace('\n','')    
    send_message_to_server(msg)
    
    
def send_message_to_server():
    client.send(msg)
    if msg == "exit":
        client.close()
        
    
def receive_message_from_server(sck, m):
    while True:
        from_server = sck.recv(4096)    
        print('message received from server')
        if not from_server: break
        print (from_server)
    sck.close()
    
