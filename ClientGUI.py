from Clientmain import *
from tkinter import * 


def changeUsername():
    username = eclientname.get()
    print('Name changed to ' + username)
    bytes(username, 'utf-8')

def connect():
    
    global username, client
    username = eclientname.get()
    connect_to_server(username)

top = Tk()

top.minsize(800,600)

top.title("Cards Against Hughmanity Client")


lservername = Label(text="User Name")
lservername.grid(column = 0, row = 0,padx=10)
eclientname = Entry(top)
eclientname.grid(column = 1, row = 0, pady=10)


lserverpassword = Label(text="Server Password")
eserverpassword = Entry(top)
lserverpassword.grid(column = 0, row = 1,padx=10)
eserverpassword.grid(column = 1, row = 1,padx=10)

lplayerlist = Label(text="Connected Players")
playerlist = Listbox(top)
lplayerlist.grid(column=4,row=4, columnspan=2)
playerlist.grid(column=4,row=5, columnspan=2)

lchatwin = Label(text="Chat window")
lchatwin.grid(column=0, row=4, columnspan =4)
chatwindow = Text(top,height = 20, width = 40)
chatwindow.grid(column=0, row=5, columnspan =4)


namebutton = Button(top,text="change name", width=20, height=2, command=changeUsername)
namebutton.grid(column=5, row=0)

connectbutton = Button(top,text="Connect", width=20, height=2, command=connect)
connectbutton.grid(column=5, row=1)

def changeUsername():
    username = eclientname.get()
    print('Name changed to ' + username)

def connect():
    
    global username, client
    connect_to_server(username)

top.mainloop()


