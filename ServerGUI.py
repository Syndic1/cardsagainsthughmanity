from Server import *
from tkinter import * 

HOST_ADDR = '0.0.0.0'
HOST_PORT = 25565

top = Tk()

top.minsize(800,600)

top.title("Cards Against Hughmanity Server")


lservername = Label(text="Server Name")
lservername.grid(column = 0, row = 0,padx=10)
eservername = Entry(top)
eservername.grid(column = 1, row = 0, pady=10)

lserverpassword = Label(text="Server Password")
eserverpassword = Entry(top)
lserverpassword.grid(column = 0, row = 1,padx=10)
eserverpassword.grid(column = 1, row = 1,padx=10)

lserverdeck = Label(text="Select Deck")
oserverdeck = OptionMenu(top, "Jon's Tiny Deck", "Jon is Great")
oserverdeck.config(width=30)
lserverdeck.grid(column = 3, row = 0,padx=10)
oserverdeck.grid(column = 3, row = 1,padx=10)
lplayerlist = Label(text="Connected Players")
playerlist = Listbox(top, height=20, width=20)
lplayerlist.grid(column=4,row=4, columnspan=2)
playerlist.grid(column=4,row=5, columnspan=2)

lchatwin = Label(text="Chat window")
lchatwin.grid(column=0, row=4, columnspan =4)
chatwindow = Text(top,height = 20, width = 40)
chatwindow.grid(column=0, row=5, columnspan =4)


startserverbutton = Button(top,text="Start Server", width=15, height=2, command=start_server)
startserverbutton.grid(column=5, row=0)
stopserverbutton = Button(top,text="Stop Server", width=15, height=2, command=stop_server)
stopserverbutton.grid(column=5, row=1)


top.mainloop()


